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
