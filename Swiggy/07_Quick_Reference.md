# 07: CheatSheet & Formula Vault

Essential formulas, Uber H3 spatial resolutions, and signature SQL patterns for quick revision before your Swiggy interview.

---

## 1. Mathematical Formula Vault

### 1. The 4-Stage ETA Equation
$$T_{	ext{ETA}} = T_{	ext{O2A}} + T_{	ext{FM}} + T_{	ext{WT}} + T_{	ext{LM}}$$

### 2. Quantile Regression (Pinball Loss)
$$L_q(y, \hat{y}) = \max(q(y - \hat{y}), (1-q)(\hat{y} - y)) = (y - \hat{y})(q - \mathbb{I}_{y < \hat{y}})$$

### 3. XGBoost Leaf Weight & Split Gain
$$w_j^* = -rac{G_j}{H_j + \lambda}, \quad 	ext{Gain} = rac{1}{2}\left[ rac{G_L^2}{H_L + \lambda} + rac{G_R^2}{H_R + \lambda} - rac{(G_L + G_R)^2}{H_L + H_R + \lambda} ight] - \gamma$$

### 4. Uber H3 Spatial Hierarchy Reference
- **Res 7:** $pprox 1.22	ext{ km}$ edge length, $pprox 5.16	ext{ km}^2$ area (Macro-dispatch zone).
- **Res 8:** $pprox 461	ext{ m}$ edge length, $pprox 0.74	ext{ km}^2$ area (Standard hyperlocal cluster, primary delivery zone).
- **Res 9:** $pprox 174	ext{ m}$ edge length, $pprox 0.10	ext{ km}^2$ area (High-density neighborhood / street block).

### 5. Price Elasticity of Demand
$$arepsilon = rac{\partial Q / Q}{\partial P / P} = rac{\partial \ln Q}{\partial \ln P}$$

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
