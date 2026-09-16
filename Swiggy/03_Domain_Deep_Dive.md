# 03: Swiggy Bytes & 4-Stage ETA Architecture

Swiggy's tech engineering blog (*Swiggy Bytes*) reveals that holistic end-to-end delivery estimation cannot be treated as a naive single-shot regression model. Instead, it is partitioned into four decoupled, statistically modeled stages.

---

## 1. The 4-Stage ETA Decomposition

$$\mathbf{T_{	ext{ETA}}} = \mathbf{T_{	ext{O2A}}} + \mathbf{T_{	ext{FM}}} + \mathbf{T_{	ext{WT}}} + \mathbf{T_{	ext{LM}}}$$

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
| **$T_{	ext{O2A}}$** | Ordered to Assignment | Fleet availability in the H3 cell, rider acceptance probability, batching potential | Available idle riders within radius $R$, surge multiplier, historical acceptance rate |
| **$T_{	ext{FM}}$** | First Mile | Real-time traffic, U-turns, flyover congestion, DE vehicle type | OSRM road graph shortest path, real-time GPS speed delta, rain intensity |
| **$T_{	ext{WT}}$** | Kitchen Wait Time | The "Wildcard": Kitchen backlog, complexity of dishes, live in-dining crowd | Active kitchen orders, dish prep time embeddings, historical restaurant delay curves |
| **$T_{	ext{LM}}$** | Last Mile & Handover | Road traffic, gate entry delay, high-rise elevator waiting | Road distance, Uber H3 customer hex, apartment gate entry barrier score |

---

## 2. Dynamic Dispatch & Combinatorial Batching

Swiggy solves the **Vehicle Routing Problem with Time Windows (VRPTW)**. When order volume surges, assigning 1 rider per order collapses unit economics. Swiggy groups multiple orders ($2$ or $3$) to one Delivery Executive.

### Batching Feasibility Matrix
Two orders $O_1 = (P_1, D_1)$ and $O_2 = (P_2, D_2)$ can be batched only if:
1. **Spatial Proximity:** Pickups $P_1$ and $P_2$ are within 800m of each other or share the same food court.
2. **Temporal Alignment:** Ready times satisfy $|Ready(O_1) - Ready(O_2)| \le 7	ext{ minutes}$.
3. **Detour & Freshness Bound:**
   $$T_{	ext{delivered}}(O_1 | 	ext{batched}) - T_{	ext{delivered}}(O_1 | 	ext{single}) \le \Delta_{\max} \quad (\Delta_{\max} pprox 8	ext{ mins})$$
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
  $$	ext{Ratio}(h_i, t) = rac{	ext{Active Orders}(h_i, t)}{	ext{Available Drivers}(h_i, t) + \epsilon}$$
- **Price Elasticity of Demand:**
  $$arepsilon = rac{\% \Delta Q}{\% \Delta P}$$
  Surge pricing dynamically increases delivery fee to depress non-urgent demand while broadcasting financial incentives (boost pay) to lure idle riders from adjacent H3 cells into deficit zones.
