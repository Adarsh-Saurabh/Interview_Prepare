# 05: Event Log Ingestion Engine LLD

## 1. System Design Requirement: High-Throughput Event Ingestion Engine
Design a Low-Level Design (LLD) for an enterprise event ingestion service that:
1. Receives raw JSON event logs from ERP connectors (SAP, Salesforce).
2. Validates mandatory schema fields (`case_id`, `activity`, `timestamp`).
3. Buffers valid events into an in-memory concurrent queue.
4. Flushes batches of events to persistent storage (PostgreSQL/Columnar DB) when batch size reaches 1,000 events OR every 500 milliseconds.
5. Adheres strictly to **SOLID design principles**.

---

## 2. Object-Oriented Class Architecture (Python Production Implementation)

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import threading
import time

@dataclass(frozen=True)
class EventRecord:
    case_id: str
    activity: str
    timestamp: datetime
    payload: dict

class EventValidator(ABC):
    @abstractmethod
    def validate(self, raw_data: dict) -> Optional[EventRecord]:
        pass

class StandardEventValidator(EventValidator):
    def validate(self, raw_data: dict) -> Optional[EventRecord]:
        try:
            case_id = str(raw_data['case_id']).strip()
            activity = str(raw_data['activity']).strip()
            timestamp_str = raw_data['timestamp']
            
            if not case_id or not activity:
                return None
            
            # ISO timestamp parsing
            timestamp = datetime.fromisoformat(timestamp_str)
            payload = raw_data.get('payload', {})
            return EventRecord(case_id, activity, timestamp, payload)
        except (KeyError, ValueError):
            return None

class EventStorageSink(ABC):
    @abstractmethod
    def flush(self, batch: List[EventRecord]) -> bool:
        pass

class PostgresStorageSink(EventStorageSink):
    def flush(self, batch: List[EventRecord]) -> bool:
        # In production: Executed via batch COPY or parameterized bulk insert
        print(f"[PostgresSink] Successfully persisted batch of {len(batch)} events.")
        return True

class BatchingIngestionEngine:
    def __init__(self, validator: EventValidator, sink: EventStorageSink, batch_size=1000, flush_interval_ms=500):
        self.validator = validator
        self.sink = sink
        self.batch_size = batch_size
        self.flush_interval_sec = flush_interval_ms / 1000.0
        self.buffer: List[EventRecord] = []
        self.lock = threading.Lock()
        self.is_running = True
        
        # Background worker for timer-based flush
        self.flusher_thread = threading.Thread(target=self._periodic_flush_worker, daemon=True)
        self.flusher_thread.start()

    def ingest(self, raw_data: dict) -> bool:
        record = self.validator.validate(raw_data)
        if not record:
            return False

        with self.lock:
            self.buffer.append(record)
            if len(self.buffer) >= self.batch_size:
                self._flush_locked()
        return True

    def _flush_locked(self):
        if not self.buffer:
            return
        batch_to_write = self.buffer
        self.buffer = []
        # Hand off batch to persistent sink
        self.sink.flush(batch_to_write)

    def _periodic_flush_worker(self):
        while self.is_running:
            time.sleep(self.flush_interval_sec)
            with self.lock:
                self._flush_locked()

    def shutdown(self):
        self.is_running = False
        with self.lock:
            self._flush_locked()
```

---

## 3. High-Level Distributed Architecture (HLD Snapshot)

```
[Enterprise ERP Source] ──> [API Gateway / Rate Limiter]
                                  │
                                  ▼
                        [Kafka Event Topic]
                     (Partitioned by Hash(case_id))
                                  │
                   ┌──────────────┴──────────────┐
                   ▼                             ▼
         [Consumer Ingestion Node 1]   [Consumer Ingestion Node 2]
                   │                             │
                   ▼                             ▼
         [In-Memory Ring Buffer]       [In-Memory Ring Buffer]
                   │                             │
                   └──────────────┬──────────────┘
                                  ▼
                     [Columnar Storage / PostgreSQL]
```
