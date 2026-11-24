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
