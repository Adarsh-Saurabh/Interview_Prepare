# 04: System Design & LLD: Payment Gateway Orchestrator ? Juspay Technologies

---

## 1. High-Level Architecture & Transaction Flow

A payment switch sits between high-volume merchant applications and heterogeneous banking rails.

```
???????????????????????????????????????????????????????????????
?                    MERCHANT CHECKOUT CLIENT                 ?
?         HyperCheckout SDK (PureScript / Native C++)         ?
???????????????????????????????????????????????????????????????
                               ? POST /v1/payments (Idempotency-Key: UUID)
                               ?
???????????????????????????????????????????????????????????????
?                 JUSPAY API GATEWAY / ROUTER                 ?
?         (TLS Termination, Rate Limiting, Fingerprint)       ?
???????????????????????????????????????????????????????????????
                               ?
            ???????????????????????????????????????
            ?                                     ?
?????????????????????????             ?????????????????????????
? Layer 1: Redis Lock   ?             ? Layer 2: PostgreSQL   ?
? SET NX EX 30s         ?             ? ACID Unique Key DDL   ?
?????????????????????????             ?????????????????????????
            ???????????????????????????????????????
                               ?
                               ?
???????????????????????????????????????????????????????????????
?               PAYMENT ORCHESTRATOR STATE MACHINE            ?
?            (Euler / Hyperswitch Distributed Core)           ?
?                                                             ?
?   ???????????????????????         ???????????????????????   ?
?   ? Dynamic MAB Router  ?         ? KvDB Write-Back WAL ?   ?
?   ? (Bank Allocation)   ?         ? (Append-Only State) ?   ?
?   ???????????????????????         ???????????????????????   ?
???????????????????????????????????????????????????????????????
               ?                               ?
               ?                               ?
??????????????????????????????????   ??????????????????????????
? BANK GATEWAYS (NPCI / HDFC)    ?   ? MERCHANT WEBHOOK S2S   ?
? ISO 8583 / REST / SDK Pin Page ?   ? Exp Backoff + Jitter   ?
??????????????????????????????????   ??????????????????????????
```

---

## 2. Payment State Machine & Invariants

```
                  ????????????????
                  ?   CREATED    ?
                  ????????????????
                         ? (User clicks Pay)
                         ?
                  ????????????????
                  ?  INITIATED   ?
                  ????????????????
                         ? (Sent to Bank / UPI PIN)
                         ?
               ??????????????????????
        ????????  PENDING_GATEWAY   ????????
        ?      ??????????????????????      ?
        ? (Success Webhook)                ? (Declined / Timeout)
        ?                                  ?
 ????????????????                   ????????????????
 ?   SUCCESS    ?                   ?    FAILED    ?
 ????????????????                   ????????????????
        ? (Refund Triggered)
        ?
 ????????????????
 ?   REFUNDED   ?
 ????????????????
```

### 2.1 State Transition Invariants
1. **Terminal Non-Reversibility**: Once a transaction reaches `SUCCESS`, `FAILED`, or `REFUNDED`, its status cannot be modified except via formal accounting reversal.
2. **Optimistic Concurrency Control (OCC)**: State mutations are guarded by monotonic version numbers to prevent concurrent duplicate updates:
```sql
UPDATE payments
SET status = 'SUCCESS',
    gateway_reference = :gateway_ref,
    version = version + 1,
    updated_at = NOW()
WHERE id = :payment_id
  AND status = 'PENDING_GATEWAY'
  AND version = :expected_version;
```

---

## 3. Distributed Idempotency Deep Dive

### 3.1 What is an Idempotency Key?
Clients supply a unique header: `Idempotency-Key: 7b83a210-9b4e-4f1b-a91c-22312b919934`.
The payment switch guarantees that multiple requests with the same key execute the underlying financial transaction **exactly once**.

### 3.2 Dual-Layer Idempotency Architecture
1. **Layer 1: Redis Fast In-Flight Interception**:
   - `SET payment:lock:{merchant_id}:{idempotency_key} {request_hash} NX EX 30`
   - If key already exists: Check hash. If identical, wait/poll Redis PubSub for cached result. If hash differs, return `HTTP 422 Unprocessable Entity`.
2. **Layer 2: PostgreSQL ACID Persistence**:
```sql
CREATE TABLE idempotency_keys (
    merchant_id VARCHAR(64) NOT NULL,
    idempotency_key VARCHAR(128) NOT NULL,
    request_hash CHAR(64) NOT NULL,
    status VARCHAR(32) NOT NULL, -- 'PROCESSING', 'RESOLVED'
    response_code INT,
    response_body JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    PRIMARY KEY (merchant_id, idempotency_key)
);
```

### 3.3 The Redlock Critique & Fencing Tokens
- **The Problem (Martin Kleppmann)**: A thread holding a Redis lock experiences a 15-second GC pause. Redis TTL expires. Thread B acquires the lock. Thread A wakes up and writes to the database?causing double payment!
- **The Solution (Monotonic Fencing Tokens)**:
  - Redis generates a monotonically increasing token (e.g. `1042`, `1043`).
  - Database rejects any write where `fencing_token <= last_seen_token`:
```sql
UPDATE merchant_accounts
SET balance = balance - :amount,
    last_fencing_token = :fencing_token
WHERE merchant_id = :merchant_id
  AND last_fencing_token < :fencing_token;
```

---

## 4. Distributed Transactions: Why 2PC Fails vs. The Saga Pattern

| Pattern | Mechanism | Latency / Scale | Failure Mode | Applicability to 350M+ Txns |
| :--- | :--- | :--- | :--- | :--- |
| **Two-Phase Commit (2PC)** | Prepare phase + Commit phase with blocking coordinator lock | Extreme latency ($>500\text{ms}$); blocks database resources | Coordinator crash leaves all databases locked | **Infeasible** at India-scale |
| **Saga (Orchestrated)** | Sequence of local transactions coordinated by a state machine; compensation actions on failure | Sub-millisecond local commits; highly scalable | Network partition triggers asynchronous compensating saga | **Industry Standard** |

---

## 5. Webhook Delivery & Resilience: Full Jitter Exponential Backoff

When delivering Server-to-Server (S2S) transaction results to merchants, network drops and merchant server overloads occur frequently.

### 5.1 Full Jitter Backoff Formula
To prevent thundering herd spikes when a merchant's server recovers:
$$T = \text{random}(0, \min(T_{\max}, T_{\text{base}} \cdot 2^{\text{attempt}}))$$

```python
import random

def get_backoff_delay(attempt: int, base: float = 1.0, cap: float = 60.0) -> float:
    temp = min(cap, base * (2 ** attempt))
    return random.uniform(0, temp)
```

---

## 6. Complete Production-Grade LLD (Python & C++)

```python
import hashlib
import json
import time
from enum import Enum
from typing import Dict, Optional, Tuple

class PaymentState(Enum):
    CREATED = "CREATED"
    INITIATED = "INITIATED"
    PENDING_GATEWAY = "PENDING_GATEWAY"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

class PaymentRequest:
    def __init__(self, merchant_id: str, idempotency_key: str, amount: float, currency: str):
        self.merchant_id = merchant_id
        self.idempotency_key = idempotency_key
        self.amount = amount
        self.currency = currency
        self.hash = self._compute_hash()

    def _compute_hash(self) -> str:
        payload = f"{self.merchant_id}:{self.idempotency_key}:{self.amount}:{self.currency}"
        return hashlib.sha256(payload.encode()).hexdigest()

class IdempotencyRecord:
    def __init__(self, request_hash: str):
        self.request_hash = request_hash
        self.state = "PROCESSING"
        self.response: Optional[Dict] = None

class MockKvDB:
    def __init__(self):
        self.payments: Dict[str, Dict] = {}
        self.idempotency_table: Dict[Tuple[str, str], IdempotencyRecord] = {}

    def insert_idempotency_key(self, merchant_id: str, key: str, req_hash: str) -> bool:
        pair = (merchant_id, key)
        if pair in self.idempotency_table:
            return False
        self.idempotency_table[pair] = IdempotencyRecord(req_hash)
        return True

    def get_idempotency_record(self, merchant_id: str, key: str) -> Optional[IdempotencyRecord]:
        return self.idempotency_table.get((merchant_id, key))

    def update_payment_occ(self, payment_id: str, expected_version: int, new_status: PaymentState) -> bool:
        record = self.payments.get(payment_id)
        if not record or record["version"] != expected_version:
            return False
        record["status"] = new_status
        record["version"] += 1
        return True

class PaymentOrchestrator:
    def __init__(self, db: MockKvDB):
        self.db = db

    def process_payment(self, req: PaymentRequest) -> Tuple[int, Dict]:
        # Step 1: Idempotency Check
        inserted = self.db.insert_idempotency_key(req.merchant_id, req.idempotency_key, req.hash)
        if not inserted:
            record = self.db.get_idempotency_record(req.merchant_id, req.idempotency_key)
            if record.request_hash != req.hash:
                return 422, {"error": "Idempotency key reused with mismatched payload"}
            if record.state == "PROCESSING":
                return 409, {"status": "IN_FLIGHT", "message": "Transaction currently processing"}
            return 200, record.response

        # Step 2: Initialize Payment Record
        payment_id = f"pay_{int(time.time() * 1000)}"
        self.db.payments[payment_id] = {
            "id": payment_id,
            "merchant_id": req.merchant_id,
            "amount": req.amount,
            "status": PaymentState.INITIATED,
            "version": 1
        }

        # Step 3: Transition to PENDING and Route to Bank
        self.db.update_payment_occ(payment_id, 1, PaymentState.PENDING_GATEWAY)

        # Mock Bank Dispatch (simulating gateway success)
        time.sleep(0.01) # Simulated bank I/O
        bank_auth_code = f"AUTH_NPCI_{payment_id}"

        # Step 4: Atomic Commit via OCC
        success = self.db.update_payment_occ(payment_id, 2, PaymentState.SUCCESS)
        if not success:
            return 500, {"error": "Concurrent modification detected"}

        response_payload = {
            "payment_id": payment_id,
            "status": "SUCCESS",
            "auth_code": bank_auth_code,
            "amount": req.amount
        }

        # Step 5: Resolve Idempotency Record
        rec = self.db.get_idempotency_record(req.merchant_id, req.idempotency_key)
        rec.state = "RESOLVED"
        rec.response = response_payload

        return 200, response_payload
```
