# modules_part2.py - Gullak Technologies Backend Engineer Interview Modules Part 2

modules_part2 = {}

# ==============================================================================
# Module 03: DBMS, ACID & Redis Distributed Systems
# ==============================================================================
modules_part2["03_Database_Internals_and_Transactions"] = """# Module 03: Database Internals, ACID & Redis Distributed Systems

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
* **PostgreSQL Auto-VACUUM:** Background daemon that scans table pages, identifies dead tuples where $\\text{xmax} < \\text{oldest active transaction snapshot}$, and reclaims disk space for future row inserts.

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
"""

# ==============================================================================
# Module 04: Fintech System Design - LLD & HLD
# ==============================================================================
modules_part2["04_System_Design_LLD_and_HLD"] = """# Module 04: Fintech System Design (LLD & HLD)

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
"""

# ==============================================================================
# Module 05: Candidate Resume Grilling & Defenses
# ==============================================================================
modules_part2["05_Candidate_Resume_Grilling"] = """# Module 05: Candidate Resume Defense & Technical Traps

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
"""

print("modules_part2.py ready with modules 03, 04, 05.")
