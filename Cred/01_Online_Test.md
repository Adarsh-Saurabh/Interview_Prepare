# 01: CRED Signature OA Coding Problems & Mastery

The CRED Online Assessment (OA) is conducted on HackerRank or HackerEarth (duration: 90-105 minutes). It is renowned for rejecting rote LeetCode grinders by testing algorithmic depth, mathematical optimization, and edge-case resilience.

---

## Problem 1: Transaction Velocity & Sliding Window Anomaly Detection

### Problem Statement
In CRED's fraud-monitoring engine, transactions arrive as a continuous stream of values [v_0, v_1, ..., v_{N-1}]. To detect sudden velocity bursts and credit-line skimming, compute the maximum transaction value in every sliding window of size k.

Return an array of the maximum values for each of the N - k + 1 sliding windows.

- **Constraints:** 1 <= k <= N <= 10^5, -10^9 <= v_i <= 10^9.
- **Target Complexity:** O(N) time, O(k) auxiliary space.

### Algorithmic Approach: Monotonic Decreasing Deque
A naive scan of size k takes O(N * k) time, which TLEs for N = 10^5, k = 50,000. A binary heap or balanced BST takes O(N log k). The optimal solution uses a **Monotonic Decreasing Deque** storing indices:
1. **Eviction:** Before adding index i, remove all indices from the back whose values are <= v[i]. They can never be the maximum in any future window containing v[i].
2. **Expiry:** Remove indices from the front that fall outside the current window (i.e. index <= i - k).
3. **Record Maximum:** The front of the deque always holds the index of the maximum element for the current window.

### Optimal Python Implementation
```python
from collections import deque
from typing import List

def max_sliding_window(transactions: List[int], k: int) -> List[int]:
    if not transactions or k <= 0:
        return []
    if k == 1:
        return transactions

    n = len(transactions)
    if k >= n:
        return [max(transactions)]

    deq = deque()  # Stores indices
    result = []

    for i in range(n):
        # 1. Evict elements out of the current sliding window
        while deq and deq[0] <= i - k:
            deq.popleft()

        # 2. Maintain monotonic decreasing property (pop smaller elements from back)
        while deq and transactions[deq[-1]] <= transactions[i]:
            deq.pop()

        # 3. Add current element index
        deq.append(i)

        # 4. Append maximum to result once the first window is formed
        if i >= k - 1:
            result.append(transactions[deq[0]])

    return result
```

### Optimal C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

class FraudVelocityDetector {
public:
    static std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
        std::vector<int> result;
        std::deque<int> dq; // Stores indices
        int n = nums.size();

        if (n == 0 || k <= 0) return result;
        if (k >= n) {
            result.push_back(*std::max_element(nums.begin(), nums.end()));
            return result;
        }

        result.reserve(n - k + 1);

        for (int i = 0; i < n; ++i) {
            while (!dq.empty() && dq.front() <= i - k) {
                dq.pop_front();
            }

            while (!dq.empty() && nums[dq.back()] <= nums[i]) {
                dq.pop_back();
            }

            dq.push_back(i);

            if (i >= k - 1) {
                result.push_back(nums[dq.front()]);
            }
        }

        return result;
    }
};
```

---

## Problem 2: Optimal Debt Settlement & Cash Flow Minimization

### Problem Statement
CRED members participate in group expense splits and cross-card debt consolidation. You are given a list of transactions where `transactions[i] = [from_user, to_user, amount]`. Compute the **minimum number of transactions** required to settle all debts among all individuals.

- **Constraints:** Number of people N <= 16, amounts are positive integers <= 10^6.
- **Target Complexity:** O(2^N * N) time via Bitmask Dynamic Programming.

### Algorithmic Approach: Bitmask DP
This problem is an NP-hard variation of the Subset Sum problem:
1. **Net Balances:** Compute net balance for each person: balance[u] = sum(inflow) - sum(outflow).
2. Filter out all persons whose net balance is 0. Suppose M non-zero persons remain.
3. If a subset of persons has balances that sum to zero, they can settle all internal debts in |S| - 1 transactions.
4. Therefore, if we partition the M people into the maximum number of disjoint zero-sum subsets K, the minimum total transactions required will be:
   Min Transactions = M - K
5. We use Bitmask DP to find K, the maximum number of zero-sum subsets.

### Optimal Python Implementation
```python
from typing import List
from collections import defaultdict

def min_transfers(transactions: List[List[int]]) -> int:
    balance_map = defaultdict(int)

    for u, v, amount in transactions:
        balance_map[u] -= amount
        balance_map[v] += amount

    balances = [b for b in balance_map.values() if b != 0]
    m = len(balances)
    if m == 0:
        return 0

    total_subsets = 1 << m
    subset_sum = [0] * total_subsets
    for mask in range(total_subsets):
        for i in range(m):
            if (mask & (1 << i)):
                subset_sum[mask] = subset_sum[mask ^ (1 << i)] + balances[i]
                break

    dp = [0] * total_subsets

    for mask in range(1, total_subsets):
        if subset_sum[mask] == 0:
            dp[mask] = 1
            submask = (mask - 1) & mask
            while submask > 0:
                if subset_sum[submask] == 0:
                    dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
                submask = (submask - 1) & mask
        else:
            submask = (mask - 1) & mask
            while submask > 0:
                dp[mask] = max(dp[mask], dp[submask] + dp[mask ^ submask])
                submask = (submask - 1) & mask

    return m - dp[total_subsets - 1]
```

---

## Problem 3: Syndicated Fraud Ring Detection (Directed Cycle Detection)

### Problem Statement
In financial fraud syndicates, fraudsters route stolen funds through a chain of intermediary mule bank accounts before laundering it back to the origin or cash-out accounts. Given V accounts and directed transfer edges (u, v, weight), determine if there exists a money laundering cycle, and return the cycle with the **maximum total transaction sum**.

- **Constraints:** V <= 10^4, E <= 5 * 10^4.
- **Complexity Target:** O(V + E) using DFS 3-Coloring.

### Python Implementation
```python
from typing import List, Tuple

def find_max_fraud_ring(v: int, edges: List[Tuple[int, int, int]]) -> Tuple[bool, int, List[int]]:
    adj = {i: [] for i in range(v)}
    for src, dst, weight in edges:
        adj[src].append((dst, weight))

    color = [0] * v  # 0=White, 1=Gray, 2=Black
    parent = [-1] * v
    edge_w = [0] * v

    max_sum = -1
    best_cycle = []

    def dfs(u: int):
        nonlocal max_sum, best_cycle
        color[u] = 1

        for nxt, w in adj[u]:
            if color[nxt] == 1:
                # Cycle found! Backtrack
                curr, curr_sum, curr_cycle = u, w, [nxt]
                while curr != nxt and curr != -1:
                    curr_cycle.append(curr)
                    curr_sum += edge_w[curr]
                    curr = parent[curr]
                curr_cycle.reverse()

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    best_cycle = curr_cycle
            elif color[nxt] == 0:
                parent[nxt] = u
                edge_w[nxt] = w
                dfs(nxt)
        color[u] = 2

    for node in range(v):
        if color[node] == 0:
            dfs(node)

    return (max_sum != -1, max_sum, best_cycle)
```

---

## 4. Advanced SQL & Probability Essentials

### Signature SQL: 3-Month Consecutive Spend Growth (>=50%)
```sql
WITH monthly_spend AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', transaction_date) AS txn_month,
        SUM(amount) AS total_amount
    FROM card_transactions
    WHERE transaction_date >= '2026-01-01'
    GROUP BY user_id, DATE_TRUNC('month', transaction_date)
),
spend_with_lags AS (
    SELECT 
        user_id,
        txn_month,
        total_amount,
        LAG(total_amount, 1) OVER (PARTITION BY user_id ORDER BY txn_month) AS prev_m1,
        LAG(total_amount, 2) OVER (PARTITION BY user_id ORDER BY txn_month) AS prev_m2
    FROM monthly_spend
)
SELECT DISTINCT user_id
FROM spend_with_lags
WHERE prev_m2 IS NOT NULL
  AND prev_m1 >= 1.5 * prev_m2
  AND total_amount >= 1.5 * prev_m1;
```

### Probability Deep Dive: Bayes' Theorem & Base Rate Fallacy
If fraud prevalence is P(Fraud) = 0.1%, with True Positive Rate 99% and False Positive Rate 1%:
P(Fraud | Alert) = (0.99 * 0.001) / ((0.99 * 0.001) + (0.01 * 0.999)) approx 9.02%
**System Design Takeaway:** Never block accounts purely on single-model raw threshold alerts. Trigger secondary step-up verification (2FA, biometric authentication) to prevent insulting creditworthy members.
