# Module 01: Signature DSA & Puzzles (With Optimal C++ & Python Solutions)

Fintech technical assessments at Gullak do not focus on obscure graph theory; instead, they simulate real-world transactional data problems, range balance queries, streaming aggregations, and mathematical reasoning puzzles.

---

## Problem 1: Transaction Ledger Balance & Prefix Range Queries

### Problem Statement
In a digital gold ledger, transactions occur sequentially. Each transaction is represented as an integer: positive for gold deposits/purchases (in milligrams) and negative for withdrawals/liquidations.
You need to support two operations in a real-time banking ledger:
1. `update(index, amount)`: Update the transaction at zero-indexed `index` with a new value `amount`.
2. `get_balance(left, right)`: Compute the net gold balance accumulated between transaction indices `left` and `right` inclusive.

Constraints: Number of transactions $N \le 10^5$, Number of queries $Q \le 10^5$. An $O(N)$ query is too slow and causes timeout.

### Optimal Solution: Binary Indexed Tree (Fenwick Tree)
* Time Complexity: $O(\log N)$ per update, $O(\log N)$ per balance query.
* Space Complexity: $O(N)$.

#### C++ Implementation
```cpp
#include <iostream>
#include <vector>

class LedgerFenwickTree {
private:
    int n;
    std::vector<long long> tree;
    std::vector<long long> original_ledger;

public:
    LedgerFenwickTree(const std::vector<long long>& ledger) {
        n = ledger.size();
        tree.assign(n + 1, 0);
        original_ledger = ledger;

        for (int i = 0; i < n; ++i) {
            add(i + 1, ledger[i]);
        }
    }

    void add(int idx, long long delta) {
        for (; idx <= n; idx += idx & -idx) {
            tree[idx] += delta;
        }
    }

    void update(int idx, long long new_val) {
        long long delta = new_val - original_ledger[idx];
        original_ledger[idx] = new_val;
        add(idx + 1, delta);
    }

    long long query_prefix(int idx) const {
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += tree[idx];
        }
        return sum;
    }

    long long get_balance(int left, int right) const {
        if (left > right || left < 0 || right >= n) return 0;
        return query_prefix(right + 1) - query_prefix(left);
    }
};

int main() {
    std::vector<long long> transactions = {500, -200, 1500, -300, 750, -100};
    LedgerFenwickTree ledger(transactions);

    std::cout << "Initial Balance [1 to 4]: " << ledger.get_balance(1, 4) << " mg\n"; // -200 + 1500 - 300 + 750 = 1750
    ledger.update(2, 2000); // Changed 1500 to 2000
    std::cout << "Updated Balance [1 to 4]: " << ledger.get_balance(1, 4) << " mg\n"; // 2250 mg
    return 0;
}
```

#### Python Implementation
```python
class LedgerFenwickTree:
    def __init__(self, ledger: list[int]):
        self.n = len(ledger)
        self.tree = [0] * (self.n + 1)
        self.ledger = list(ledger)
        for i, val in enumerate(ledger):
            self._add(i + 1, val)

    def _add(self, idx: int, delta: int):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def update(self, idx: int, new_val: int):
        delta = new_val - self.ledger[idx]
        self.ledger[idx] = new_val
        self._add(idx + 1, delta)

    def _query_prefix(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)
        return total

    def get_balance(self, left: int, right: int) -> int:
        if left > right or left < 0 or right >= self.n:
            return 0
        return self._query_prefix(right + 1) - self._query_prefix(left)
```

---

## Problem 2: Two-Pointer Payment Stream Reconciliation

### Problem Statement
In Gullak's payment reconciliation system, you receive two sorted streams of payment records:
1. `bank_records`: Payments recorded by the partner bank/gateway.
2. `internal_records`: Payments recorded by Gullak's backend.
Each record contains an integer transaction ID and an amount in paise. Due to minor network timing and rounding variations, a match between `bank_records[i]` and `internal_records[j]` is declared if:
* The transaction IDs match (`bank_id == internal_id`), AND
* The amount difference is at most `tolerance` paise ($|\text{bank\_amt} - \text{internal\_amt}| \le \text{tolerance}$).

Return the list of unmatched bank records and unmatched internal records for manual audit. Both input lists are sorted in ascending order of transaction ID.

### Optimal Solution: Two Pointers Linear Scan
* Time Complexity: $O(N + M)$ where $N$ and $M$ are record lengths.
* Space Complexity: $O(1)$ auxiliary (excluding output lists).

#### C++ Implementation
```cpp
#include <iostream>
#include <vector>
#include <cmath>

struct Record {
    long long txn_id;
    long long amount;
};

struct ReconciliationResult {
    std::vector<Record> unmatched_bank;
    std::vector<Record> unmatched_internal;
};

ReconciliationResult reconcile(const std::vector<Record>& bank, const std::vector<Record>& internal_recs, long long tolerance) {
    ReconciliationResult result;
    int i = 0, j = 0;
    int n = bank.size(), m = internal_recs.size();

    while (i < n && j < m) {
        if (bank[i].txn_id == internal_recs[j].txn_id) {
            if (std::abs(bank[i].amount - internal_recs[j].amount) > tolerance) {
                // Same ID but amount discrepancy
                result.unmatched_bank.push_back(bank[i]);
                result.unmatched_internal.push_back(internal_recs[j]);
            }
            i++;
            j++;
        } else if (bank[i].txn_id < internal_recs[j].txn_id) {
            result.unmatched_bank.push_back(bank[i]);
            i++;
        } else {
            result.unmatched_internal.push_back(internal_recs[j]);
            j++;
        }
    }

    while (i < n) result.unmatched_bank.push_back(bank[i++]);
    while (j < m) result.unmatched_internal.push_back(internal_recs[j++]);

    return result;
}
```

---

## Problem 3: Streaming Top-K Gold Investors (Min-Heap)

### Problem Statement
Gullak processes millions of transactions streaming across the day. The analytics team requires a real-time monitor displaying the **Top K** highest value gold purchases made today.
Because the total transaction stream size $N$ is unbound ($N > 10^7$) and cannot fit into RAM simultaneously, design a streaming processor that maintains the Top K transactions in $O(\log K)$ time per incoming transaction.

### Optimal Solution: Bounded Min-Heap
* Time Complexity: $O(N \log K)$ overall, $O(\log K)$ per event.
* Space Complexity: Strictly $O(K)$.

#### Python Implementation
```python
import heapq
from typing import List, Tuple

class TopKInvestorStream:
    def __init__(self, k: int):
        self.k = k
        self.min_heap: List[Tuple[float, str]] = []  # (amount, user_id)

    def process_transaction(self, user_id: str, amount: float):
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, (amount, user_id))
        elif amount > self.min_heap[0][0]:
            heapq.heapreplace(self.min_heap, (amount, user_id))

    def get_top_k(self) -> List[Tuple[str, float]]:
        # Return sorted in descending order of purchase amount
        sorted_top = sorted(self.min_heap, key=lambda x: x[0], reverse=True)
        return [(user, amt) for amt, user in sorted_top]
```

---

## Problem 4: The 100-Locker Toggle Puzzle (Signature Gullak Interview Question)

### Problem Statement
There are 100 closed lockers in a row, numbered 1 to 100. 100 people walk past them in succession:
* Person 1 toggles (opens) every locker.
* Person 2 toggles (closes) lockers 2, 4, 6, 8...
* Person 3 toggles lockers 3, 6, 9, 12...
* In general, Person $k$ toggles every locker whose number is a multiple of $k$.
After all 100 people have walked through, which lockers remain **OPEN**?

### Mathematical Solution & First-Principles Proof
A locker $L$ is toggled once for every positive divisor of $L$.
* For example, locker 12 has divisors: 1, 2, 3, 4, 6, 12 (6 divisors $\to$ even number of toggles $\to$ Closed $\to$ Open $\to$ Closed $\to$ Open $\to$ Closed $\to$ Closed).
* In general, divisors of a number $L$ come in distinct pairs $(d, L/d)$.
* The only time a number has an **odd number of divisors** is when $d = L/d$, which means $L = d^2$ (i.e., $L$ is a **perfect square**!).
* Therefore, only lockers whose numbers are perfect squares will end up **OPEN**.

For $N = 100$:
The open lockers are: $1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2, 8^2, 9^2, 10^2$
$= \mathbf{\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\}}$.
**Total lockers open = 10.**

---

## Problem 5: Deadlock / Cycle Detection in P2P Money Transfers

### Problem Statement
In peer-to-peer gold gifting or chained transfers, User A owes gold to User B, User B owes User C, and User C owes User A. Detect whether a dependency cycle exists in the transaction graph to avoid deadlocks in atomic batch settlement.

### Optimal Solution: Kahn's Topological Sort (In-Degree BFS)
* Time Complexity: $O(V + E)$
* Space Complexity: $O(V + E)$

#### C++ Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>

bool hasCycle(int numUsers, const std::vector<std::pair<int, int>>& transfers) {
    std::vector<std::vector<int>> adj(numUsers);
    std::vector<int> inDegree(numUsers, 0);

    for (const auto& [from, to] : transfers) {
        adj[from].push_back(to);
        inDegree[to]++;
    }

    std::queue<int> q;
    for (int i = 0; i < numUsers; ++i) {
        if (inDegree[i] == 0) q.push(i);
    }

    int processedCount = 0;
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        processedCount++;

        for (int neighbor : adj[curr]) {
            if (--inDegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    return processedCount != numUsers; // If processedCount != numUsers, a cycle exists!
}
```
