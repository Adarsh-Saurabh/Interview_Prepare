# 05: Real-Time Credit Underwriting & Fraud ML System Design

Design an enterprise-grade, low-latency machine learning system for real-time credit limit decisioning and fraud detection at CRED.

---

## 1. System Requirements & Design Goals

### Functional Requirements
1. **Real-Time Risk Decision:** For every transaction event ($N \le 5,000 \text{ TPS}$), score the transaction and return an underwriting decision: `APPROVE`, `STEP_UP_VERIFY`, or `DECLINE`.
2. **Dynamic Limit Adjustments:** Automatically evaluate members for instant credit-line enhancements on CRED Cash based on repayment discipline.
3. **Continuous Drift Telemetry:** Detect data drift and feature degradation without impacting online transaction latency.

### Non-Functional Requirements & Latency Budget
- **Latency SLA:** Total end-to-end evaluation latency $\le 25\text{ms}$ (p99); ML model inference budget strictly $\le 12\text{ms}$.
- **Availability:** $99.999\%$ uptime (Multi-AZ active-active deployment).
- **Fault Tolerance:** If the ML inference engine experiences an outage or times out ($>20\text{ms}$), fallback gracefully to deterministic heuristic rules (Circuit Breaker).

---

## 2. High-Level Architectural Blueprint

```
 ┌────────────────┐
 │  CRED Member   │
 │   Mobile App   │
 └───────┬────────┘
         │ HTTPS / gRPC
         ▼
 ┌─────────────────────────────────────────────────────────────┐
 │               API Gateway (Envoy / Rate Limiter)            │
 └───────┬─────────────────────────────────────────────┬───────┘
         │                                             │
         ▼ (Async Audit Stream)                        ▼ (Sync Evaluation <25ms)
 ┌───────────────┐                             ┌───────────────────────────────┐
 │ Apache Kafka  │                             │   Risk Decision Orchestrator  │
 │  Event Bus    │                             │       (Go Microservice)       │
 └───────┬───────┘                             └───────┬───────────────┬───────┘
         │                                             │               │
         ▼                                             │               │ Fetch Features (<5ms)
 ┌───────────────┐                                     │               ▼
 │ Apache Flink  │                                     │     ┌───────────────────┐
 │ Stream Engine │                                     │     │ Feast Feature Store│
 └───────┬───────┘                                     │     │   (Redis Cache)   │
         │                                             │     └───────────────────┘
         ▼ Write Rolling Aggregates                    │
 ┌───────────────┐                                     │ Predict Risk (<10ms)
 │ Redis Cluster │◄────────────────────────────────────┘               ▼
 │  (Hot Cache)  │                                           ┌───────────────────┐
 └───────────────┘                                           │  Triton Inference │
                                                             │ (ONNX / LightGBM) │
                                                             └───────────────────┘
```

---

## 3. The Dual-Path Feature Pipeline

Features are bifurcated into two independent computational streams:

| Feature Layer | Source | Ingestion Technology | Storage & Freshness |
| :--- | :--- | :--- | :--- |
| **Real-Time (Hot)** | Transaction stream | Apache Flink streaming sliding-window aggregations | In-Memory Redis via Feast ($\le 5\text{ms}$ freshness) |
| **Near-Line (Warm)** | App session telemetry | Kafka consumer microservice | Amazon DynamoDB ($\le 30\text{s}$ freshness) |
| **Batch (Cold)** | Historical bureau & repayment data | Airflow / Spark batch jobs running nightly | Snowflake / PostgreSQL (24-hour freshness) |

---

## 4. Serving Engine: Triton Inference Server & ONNX Runtime

At CRED's scale, serving Python models directly via Flask or FastAPI is prohibited due to Python's Global Interpreter Lock (GIL) and CPU inference latency spikes ($>50\text{ms}$).

### The High-Throughput MLE Stack
1. **Model Optimization:** Trained LightGBM and XGBoost models are compiled to **ONNX Runtime** or **Treelite** format, converting decision trees into vectorized C-code without runtime interpretation overhead.
2. **Model Serving:** Deployed on **NVIDIA Triton Inference Server** instances on AWS EKS:
   - Dynamic batching enabled: Batches requests arriving within a $2\text{ms}$ window.
   - Concurrent model execution across multiple CPU cores / GPU instances.
   - Sub-6ms p99 inference latency for tree models.
3. **Circuit Breaker Pattern:**
   - Wrapped in a resilience circuit breaker (e.g. Netflix Hystrix or Resilience4j).
   - If Triton fails to return a score within $20\text{ms}$, the circuit opens and routes the request to a deterministic fallback rule engine (`fallback_approve_if_bureau_gt_800`).

---

## 5. Drift Monitoring & Shadow Retraining Pipeline

```
 [Live Ingestion] ──> [Sample 5% of Predictions] ──> [Kafka Telemetry Topic]
                                                             │
                                                             ▼
                                                    [Evidently AI Engine]
                                                             │
                                       ┌─────────────────────┴─────────────────────┐
                                       ▼                                           ▼
                            [Compute PSI & KS Metrics]                  [Prometheus & Grafana]
                                       │
                         (If PSI >= 0.25: Trigger Retrain)
                                       ▼
                            [Kubeflow Retraining DAG]
                                       │
                                       ▼
                       [MLflow Registry: Challenger Model]
                                       │
                                       ▼
                     [Shadow Canary Deployment (10% Traffic)]
```

- **Champion-Challenger Routing:** Newly retrained models run in shadow mode for 7 days, scoring live traffic alongside the production champion without executing transactions.
- **Automated Promotion:** If the challenger model exhibits superior KS separation and stable PSI without increased false decline rates, traffic is dynamically shifted via Envoy weighted routing.
