# 05: Real-Time ML System Design

### System Design Challenge: Swiggy Real-Time ETA Prediction & Batching Platform at 100,000 RPS

---

## 1. System Requirements & Scale

- **Read Throughput:** 100,000 Requests Per Second (RPS) during peak dinner hours (8:00 PM – 9:30 PM).
- **Latency SLA:**
  - p50 $< 10$ms, p99 $< 25$ms for customer checkout ETA.
  - Background batching optimization cycle runs every 15–30s per geographic cluster.
- **Availability:** 99.99% uptime. Failure to return ETA prevents checkout and directly causes revenue loss.
- **Accuracy Constraint:** Median Absolute Error $\le 2.5$ minutes; $90\%$ of deliveries must fall within promised interval $[\hat{y}_{p10}, \hat{y}_{p90}]$.

---

## 2. High-Level Architecture Diagram

```
[Mobile Client] ────► [Cloudflare CDN / WAF]
                              │
                              ▼
                      [Envoy API Gateway]
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
       [Checkout Service]           [Live Tracking Service]
               │                             │
               └──────────────┬──────────────┘
                              │ gRPC (<5ms)
                              ▼
                [ETA Prediction Microservice]
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
[Feast Online Store]  [Triton Model Server]  [Kafka Event Bus]
  (Redis Cluster)      (ONNX / TensorRT)    (Async Logging)
  • Rider Speed        • Quantile XGBoost          │
  • Kitchen Queue      • Model p10, p50, p90       ▼
  • Weather/Rain       • Sub-4ms inference    [Apache Flink]
  (<3ms latency)                                   │
                                                   ▼
                                          [Evidently AI Drift]
```

---

## 3. Storage & Low-Latency Feature Serving

To meet the $<25$ms SLA, feature lookup must complete in $<5$ms:
- **Dual-Path Feature Store (Feast):**
  - **Online Store (Redis Cluster):** Keyed by `H3_hex_id:hour` and `restaurant_id`. Stores pre-computed sliding window aggregates:
    - `rest:1234:active_orders_last_15m`
    - `rest:1234:avg_wait_time_last_1h`
    - `h3:8861892547fffff:rider_supply_count`
    - `h3:8861892547fffff:rain_status`
  - **Offline Store (Apache Iceberg on S3):** Stores petabytes of raw trip telemetry for daily model retraining.
- **Real-Time Stream Processing (Apache Flink):**
  - Consumes rider location pings and kitchen status events from Kafka.
  - Updates sliding window state in Redis every 10 seconds.

---

## 4. Triton Inference Server Deployment & Model Serving

- Model artifacts (LightGBM/XGBoost) are compiled to **ONNX format** and served via **Triton Inference Server**:
  - Dynamic Batching: Aggregates concurrent incoming requests over a 1ms window into mini-batches, maximizing CPU SIMD/AVX-512 throughput.
  - Worker concurrency: Multi-threaded C++ runtime eliminates Python Global Interpreter Lock (GIL) overhead.
  - Latency: Pure model execution completes in $1.8	ext{ms}$ per request.

---

## 5. Resiliency, Graceful Degradation & Circuit Breaking

When incoming traffic surges $5	imes$ during rainstorms or server failure occurs:
1. **Tier 1 (Normal Operation):** Full 4-stage ML model inference with live Redis features.
2. **Tier 2 (Degraded Mode - Redis Latency $>15$ms):** Bypass real-time feature lookup; fallback to static H3 lookup tables (historical median ETAs for that hour and day).
3. **Tier 3 (Complete Inference Crash):** Circuit breaker (Resilience4j) trips; returns rule-based deterministic formula:
   $$	ext{ETA} = 	ext{Default Prep Time (20m)} + rac{	ext{Haversine Distance}}{15	ext{ km/h}} 	imes 60$$
4. **Data Drift & Concept Drift Monitoring:**
   - Asynchronous Kafka logger captures $(\mathbf{x}, \hat{y})$ pairs alongside ground-truth actual delivery time $y$.
   - Flink streams actual vs predicted differences to **Evidently AI / MLflow**.
   - If Kolmogorov-Smirnov (KS) test or Population Stability Index ($	ext{PSI} \ge 0.25$), an automated pipeline alert is triggered for retraining.
