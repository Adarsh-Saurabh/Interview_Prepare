# 07: Caveman & Ponytail Ultra-Dense CheatSheet

Ultra-compressed technical reference for rapid revision 30 minutes before your CRED technical and architectural interviews.

---

## 1. Caveman Mode (High Signal, Zero Fluff)

- **CRED Numbers:** 13M+ users. >$100B TPV. ~350M card bills/yr. 35-40% card bill market in India.
- **Role:** Data Science & MLE Intern. 6M + PPO. Stipend 1.1 LPM. CTC 24 LPA.
- **Tech Stack:** Go, Kotlin, Python, Kafka, Flink, Redis, DynamoDB, Postgres, Snowflake, Triton, ONNX.
- **Risk Math:** $\text{Expected Loss} = \text{PD} \times \text{EAD} \times \text{LGD}$.
- **KS Metric:** $\text{KS} = \max |F_{\text{good}}(s) - F_{\text{bad}}(s)|$. Good scorecards hit $40\%\text{--}60\%$.
- **PSI Formula:** $\sum (A_i - E_i) \ln(A_i / E_i)$. $<0.1$ good, $0.1\text{--}0.25$ watch, $>0.25$ retrain immediately.
- **Focal Loss:** $-\alpha (1 - p_t)^\gamma \log(p_t)$. Kills easy negative gradients, forces focus on hard fraud.
- **XGBoost Objective:** Taylor expansion: $g_i$ (grad), $h_i$ (hessian). Optimal leaf weight $w^* = -G / (H + \lambda)$.
- **L1 vs L2:** L1 = Diamond, Laplace, exact zeros, feature selector. L2 = Circle, Gaussian, shrinks weights, handles collinearity.
- **Sliding Window Max:** Monotonic Decreasing Deque. $O(N)$ time, $O(k)$ space.
- **Debt Settlement:** NP-hard. Bitmask DP on zero-sum subsets. Min transfers = $M - K$. $O(2^M \cdot M)$.
- **Fraud Graph:** Heterogeneous GNN (GraphSAGE). 2-hop sampling ($K_1=15, K_2=10$) for sub-15ms inference.
- **Serving SLA:** End-to-end $\le 25\text{ms}$. Feast Redis lookup $\le 5\text{ms}$. Triton ONNX $\le 8\text{ms}$. Policy engine $\le 3\text{ms}$.
- **Fallback Rule:** Circuit breaker pattern. If Triton $>20\text{ms}$, approve if CIBIL $>800$, else step-up SMS.
- **PathMapper Pitch:** $A^*$ spatial routing on 10k nodes in $<0.5\text{s}$ maps 1:1 to dynamic payment gateway routing.
- **Uplan Pitch:** LangGraph multi-agent + AST 98% token compression maps directly to statement OCR & compliance auditing.

---

## 2. Ponytail Mode (Architectural Mental Models)

```
                       THE CRED MLE FLYWHEEL
                       
        [ High-Trust Community (CIBIL >= 750) ]
                          │
                          ▼
            [ Low Default & Fraud Risk ]
                          │
                          ▼
          [ Better Lending Terms & Rewards ]
                          │
                          ▼
        [ Massive Telemetry (Kafka Event Bus) ]
                          │
                          ▼
    [ Low-Latency Dual-Path ML (Flink + Triton) ]
                          │
                          ▼
       [ Real-Time Limit & Checkout Decisions ]
```

---

## 3. 10 Rapid-Fire Interview Q&As

1. **Q: Why does CRED need low-latency ML instead of offline batch scoring?**
   - *A:* Real-time checkout (CRED Flash/Pay) requires sub-25ms decisions to prevent payment timeouts; fraud velocity attacks unfold in seconds, not hours.
2. **Q: How do you handle point-in-time feature leakage during model training?**
   - *A:* Use Feast feature store with entity timestamps; features are extracted as-of the exact transaction epoch, strictly forbidding future data lookahead.
3. **Q: What is the difference between ROC-AUC and PR-AUC in fraud detection?**
   - *A:* ROC-AUC evaluates False Positive Rate, which is diluted by millions of true negatives in extreme imbalance ($99.9\%$ legit). PR-AUC focuses exclusively on Precision and Recall over the positive minority class.
4. **Q: How do you choose between LightGBM and Deep Learning for tabular financial data?**
   - *A:* LightGBM consistently outperforms deep networks on tabular structured data due to invariant decision boundaries, handling unnormalized features, and sub-millisecond tree evaluation speed.
5. **Q: What is the mathematical meaning of Hessian $h_i$ in XGBoost logloss?**
   - *A:* For binary logistic loss, $h_i = p_i(1 - p_i)$. It represents the curvature of the loss surface and acts as a certainty-weighting factor.
6. **Q: How do you prevent cold-start credit fraud on newly onboarded users?**
   - *A:* Restrict initial credit limit to low conservative caps, verify device fingerprinting, and enforce step-up KYC verification before credit expansion.
7. **Q: What is the main cause of high tail latency in Python ML microservices?**
   - *A:* Python's Global Interpreter Lock (GIL) preventing true multithreading, and uncontrolled garbage collection (GC) sweeps pausing execution.
8. **Q: How does Triton Inference Server solve the GIL problem?**
   - *A:* Triton runs as an independent C++ process executing compiled C++ backends (ONNX Runtime, TensorRT) with thread pools and dynamic request batching.
9. **Q: What is the primary metric to detect feature drift before it causes default spikes?**
   - *A:* Population Stability Index (PSI). A feature PSI $>0.10$ triggers automated alerts; $>0.25$ triggers retraining.
10. **Q: What happens if a credit risk model denies credit to an honest affluent member?**
    - *A:* High insult rate destroys brand equity. Implement non-blocking step-up biometric/SMS verification rather than hard decline.
