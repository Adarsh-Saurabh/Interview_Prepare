# 01: Signature OA Coding Problems

Citi's Online Assessment (administered via SHL or HackerRank) features timed algorithmic challenges emphasizing streaming data, sliding windows, graph arbitrage, and priority matching engines.

---

## Problem 1: Transaction Sliding Window Anomaly Detection

### Problem Statement
In a real-time banking ledger, a stream of financial transactions is received as pairs of `(timestamp, amount)` where timestamps are strictly increasing in seconds. 
A transaction at timestamp $T_i$ with amount $A_i$ is flagged as an **anomaly** if:
1. $A_i > 2 \times \mu_W$, where $\mu_W$ is the arithmetic mean of all transactions occurring within the preceding time window $[T_i - W, T_i)$ of duration $W$ seconds.
2. The window must contain at least $K$ prior transactions ($K \ge 1$) to compute a valid mean; otherwise, the transaction cannot be flagged.

Given an array of transactions and window parameters $W$ and $K$, return the list of transaction timestamps that are flagged as anomalies.

### Mathematical Invariant & Optimal Strategy
* A naive calculation scans all preceding transactions for each element, costing $\mathcal{O}(N \cdot W)$ in time, which times out for $N = 10^5$.
* We maintain a **Two-Pointer Sliding Window** with running sum $S$ and running count $C$.
* As the right pointer $R$ visits transaction $(T_R, A_R)$, the left pointer $L$ advances while $T_R - T_L > W$.
* $S \leftarrow S - A_L$ and $C \leftarrow C - 1$.
* If $C \ge K$ and $A_R > 2 \cdot \frac{S}{C}$, record $T_R$ as an anomaly.
* Add $A_R$ to the window sum after evaluation.
* **Time Complexity**: $\mathcal{O}(N)$ since each element is added and removed from window at most once.
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary beyond input/output storage.

### Production Solution in Python (3.12)
```python
from typing import List, Tuple

def detect_transaction_anomalies(
    transactions: List[Tuple[int, float]], 
    window_seconds: int, 
    min_count: int
) -> List[int]:
    """
    Detects anomalous transaction amounts based on a sliding time window.
    
    :param transactions: List of (timestamp, amount) sorted by timestamp.
    :param window_seconds: Duration W in seconds.
    :param min_count: Minimum preceding transactions K required to flag.
    :return: List of anomalous timestamps.
    """
    if not transactions or min_count <= 0:
        return []

    anomalies: List[int] = []
    window_sum: float = 0.0
    left: int = 0
    n: int = len(transactions)

    for right in range(n):
        curr_time, curr_amount = transactions[right]

        # Shrink window from the left while elements are outside [curr_time - window_seconds, curr_time)
        while left < right and (curr_time - transactions[left][0]) > window_seconds:
            window_sum -= transactions[left][1]
            left += 1

        window_count = right - left
        
        # Check anomaly condition against preceding elements
        if window_count >= min_count:
            window_mean = window_sum / window_count
            if curr_amount > 2.0 * window_mean:
                anomalies.append(curr_time)

        # Include current transaction into running window sum
        window_sum += curr_amount

    return anomalies

# Unit Verification
if __name__ == "__main__":
    stream = [
        (10, 100.0),
        (20, 120.0),
        (30, 110.0),
        (45, 130.0),
        (50, 500.0), # Window [50-30, 50) = [20, 50) -> (20:120), (30:110), (45:130). Mean=120. 500 > 240! Anomaly!
        (90, 150.0),
    ]
    res = detect_transaction_anomalies(stream, window_seconds=30, min_count=2)
    print("Detected anomalies at timestamps:", res)
    assert res == [50]
```

### Optimal Solution in C++ (C++17)
```cpp
#include <iostream>
#include <vector>

struct Transaction {
    int64_t timestamp;
    double amount;
};

std::vector<int64_t> detectTransactionAnomalies(
    const std::vector<Transaction>& transactions,
    int64_t window_seconds,
    size_t min_count
) {
    std::vector<int64_t> anomalies;
    double window_sum = 0.0;
    size_t left = 0;
    const size_t n = transactions.size();

    for (size_t right = 0; right < n; ++right) {
        const int64_t curr_time = transactions[right].timestamp;
        const double curr_amount = transactions[right].amount;

        // Evict expired transactions outside (curr_time - window_seconds, curr_time]
        while (left < right && (curr_time - transactions[left].timestamp) > window_seconds) {
            window_sum -= transactions[left].amount;
            left++;
        }

        size_t window_count = right - left;
        if (window_count >= min_count) {
            double window_mean = window_sum / static_cast<double>(window_count);
            if (curr_amount > 2.0 * window_mean) {
                anomalies.push_back(curr_time);
            }
        }

        window_sum += curr_amount;
    }

    return anomalies;
}

int main() {
    std::vector<Transaction> stream = {
        {10, 100.0}, {20, 120.0}, {30, 110.0}, {45, 130.0}, {50, 500.0}, {90, 150.0}
    };
    auto result = detectTransactionAnomalies(stream, 30, 2);
    for (auto ts : result) {
        std::cout << "Anomaly detected at: " << ts << "
";
    }
    return 0;
}
```

---

## Problem 2: Foreign Exchange (FX) Currency Arbitrage Detection

### Problem Statement
In Citi's FX trading engine, currencies can be traded in pairs. You are given a list of $V$ currency names and a table of directed exchange rates $R[i][j]$ representing how many units of currency $j$ you receive for 1 unit of currency $i$.
An **arbitrage opportunity** exists if there is a sequence of currency exchanges $c_1 \rightarrow c_2 \rightarrow \dots \rightarrow c_k \rightarrow c_1$ such that:
$$\prod_{m=1}^{k} R[c_m][c_{m+1}] > 1.0 \quad (\text{where } c_{k+1} = c_1)$$

Determine whether an arbitrage cycle exists and output the sequence of currency codes forming the cycle.

### Mathematical Invariant & Transformation
* Standard shortest-path algorithms find the minimum sum of weights: $\sum w_i$.
* Here, we want to maximize the product: $\prod R_i > 1$.
* Taking the natural logarithm on both sides:
  $$\ln\left(\prod R_i\right) > 0 \iff \sum \ln(R_i) > 0 \iff \sum -\ln(R_i) < 0$$
* By defining edge weight $w(i, j) = -\ln(R[i][j])$, finding an arbitrage loop becomes **detecting a Negative Weight Cycle** in a directed graph!
* We apply the **Bellman-Ford Algorithm** running $V - 1$ relaxation passes followed by a $V$-th pass to identify and reconstruct the cycle.
* **Time Complexity**: $\mathcal{O}(V \cdot E) = \mathcal{O}(V^3)$ for a dense currency matrix.
* **Space Complexity**: $\mathcal{O}(V)$ for distance and predecessor tables.

### Complete Solution in Python (3.12)
```python
import math
from typing import List, Optional, Tuple

def find_currency_arbitrage(
    currencies: List[str], 
    exchange_matrix: List[List[float]]
) -> Optional[List[str]]:
    """
    Detects foreign exchange arbitrage cycles using log-transformed Bellman-Ford.
    
    :param currencies: List of currency strings (e.g., ['USD', 'EUR', 'GBP', 'JPY']).
    :param exchange_matrix: NxN matrix where matrix[i][j] is the rate to convert i to j.
    :return: List of currencies in the arbitrage cycle, or None if no arbitrage exists.
    """
    n = len(currencies)
    # Build edge list: (u, v, weight = -log(rate))
    edges: List[Tuple[int, int, float]] = []
    for i in range(n):
        for j in range(n):
            if i != j and exchange_matrix[i][j] > 0.0:
                edges.append((i, j, -math.log(exchange_matrix[i][j])))

    # Use virtual source connecting to all nodes with 0 weight, or initialize dist = 0 for all
    dist = [0.0] * n
    parent = [-1] * n

    # Relax edges n - 1 times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v] - 1e-9:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            return None # No negative cycle possible

    # n-th pass: check for negative cycle
    cycle_start = -1
    for u, v, w in edges:
        if dist[u] + w < dist[v] - 1e-9:
            cycle_start = v
            break

    if cycle_start == -1:
        return None

    # Step back n times to guarantee we are inside the cycle loop
    curr = cycle_start
    for _ in range(n):
        curr = parent[curr]

    # Reconstruct the cycle
    cycle: List[str] = []
    node = curr
    while True:
        cycle.append(currencies[node])
        node = parent[node]
        if node == curr and len(cycle) > 1:
            break
    cycle.append(currencies[curr])
    cycle.reverse()
    return cycle

# Verification
if __name__ == "__main__":
    curr_list = ["USD", "EUR", "GBP"]
    # USD -> EUR = 0.9, EUR -> GBP = 0.85, GBP -> USD = 1.35
    # Product: 0.9 * 0.85 * 1.35 = 1.03275 > 1.0 (Arbitrage!)
    rates = [
        [1.00, 0.90, 0.70],
        [1.11, 1.00, 0.85],
        [1.35, 1.17, 1.00]
    ]
    arbitrage_cycle = find_currency_arbitrage(curr_list, rates)
    print("Found Arbitrage Cycle:", arbitrage_cycle)
```
