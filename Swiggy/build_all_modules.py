#!/usr/bin/env python3
"""
build_all_modules.py
Writes all Markdown (.md) and HTML (.html) modules for Swiggy Data Scientist preparation.
"""

import os
import markdown
from template import render_swiggy_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

modules_data = {}

# -------------------------------------------------------------
# Module 00: Company & Role Deep Dive
# -------------------------------------------------------------
modules_data["00_START_HERE"] = {
    "title": "00: Swiggy Company & Role Deep Dive",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Swiggy Company & Role Deep Dive

## 1. Executive Intelligence & Founding Thesis
Swiggy (Bundl Technologies Pvt. Ltd.) was founded in 2014 by **Sriharsha Majety**, **Nandan Reddy**, and **Rahul Jaimini** with a fundamental operational insight:
- **The Delivery Deficit:** Prior to Swiggy, food aggregators (like early Zomato) were mere restaurant discovery directories with decentralized, restaurant-managed deliveries. Delivery times were unpredictable ($>60$ minutes), tracking was non-existent, and order cancellation was rampant.
- **The Full-Stack Logistics Model:** Swiggy brought delivery fleet in-house, implementing a dedicated, algorithmic fleet of Delivery Executives (DEs). Controlling both the digital storefront and physical last-mile fulfillment transformed reliability and lowered delivery times to under 30 minutes.
- **The Hyperlocal Density Flywheel:**
  - Higher order density in a geographic cell (Uber H3 hexagon).
  - Shorter delivery partner travel distances between orders.
  - Higher completed orders per delivery executive hour (utilization rate).
  - Lower delivery fulfillment cost per order.
  - Reduced consumer delivery charges & improved merchant payout.
  - Accelerates order volume and repeat customer stickiness.

---

## 2. Business Ecosystem & Verticals

| Business Vertical | Core Offering | Key Operational Constraints | Data Science & ML Opportunities |
| :--- | :--- | :--- | :--- |
| **Food Marketplace** | Hyperlocal restaurant food discovery & doorstep delivery | Perishable food quality, dynamic kitchen preparation variance, peak rush-hour demand spikes | 4-Stage dynamic ETA prediction, combinatorial order batching, personalized dish recommendations, multi-task ranking (CTR, CVR) |
| **Instamart** | Quick-commerce grocery & daily essentials delivery ($<10$ mins) | High-density dark stores (micro-fulfillment centers), inventory perishability, rapid in-store picking SLA ($<150$s) | Hyperlocal SKU demand forecasting, automated stock replenishment, dark store layout & picker TSP pathfinding |
| **Swiggy Dineout** | Table reservations, exclusive discounts, and bill pay at dining venues | Real-time table inventory availability, merchant yield management | Personalized dining discovery, dynamic discount optimization, churn prediction |
| **Swiggy Genie / Minis** | Hyperlocal point-to-point courier service & creator D2C storefronts | Asymmetric pickup-drop locations, unpredictable cargo dimensions | Dynamic routing, courier capacity allocation, fraud detection |

---

## 3. Scale Metrics & Technical Topology

```
                              ┌──────────────────────────────────────────────────┐
                              │            Swiggy Mobile Client (React Native)   │
                              └────────────────────────┬─────────────────────────┘
                                                       │ HTTPS / gRPC
                                                       ▼
                              ┌──────────────────────────────────────────────────┐
                              │        Kong / Envoy API Gateway & Routing        │
                              └───────────┬──────────────────────────┬───────────┘
                                          │                          │
                                          ▼                          ▼
                              ┌───────────────────────┐  ┌───────────────────────┐
                              │ Order & Dispatch Core │  │  Search & Reco Engine │
                              │    (Go / Java)        │  │     (Python / Ray)    │
                              └───────────┬───────────┘  └───────────┬───────────┘
                                          │ Real-Time Events         │
                                          ▼                          ▼
                              ┌──────────────────────────────────────────────────┐
                              │              Apache Kafka Event Bus              │
                              └───────────┬──────────────────────────┬───────────┘
                                          │                          │
                     ┌────────────────────┴────────┐        ┌────────┴─────────────────────┐
                     ▼                             ▼        ▼                              ▼
          ┌─────────────────────┐       ┌──────────────────────┐               ┌───────────────────────┐
          │ Apache Flink Stream │       │ Feast Feature Store  │               │ Triton / Ray Serving  │
          │ (Rolling aggregates)│       │ (Redis Cluster <5ms) │               │ (Quantized ML Models) │
          └──────────┬──────────┘       └──────────┬───────────┘               └───────────┬───────────┘
                     │                             │                                       │
                     └─────────────────────────────┼───────────────────────────────────────┘
                                                   ▼
                                        ┌──────────────────────┐
                                        │ Apache Iceberg / S3  │
                                        │ Data Lakehouse       │
                                        └──────────────────────┘
```

- **Scale Numbers:**
  - $3.5\text{B}+$ cumulative orders delivered across $600+$ Indian cities.
  - $300,000+$ active monthly Delivery Executives.
  - $250,000+$ registered restaurant and merchant partners.
  - Peak handling of $>120,000$ orders per minute during major festivals and ICC Cricket World Cup events.
- **Latency SLAs:**
  - $<25$ms p99 inference latency for customer ETA queries on the checkout screen.
  - Continuous background batching & dispatch solver cycle running every $15$ to $30$ seconds per geographic cluster.
- **Tech Stack:**
  - **Core Languages:** Python (NumPy, SciPy, Pandas, PyTorch), SQL (Trino, PostgreSQL, SparkSQL), C++, Go.
  - **ML Frameworks:** PyTorch, XGBoost, LightGBM, Scikit-learn, Ray, PyTorch Geometric (GNNs).
  - **Geospatial & Operations Research:** Uber H3 hexagonal spatial indexing, Google OR-Tools, NetworkX, OSRM (Open Source Routing Machine).
  - **Streaming & Storage:** Apache Kafka, Apache Flink, Redis, Amazon DynamoDB, Apache Iceberg, Snowflake.

---

## 4. On-Campus Placement Details (NIT Rourkela)

- **Job Role:** Data Scientist (FTE)
- **Target Batch:** 2027 (B.Tech, M.Tech, Dual Degree, Int. M.Sc.)
- **Total Compensation (CTC):** ₹26.00 LPA
  - **Base / Fixed Salary:** ₹18.00 LPA
  - **ESOPs (Employee Stock Options):** ₹8.00 Lakhs (vested over 4 years)
- **Eligibility:** CGPA $\ge 6.5$, No active backlogs.
- **Deadline:** 11:59 PM, 17th September 2026.

---

## 5. The Exact On-Campus Hiring Blueprint

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 1: Resume Shortlisting & Screening                                                    │
│   • Keyword scoring: Machine learning, spatial graphs, optimization, Python, SQL, GNNs      │
│   • Core differentiator: Warehouse PathMapper (logistics routing) & time-series signal noise│
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 2: Online Assessment (OA) — HackerEarth / Mettl (90–105 Mins)                         │
│   • 2 DSA / Algorithmic Coding Problems (Interval Scheduling, Bipartite Graphs, Bitmask DP)  │
│   • 15–20 MCQs: Probability, Statistics, Gradient Boosted Tree Splitting Math, SQL Windows   │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 3: Technical Round 1: DSA, Python & ML Foundations (60 Mins)                          │
│   • Live coding of DSA or data manipulation (Pandas / NumPy vectorization).                  │
│   • Mathematical derivation of XGBoost objective function and Taylor series expansion.       │
│   • Quantile regression loss (Pinball loss) and evaluation metrics (MAPE, RMSE, Coverage).   │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 4: Technical Round 2: ML System Design & Swiggy Case Study (60 Mins)                  │
│   • End-to-end design: Real-time 4-stage ETA prediction system or Dispatch Batching engine.  │
│   • Grilling of candidate projects: Deep dive into Warehouse PathMapper and heuristic grids. │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ Stage 5: Hiring Manager & Culture Round (45 Mins)                                           │
│   • Swiggy Leadership Principles: Customer First, Always Curious, Bias for Action.          │
│   • Behavioral situational questions (STAR framework) and architectural trade-offs.         │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```
"""
}

# -------------------------------------------------------------
# Module 01: Signature OA Coding Problems
# -------------------------------------------------------------
modules_data["01_Online_Test"] = {
    "title": "01: Signature OA Coding Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company Deep Dive",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: Machine Coding & ML Pipeline",
    "markdown": """# 01: Signature OA Coding Problems

Swiggy's Online Assessment features algorithmic challenges inspired by hyperlocal logistics: geospatial graph bipartite matching, interval scheduling for kitchen capacity, and dark-store pick route optimization.

---

## Problem 1: Optimal Bipartite Rider-to-Order Dispatch

### Problem Statement
Given $M$ pending orders with pickup coordinates $[rx_i, ry_i]$ and ready timestamps $T_i$, and $N$ active delivery partners located at $[dx_j, dy_j]$ with speed $S_j$. 
Each delivery partner can accept at most 1 order. Travel time between points $(x_1, y_1)$ and $(x_2, y_2)$ is defined by Manhattan distance divided by speed:
$$\\text{time}(i, j) = \\frac{|rx_i - dx_j| + |ry_i - dy_j|}{S_j}$$
If a delivery partner arrives before food ready time $T_i$, they wait until $T_i$. Total delay penalty for an order is:
$$\\text{Penalty}(i, j) = \\max(0, \\text{time}(i, j) - T_i) + 0.5 \\times \\text{time}(i, j)$$
Find the global assignment of riders to orders that minimizes the sum of delay penalties for all matched orders, ensuring at least $\\min(M, N)$ orders are dispatched.

### Python 3 Solution (Min-Cost Max-Flow / Hungarian Equivalent via SciPy)
```python
import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_dispatch(orders, riders):
    \"\"\"
    orders: list of dicts [{'rx': float, 'ry': float, 'ready_t': float}]
    riders: list of dicts [{'dx': float, 'dy': float, 'speed': float}]
    Returns: list of (order_idx, rider_idx, cost), total_cost
    \"\"\"
    M = len(orders)
    N = len(riders)
    
    # Cost matrix C of dimension M x N
    cost_matrix = np.zeros((M, N), dtype=np.float64)
    
    for i in range(M):
        rx, ry, ready_t = orders[i]['rx'], orders[i]['ry'], orders[i]['ready_t']
        for j in range(N):
            dx, dy, speed = riders[j]['dx'], riders[j]['dy'], riders[j]['speed']
            travel_time = (abs(rx - dx) + abs(ry - dy)) / speed
            delay = max(0.0, travel_time - ready_t)
            cost_matrix[i, j] = delay + 0.5 * travel_time

    # Hungarian Algorithm (Modified Jonker-Volgenant) O(min(M,N) * M * N)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    matches = []
    total_cost = 0.0
    for r, c in zip(row_ind, col_ind):
        matches.append((int(r), int(c), float(cost_matrix[r, c])))
        total_cost += cost_matrix[r, c]
        
    return matches, total_cost
```

### C++20 Solution (Successive Shortest Path with SPFA / Dijkstra Potentials)
```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <numeric>
#include <iomanip>

struct Edge {
    int to;
    int capacity;
    int flow;
    double cost;
    int rev;
};

class MinCostMaxFlow {
    int n;
    std::vector<std::vector<Edge>> adj;
    std::vector<double> dist, potential;
    std::vector<int> parent_edge, parent_node;

public:
    MinCostMaxFlow(int nodes) : n(nodes), adj(nodes), dist(nodes), potential(nodes, 0.0),
                                parent_edge(nodes), parent_node(nodes) {}

    void add_edge(int from, int to, int cap, double cost) {
        adj[from].push_back({to, cap, 0, cost, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, -cost, (int)adj[from].size() - 1});
    }

    std::pair<int, double> solve(int src, int sink) {
        int flow = 0;
        double cost = 0;
        const double INF = 1e18;

        while (true) {
            std::fill(dist.begin(), dist.end(), INF);
            std::priority_queue<std::pair<double, int>, 
                                std::vector<std::pair<double, int>>, 
                                std::greater<>> pq;

            dist[src] = 0.0;
            pq.push({0.0, src});

            while (!pq.empty()) {
                auto [d, u] = pq.top();
                pq.pop();
                if (d > dist[u]) continue;

                for (int i = 0; i < (int)adj[u].size(); ++i) {
                    const Edge& e = adj[u][i];
                    if (e.capacity - e.flow > 0) {
                        double red_cost = e.cost + potential[u] - potential[e.to];
                        if (dist[e.to] > dist[u] + red_cost + 1e-9) {
                            dist[e.to] = dist[u] + red_cost;
                            parent_node[e.to] = u;
                            parent_edge[e.to] = i;
                            pq.push({dist[e.to], e.to});
                        }
                    }
                }
            }

            if (dist[sink] >= INF - 1e-4) break;

            for (int i = 0; i < n; ++i) {
                if (dist[i] < INF) potential[i] += dist[i];
            }

            int push = 1; // unit capacity match
            flow += push;
            cost += push * potential[sink];

            for (int curr = sink; curr != src; curr = parent_node[curr]) {
                int p = parent_node[curr];
                int idx = parent_edge[curr];
                adj[p][idx].flow += push;
                adj[curr][adj[p][idx].rev].flow -= push;
            }
        }
        return {flow, cost};
    }
};
```

---

## Problem 2: Kitchen Capacity & Delay Cascade Detection

### Problem Statement
A restaurant kitchen has $K$ cooking burners. Each order $i$ requires cooking continuously from $start_i$ to $end_i$ with burner requirement $b_i$. If incoming orders exceed capacity $K$, lower-priority orders are queued, delaying subsequent deliveries.
Given $N$ orders with tuples $[start_i, end_i, b_i, priority_i]$, determine:
1. Peak simultaneous burner utilization.
2. The exact timestamps where capacity $K$ was breached.

### Python 3 Solution (Sweep-Line Event Processing)
```python
def analyze_kitchen_capacity(orders, K):
    \"\"\"
    orders: list of [start, end, burners, priority]
    K: total available burners
    Returns: peak_burners, breach_intervals
    \"\"\"
    events = []
    for idx, (s, e, b, p) in enumerate(orders):
        events.append((s, +b, idx))  # order starts cooking
        events.append((e, -b, idx))  # order finishes

    # Sort events by time; on tie, process end (-b) before start (+b)
    events.sort(key=lambda x: (x[0], x[1]))

    current_load = 0
    peak_load = 0
    breaches = []
    in_breach = False
    breach_start = None

    for t, delta_b, idx in events:
        current_load += delta_b
        peak_load = max(peak_load, current_load)

        if current_load > K and not in_breach:
            in_breach = True
            breach_start = t
        elif current_load <= K and in_breach:
            in_breach = False
            breaches.append((breach_start, t))

    return peak_load, breaches
```

---

## Problem 3: Signature Swiggy SQL Window Questions

### Challenge A: Rolling 7-Day Rider Utilization & Idle Ratio
Calculate each delivery partner's 7-day rolling average of completed orders and their idle ratio.

```sql
WITH daily_stats AS (
    SELECT 
        de_id,
        order_date,
        COUNT(order_id) AS completed_orders,
        SUM(login_duration_mins) AS total_login_mins,
        SUM(active_trip_duration_mins) AS active_trip_mins
    FROM delivery_executive_logs
    GROUP BY de_id, order_date
),
rolling_metrics AS (
    SELECT 
        de_id,
        order_date,
        completed_orders,
        ROUND(AVG(completed_orders) OVER (
            PARTITION BY de_id 
            ORDER BY order_date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS rolling_7d_avg_orders,
        ROUND(
            (SUM(total_login_mins - active_trip_mins) OVER (
                PARTITION BY de_id 
                ORDER BY order_date 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ) * 100.0) / 
            NULLIF(SUM(total_login_mins) OVER (
                PARTITION BY de_id 
                ORDER BY order_date 
                ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
            ), 0), 2
        ) AS rolling_7d_idle_pct
    FROM daily_stats
)
SELECT * 
FROM rolling_metrics
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY de_id, order_date DESC;
```

### Challenge B: Detecting Persistent Kitchen Delay Outliers
Identify restaurant branches where the 90th percentile food prep time exceeds the promised standard SLA by $>15$ minutes over the last 14 days.

```sql
WITH order_delays AS (
    SELECT 
        restaurant_id,
        cuisine_type,
        DATE(placed_at) AS order_day,
        prep_time_minutes,
        standard_sla_minutes,
        (prep_time_minutes - standard_sla_minutes) AS delay_minutes,
        PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY prep_time_minutes) OVER (
            PARTITION BY restaurant_id, DATE(placed_at)
        ) AS p90_prep_time
    FROM food_orders
    WHERE placed_at >= CURRENT_DATE - INTERVAL '14 days'
)
SELECT 
    restaurant_id,
    cuisine_type,
    ROUND(AVG(p90_prep_time), 1) AS avg_p90_prep_time,
    ROUND(AVG(standard_sla_minutes), 1) AS avg_promised_sla,
    COUNT(DISTINCT order_day) AS days_with_severe_breach
FROM order_delays
WHERE (p90_prep_time - standard_sla_minutes) > 15
GROUP BY restaurant_id, cuisine_type
HAVING COUNT(DISTINCT order_day) >= 5
ORDER BY days_with_severe_breach DESC, avg_p90_prep_time DESC;
```
"""
}

# -------------------------------------------------------------
# Module 02: Machine Coding & ML Pipeline
# -------------------------------------------------------------
modules_data["02_Technical_Rounds"] = {
    "title": "02: Machine Coding & ML Pipeline",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Coding",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Swiggy Bytes & 4-Stage ETA",
    "markdown": """# 02: Machine Coding & ML Pipeline

In Technical Round 1, Swiggy assesses mathematical rigor in ML theory, custom scikit-learn transformers, and low-level understanding of Gradient Boosted Decision Trees.

---

## 1. End-to-End Production ETA Regressor with Quantile Loss

Swiggy provides customers with a delivery window (e.g. "30–40 mins") rather than a single point estimate. This requires **Quantile Regression (Pinball Loss)**:

$$L_q(y, \\hat{y}) = \\max(q(y - \\hat{y}), (1-q)(\\hat{y} - y)) = (y - \\hat{y})(q - \\mathbb{I}_{y < \\hat{y}})$$

For $q = 0.10$ (10th percentile, lower bound) and $q = 0.90$ (90th percentile, upper bound), the interval $[\hat{y}_{0.1}, \hat{y}_{0.9}]$ gives an empirical 80% confidence interval.

```python
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import lightgbm as lgb
from sklearn.metrics import mean_pinball_loss, mean_absolute_error

class SwiggyFeatureEngineering(BaseEstimator, TransformerMixin):
    \"\"\"
    Production feature pipeline:
    - Cyclical encoding of hour of day and day of week.
    - Haversine distance computation between DE, Restaurant, and Customer.
    - Smoothed Target Encoding for Restaurant IDs with empirical Bayes shrinkage.
    \"\"\"
    def __init__(self, smoothing_weight=10.0):
        self.smoothing_weight = smoothing_weight
        self.restaurant_stats_ = {}
        self.global_mean_ = 0.0

    def fit(self, X, y):
        df = X.copy()
        df['target'] = y
        self.global_mean_ = float(y.mean())
        
        # Smoothed target encoding: S_i = (n_i * mean_i + m * global_mean) / (n_i + m)
        stats = df.groupby('restaurant_id')['target'].agg(['count', 'mean'])
        smooth = (stats['count'] * stats['mean'] + self.smoothing_weight * self.global_mean_) / (stats['count'] + self.smoothing_weight)
        self.restaurant_stats_ = smooth.to_dict()
        return self

    def transform(self, X):
        df = X.copy()
        
        # Cyclical temporal features
        hour = df['order_hour'].values
        df['hour_sin'] = np.sin(2 * np.pi * hour / 24.0)
        df['hour_cos'] = np.cos(2 * np.pi * hour / 24.0)
        
        dow = df['order_dow'].values
        df['dow_sin'] = np.sin(2 * np.pi * dow / 7.0)
        df['dow_cos'] = np.cos(2 * np.pi * dow / 7.0)
        
        # Vectorized Haversine distance
        lat1, lon1 = np.radians(df['rest_lat']), np.radians(df['rest_lon'])
        lat2, lon2 = np.radians(df['cust_lat']), np.radians(df['cust_lon'])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
        c = 2 * np.arcsin(np.sqrt(a))
        df['haversine_km'] = 6371.0 * c
        
        # Apply target encoding
        df['rest_encoded_duration'] = df['restaurant_id'].map(self.restaurant_stats_).fillna(self.global_mean_)
        
        feature_cols = [
            'haversine_km', 'hour_sin', 'hour_cos', 'dow_sin', 'dow_cos',
            'rest_encoded_duration', 'kitchen_active_orders', 'rain_mm_per_hr'
        ]
        return df[feature_cols].values

class SwiggyQuantileETAPipeline:
    def __init__(self, quantiles=[0.1, 0.5, 0.9]):
        self.quantiles = quantiles
        self.fe = SwiggyFeatureEngineering()
        self.models = {}

    def fit(self, X_train, y_train):
        features = self.fe.fit_transform(X_train, y_train)
        
        for q in self.quantiles:
            reg = lgb.LGBMRegressor(
                objective='quantile',
                alpha=q,
                n_estimators=300,
                learning_rate=0.05,
                num_leaves=31,
                random_state=42,
                n_jobs=-1
            )
            reg.fit(features, y_train)
            self.models[q] = reg

    def predict_interval(self, X_test):
        features = self.fe.transform(X_test)
        preds = {}
        for q, model in self.models.items():
            preds[f'p{int(q*100)}'] = model.predict(features)
        return pd.DataFrame(preds)
```

---

## 2. Gradient Boosted Trees: Mathematical Split Derivation (XGBoost)

During technical grilling, Swiggy interviewers demand exact derivations of tree split criteria.

### Objective Function with Second-Order Taylor Expansion
Given training dataset $\mathcal{D} = \{(x_i, y_i)\}$, at step $t$, the objective is:
$$\mathcal{L}^{(t)} = \sum_{i=1}^n l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) + \Omega(f_t)$$
Where tree complexity penalty is:
$$\Omega(f_t) = \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$$
Expanding $l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i))$ via 2nd-order Taylor series around $\hat{y}_i^{(t-1)}$:
$$l(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) \approx l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2}h_i f_t^2(x_i)$$
Where:
$$g_i = \frac{\partial l(y_i, \hat{y}^{(t-1)})}{\partial \hat{y}^{(t-1)}}, \quad h_i = \frac{\partial^2 l(y_i, \hat{y}^{(t-1)})}{\partial (\hat{y}^{(t-1)})^2}$$

Removing constant terms:
$$\tilde{\mathcal{L}}^{(t)} = \sum_{j=1}^T \left[ \left(\sum_{i \in I_j} g_i\right) w_j + \frac{1}{2}\left(\sum_{i \in I_j} h_i + \lambda\right) w_j^2 \right] + \gamma T$$
Defining $G_j = \sum_{i \in I_j} g_i$ and $H_j = \sum_{i \in I_j} h_i$:
$$\tilde{\mathcal{L}}^{(t)} = \sum_{j=1}^T \left[ G_j w_j + \frac{1}{2}(H_j + \lambda) w_j^2 \right] + \gamma T$$

### Optimal Leaf Weight $w_j^*$
Taking derivative with respect to $w_j$ and setting to zero:
$$\frac{\partial \tilde{\mathcal{L}}^{(t)}}{\partial w_j} = G_j + (H_j + \lambda)w_j = 0 \implies w_j^* = -\frac{G_j}{H_j + \lambda}$$

Substituting $w_j^*$ back gives the minimum loss for fixed structure:
$$\mathcal{L}^* = -\frac{1}{2}\sum_{j=1}^T \frac{G_j^2}{H_j + \lambda} + \gamma T$$

### Tree Split Evaluation Gain Formula
When considering splitting a leaf into Left ($L$) and Right ($R$) subsets:
$$\text{Gain} = \frac{1}{2}\left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$
If $\text{Gain} \le 0$, the split is pruned.
"""
}

# -------------------------------------------------------------
# Module 03: Swiggy Bytes & 4-Stage ETA
# -------------------------------------------------------------
modules_data["03_Domain_Deep_Dive"] = {
    "title": "03: Swiggy Bytes & 4-Stage ETA",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: Machine Coding & ML Pipeline",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Candidate Resume Defense",
    "markdown": """# 03: Swiggy Bytes & 4-Stage ETA Architecture

Swiggy's tech engineering blog (*Swiggy Bytes*) reveals that holistic end-to-end delivery estimation cannot be treated as a naive single-shot regression model. Instead, it is partitioned into four decoupled, statistically modeled stages.

---

## 1. The 4-Stage ETA Decomposition

$$\mathbf{T_{\text{ETA}}} = \mathbf{T_{\text{O2A}}} + \mathbf{T_{\text{FM}}} + \mathbf{T_{\text{WT}}} + \mathbf{T_{\text{LM}}}$$

```
Order Placed (t=0)
   │
   ├─► Stage 1: T_O2A (Ordered to Assignment)
   │     • Matching delay: Finding the optimal delivery partner
   │
   ├─► Stage 2: T_FM (First Mile Travel)
   │     • DE travels from current location to restaurant
   │
   ├─► Stage 3: T_WT (Kitchen Wait Time)
   │     • Kitchen prep wildcard: Time until food is bagged and ready
   │
   └─► Stage 4: T_LM (Last Mile Travel & Doorstep)
         • Travel from restaurant to customer gate + vertical elevation
```

### Breakdown of Each Stage

| Stage | Name | Key Modeling Complexities | Feature Inputs & Techniques |
| :--- | :--- | :--- | :--- |
| **$T_{\text{O2A}}$** | Ordered to Assignment | Fleet availability in the H3 cell, rider acceptance probability, batching potential | Available idle riders within radius $R$, surge multiplier, historical acceptance rate |
| **$T_{\text{FM}}$** | First Mile | Real-time traffic, U-turns, flyover congestion, DE vehicle type | OSRM road graph shortest path, real-time GPS speed delta, rain intensity |
| **$T_{\text{WT}}$** | Kitchen Wait Time | The "Wildcard": Kitchen backlog, complexity of dishes, live in-dining crowd | Active kitchen orders, dish prep time embeddings, historical restaurant delay curves |
| **$T_{\text{LM}}$** | Last Mile & Handover | Road traffic, gate entry delay, high-rise elevator waiting | Road distance, Uber H3 customer hex, apartment gate entry barrier score |

---

## 2. Dynamic Dispatch & Combinatorial Batching

Swiggy solves the **Vehicle Routing Problem with Time Windows (VRPTW)**. When order volume surges, assigning 1 rider per order collapses unit economics. Swiggy groups multiple orders ($2$ or $3$) to one Delivery Executive.

### Batching Feasibility Matrix
Two orders $O_1 = (P_1, D_1)$ and $O_2 = (P_2, D_2)$ can be batched only if:
1. **Spatial Proximity:** Pickups $P_1$ and $P_2$ are within 800m of each other or share the same food court.
2. **Temporal Alignment:** Ready times satisfy $|Ready(O_1) - Ready(O_2)| \le 7\text{ minutes}$.
3. **Detour & Freshness Bound:**
   $$T_{\text{delivered}}(O_1 | \text{batched}) - T_{\text{delivered}}(O_1 | \text{single}) \le \Delta_{\max} \quad (\Delta_{\max} \approx 8\text{ mins})$$
4. **Thermal Constraints:** Hot items cannot be paired with ice cream / cold beverages without thermal segregation bags.

---

## 3. Instamart Dark Store Operations & TSP Picking

Instamart delivers groceries in $<10$ minutes by operating micro-fulfillment centers (MFCs / Dark Stores):
- **Store Layout Optimization (ABC Analysis):**
  - **Category A (Top 10% Fast-Moving SKUs e.g. milk, bread, onions):** Positioned within 5 meters of the checkout packing station.
  - **Category B (Medium velocity):** Placed in middle aisles.
  - **Category C (Long-tail items e.g. specialty spices, electronics accessories):** Placed in deep aisles.
- **In-Store Picking Path Optimization:**
  - When an order contains $K = 15$ SKUs, the picker app generates an exact single-direction serpentine traversal path through the dark store aisles, reducing total walking distance by 42% and keeping in-store pick-and-pack time under 150 seconds.

---

## 4. Dynamic Surge Pricing & Geospatial Equilibrium

Swiggy divides cities into hierarchical hexagonal grids using **Uber H3 (Resolution 8 & 9)**.
- Each H3 cell calculates real-time supply-demand ratio:
  $$\text{Ratio}(h_i, t) = \frac{\text{Active Orders}(h_i, t)}{\text{Available Drivers}(h_i, t) + \epsilon}$$
- **Price Elasticity of Demand:**
  $$\varepsilon = \frac{\% \Delta Q}{\% \Delta P}$$
  Surge pricing dynamically increases delivery fee to depress non-urgent demand while broadcasting financial incentives (boost pay) to lure idle riders from adjacent H3 cells into deficit zones.
"""
}

# -------------------------------------------------------------
# Module 04: Candidate Resume Defense
# -------------------------------------------------------------
modules_data["04_Candidate_Resume_Grilling"] = {
    "title": "04: Candidate Resume Defense",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Swiggy Bytes & 4-Stage ETA",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: Real-Time ML System Design",
    "markdown": """# 04: Candidate Resume Defense

Tailored defense strategies for **Adarsh Saurabh** (M.Tech Signal & Image Processing @ NIT Rourkela, B.Tech CSE). Interviewers at Swiggy will probe project scalability, algorithmic limits, and theoretical connections to hyperlocal food delivery.

---

## 1. Project Defense: IBYD Technology — Warehouse PathMapper (Mandatory)

### Elevator Pitch to Swiggy
> *"In Warehouse PathMapper, I developed a high-throughput spatial routing engine for industrial facilities. I modeled massive topological grids ($10,000 \\times 10,000$) as directed spatial graphs, executing multi-point heuristic trajectory optimization through 10,000+ coordinates simultaneously in under 0.5 seconds on standard CPU. This directly mirrors Swiggy’s logistics challenges: both Instamart’s in-store dark-store pick routing and city-scale multi-drop dispatch batching over hexagonal H3 spatial grids."*

### Trap 1: "A 2D warehouse grid is simple. City road networks are directed, non-planar, and experience dynamic traffic. How does your grid heuristic apply to Swiggy?"
- **Candidate Defense:**
  1. **Direct Application to Instamart:** Instamart dark stores are literally high-density warehouse grids where pickers must collect multi-SKU orders within 150 seconds. My algorithm solves the exact NP-hard Traveling Salesperson Problem (TSP) with obstacle avoidance for store aisles.
  2. **Hierarchical Abstraction on City Graphs:** For city-level routing, raw road networks (OSRM) are too expensive to compute globally in real-time dispatch loops. Swiggy aggregates road coordinates into Uber H3 hexagonal grid cells (Resolution 8/9). The inter-cell transitions form a grid-graph topology where heuristic search algorithms (A*, Jump Point Search, Contraction Hierarchies) prune search spaces by $>95\%$.

### Trap 2: "What heuristics did you use, and did you guarantee admissibility?"
- **Candidate Defense:**
  - For Euclidean distance $h(u, v) = \sqrt{(x_u - x_v)^2 + (y_u - y_v)^2}$, the heuristic is strictly admissible ($h(u, v) \le d^*(u, v)$) and monotonic/consistent, ensuring that the first time a node is expanded in A*, its optimal path is found without reopening nodes.
  - To achieve $<0.5$s execution across 10,000 coordinates, I implemented **Hierarchical Pathfinding (HPA\*)**: partitioning the $10,000 \times 10,000$ grid into $64 \times 64$ macro-clusters, precomputing border-to-border transitions, and executing heuristic search on the abstracted macro-graph before refining local paths.

---

## 2. Project Defense: Autobot Robotics (ML Intern)

### Trap: "You processed robotic sensor telemetry. How does that relate to delivery partner mobile signals?"
- **Candidate Defense:**
  - Both domains suffer from **noisy, high-frequency spatial telemetry**. Delivery executive mobile GPS in urban Indian cities (e.g. Bangalore, Mumbai) suffers from severe multipath interference, satellite shadow between skyscrapers, and battery-saver GPS throttling.
  - At Autobot Robotics, I handled sensor noise filtering using **Discrete Kalman Filters** and moving window variance thresholds.
  - At Swiggy, this exact mathematical foundation is required for **Map Matching**: taking raw, jittery GPS coordinates $(lat, lon)$ and projecting them onto the underlying directed road graph using Hidden Markov Models (HMM) with emission and transition probabilities based on road speed limits.

---

## 3. Project Defense: Alternative Data Radar

### Connection to Swiggy
- Scraped corporate and pricing signals mapped directly to:
  - Competitive price scraping of rival food delivery and quick commerce catalogs.
  - Detecting restaurant menu price inflation on delivery platforms vs in-store dining.
  - Real-time indexing of local events, concerts, and weather alerts that cause sudden localized demand surges.

---

## 4. Academic Background: M.Tech Signal Processing Advantage

### Trap: "You are an M.Tech in Signal & Image Processing. Why should Swiggy hire you over a pure Computer Science graduate for Data Science?"
- **Candidate Defense:**
  - *"Machine Learning at scale is applied statistical estimation. In Signal Processing, we treat telemetry not as static database rows, but as continuous, non-stationary stochastic signals.
  - Concepts like **Fourier & Wavelet analysis** provide deep mathematical grounding for decomposing seasonal demand into trend, daily cycles, and high-frequency noise.
  - **Kalman Filtering and State-Space Models** are the optimal estimators for tracking real-time delivery rider trajectories and battery-efficient location extrapolation.
  - Combined with my B.Tech in Computer Science, I possess both the low-level systems engineering capability (DSA, C++, SQL) and advanced mathematical rigor (linear algebra, probability, optimization) necessary for production Data Science at Swiggy."*
"""
}

# -------------------------------------------------------------
# Module 05: Real-Time ML System Design
# -------------------------------------------------------------
modules_data["05_System_Design_or_HIL"] = {
    "title": "05: Real-Time ML System Design",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Candidate Resume Defense",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Life at Swiggy & Culture",
    "markdown": """# 05: Real-Time ML System Design

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
  - Latency: Pure model execution completes in $1.8\text{ms}$ per request.

---

## 5. Resiliency, Graceful Degradation & Circuit Breaking

When incoming traffic surges $5\times$ during rainstorms or server failure occurs:
1. **Tier 1 (Normal Operation):** Full 4-stage ML model inference with live Redis features.
2. **Tier 2 (Degraded Mode - Redis Latency $>15$ms):** Bypass real-time feature lookup; fallback to static H3 lookup tables (historical median ETAs for that hour and day).
3. **Tier 3 (Complete Inference Crash):** Circuit breaker (Resilience4j) trips; returns rule-based deterministic formula:
   $$\text{ETA} = \text{Default Prep Time (20m)} + \frac{\text{Haversine Distance}}{15\text{ km/h}} \times 60$$
4. **Data Drift & Concept Drift Monitoring:**
   - Asynchronous Kafka logger captures $(\mathbf{x}, \hat{y})$ pairs alongside ground-truth actual delivery time $y$.
   - Flink streams actual vs predicted differences to **Evidently AI / MLflow**.
   - If Kolmogorov-Smirnov (KS) test or Population Stability Index ($\text{PSI} \ge 0.25$), an automated pipeline alert is triggered for retraining.
"""
}

# -------------------------------------------------------------
# Module 06: Managerial & Cultural Values
# -------------------------------------------------------------
modules_data["06_Managerial_and_HR"] = {
    "title": "06: Life at Swiggy & Cultural Values",
    "prev_link": "05_System_Design_or_HIL.html",
    "prev_title": "05: Real-Time ML System Design",
    "next_link": "07_Quick_Reference.html",
    "next_title": "07: CheatSheet & Formula Vault",
    "markdown": """# 06: Life at Swiggy & Cultural Values

Swiggy assesses cultural alignment through its **Core Leadership Values**. Candidates must demonstrate a founder's mindset, customer empathy, and comfort with rapid experimentation.

---

## 1. Swiggy's Core Leadership Values

1. **Consumer Comes First:** In any conflict between short-term monetization and customer trust, customer trust wins. (e.g. accurate ETAs are better than unrealistically short ETAs that cause frustration).
2. **Always Curious, Always Learning:** Relentlessly experimenting with new AI architectures (GNNs, two-tower embeddings, LLM agentic search).
3. **Bias for Action:** In fast-paced hyperlocal markets, speed is of the essence. Perfect is the enemy of good. Deploy, measure, and iterate.
4. **Displaying Founder's Mentality:** Taking extreme ownership. If deliveries fail during torrential rain, you don't blame the weather; you optimize geospatial routing.
5. **Think Win-Win:** Balancing the delicate three-sided marketplace: Customers, Delivery Partners, and Restaurant Partners.
6. **Honest, Transparent Communication:** Being intellectually honest about model flaws and evaluation metrics.

---

## 2. STAR Behavioral Defense Scenarios for Adarsh Saurabh

### Question 1: "Tell me about a time you faced ambiguous technical requirements and had to deliver on a deadline."
- **Situation:** During the development of *Uplan* (Multi-Agent System for Document Verification), our goal was to verify complex cross-document constraints, but there was no labeled dataset or standard ground truth benchmark.
- **Task:** I needed to architect an automated, reliable verification pipeline within the 48-hour hackathon timeframe.
- **Action:** Instead of chasing complex fine-tuning without data, I exercised a strong *Bias for Action*. I architected an adversarial multi-agent system using LangGraph: one agent acted as an extraction specialist, while an auditor agent checked for mathematical consistency and hallucination flags. To ensure deterministic accuracy, I engineered a graph-encoding layer that compressed metadata into semantic representations.
- **Result:** Cut manual auditing overhead by 85% with explainable failure rebuttals, winning recognition at the AMD Developer Hackathon.

### Question 2: "Describe a situation where you had to make a trade-off between model accuracy and system latency."
- **Situation:** In *Warehouse PathMapper*, calculating the exact globally optimal TSP trajectory across 10,000 coordinates using mixed-integer linear programming (MILP) took several minutes per calculation, making it useless for real-time interactive routing.
- **Task:** Balance the path optimality against a sub-second execution requirement.
- **Action:** I replaced exhaustive MILP solving with a multi-level hierarchical heuristic: partitioning the grid into coarse clusters, computing cluster-to-cluster transfers using precomputed lookup tables, and using local A* search for fine-grained steps.
- **Result:** Path length was within 2.3% of the theoretical global optimum, while computation time dropped from 3 minutes to $<0.5$ seconds—a $360\times$ speedup that enabled real-time deployment.
"""
}

# -------------------------------------------------------------
# Module 07: CheatSheet & Formula Vault
# -------------------------------------------------------------
modules_data["07_Quick_Reference"] = {
    "title": "07: CheatSheet & Formula Vault",
    "prev_link": "06_Managerial_and_HR.html",
    "prev_title": "06: Life at Swiggy & Culture",
    "next_link": "README.html",
    "next_title": "3-Day Study Roadmap",
    "markdown": """# 07: CheatSheet & Formula Vault

Essential formulas, Uber H3 spatial resolutions, and signature SQL patterns for quick revision before your Swiggy interview.

---

## 1. Mathematical Formula Vault

### 1. The 4-Stage ETA Equation
$$T_{\text{ETA}} = T_{\text{O2A}} + T_{\text{FM}} + T_{\text{WT}} + T_{\text{LM}}$$

### 2. Quantile Regression (Pinball Loss)
$$L_q(y, \hat{y}) = \max(q(y - \hat{y}), (1-q)(\hat{y} - y)) = (y - \hat{y})(q - \mathbb{I}_{y < \hat{y}})$$

### 3. XGBoost Leaf Weight & Split Gain
$$w_j^* = -\frac{G_j}{H_j + \lambda}, \quad \text{Gain} = \frac{1}{2}\left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$

### 4. Uber H3 Spatial Hierarchy Reference
- **Res 7:** $\approx 1.22\text{ km}$ edge length, $\approx 5.16\text{ km}^2$ area (Macro-dispatch zone).
- **Res 8:** $\approx 461\text{ m}$ edge length, $\approx 0.74\text{ km}^2$ area (Standard hyperlocal cluster, primary delivery zone).
- **Res 9:** $\approx 174\text{ m}$ edge length, $\approx 0.10\text{ km}^2$ area (High-density neighborhood / street block).

### 5. Price Elasticity of Demand
$$\varepsilon = \frac{\partial Q / Q}{\partial P / P} = \frac{\partial \ln Q}{\partial \ln P}$$

---

## 2. Signature SQL Window CheatSheet

### Percentile Ranks & Rolling Averages
```sql
-- Rolling 7-day average orders per delivery executive
AVG(completed_orders) OVER (
    PARTITION BY de_id 
    ORDER BY order_date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
)

-- Identify high-delay kitchen outliers (top 5% worst)
DENSE_RANK() OVER (
    PARTITION BY city_id 
    ORDER BY avg_prep_delay_minutes DESC
)

-- Continuous Haversine Distance in SQL
6371 * 2 * ASIN(SQRT(
    POWER(SIN((RADIANS(cust_lat) - RADIANS(rest_lat)) / 2), 2) +
    COS(RADIANS(rest_lat)) * COS(RADIANS(cust_lat)) *
    POWER(SIN((RADIANS(cust_lon) - RADIANS(rest_lon)) / 2), 2)
)) AS distance_km
```

---

## 3. 60-Second Elevator Pitch
> *"I am an M.Tech in Signal and Image Processing from NIT Rourkela with a B.Tech in Computer Science. My core strengths lie at the intersection of mathematical modeling and low-latency algorithmic systems. In Warehouse PathMapper, I built a high-throughput spatial routing engine optimizing 10,000 coordinates in under 0.5s, directly mirroring Swiggy's Instamart pick routing and city-wide dispatch batching. My signal processing background provides a natural mathematical framework for noisy GPS telemetry, time-series forecasting, and real-time ML systems. I am excited to apply these skills to solve Swiggy’s high-concurrency hyperlocal logistics challenges."*
"""
}

# -------------------------------------------------------------
# Module 08: 3-Day Study Roadmap (README)
# -------------------------------------------------------------
modules_data["README"] = {
    "title": "3-Day Study Roadmap",
    "prev_link": "07_Quick_Reference.html",
    "prev_title": "07: CheatSheet",
    "next_link": "index.html",
    "next_title": "Overview Hub",
    "markdown": """# 3-Day Study Roadmap for Swiggy Data Scientist

A structured, high-intensity preparation plan designed to maximize performance across all rounds.

---

## Day 1: Algorithmic OA & SQL Mastery
- **Morning (09:00 – 13:00):**
  - Solve Hungarian bipartite matching problem and interval sweep-line algorithm in [01_Online_Test](01_Online_Test.html).
  - Practice C++ and Python implementations for minimum-cost maximum flow.
- **Afternoon (14:00 – 18:00):**
  - Practice complex SQL window functions: `AVG() OVER (ROWS BETWEEN)`, `PERCENTILE_CONT`, `LAG/LEAD`.
  - Review Haversine distance and geospatial coordinate calculations.
- **Evening (19:00 – 22:00):**
  - Brush up on probability, Bayes rule, Poisson processes (order arrivals), and Markov chains.

---

## Day 2: ML Foundations & Swiggy Bytes Deep Dive
- **Morning (09:00 – 13:00):**
  - Study [02_Technical_Rounds](02_Technical_Rounds.html): Derive XGBoost Taylor series expansion and split gain formula on paper.
  - Implement quantile loss (Pinball loss) and custom scikit-learn transformers.
- **Afternoon (14:00 – 18:00):**
  - Master [03_Domain_Deep_Dive](03_Domain_Deep_Dive.html): Memorize the 4-Stage ETA framework ($T_{\text{O2A}} + T_{\text{FM}} + T_{\text{WT}} + T_{\text{LM}}$).
  - Understand batching trade-offs, VRPTW constraints, and Instamart dark store picking heuristics.
- **Evening (19:00 – 22:00):**
  - Review tree regularization parameters ($\lambda, \gamma, \text{max\_depth}$) and handle real-time feature missingness.

---

## Day 3: Real-Time System Design, Resume Defense & Culture
- **Morning (09:00 – 13:00):**
  - Study [05_System_Design_or_HIL](05_System_Design_or_HIL.html): Draw the 100k RPS live ETA prediction architecture from scratch.
  - Understand Feast Redis feature caching, Triton ONNX serving, and Flink streaming pipelines.
- **Afternoon (14:00 – 18:00):**
  - Rehearse [04_Candidate_Resume_Grilling](04_Candidate_Resume_Grilling.html): Practice out-loud defense of Warehouse PathMapper and Autobot Robotics telemetry.
  - Connect your M.Tech Signal Processing background to spatio-temporal noise filtering.
- **Evening (19:00 – 21:00):**
  - Review Swiggy Core Leadership Values in [06_Managerial_and_HR](06_Managerial_and_HR.html) and align your STAR stories.
  - Memorize formulas from [07_Quick_Reference](07_Quick_Reference.html) and rehearse your 60-second elevator pitch.
"""
}

# -------------------------------------------------------------
# Module 09: Portal Overview & Hub (index.html)
# -------------------------------------------------------------
index_html_content = """
<div style="text-align: center; margin-bottom: 2.5rem;">
  <div style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 16px; border-radius: 9999px; background: rgba(252, 128, 25, 0.16); border: 1px solid #ea580c; color: #fc8019; font-weight: 700; font-size: 0.85rem; margin-bottom: 1rem;">
    ⚡ On-Campus Placement Preparation Suite
  </div>
  <h1 style="font-size: clamp(2rem, 5vw, 2.7rem); font-weight: 900; letter-spacing: -0.03em; margin-bottom: 0.75rem;">
    Swiggy Data Scientist Hub
  </h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 750px; margin: 0 auto;">
    Complete interview master guide tailored for <strong>Adarsh Saurabh</strong> (M.Tech Signal & Image Processing, NIT Rourkela). Verified hiring architecture, real-world 4-stage ETA systems, and airtight resume defense.
  </p>
</div>

<!-- Key Highlights Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-bottom: 2.5rem;">
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; text-align: center;">
    <div style="font-size: 1.7rem; font-weight: 900; color: var(--accent-primary);">₹26.00 LPA</div>
    <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Total CTC (18L Base + 8L ESOP)</div>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; text-align: center;">
    <div style="font-size: 1.7rem; font-weight: 900; color: #10b981;">100k RPS</div>
    <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Peak Dinner Inference Scale</div>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; text-align: center;">
    <div style="font-size: 1.7rem; font-weight: 900; color: #6366f1;">&lt; 25 ms</div>
    <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">p99 Live Checkout SLA</div>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; text-align: center;">
    <div style="font-size: 1.7rem; font-weight: 900; color: #f59e0b;">10 Modules</div>
    <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600; text-transform: uppercase;">Comprehensive Suite</div>
  </div>
</div>

<!-- Modules Cards Grid -->
<h2 style="font-size: 1.35rem; font-weight: 800; margin-bottom: 1.2rem; border-bottom: 2px solid var(--border-color); padding-bottom: 0.5rem;">
  📑 Preparation Modules
</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin-bottom: 2.5rem;">

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">00: Company & Role Deep Dive</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Strategy</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Executive founding thesis, food marketplace economics, Instamart dark-store logistics, and on-campus selection stages.
    </p>
    <a href="00_START_HERE.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">01: Signature OA Coding</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Algorithms</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Hungarian bipartite rider matching, sweep-line kitchen interval bottlenecks, and advanced SQL window analytics.
    </p>
    <a href="01_Online_Test.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">02: Machine Coding & ML Pipeline</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Coding</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Custom scikit-learn quantile loss ETA regression, cyclical features, and mathematical derivation of XGBoost split gain.
    </p>
    <a href="02_Technical_Rounds.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">03: Swiggy Bytes & 4-Stage ETA</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Domain</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Deconstructing Swiggy's core architecture: O2A, First Mile, Kitchen Wait Time, Last Mile, and VRPTW order batching.
    </p>
    <a href="03_Domain_Deep_Dive.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">04: Candidate Resume Defense</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Defense</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Defending Warehouse PathMapper ($10k \\times 10k$ grid heuristics), Autobot Robotics telemetry, and M.Tech Signal Processing.
    </p>
    <a href="04_Candidate_Resume_Grilling.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">05: Real-Time ML System Design</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">System Design</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      100k RPS live ETA prediction engine, Redis feature store, Triton ONNX inference, and fallback circuit breakers.
    </p>
    <a href="05_System_Design_or_HIL.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">06: Life at Swiggy & Cultural Values</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Behavioral</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Swiggy core values ("Customer First", "Bias for Action", "Always Curious") and STAR method interview answers.
    </p>
    <a href="06_Managerial_and_HR.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">07: CheatSheet & Formula Vault</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">CheatSheet</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Instant equations vault: Pinball loss, XGBoost objective, Uber H3 spatial resolutions, and elevator pitch.
    </p>
    <a href="07_Quick_Reference.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700;">3-Day Study Roadmap</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Roadmap</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Hour-by-hour structured preparation schedule spanning Algorithms, ML derivations, and System Design.
    </p>
    <a href="README.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Roadmap →</a>
  </div>

</div>
"""

# Render all modules
print("Building Swiggy interview prep modules...")

for key, mod in modules_data.items():
    md_file = os.path.join(BASE_DIR, f"{key}.md")
    html_file = os.path.join(BASE_DIR, f"{key}.html")

    # 1. Write Markdown
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(mod["markdown"])
    print(f"Written {md_file}")

    # 2. Render to HTML
    body_html = markdown.markdown(
        mod["markdown"],
        extensions=["fenced_code", "tables", "nl2br"]
    )
    full_html = render_swiggy_page(
        title=mod["title"],
        active_page=f"{key}.html",
        content_html=body_html,
        prev_link=mod["prev_link"],
        prev_title=mod["prev_title"],
        next_link=mod["next_link"],
        next_title=mod["next_title"]
    )

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Written {html_file}")

# Render index.html hub page
index_file = os.path.join(BASE_DIR, "index.html")
index_full_html = render_swiggy_page(
    title="Overview & Hub",
    active_page="index.html",
    content_html=index_html_content,
    prev_link="../index.html",
    prev_title="All Companies Hub",
    next_link="00_START_HERE.html",
    next_title="00: Company Deep Dive"
)
with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_full_html)
print(f"Written {index_file}")

print("All Swiggy preparation modules successfully generated!")
