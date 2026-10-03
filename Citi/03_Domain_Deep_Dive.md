# 03: FinTech, Payment Rails & Banking Architecture

This module details the financial technology concepts central to Citi's Treasury and Trade Solutions (TTS) and Markets Technology divisions.

---

## 1. Global Payment Rails & Clearing Systems

### RTGS vs Batch Clearing
1. **Real-Time Gross Settlement (RTGS)**:
   * Transactions are settled individually and immediately upon processing across central bank reserve accounts.
   * **Characteristics**: Zero credit risk, irrevocable, high value, continuous real-time settlement.
2. **Automated Clearing House (ACH / NEFT / NACH)**:
   * Net settlement processed in cyclical batches. Receivables and payables are netted before funds transfer.
   * **Characteristics**: Low cost, higher volume, delayed settlement (batch intervals).

### Messaging Standards: SWIFT MT to ISO 20022
* Legacy international financial messaging used SWIFT **MT (Message Type)** formats (e.g., `MT103` for single customer credit transfers, `MT202` for bank-to-bank transfers).
* **ISO 20022 Migration (`pacs.008`)**: Modern XML/JSON financial data dictionary providing richer unstructured data, Unicode support, end-to-end audit tracing, and fraud screening attributes.

---

## 2. Distributed Consensus & Transactional Guarantees

In distributed banking systems spanning multiple microservices (Account Service, Fraud Service, Ledger Service), transactions cannot rely on a single database lock.

### The Two-Phase Commit (2PC) vs Saga Pattern
* **Two-Phase Commit (2PC)**:
  * Coordinator sends `Prepare` to all participants; if all vote `Commit`, coordinator issues `Commit`.
  * **Drawback**: Blocking protocol. If coordinator or network stalls during prepare, locks remain held, causing severe latency and cascading failure.
* **Saga Pattern (Modern Microservices)**:
  * A series of local transactions coordinated via events. Each step updates its local database.
  * If a step fails, the Saga executes **Compensating Transactions** in reverse order to undo changes (e.g., `RefundAccount`).
  * Implemented via **Orchestration** (central orchestrator state machine) or **Choreography** (Kafka event topics).

```
[Client Request: Transfer $1,000]
          │
          ▼
   [Saga Orchestrator]
     ├── 1. Reserve Funds (Debit Account Service)
     ├── 2. Anti-Money Laundering (AML) Screening
     ├── 3. Credit Recipient (Ledger Service)
     └── [On Failure in Step 2] ──> Execute Compensating Refund on Step 1
```

---

## 3. Idempotent Payment APIs & Outbox Pattern

### Idempotency Keys in Financial APIs
* **The Network Timeout Trap**: Client sends `POST /api/v1/payments`. The server completes the debit, but the network drops before returning the `200 OK`. The client automatically retries.
* **Idempotency Key Mechanism**:
  1. Client generates a unique UUID `Idempotency-Key` header with each request.
  2. Server uses atomic storage (Redis / MongoDB unique index) to store `(Idempotency-Key, Status, ResponsePayload)`.
  3. If duplicate key arrives while processing: return `409 Conflict` or wait.
  4. If duplicate arrives after completion: return cached original response without re-executing debit.

### Transactional Outbox Pattern
Ensures reliable delivery between database updates and message broker publishing (e.g., Kafka):
* Within the database ACID transaction, write both the business entity AND an `outbox` event record into the same DB.
* A separate CDC (Change Data Capture) or polling worker reads the outbox table and dispatches events to Kafka, guaranteeing **at-least-once delivery**.

---

## 4. Banking Security & Compliance Architecture
* **PCI-DSS (Payment Card Industry Data Security Standard)**: Never store raw CVV codes; primary account numbers (PAN) must be tokenized or strongly encrypted using AES-256.
* **Mutual TLS (mTLS)**: Both client and server authenticate each other using X.509 digital certificates for inter-service communication.
* **HMAC Signatures**: Webhook payloads are hashed with a shared secret (`HMAC-SHA256`) and sent in HTTP headers (`X-Signature`) to prevent tampering.
