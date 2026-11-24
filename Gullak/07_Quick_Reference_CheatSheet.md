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
