# 02: Machine Coding & ML Pipeline Foundations

CRED is famous for its **Machine Coding Round** (often conducted in 90-120 minutes), followed by rigorous questioning on fundamental Machine Learning mathematical formulations.

---

## 1. The Machine Coding Round: Low-Latency Feature Store Registry

### The Problem Prompt
In real-time credit decisioning and fraud detection, feature freshness is critical. Implement an in-memory, thread-safe **Feature Store & Sliding Window Rate Limiter** that can:
1. `record_transaction(user_id, amount, timestamp)`: Ingest a transaction event.
2. `get_feature(user_id, feature_name, window_seconds)`: Compute rolling aggregations (e.g. `TRANSACTION_COUNT`, `TOTAL_SPEND`, `MAX_SPEND`) over arbitrary rolling time windows (e.g., last 60s, last 300s, last 86400s).
3. `is_rate_limited(user_id, max_txns, window_seconds)`: Return boolean if user exceeds velocity thresholds.
4. Provide thread safety, modular architecture, and automatic memory eviction (TTL).

### Production Python Implementation (Thread-Safe with Mutex)
```python
import threading
import time
from collections import defaultdict, deque
from typing import Dict, List, Tuple, Any

class Transaction:
    def __init__(self, amount: float, timestamp: float):
        self.amount = amount
        self.timestamp = timestamp

class FeatureStoreRegistry:
    def __init__(self, ttl_seconds: float = 86400):
        self.ttl = ttl_seconds
        # user_id -> deque of Transaction
        self._user_txns: Dict[str, deque] = defaultdict(deque)
        self._lock = threading.Lock()

    def record_transaction(self, user_id: str, amount: float, timestamp: float = None) -> None:
        if timestamp is None:
            timestamp = time.time()
        
        with self._lock:
            user_deque = self._user_txns[user_id]
            user_deque.append(Transaction(amount, timestamp))
            self._evict_expired(user_deque, timestamp)

    def _evict_expired(self, user_deque: deque, current_time: float) -> None:
        expiry_boundary = current_time - self.ttl
        while user_deque and user_deque[0].timestamp < expiry_boundary:
            user_deque.popleft()

    def get_feature(self, user_id: str, feature_name: str, window_seconds: float, current_time: float = None) -> float:
        if current_time is None:
            current_time = time.time()
        
        with self._lock:
            if user_id not in self._user_txns:
                return 0.0
            
            user_deque = self._user_txns[user_id]
            cutoff = current_time - window_seconds
            
            recent_txns = [t for t in user_deque if t.timestamp >= cutoff]
            
            if not recent_txns:
                return 0.0

            if feature_name == "TRANSACTION_COUNT":
                return float(len(recent_txns))
            elif feature_name == "TOTAL_SPEND":
                return sum(t.amount for t in recent_txns)
            elif feature_name == "MAX_SPEND":
                return max(t.amount for t in recent_txns)
            elif feature_name == "AVG_SPEND":
                return sum(t.amount for t in recent_txns) / len(recent_txns)
            else:
                raise ValueError(f"Unsupported feature: {feature_name}")

    def is_rate_limited(self, user_id: str, max_txns: int, window_seconds: float) -> bool:
        count = self.get_feature(user_id, "TRANSACTION_COUNT", window_seconds)
        return count >= max_txns
```

---

## 2. Core Machine Learning Mathematical Foundations

### 1. Bias-Variance Decomposition (MSE)
For a true function $y = f(x) + \epsilon$ where $\epsilon \sim \mathcal{N}(0, \sigma^2)$, and an estimated model $\hat{f}(x)$:
$$\mathbb{E}[(y - \hat{f}(x))^2] = \text{Bias}^2 + \text{Variance} + \sigma^2$$
- **Bias^2:** Error introduced by approximating complex real-world financial relationships by overly simple models (Underfitting).
- **Variance:** Model sensitivity to small fluctuations in training samples (Overfitting).
- **sigma^2:** Irreducible noise in market transactions and user behavior.

### 2. Regularization Mechanics: L1 (Lasso) vs L2 (Ridge)

| Property | L1 Regularization (Lasso) | L2 Regularization (Ridge) |
| :--- | :--- | :--- |
| **Penalty Term** | $\lambda \sum |w_i|$ | $\frac{\lambda}{2} \sum w_i^2$ |
| **Geometry** | Diamond / Polytope (Sharp corners on axes) | Hypersphere (Smooth circle) |
| **Sparsity** | Produces exact zeros -> **Automated Feature Selection** | Shrinks weights asymptotically toward zero |
| **Bayesian Prior** | Zero-mean Laplace distribution | Zero-mean Gaussian (Normal) distribution |
| **Derivative** | Sign function: $\text{sgn}(w)$ (undefined at $w=0$) | Linear: $w$ |

**CRED Application:** In high-dimensional credit scoring (evaluating 500+ raw transactional features), L1 regularization or CatBoost/LightGBM feature importances are applied to prune co-linear features before production serving.

### 3. Tree Splitting: Gini Impurity vs Entropy vs XGBoost Split Gain
- **Gini Impurity:** $I_G(p) = 1 - \sum p_i^2$
- **Shannon Entropy:** $H(p) = -\sum p_i \log_2(p_i)$
- **XGBoost Second-Order Taylor Expansion:**
  $$\mathcal{L}_{\text{split}} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
  Where $G$ and $H$ are cumulative first and second order gradients.

### 4. Handling Extreme Class Imbalance in Fraud & Default
In credit card fraud, positive class (fraud) is often < 0.1%. Standard binary cross-entropy fails because trivial majority predictions achieve 99.9% accuracy.

**Solutions used at CRED:**
1. **Focal Loss:**
   $$\text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)$$
   The modulating factor $(1 - p_t)^\gamma$ suppresses the loss of easy-to-classify legitimate transactions ($p_t > 0.9$) and forces gradient updates to focus on hard, ambiguous fraud cases.
2. **Cost-Sensitive Learning:**
   Set asymmetric misclassification penalties in XGBoost (`scale_pos_weight = N_neg / N_pos`).
3. **Evaluation Metrics:** Never report accuracy or ROC-AUC alone; use **PR-AUC (Precision-Recall AUC)** and **Top-k Precision at Recall 80%**.
