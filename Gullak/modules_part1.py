# modules_part1.py - Gullak Technologies Backend Engineer Interview Modules Part 1

modules_part1 = {}

# ==============================================================================
# Module 00: START HERE - Executive Intel & Interview Blueprint
# ==============================================================================
modules_part1["00_START_HERE"] = """# Module 00: Executive Intel & Interview Blueprint

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
"""

# ==============================================================================
# Module 01: Signature OA & Algorithms Problems (C++ & Python)
# ==============================================================================
modules_part1["01_Online_Test_and_Algorithms"] = """# Module 01: Signature DSA & Puzzles (With Optimal C++ & Python Solutions)

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
* Time Complexity: $O(\\log N)$ per update, $O(\\log N)$ per balance query.
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

    std::cout << "Initial Balance [1 to 4]: " << ledger.get_balance(1, 4) << " mg\\n"; // -200 + 1500 - 300 + 750 = 1750
    ledger.update(2, 2000); // Changed 1500 to 2000
    std::cout << "Updated Balance [1 to 4]: " << ledger.get_balance(1, 4) << " mg\\n"; // 2250 mg
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
* The amount difference is at most `tolerance` paise ($|\\text{bank\\_amt} - \\text{internal\\_amt}| \\le \\text{tolerance}$).

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
Because the total transaction stream size $N$ is unbound ($N > 10^7$) and cannot fit into RAM simultaneously, design a streaming processor that maintains the Top K transactions in $O(\\log K)$ time per incoming transaction.

### Optimal Solution: Bounded Min-Heap
* Time Complexity: $O(N \\log K)$ overall, $O(\\log K)$ per event.
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
* For example, locker 12 has divisors: 1, 2, 3, 4, 6, 12 (6 divisors $\\to$ even number of toggles $\\to$ Closed $\\to$ Open $\\to$ Closed $\\to$ Open $\\to$ Closed $\\to$ Closed).
* In general, divisors of a number $L$ come in distinct pairs $(d, L/d)$.
* The only time a number has an **odd number of divisors** is when $d = L/d$, which means $L = d^2$ (i.e., $L$ is a **perfect square**!).
* Therefore, only lockers whose numbers are perfect squares will end up **OPEN**.

For $N = 100$:
The open lockers are: $1^2, 2^2, 3^2, 4^2, 5^2, 6^2, 7^2, 8^2, 9^2, 10^2$
$= \\mathbf{\\{1, 4, 9, 16, 25, 36, 49, 64, 81, 100\\}}$.
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
"""

# ==============================================================================
# Module 02: Core CS - OS, Concurrency & Networking
# ==============================================================================
modules_part1["02_Technical_Rounds_CS_Core"] = """# Module 02: OS, Concurrency & Networking Internals

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
* The backend initiates socket closure $\\to$ Sockets enter `TIME_WAIT` for 60 seconds.
* Linux has ~28,000 ephemeral ports (`/proc/sys/net/ipv4/ip_local_port_range`).
* At 1,000 requests/sec, all 28,000 ports are consumed in 28 seconds, throwing `EADDRNOTAVAIL` (Cannot assign requested address).
* **The Fix:** Enable HTTP Keep-Alive connection pooling (`MaxIdleConnsPerHost`), reuse TCP connections, or tune `tcp_tw_reuse` in Linux sysctl.
"""

print("modules_part1.py ready with modules 00, 01, 02.")
