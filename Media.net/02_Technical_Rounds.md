# 02: Systems, Memory, OS, Networks & DBMS

Technical Round 2 at Media.net is famous for deep architectural grilling on core Computer Science fundamentals. You will not pass by reciting textbook definitions—interviewers probe memory layout, latency trade-offs, kernel boundaries, and concurrency pitfalls.

---

## 1. Operating Systems: Deep Mechanics

```
┌─────────────────────────────────────────────────────────────────┐
│                    Virtual Address Space                        │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│  Text / Code │ Data (BSS)   │  Heap (▲)    │  Stack (▼)         │
│  (Read-Only) │ Global / Var │  malloc / new│  Local / Ptrs / RA │
└──────────────┴──────────────┴──────────────┴────────────────────┘
```

### A. Process vs. Thread: Low-Level Reality
* **Process**: An independent instance of an executing program with its own isolated **Virtual Address Space**, page tables, file descriptor tables, and Process Control Block (PCB).
  * Context switch cost: High (typically 1–3 $\mu s$). Forces invalidation of CPU Translation Lookaside Buffer (TLB), triggering cache misses and pipeline stalls.
* **Thread**: A unit of CPU execution within a process. Threads of the same process share the text, data, and heap segments, file descriptors, and socket handles, but possess their own **Program Counter (PC)**, registers, and private **Stack**.
  * Context switch cost: Low (~100–300 ns). Page tables remain mapped; TLB entries remain valid.

### B. Virtual Memory, Paging & TLB
* **Virtual Address Translation**: When CPU issues a virtual memory address, the Memory Management Unit (MMU) uses the CR3 register to traverse the multi-level page table (e.g., 4-level paging on x86-64: PML4 $\to$ PDP $\to$ PD $\to$ PT $\to$ Physical Frame).
* **Translation Lookaside Buffer (TLB)**: An ultra-fast hardware cache of virtual-to-physical address mappings.
* **Page Fault**: Triggered by hardware interrupt when a virtual page is accessed that is either unmapped or paged out to swap disk. The kernel suspends the thread, loads the 4KB page from disk into RAM, updates the page table, and resumes execution.

### C. Concurrency: Mutex vs. Spinlock vs. Semaphore
| Mechanism | Blocking Behavior | When to Use at Media.net |
| :--- | :--- | :--- |
| **Mutex** | Puts waiting thread into kernel sleep (`futex` wait); yields CPU. | Critical sections lasting $> 500$ ns or involving I/O. |
| **Spinlock** | Busy-loops in user space burning CPU cycles (`PAUSE` instruction). | Ultra-low-latency in-memory RTB locks lasting $< 50$ ns. |
| **Counting Semaphore** | Maintains an integer counter; permits up to $N$ concurrent threads. | Resource pool throttling (e.g., maximum 50 concurrent DSP connections). |

### D. Deadlocks: The 4 Coffman Conditions
A deadlock can occur **if and only if** all four conditions hold simultaneously:
1. **Mutual Exclusion**: Resources cannot be shared.
2. **Hold and Wait**: Process holding a resource requests another.
3. **No Preemption**: Resources cannot be forcibly revoked.
4. **Circular Wait**: $P_1$ waits for $P_2$, ..., $P_n$ waits for $P_1$.
* **Deadlock Prevention Strategy**: Enforce a strict **global lock acquisition hierarchy** (always acquire Lock A before Lock B) to break Circular Wait.

---

## 2. Computer Networks: Real-Time Bidding Protocol Mechanics

```
Client / Browser             Media.net Edge SSP                 DSP Partner
     │                                │                              │
     │─── HTTP GET /ad_request ──────►│                              │
     │                                │─── TCP Handshake (SYN) ─────►│
     │                                │◄── SYN-ACK ──────────────────│
     │                                │─── ACK + OpenRTB Bid Req ───►│ (Hard 25ms timer)
     │                                │◄── OpenRTB Bid Response ─────│
     │◄── Ad Markup (HTML/JS) ────────│                              │
```

### A. TCP vs. UDP in Low-Latency Ad Bidding
* **Why RTB uses TCP**: Even though UDP has zero handshake overhead, financial transactions (ad impressions costing millions of dollars) require guaranteed packet delivery and data integrity. Losing bid responses causes revenue discrepancy and billing disputes.
* **Mitigating TCP Latency**: Media.net uses **Long-Lived Persistent TCP Connections (Keep-Alive)** and HTTP/2 connection pooling with DSPs. The 3-way handshake is performed once at startup, eliminating the 1-RTT handshake penalty during real-time auctions.

### B. TCP Connection Teardown & The `TIME_WAIT` Danger
* **The 4-Way FIN Handshake**: Initiator sends `FIN` $\to$ Responder sends `ACK` $\to$ Responder sends `FIN` $\to$ Initiator sends `ACK` $\to$ Initiator enters `TIME_WAIT`.
* **Duration**: $2 \times \text{MSL}$ (Maximum Segment Life, typically 60 seconds).
* **The Danger at Scale**: In an SSP processing 50,000 req/sec, closing connections naively creates tens of thousands of sockets trapped in `TIME_WAIT`. This exhausts the ephemeral port range ($1024 - 65535$), throwing `EADDRNOTAVAIL` (connection refused).
* **Production Fix**: Enable `SO_REUSEADDR`, implement connection pooling, and tune `net.ipv4.tcp_tw_reuse = 1`.

### C. HTTP/1.1 vs. HTTP/2 in Ad Exchanges
* **HTTP/1.1**: Suffers from **Head-of-Line (HoL) Blocking** at the application layer. Each HTTP request must wait for the previous response unless multiple TCP connections are opened.
* **HTTP/2**: Introduces **Binary Framing** and **Stream Multiplexing**. Hundreds of bid requests and responses travel concurrently over a single TCP connection, interleaved in independent streams with stream prioritization.

---

## 3. Database Management Systems (DBMS) Internals

### A. B-Tree vs. B+ Tree Indexing
Media.net relies heavily on MySQL (InnoDB) and custom distributed indexes.
* **Why B+ Trees Beat B-Trees for Disk & SSD Storage**:
  1. **Higher Fan-out**: Internal nodes in a B+ Tree store only keys and child pointers (no row data). This allows thousands of keys to fit into a single 16KB disk page, keeping the tree height shallow ($h \le 3$ for millions of rows).
  2. **Sequential Leaf Traversal**: All leaf nodes are linked in a bidirectional doubly-linked list. Range scans (e.g., `WHERE timestamp BETWEEN t1 AND t2`) require one $O(\log N)$ tree traversal to find the start, then linear linked-list traversal, avoiding costly random I/O.

### B. Clustered vs. Secondary (Non-Clustered) Index
* **Clustered Index**: The leaf pages *are* the actual data pages. The physical table rows are sorted and stored in primary key order. A table can have **only one** clustered index.
* **Secondary Index**: Leaves store the indexed column value plus the primary key pointer.
* **Double Lookup (Bookmark Lookup)**: Querying by a secondary index (`WHERE email = ?`) first navigates the secondary index to find the primary key, then navigates the clustered index to retrieve full row data.
* **Covering Index Optimization**: If a secondary index includes all required columns (`SELECT user_id, campaign_id FROM impressions WHERE user_id = ?`), the engine avoids the second lookup entirely.

### C. ACID Properties & Isolation Levels
* **Dirty Read**: Reading uncommitted data that is later rolled back.
* **Non-Repeatable Read**: Re-reading the same row returns different values because another transaction committed an `UPDATE`.
* **Phantom Read**: Re-running a range query returns newly inserted rows committed by another transaction.

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Mechanism |
| :--- | :---: | :---: | :---: | :--- |
| **Read Uncommitted** | Yes | Yes | Yes | Dirty reads allowed; no shared locks. |
| **Read Committed** | No | Yes | Yes | MVCC snapshot read per statement. |
| **Repeatable Read** (MySQL default) | No | No | No (MVCC) | MVCC snapshot read created at first query; Next-Key locking. |
| **Serializable** | No | No | No | Strict 2-Phase Locking (2PL); shared locks on ranges. |

---

## 4. High-Yield SQL Interview Queries

### Query 1: Find the $N$-th Highest Bidder Price
```sql
-- Using Window Function DENSE_RANK()
WITH RankedBids AS (
    SELECT 
        bidder_id,
        bid_price,
        DENSE_RANK() OVER (ORDER BY bid_price DESC) as price_rank
    FROM dsp_bids
)
SELECT DISTINCT bid_price 
FROM RankedBids 
WHERE price_rank = 3; -- 3rd highest price
```

### Query 2: Publisher Click-Through-Rate (CTR) and eCPM Aggregation
```sql
SELECT 
    publisher_id,
    COUNT(impression_id) AS total_impressions,
    COUNT(click_id) AS total_clicks,
    ROUND((COUNT(click_id) * 100.0) / NULLIF(COUNT(impression_id), 0), 2) AS ctr_percentage,
    ROUND((SUM(clearing_price) / NULLIF(COUNT(impression_id), 0)) * 1000.0, 4) AS ecpm_usd
FROM ad_logs
WHERE event_date = CURRENT_DATE
GROUP BY publisher_id
HAVING total_impressions >= 1000
ORDER BY ecpm_usd DESC;
```
