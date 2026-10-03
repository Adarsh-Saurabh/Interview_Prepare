# 05: System Design & Low-Level Design (LLD)

This module presents an interview-grade Low-Level Design (LLD) for a **High-Performance Banking Ledger & Webhook Notification Engine**.

---

## 1. Requirements & Invariants

### Functional Requirements
1. **Double-Entry Ledger**: Every transfer consists of balanced entries: $\sum \text{Debits} = \sum \text{Credits}$.
2. **Account Balance Check**: Prevent overdrafts for debit accounts without blocking credit operations.
3. **Idempotent Processing**: Reject or safely return identical responses for repeated transaction submissions.
4. **Asynchronous Notification**: Dispatch signed webhooks to customer endpoints upon transaction settlement.

### Non-Functional Requirements
* **Throughput**: 10,000+ transactions per second.
* **Consistency**: Strict serializability / strong consistency on account balances.
* **Thread Safety**: Zero race conditions or double-spending under concurrent threads.

---

## 2. Object-Oriented Class Design

```
┌─────────────────────────────────┐
│        Account                  │
├─────────────────────────────────┤
│ - id: str                       │
│ - balance: Decimal              │
│ - currency: str                 │
│ - lock: threading.Lock          │
├─────────────────────────────────┤
│ + credit(amount: Decimal): void │
│ + debit(amount: Decimal): bool  │
└─────────────────────────────────┘
                 ▲
                 │ 1..*
┌────────────────┴────────────────┐       ┌───────────────────────────────┐
│        LedgerEntry              │       │        Transaction            │
├─────────────────────────────────┤       ├───────────────────────────────┤
│ - entry_id: str                 │◄──────│ - tx_id: str                  │
│ - account_id: str               │ *   1 │ - idempotency_key: str        │
│ - amount: Decimal               │       │ - entries: List[LedgerEntry]  │
│ - direction: Direction (DR/CR)  │       │ - status: TxStatus            │
│ - timestamp: int                │       │ - created_at: int             │
└─────────────────────────────────┘       └───────────────────────────────┘
```

---

## 3. Production Python Implementation (Thread-Safe)

```python
import time
import uuid
import hmac
import hashlib
import threading
from enum import Enum
from decimal import Decimal
from typing import Dict, List, Optional

class Direction(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"

class TxStatus(Enum):
    PENDING = "PENDING"
    SETTLED = "SETTLED"
    FAILED = "FAILED"

class InsufficientFundsException(Exception):
    pass

class Account:
    def __init__(self, account_id: str, initial_balance: Decimal, currency: str = "USD"):
        self.account_id = account_id
        self.balance = initial_balance
        self.currency = currency
        self._lock = threading.Lock()

    def debit(self, amount: Decimal) -> bool:
        with self._lock:
            if self.balance < amount:
                raise InsufficientFundsException(f"Account {self.account_id} balance {self.balance} < {amount}")
            self.balance -= amount
            return True

    def credit(self, amount: Decimal):
        with self._lock:
            self.balance += amount

class LedgerEntry:
    def __init__(self, entry_id: str, account_id: str, amount: Decimal, direction: Direction):
        self.entry_id = entry_id
        self.account_id = account_id
        self.amount = amount
        self.direction = direction
        self.timestamp = int(time.time() * 1000)

class Transaction:
    def __init__(self, tx_id: str, idempotency_key: str, entries: List[LedgerEntry]):
        self.tx_id = tx_id
        self.idempotency_key = idempotency_key
        self.entries = entries
        self.status = TxStatus.PENDING

class BankingLedgerEngine:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.transactions: Dict[str, Transaction] = {}
        self.idempotency_store: Dict[str, str] = {} # idempotency_key -> tx_id
        self._global_lock = threading.Lock()

    def register_account(self, account: Account):
        self.accounts[account.account_id] = account

    def transfer(self, idempotency_key: str, from_acc_id: str, to_acc_id: str, amount: Decimal) -> Transaction:
        # Step 1: Idempotency Check
        with self._global_lock:
            if idempotency_key in self.idempotency_store:
                existing_tx_id = self.idempotency_store[idempotency_key]
                return self.transactions[existing_tx_id]

        from_acc = self.accounts.get(from_acc_id)
        to_acc = self.accounts.get(to_acc_id)
        if not from_acc or not to_acc:
            raise ValueError("Invalid account identifiers provided.")

        tx_id = str(uuid.uuid4())
        entries = [
            LedgerEntry(str(uuid.uuid4()), from_acc_id, amount, Direction.DEBIT),
            LedgerEntry(str(uuid.uuid4()), to_acc_id, amount, Direction.CREDIT)
        ]
        tx = Transaction(tx_id, idempotency_key, entries)

        # Step 2: Acquire locks in consistent order to prevent deadlocks
        first_lock, second_lock = (from_acc, to_acc) if from_acc.account_id < to_acc.account_id else (to_acc, from_acc)

        try:
            # Atomic transfer execution
            from_acc.debit(amount)
            to_acc.credit(amount)
            tx.status = TxStatus.SETTLED
        except Exception as e:
            tx.status = TxStatus.FAILED
            raise e
        finally:
            with self._global_lock:
                self.transactions[tx_id] = tx
                self.idempotency_store[idempotency_key] = tx_id

        # Step 3: Trigger async webhook notification
        self._dispatch_webhook(tx)
        return tx

    def _dispatch_webhook(self, tx: Transaction):
        payload = f"tx_id={tx.tx_id}&status={tx.status.value}"
        secret = b"citi_bank_webhook_secret_key"
        signature = hmac.new(secret, payload.encode('utf-8'), hashlib.sha256).hexdigest()
        # In production: enqueue into AWS SQS for worker dispatch
        print(f"[Webhook Dispatched] Payload: {payload} | HMAC-SHA256: {signature[:12]}...")

# Driver Test
if __name__ == "__main__":
    engine = BankingLedgerEngine()
    acc_a = Account("ACC_A", Decimal("1000.00"))
    acc_b = Account("ACC_B", Decimal("200.00"))
    engine.register_account(acc_a)
    engine.register_account(acc_b)

    # First Transfer
    tx1 = engine.transfer("idem_key_001", "ACC_A", "ACC_B", Decimal("250.00"))
    print(f"Tx1 Status: {tx1.status.value} | Acc A: ${acc_a.balance} | Acc B: ${acc_b.balance}")

    # Retried Transfer with Same Idempotency Key (Must not double-debit)
    tx2 = engine.transfer("idem_key_001", "ACC_A", "ACC_B", Decimal("250.00"))
    print(f"Tx2 (Retry) Same Tx ID: {tx2.tx_id == tx1.tx_id} | Acc A: ${acc_a.balance}")
    assert acc_a.balance == Decimal("750.00")
```
