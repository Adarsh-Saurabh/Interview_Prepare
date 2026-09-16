# 00: Swiggy Company & Role Deep Dive

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
  - $3.5	ext{B}+$ cumulative orders delivered across $600+$ Indian cities.
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
