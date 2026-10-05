# 05: Low-Level System Design & Test Architecture

This module details two production-grade system designs matching Apple's hiring tracks:
1. **AI/ML Track**: On-Device ML Inference Pipeline & Thermal-Aware Telemetry Dispatcher.
2. **SDET Track**: Distributed Automated Test Execution Harness with Flaky Test Quarantine.

---

## DESIGN 1 (AI/ML): On-Device ML Inference Pipeline

### Problem Definition
Design an on-device inference management system for iOS/macOS that accepts ML inference requests from multiple concurrent apps, optimizes execution on the **Apple Neural Engine (ANE)**, dynamically batches inputs, and throttles compute when device thermals rise.

### Architectural Diagram

```
[App 1 (Camera)]     [App 2 (Siri)]     [App 3 (Photos)]
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Inference Request Queue      │
          │   (Priority-Sorted Task Heap)    │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Dynamic Batching Engine      │
          │  (Timeout-Window / Max-Batch)    │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Thermal & Power Governor     │ ◄── [Device Thermal State API]
          │  (Nominal / Fair / Serious /     │
          │   Critical -> Throttling/Skip)   │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │       Core ML Execution Unit     │
          │   ANE / MPS GPU / Accelerate CPU │
          └──────────────────────────────────┘
```

### Key Components & Requirements
1. **Priority Scheduling**: Foreground user interactions (e.g., Camera real-time face tracking) receive `CRITICAL` priority; background indexing (e.g., Photos facial clustering) runs at `BACKGROUND` priority.
2. **Dynamic Batching**: If multiple inference requests for the same model arrive within a $5\text{ms}$ window, batch them up to batch size $B=8$ to maximize ANE tensor utilization.
3. **Thermal Throttling**: Query the OS thermal state. If thermal state is `SERIOUS` or `CRITICAL`, drop background tasks and throttle batch frequency to prevent device overheating and thermal shutdown.

### Working Python Scaffold Implementation

```python
import time
import heapq
import threading
from typing import List, Any
from dataclasses import dataclass, field

@dataclass(order=True)
class InferenceRequest:
    priority: int  # 0: Critical (User-Facing), 1: High, 2: Background
    timestamp: float = field(compare=True)
    task_id: str = field(compare=False)
    input_tensor: Any = field(compare=False)
    callback: Any = field(compare=False)

class OnDeviceInferenceEngine:
    def __init__(self, max_batch_size: int = 8, batch_timeout_sec: float = 0.005):
        self.max_batch_size = max_batch_size
        self.batch_timeout = batch_timeout_sec
        self.queue: List[InferenceRequest] = []
        self.lock = threading.Lock()
        self.running = True
        self.worker_thread = threading.Thread(target=self._dispatch_loop, daemon=True)
        self.worker_thread.start()

    def submit_request(self, task_id: str, priority: int, input_tensor: Any, callback: Any) -> None:
        req = InferenceRequest(
            priority=priority,
            timestamp=time.time(),
            task_id=task_id,
            input_tensor=input_tensor,
            callback=callback
        )
        with self.lock:
            heapq.heappush(self.queue, req)

    def _get_thermal_state(self) -> str:
        # Simulates querying Apple ProcessInfo.thermalState
        return "Nominal"

    def _dispatch_loop(self) -> None:
        while self.running:
            batch = []
            start_time = time.time()

            while time.time() - start_time < self.batch_timeout and len(batch) < self.max_batch_size:
                with self.lock:
                    if self.queue:
                        thermal = self._get_thermal_state()
                        # If thermal is critical, skip background tasks
                        if thermal == "Critical" and self.queue[0].priority > 0:
                            continue
                        batch.append(heapq.heappop(self.queue))
                    else:
                        break
                time.sleep(0.001)

            if batch:
                self._execute_batch(batch)

    def _execute_batch(self, batch: List[InferenceRequest]) -> None:
        # Hardware execution on Apple Neural Engine (ANE)
        inputs = [b.input_tensor for b in batch]
        # Simulated tensor inference
        results = [f"Inferred_{inp}" for inp in inputs]
        for req, res in zip(batch, results):
            if req.callback:
                req.callback(res)
```

---

## DESIGN 2 (SDET): Distributed Test Execution Harness with Flaky Quarantine

### Problem Definition
Design a high-throughput, distributed test execution framework that runs thousands of XCUITest and integration tests across a matrix of real iOS devices and simulators, isolating flaky tests automatically to prevent pipeline stalls.

### Architecture Overview

```
[Developer Git Push] ──► [CI Orchestrator (Jenkins / GitHub Actions)]
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │      Test Dispatcher Engine      │
                 │   • Reads test suite metadata    │
                 │   • Queries Flaky Test Quarantine│
                 └─────────────────┬────────────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 ▼                                   ▼
   ┌───────────────────────────┐       ┌───────────────────────────┐
   │    Main Test Runner       │       │  Quarantine Sandbox Pool  │
   │  (Gatekeeper for merges)  │       │  (Non-blocking diagnosis) │
   └─────────────┬─────────────┘       └─────────────┬─────────────┘
                 │                                   │
                 └─────────────────┬─────────────────┘
                                   ▼
                 ┌──────────────────────────────────┐
                 │        Worker Agent Farm         │
                 │  • iPhone 15 / 16 Simulators     │
                 │  • Physical Test Devices         │
                 │  • macOS Runner Nodes            │
                 └─────────────────┬────────────────┘
                                   ▼
                 ┌──────────────────────────────────┐
                 │    Artifact & Telemetry Store    │
                 │  Crash dumps, video, logs, traces│
                 └──────────────────────────────────┘
```

### Core Design Rules
1. **Flaky Test Quarantine**: If a test passes 2 times and fails 1 time on the exact same commit, its flaky variance score triggers quarantine. The test continues running in a non-blocking sandbox pool to accumulate diagnostic traces, but does not block developer pull requests.
2. **Exponential Backoff with Jitter for Retries**:
$$t_{\text{retry}} = \min(t_{\text{max}}, t_{\text{base}} \cdot 2^{\text{attempt}}) + \text{random}(0, 1)$$
3. **Artifact Isolation**: Each test run captures stdout, stderr, sysdiagnose dumps, and video screen captures into a structured object bucket keyed by `[commit_sha]/[test_id]/[run_index]`.
