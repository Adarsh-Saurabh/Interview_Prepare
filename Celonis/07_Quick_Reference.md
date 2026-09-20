# 07: Process Mining & Systems CheatSheet

## 1. High-Yield Process Mining Concepts

| Concept | Definition in 1 Line |
| :--- | :--- |
| **Event Log** | A tabular dataset with minimum 3 columns: `case_id`, `activity`, and `timestamp`. |
| **Case ID** | The discrete business instance being tracked (e.g., invoice number, claim ID). |
| **Happy Path** | The most frequent, ideal execution sequence with zero rework or delays. |
| **Process Variant** | A distinct permutation of activity sequences observed in real data. |
| **Throughput Time** | The total elapsed duration from process start to termination. |
| **Rework / Loop** | Repeating the exact same activity multiple times within a single case. |
| **Bottleneck** | A transition step where cases spend disproportionately long waiting times. |
| **Conformance** | Quantifying how well real execution matches pre-defined business policy. |
| **OCPM** | Object-Centric Process Mining: tracking multiple interrelated entities concurrently. |

---

## 2. Big-O Complexity Reference for Signature OA Algorithms

| Algorithm | Best Time | Average Time | Worst Time | Space | Signature Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kahn's Topological Sort** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | Process deadlock detection |
| **Dijkstra with Min-Heap** | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V)$ | Minimum throughput pathfinding |
| **Sliding Window (Two-Pointer)**| $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(1)$ | Peak event ingestion detection |
| **Monotonic Queue** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(K)$ | Window minimum / maximum queries |

---

## 3. Concurrency Rules in 5 Bullets
1. **Never synchronize on `String` literals** or boxed primitives in Java (`synchronized("lock")` creates JVM-wide contention).
2. **Always lock in a consistent global order** when acquiring multiple locks to eliminate deadlocks.
3. **Double-Checked Locking requires `volatile`** to prevent out-of-order instruction execution during object construction.
4. **Use CAS (Compare-And-Swap) for high-contention counters** instead of heavy mutexes.
5. **Thread pools must never have unbounded queues**; always configure explicit rejection policies (`CallerRunsPolicy` or `AbortPolicy`).
