# 03: Financial Intelligence, Credit Risk & Graph Neural Networks

At CRED, data science is the foundational engine of business solvency and risk management. This module breaks down the mathematical economics of credit underwriting, default probability, population stability, and graph neural network fraud detection.

---

## 1. Mathematical Economics of Credit Risk Underwriting

Financial institutions and lending partners (such as IDFC First Bank on CRED Cash) evaluate credit risk using the Basel II regulatory and quantitative framework:

$$\text{Expected Loss (EL)} = \text{PD} \times \text{EAD} \times \text{LGD}$$

1. **Probability of Default (PD):** The statistical likelihood that a borrower fails to meet debt obligations within a designated time horizon (typically 12 months). Modeled using Gradient Boosted Trees (LightGBM/XGBoost) or Logistic Scorecards calibrated to log-odds.
2. **Exposure at Default (EAD):** The total monetary value outstanding when default occurs (e.g. drawn credit line + accrued interest).
3. **Loss Given Default (LGD):** The proportion of exposure that cannot be recovered through collections or legal recourse:
   $$\text{LGD} = 1 - \text{Recovery Rate}$$

### Scorecard Validation Metrics: KS Statistic & Gini
- **Kolmogorov-Smirnov (KS) Statistic:** Measures the maximum vertical separation between the cumulative distribution function (CDF) of good borrowers and bad borrowers (defaulters):
  $$\text{KS} = \max_s |F_{\text{good}}(s) - F_{\text{bad}}(s)|$$
  - In consumer lending, a **KS between 40% and 60%** indicates a highly discriminative model.
- **Gini Coefficient / Somers' D:**
  $$\text{Gini} = 2 \times \text{ROC-AUC} - 1$$
  A model with $\text{AUC} = 0.85$ yields $\text{Gini} = 0.70$.

---

## 2. Population Stability Index (PSI) & Concept Drift

Lending models trained on pre-recession or festival-season data degrade over time. The **Population Stability Index (PSI)** quantifies distribution shift between the baseline development sample ($E_i$) and the live production population ($A_i$):

$$\text{PSI} = \sum_{i=1}^{B} (A_i - E_i) \times \ln\left(\frac{A_i}{E_i}\right)$$

Where $B$ is the number of score/feature buckets (typically 10 deciles), $A_i$ is the actual live percentage, and $E_i$ is the expected development percentage.

| PSI Value | Interpretation | Production Action at CRED |
| :--- | :--- | :--- |
| **$\text{PSI} < 0.10$** | Insignificant shift | Model remains in production with standard monitoring |
| **$0.10 \le \text{PSI} < 0.25$** | Moderate distribution drift | Alert engineering team; trigger shadow model evaluation |
| **$\text{PSI} \ge 0.25$** | Significant population shift | Halt automated limit increases; trigger automated model retraining |

### Python Implementation: PSI Computation
```python
import numpy as np

def calculate_psi(expected: np.ndarray, actual: np.ndarray, num_buckets: int = 10) -> float:
    # Computes the Population Stability Index (PSI) between baseline and production scores.
    percentiles = np.linspace(0, 100, num_buckets + 1)
    cutoffs = np.percentile(expected, percentiles)
    cutoffs[0] -= 1e-5
    cutoffs[-1] += 1e-5

    # Count occurrences in buckets
    expected_counts = np.histogram(expected, bins=cutoffs)[0]
    actual_counts = np.histogram(actual, bins=cutoffs)[0]

    # Convert to proportions with Laplace smoothing to avoid log(0)
    e_pct = np.maximum(expected_counts / len(expected), 1e-4)
    a_pct = np.maximum(actual_counts / len(actual), 1e-4)

    # Calculate PSI
    psi_val = np.sum((a_pct - e_pct) * np.log(a_pct / e_pct))
    return float(psi_val)
```

---

## 3. Real-Time Fraud Detection via Heterogeneous Graph Neural Networks (GNNs)

Organized fraud syndicates bypass individual rule checks by using distinct SIM cards, stolen credit card numbers, and virtual device instances. However, they share topological links across an **Identity & Transaction Graph**:

```
 [User A] ──(Used Device)──> [Device ID: #8f92] <──(Used Device)── [User B]
    │                                                                   │
(Made Txn)                                                         (Made Txn)
    ▼                                                                   ▼
 [Merchant X] <─────────────────(Shared Wi-Fi Subnet)───────────────────┘
```

### GraphSAGE / Relational GCN Formulation
At CRED, graph embedding layers aggregate contextual information across heterogeneous edge types (Card-to-User, User-to-Device, Transaction-to-Merchant).

**Message Passing Equation:**
$$h_v^{(k)} = \sigma\left( W^{(k)} \cdot \left[ h_v^{(k-1)} \;\Vert\; \text{AGGREGATE}\left( \{ h_u^{(k-1)} : u \in \mathcal{N}(v) \} \right) \right] \right)$$

1. **Neighbor Sampling:** During live inference (<15ms), sample a 2-hop neighborhood of size 20 to avoid exponential node explosion.
2. **Aggregation:** Mean or pooling aggregation over neighbor embeddings.
3. **Downstream Classifier:** Concatenate graph structural embedding $h_v$ with tabular transaction features (amount, velocity, time-of-day) and feed into an XGBoost or MLP inference head.

---

## 4. Multi-Tier Feature Serving Architecture

To maintain sub-15ms p99 inference SLAs while computing high-signal features:

| Feature Tier | Refresh Latency | Storage Backend | Example Feature |
| :--- | :--- | :--- | :--- |
| **Hot Features** | <= 5ms | In-Memory Redis (Feast) | user_txns_last_5min, ip_distinct_cards_last_1hr |
| **Warm Features** | 10-25ms | Amazon DynamoDB | user_30day_total_spend, avg_bill_settlement_delay |
| **Cold Features** | Batch (Daily/Weekly) | Snowflake / PostgreSQL | bureau_cibil_score_v3, lifetime_repayment_consistency_ratio |
