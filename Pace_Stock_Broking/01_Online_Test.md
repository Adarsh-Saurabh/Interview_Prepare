# 01: Signature Online Assessment (OA) Problems

## 1. Test Architecture & Scoring Strategy
The Pace Stock Broking Online Test runs for **165 minutes** on HackerRank in the TIIR lab:
* **Section 1: Quantitative Aptitude & Fast Logic (approx. 20 mins):** Probability, mental arithmetic, series, and time-speed-distance.
* **Section 2: Mathematical Foundations (approx. 35 mins):** Bayes theorem, discrete probability distributions, expected value puzzles, and matrix linear algebra.
* **Section 3: Data Structures & Algorithms (approx. 110 mins):** 4 medium-to-hard coding problems requiring optimal asymptotic time and memory complexity.

---

## 2. Signature Coding Problem 1: Subarray Value Contribution (Two Pointers)

### Problem Description:
Given an array $A$ of $N$ integers, calculate the sum of $\max(B) - \min(B)$ across all non-empty contiguous subarrays $B$ of $A$. Return the result modulo $10^9 + 7$.
* **Constraints:** $N \le 2 \times 10^5$, $1 \le A[i] \le 10^9$.
* **HFT Significance:** Quant desks compute streaming volatility and rolling price spreads across thousands of market windows. An $O(N^2)$ solution will TLE instantly.

### Optimal Solution ($O(N)$ Time, $O(N)$ Space):
Instead of iterating through every subarray, compute how many subarrays have $A[i]$ as their maximum, and how many have $A[i]$ as their minimum using a **Monotonic Stack**.
$$\text{Total Sum} = \sum_{i=0}^{N-1} A[i] \times (\text{count\_max}(i) - \text{count\_min}(i))$$

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

long long totalSubarrayVariance(const vector<int>& arr) {
    int n = arr.size();
    long long MOD = 1e9 + 7;

    // left_max[i]: distance to previous strictly greater element
    // right_max[i]: distance to next greater or equal element
    vector<int> left_max(n), right_max(n);
    // left_min[i]: distance to previous strictly smaller element
    // right_min[i]: distance to next smaller or equal element
    vector<int> left_min(n), right_min(n);

    stack<int> s;

    // 1. Compute max contributions
    for (int i = 0; i < n; ++i) {
        while (!s.empty() && arr[s.top()] <= arr[i]) s.pop();
        left_max[i] = s.empty() ? (i + 1) : (i - s.top());
        s.push(i);
    }
    while (!s.empty()) s.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!s.empty() && arr[s.top()] < arr[i]) s.pop();
        right_max[i] = s.empty() ? (n - i) : (s.top() - i);
        s.push(i);
    }
    while (!s.empty()) s.pop();

    // 2. Compute min contributions
    for (int i = 0; i < n; ++i) {
        while (!s.empty() && arr[s.top()] >= arr[i]) s.pop();
        left_min[i] = s.empty() ? (i + 1) : (i - s.top());
        s.push(i);
    }
    while (!s.empty()) s.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!s.empty() && arr[s.top()] > arr[i]) s.pop();
        right_min[i] = s.empty() ? (n - i) : (s.top() - i);
        s.push(i);
    }

    // 3. Aggregate totals
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long max_subarrays = (1LL * left_max[i] * right_max[i]);
        long long min_subarrays = (1LL * left_min[i] * right_min[i]);
        long long diff = (max_subarrays - min_subarrays);
        total = (total + (diff % MOD) * arr[i]) % MOD;
    }

    return (total + MOD) % MOD;
}
```

---

## 3. Signature Coding Problem 2: Dynamic Connectivity (DSU with Minimum Path)

### Problem Description:
You are given $N$ trading venues and $M$ optical communication fiber lines being constructed sequentially at timestamps $t_1, t_2, \dots, t_M$. Each link connects venue $u$ and $v$ with propagation latency $L$. Answer $Q$ queries: *"At what earliest timestamp can venue $A$ and venue $B$ communicate with total maximum edge latency $\le X$?"*
* **Constraints:** $N \le 10^5$, $M \le 2 \times 10^5$, $Q \le 10^5$.
* **HFT Significance:** Exchange inter-connectivity routing and dynamic risk circuit-breaker partitioning.

### Optimal C++ Solution (Disjoint Set Union with Path Compression & Union by Rank):

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> rank;

    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        rank.assign(n + 1, 0);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path compression
    }

    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            // Union by rank
            if (rank[root_i] < rank[root_j])
                swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank[root_i] == rank[root_j])
                rank[root_i]++;
            return true;
        }
        return false;
    }
};
```

---

## 4. Mathematics & Probability Section Mastery

### Problem: The High-Frequency Coin Toss Game
**Question:** A trader flips a fair coin repeatedly. What is the expected number of flips until the pattern **HTH** appears, versus the pattern **HTT**?
* **Analytical Derivation:**
  * Let $E[\text{HTT}]$ and $E[\text{HTH}]$ denote the expected flips.
  * For any pattern $S$, by Conway's Leading Crosses Algorithm or Martingale Optional Stopping Theorem:
    $$E[S] = \sum_{k=1}^{L} I(k) \cdot 2^k$$
    where $I(k) = 1$ if the prefix of length $k$ equals the suffix of length $k$.
  * For **HTT**:
    * Prefix/Suffix matches: Length 3 (`HTT` $\ne$ `HTT` prefix match? Only full string matches).
    * Prefix of length 1 is `H`, suffix is `T` (no).
    * Prefix of length 2 is `HT`, suffix is `TT` (no).
    * Prefix of length 3 is `HTT`, suffix is `HTT` (yes: $2^3 = 8$).
    * **$E[\text{HTT}] = 8$ flips.**
  * For **HTH**:
    * Prefix of length 1 is `H`, suffix is `H` (match! $2^1 = 2$).
    * Prefix of length 2 is `HT`, suffix is `TH` (no).
    * Prefix of length 3 is `HTH`, suffix is `HTH` (match! $2^3 = 8$).
    * **$E[\text{HTH}] = 8 + 2 = 10$ flips.**
  * **HFT Interviewer Follow-up:** *Why does HTH take longer on average than HTT?*
    * *Answer:* Because HTH has internal self-overlap. If you have `HT` and roll `T`, you fail and start completely over. But for `HTT`, failing on the 3rd roll gives `HTH`, which already gives you the first `H` of the next attempt!
