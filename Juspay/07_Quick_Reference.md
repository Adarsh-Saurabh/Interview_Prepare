# 07: Caveman & Ponytail Ultra-Dense Cheat Sheet ? Juspay Technologies

---

## 1. Caveman Core Axioms (Drop Fluff, Keep Substance)

### 1.1 Tree of Space in 3 Lines
- **Lock(u, uid)**: $O(\text{depth})$. Check $c(u) == 0$, climb ancestors check $\sigma == \text{UNLOCKED}$. Set $\sigma = \text{LOCKED}$, climb ancestors increment $c(a)$, insert $u$.
- **Unlock(u, uid)**: $O(\text{depth})$. Check $\sigma == \text{LOCKED}, \omega == \text{uid}$. Set $\sigma = \text{UNLOCKED}$, climb ancestors decrement $c(a)$, erase $u$.
- **UpgradeLock(u, uid)**: $O(\text{depth} + k)$. Check $c(u) > 0$, ancestors unlocked, all $k \in \mathcal{L}(u)$ owned by `uid`. Unlock $k$ descendants, set $u$ locked, update ancestor counters by $-(k-1)$.
- **Deadlock Freedom**: Sort lock acquisition along Canonical Total Order: $\text{depth}$ ascending, then $\text{id}$ ascending. Circular wait impossible.

### 1.2 The 3 Graph OA Algorithms in 3 Lines
- **Max Weight Node**: Array `weights[edges[i]] += i`. Return $\arg\max(\text{weights}[i])$, tie-break larger index. $O(N)$ time, $O(N)$ space.
- **Nearest Meeting Cell**: Single-path traversal from $C_1$ with `visited` set to build `dist1`. Same for $C_2$ to build `dist2`. Minimize $\max(\text{dist1}[u], \text{dist2}[u])$, tie-break smaller index. $O(N)$ time.
- **Largest Sum Cycle**: Kahn's topological sort on in-degrees. Queue in-degree 0 nodes, peel off tree branches. Remaining nodes with in-degree > 0 strictly form cycles. Traverse and sum. Return max sum or -1. $O(N)$ time.

---

## 2. Concurrency & Systems Formulas

| Concept | Equation / Axiom | Practical Meaning |
| :--- | :--- | :--- |
| **Amdahl's Law** | $S(s) = \frac{1}{(1 - p) + \frac{p}{s}}$ | Parallel speedup bounded by sequential fraction $(1-p)$. |
| **Little's Law** | $L = \lambda \cdot W$ | Concurrency ($L$) = Arrival Rate ($\lambda$) $\times$ Average Latency ($W$). |
| **Cache Line Size** | $64 \text{ Bytes}$ | Avoid False Sharing using `alignas(64)`. |
| **SMA Group Delay** | $\tau_g = \frac{N-1}{2}$ | Simple moving averages lag real-time bank failure; use Kalman filters. |
| **Jittered Backoff** | $T = \text{random}(0, \min(T_{\max}, T_{\text{base}} \cdot 2^k))$ | Prevents thundering herd retries against recovering APIs. |
| **4 Coffman Conditions** | 1. Mutex 2. Hold & Wait 3. No Preemption 4. Circular Wait | Deadlock occurs iff all 4 hold. Break Circular Wait via total order. |

---

## 3. Distributed Payments & Idempotency Cheat Sheet

### 3.1 Idempotency Key Flow
- Header: `Idempotency-Key: UUID`.
- Layer 1: Redis `SET payment:lock:{merchant}:{key} {hash} NX EX 30`.
- Layer 2: SQL `INSERT INTO idempotency_records ... ON CONFLICT DO NOTHING`.
- OCC Update: `UPDATE payments SET status = :new, version = version + 1 WHERE id = :id AND version = :exp`.

### 3.2 Key HTTP Status Codes in Payments
- `200 OK`: Payment executed or cached idempotent response returned.
- `409 Conflict`: Concurrent request with identical idempotency key is actively in flight.
- `422 Unprocessable Entity`: Idempotency key reused with mismatched payload / tampering.
- `504 Gateway Timeout`: Bank did not respond. Transaction status is indeterminate; DO NOT fail?trigger async reconciliation.

---

## 4. 30-Second Resume Elevator Pitches

### Pitch 1: Why Signal Processing M.Tech to Distributed Systems?
*"High-throughput payment routing is a discrete-time stochastic control problem. Naive moving averages introduce group delay ($\tau_g = (N-1)/2$) that routes money into failing bank black holes. My signal processing foundation allows me to apply Kalman filters and feedback control theory to steer traffic in sub-second windows without inducing hunting oscillations."*

### Pitch 2: Uplan to Xyne Spaces
*"In Uplan, I orchestrated multi-agent LangGraph pipelines that compiled unstructured data into typed semantic knowledge graphs with 98% token compression and deterministic rule gates. This directly mirrors Xyne Spaces' core problem: building a structured, verifiable Org Brain context layer where agents reason without hallucination."*

### Pitch 3: PathMapper to Payment Routing
*"PathMapper computed optimal routes across 10,000+ points on a 10k?10k grid in <0.5s by pruning the search state space using domain heuristics. Dynamic payment routing across banks under varying latency, success rates, and cost constraints is structurally the exact same constrained multi-objective path optimization problem."*
