# 01: Signature OA Coding Problems

Swiggy's Online Assessment features algorithmic challenges inspired by hyperlocal logistics: geospatial graph bipartite matching, interval scheduling for kitchen capacity, and dark-store pick route optimization.

---

## Problem 1: Optimal Bipartite Rider-to-Order Dispatch

### Problem Statement
Given $M$ pending orders with pickup coordinates $[rx_i, ry_i]$ and ready timestamps $T_i$, and $N$ active delivery partners located at $[dx_j, dy_j]$ with speed $S_j$. 
Each delivery partner can accept at most 1 order. Travel time between points $(x_1, y_1)$ and $(x_2, y_2)$ is defined by Manhattan distance divided by speed:
$$\text{time}(i, j) = \frac{|rx_i - dx_j| + |ry_i - dy_j|}{S_j}$$
If a delivery partner arrives before food ready time $T_i$, they wait until $T_i$. Total delay penalty for an order is:
$$\text{Penalty}(i, j) = \max(0, \text{time}(i, j) - T_i) + 0.5 \times \text{time}(i, j)$$
Find the global assignment of riders to orders that minimizes the sum of delay penalties for all matched orders, ensuring at least $\min(M, N)$ orders are dispatched.

### Python 3 Solution (Min-Cost Max-Flow / Hungarian Equivalent via SciPy)
```python
import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_dispatch(orders, riders):
    """
    orders: list of dicts [{'rx': float, 'ry': float, 'ready_t': float}]
    riders: list of dicts [{'dx': float, 'dy': float, 'speed': float}]
    Returns: list of (order_idx, rider_idx, cost), total_cost
    """
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
    """
    orders: list of [start, end, burners, priority]
    K: total available burners
    Returns: peak_burners, breach_intervals
    """
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
