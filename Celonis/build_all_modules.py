#!/usr/bin/env python3
"""
build_all_modules.py
Generates all Markdown (.md) and HTML (.html) modules for Celonis
Associate Engineer Interview Preparation Portal.
"""

import os
import markdown
from template import render_celonis_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modules_data = {}

# =============================================================================
# MODULE 00: Company & Role Intel
# =============================================================================
modules_data["00_START_HERE"] = {
    "title": "00: Celonis Company & Role Intel",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Celonis Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Celonis SE** (Founded 2011 in Munich, Germany, by Alexander Rinke, Bastian Nominacher, and Martin Klenk from Technical University of Munich - TUM).
* **Valuation**: **$13 Billion+ Decacorn**, backed by premier venture capital firms including 83North, Accel, Arena Holdings, and T. Rowe Price.
* **Dual Headquarters**: Munich (Germany) & New York City (USA), with major global engineering hubs in **Bengaluru (India)**, Madrid, Pristina, and Tokyo.
* **Core Product**: Pioneer and uncontested global leader in **Process Mining** and the **Execution Management System (EMS)**.
* **Enterprise Customer Base**: Over 1,400+ leading enterprises globally, including Siemens, BMW, Uber, Dell, Cisco, L'Oréal, AstraZeneca, and Johnson & Johnson.

---

## 2. Core Architecture & Engineering Foundation

Celonis bridges the gap between raw enterprise IT transaction records and real-world operational execution:

```
[Enterprise Source Systems]
(SAP ERP, Salesforce, Oracle, ServiceNow, Workday)
         │
         │ Real-time & Batch Connectors (Kafka / CDC / APIs)
         ▼
[Data Extraction & Ingestion Engine]
         │ (Extract Event Logs: Case ID, Activity, Timestamp, Resource)
         ▼
[In-Memory Columnar Database & PQL Engine]
         │ (Process Query Language: Custom vector engine optimized for graphs)
         ▼
[Process Graph & Variant Discovery Layer]
         │ (Directed Graphs, Petri Nets, Inductive / Alpha Miner)
         ▼
[Execution Management System (EMS)]
  ├── Process Analytics (Bottlenecks, Cycle Time, Deviations)
  ├── Conformance Checking (Prescribed vs Actual Execution)
  ├── Action Engine (Automated Webhooks, Alerts, RPA triggers)
  └── Process Copilot (GenAI & LLM-assisted process queries)
```

### Key Technical Concepts to Know:
1. **The Event Log**: Every process starts with 3 mandatory columns:
   * **Case ID**: The unique identifier of a process instance (e.g., Purchase Order `#450012`).
   * **Activity**: The specific step completed (e.g., `Create PO`, `Approve PO`, `Goods Receipt`, `Pay Invoice`).
   * **Timestamp**: Exact UTC epoch when the activity transpired.
2. **Process Graph**: Directed graphs reconstructed from timestamp ordering across all cases. Nodes represent activities; edges represent process transitions with throughput times and transition frequencies.
3. **PQL (Process Query Language)**: Celonis's custom in-memory query language built in C++ and Java that evaluates graph calculations (e.g., `CALC_THROUGHPUT(ALL_RUNS)`) over billions of rows at sub-second response times.
4. **Object-Centric Process Mining (OCPM)**: Next-generation process intelligence that models multiple interacting business entities simultaneously (Orders, Items, Invoices, Deliveries) eliminating legacy 2D Case ID bottlenecks.

---

## 3. Placement Drive Specification (NIT Rourkela 2027 Batch)

| Parameter | Placement Drive Details |
| :--- | :--- |
| **Target Role** | **Associate Engineer** |
| **Location** | Bengaluru Tech Hub, India |
| **Compensation (CTC)** | **₹22.00 LPA Total**<br>• Fixed Base: ₹16.20 LPA<br>• Annual Performance Bonus: ₹1.80 Lakhs<br>• Sign-on Bonus: ₹4.00 LPA |
| **Internship Duration** | 6-Month Internship leading directly into Full-Time Employment (FTE) |
| **Eligible Batches** | 2027 (B.Tech, M.Tech, Dual Degree, Int MSc - All Branches eligible) |
| **Eligibility Criteria** | **CGPA $\ge 7.0$**, No Active Backlogs |
| **Application Deadline** | **11:59 PM, 23rd September 2026** |
| **Pre-Placement Talk (PPT)** | **24th September 2026** |
| **Online Assessment (OA)** | **25th September 2026** |
| **Personal Interviews** | **28th September 2026** |

---

## 4. The 3 Technical Pillars Evaluated at Celonis

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     1. Algorithmic Graph DSA    │   │  2. Concurrency & Core Systems  │   │  3. Enterprise SaaS & Backend   │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ • Directed Graph Traversal      │   │ • Multithreading & Race Conds   │   │ • RESTful API & Microservices   │
│ • DAG Topological Sorting       │   │ • Thread Pools & Synchronization│   │ • PostgreSQL & SQL Windowing    │
│ • Cycle Detection in Workflow   │   │ • Locks, Mutexes, CAS Atomics   │   │ • Multi-Tenant Data Isolation   │
│ • Sliding Window Burst Ingestion│   │ • JVM / C++ Memory Internals    │   │ • High-Throughput Buffers & LLD │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```
"""
}

# =============================================================================
# MODULE 01: Online Test (OA)
# =============================================================================
modules_data["01_Online_Test"] = {
    "title": "01: Signature OA Coding & Core CS Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company & Role Intel",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: Concurrency & Core Systems",
    "markdown": """# 01: Signature OA Coding & Core CS Problems

## 1. Online Assessment (OA) Architecture
* **Platform**: HackerRank / HackerEarth / Mettl
* **Duration**: 90 – 120 Minutes
* **Section 1**: 2–3 Algorithmic Coding Problems (Medium to Hard difficulty).
* **Section 2**: 10–15 Computer Science Fundamentals MCQs (Operating Systems, DBMS, OOPs, Concurrency, and SQL).

---

## 2. Signature Coding Problem 1: Process Variant Topological Sort & Cycle Detection

### Problem Statement
In an automated process mining engine, business workflows are represented as a directed graph where vertices represent activities (e.g., `Create Order`, `Credit Check`, `Dispatch`) and directed edges represent valid sequencing dependencies.
Given $N$ activities labeled $0$ to $N-1$ and a list of directed prerequisite pairs $[u, v]$ meaning activity $u$ must complete before activity $v$ can start:
1. Determine if the business process contains circular deadlocks (infinite looping/cycles).
2. If no cycle exists, return a valid linear execution order (Topological Sort).
3. If multiple valid orders exist, return the lexicographically smallest execution order. If a cycle exists, return an empty array.

### Optimal Solution: Kahn's Algorithm with Min-Heap (Priority Queue)
* **Time Complexity**: $\\mathcal{O}(V \\log V + E)$ where $V$ is the number of activities and $E$ is dependencies.
* **Space Complexity**: $\\mathcal{O}(V + E)$ for adjacency list and in-degree tracking.

#### C++ Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>

std::vector<int> findProcessExecutionOrder(int numActivities, const std::vector<std::pair<int, int>>& dependencies) {
    std::vector<std::vector<int>> adj(numActivities);
    std::vector<int> inDegree(numActivities, 0);

    for (const auto& edge : dependencies) {
        adj[edge.first].push_back(edge.second);
        inDegree[edge.second]++;
    }

    // Min-heap ensures lexicographically smallest ordering
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    for (int i = 0; i < numActivities; ++i) {
        if (inDegree[i] == 0) {
            minHeap.push(i);
        }
    }

    std::vector<int> executionOrder;
    while (!minHeap.empty()) {
        int current = minHeap.top();
        minHeap.pop();
        executionOrder.push_back(current);

        for (int neighbor : adj[current]) {
            inDegree[neighbor]--;
            if (inDegree[neighbor] == 0) {
                minHeap.push(neighbor);
            }
        }
    }

    // If topological order does not contain all activities, a cycle exists
    if (executionOrder.size() != static_cast<size_t>(numActivities)) {
        return {}; // Process Deadlock Detected
    }

    return executionOrder;
}
```

#### Python Implementation
```python
import heapq
from typing import List, Tuple

def find_process_execution_order(num_activities: int, dependencies: List[Tuple[int, int]]) -> List[int]:
    adj = {i: [] for i in range(num_activities)}
    in_degree = [0] * num_activities

    for u, v in dependencies:
        adj[u].append(v)
        in_degree[v] += 1

    min_heap = [i for i in range(num_activities) if in_degree[i] == 0]
    heapq.heapify(min_heap)

    order = []
    while min_heap:
        curr = heapq.heappop(min_heap)
        order.append(curr)

        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(min_heap, neighbor)

    return order if len(order) == num_activities else []
```

---

## 3. Signature Coding Problem 2: Maximum Ingested Events in Sliding Window $\Delta T$

### Problem Statement
A Celonis ingestion buffer receives high-frequency event records $[t_0, t_1, \\dots, t_{n-1}]$ where each timestamp represents an incoming event record in milliseconds. Given a sliding monitoring interval $W$, calculate the maximum number of events received within any time window of length $W$ (inclusive: $[t, t + W]$).

#### Python Optimal Two-Pointer Sliding Window Solution
```python
def max_events_in_window(timestamps: List[int], window_size: int) -> int:
    if not timestamps:
        return 0
    
    timestamps.sort()
    max_events = 0
    left = 0

    for right in range(len(timestamps)):
        # Shrink left pointer if window duration exceeded
        while timestamps[right] - timestamps[left] > window_size:
            left += 1
        max_events = max(max_events, right - left + 1)

    return max_events
```
* **Time Complexity**: $\\mathcal{O}(N \\log N)$ for sorting (or $\\mathcal{O}(N)$ if already sorted by time).
* **Space Complexity**: $\\mathcal{O}(1)$ auxiliary.

---

## 4. Signature SQL Assessment Problem: Process Bottleneck Transition Detection

### Problem Statement
Given an event log table `celonis_event_log` with columns `case_id`, `activity_name`, and `event_timestamp`, write an optimal SQL query to calculate:
1. The immediate next activity in each case.
2. The duration in hours between consecutive activities.
3. Filter out all cases where any single activity transition took longer than 48 hours (Process Bottlenecks).

#### Production SQL Solution
```sql
WITH ProcessTransitions AS (
    SELECT 
        case_id,
        activity_name AS current_activity,
        event_timestamp AS start_time,
        LEAD(activity_name) OVER (
            PARTITION BY case_id 
            ORDER BY event_timestamp ASC
        ) AS next_activity,
        LEAD(event_timestamp) OVER (
            PARTITION BY case_id 
            ORDER BY event_timestamp ASC
        ) AS next_time
    FROM celonis_event_log
),
TransitionDurations AS (
    SELECT
        case_id,
        current_activity,
        next_activity,
        start_time,
        next_time,
        ROUND(EXTRACT(EPOCH FROM (next_time - start_time)) / 3600.0, 2) AS duration_hours
    FROM ProcessTransitions
    WHERE next_activity IS NOT NULL
)
SELECT 
    case_id,
    current_activity,
    next_activity,
    duration_hours
FROM TransitionDurations
WHERE duration_hours > 48.0
ORDER BY duration_hours DESC;
```
"""
}

# =============================================================================
# MODULE 02: Technical Rounds
# =============================================================================
modules_data["02_Technical_Rounds"] = {
    "title": "02: Concurrency & Core Systems",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Problems",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Process Mining & OCPM",
    "markdown": """# 02: Concurrency & Core Systems

## 1. Concurrency, Multithreading & Race Conditions
Celonis backend systems process millions of real-time event logs simultaneously. Interviewers frequently probe deep into thread safety, synchronization primitives, and lock contention.

### Core Concurrency Primitives
| Concept | Mechanism | Overhead | Use Case in Celonis |
| :--- | :--- | :--- | :--- |
| **Mutex / Lock** | Mutual exclusion; blocks thread execution until lock acquired | Kernel context switch on contention | Protecting shared process variant state |
| **Reader-Writer Lock** | Multiple concurrent readers, exclusive single writer | Moderate | Heavy read traffic on static process models |
| **Spinlock** | Busy-wait loop checking atomic flag | Burns CPU cycles | Ultra-short critical sections in hot loops |
| **Atomic Operations** | Hardware-level atomic instructions (CAS: Compare-And-Swap) | Zero context switch | Lock-free metrics & event counters |
| **Condition Variable** | Sleep thread until signaled by another thread | Low | Producer-consumer event ingestion queues |

---

## 2. Production Producer-Consumer Pattern in C++

```cpp
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>

template <typename T>
class ThreadSafeEventQueue {
private:
    std::queue<T> queue_;
    mutable std::mutex mutex_;
    std::condition_variable not_empty_;
    std::condition_variable not_full_;
    size_t capacity_;
    bool stopped_{false};

public:
    explicit ThreadSafeEventQueue(size_t capacity) : capacity_(capacity) {}

    void push(T item) {
        std::unique_lock<std::mutex> lock(mutex_);
        not_full_.wait(lock, [this]() { return queue_.size() < capacity_ || stopped_; });
        if (stopped_) return;
        queue_.push(std::move(item));
        not_empty_.notify_one();
    }

    bool pop(T& item) {
        std::unique_lock<std::mutex> lock(mutex_);
        not_empty_.wait(lock, [this]() { return !queue_.empty() || stopped_; });
        if (queue_.empty() && stopped_) return false;
        item = std::move(queue_.front());
        queue_.pop();
        not_full_.notify_one();
        return true;
    }

    void stop() {
        std::lock_guard<std::mutex> lock(mutex_);
        stopped_ = true;
        not_empty_.notify_all();
        not_full_.notify_all();
    }
};
```

---

## 3. Java Concurrency Essentials (Frequently Asked)
1. **Volatile Keyword**: Guarantees visibility across threads (prevents CPU core caching of stale values), but does **not** guarantee atomicity for compound actions like `count++`.
2. **Synchronized vs ReentrantLock**:
   * `synchronized`: Implicit language keyword, automatically releases lock on exception, no timeout capability.
   * `ReentrantLock`: Explicit lock management with `tryLock(timeout)`, fairness policies, and multiple `Condition` variables.
3. **Thread Pool Tuning Formula**:
   $$\\text{Optimal Threads} = \\text{Number of CPU Cores} \\times \\left(1 + \\frac{\\text{Wait Time}}{\\text{Compute Time}}\\right)$$
   * For CPU-bound tasks (e.g. Graph mining): `Runtime.getRuntime().availableProcessors() + 1`.
   * For I/O-bound tasks (e.g. Database queries, SAP REST calls): Significantly higher thread count (e.g., $10 \\times \\text{Cores}$).

---

## 4. Database Storage & Transaction Internals
* **B+ Trees vs LSM Trees**:
  * PostgreSQL uses B+ Trees for indices: Fast $O(\\log N)$ point reads, balanced height, efficient range scans.
  * Ingestion-heavy systems often use LSM Trees (Log-Structured Merge Trees) for ultra-fast sequential disk writes.
* **ACID Isolation Levels & Anomalies**:
  * **Read Committed** (Default in PostgreSQL): Prevents dirty reads.
  * **Repeatable Read**: Prevents non-repeatable reads using MVCC snapshots.
  * **Serializable**: Guarantees serial execution; detects read/write conflicts using serialization graphs.
"""
}

# =============================================================================
# MODULE 03: Domain Deep Dive
# =============================================================================
modules_data["03_Domain_Deep_Dive"] = {
    "title": "03: Process Mining & OCPM Deep Dive",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: Concurrency & Core Systems",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Resume Defense & Traps",
    "markdown": """# 03: Process Mining & OCPM Deep Dive

## 1. What is Process Mining?
Process Mining is an analytical discipline that sits at the intersection of **Data Science** and **Business Process Management (BPM)**. It discovers, monitors, and improves real processes by extracting knowledge from event logs readily available in corporate IT systems.

```
Traditional BI (What happened?):    "Revenue fell 12% in Q3."
Process Mining (WHY did it happen?): "In 34% of orders, credit approval took 14 days due to manual paperwork loops between sales and finance."
```

---

## 2. The Three Pillars of Process Mining

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     1. Process Discovery        │   │    2. Conformance Checking      │   │     3. Process Enhancement      │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ Takes raw event log and outputs │   │ Compares real event log against │   │ Uses discovered bottlenecks to  │
│ an accurate, data-driven        │   │ a pre-defined standard model to │   │ optimize, automate, or redesign │
│ process model without human bias│   │ flag compliance violations.     │   │ operational execution steps.    │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```

### Signature Discovery Algorithms:
1. **Alpha Miner**: The foundational algorithm based on footprint causal dependencies ($a \\rightarrow b$, $a \\# b$, $a \\parallel b$). Generates Petri nets but struggles with noise and loops.
2. **Heuristics Miner**: Uses frequency thresholds to filter out rare outliers and noisy paths, making it practical for real-world enterprise data.
3. **Inductive Miner**: The state-of-the-art discovery algorithm. Recursively splits the event log using process trees (sequence, choice, parallel, loop cuts), guaranteeing a deadlock-free model.

---

## 3. Object-Centric Process Mining (OCPM)

### The Legacy Problem: The 2D Case ID Limitation
In traditional process mining, every row must be tied to a single `case_id`. For example:
* If Case ID = `Order`, where does `Invoice` belong?
* One Purchase Order can contain **5 Order Lines**, which are delivered across **2 Shipments**, and billed in **3 separate Invoices**.
* Forcing multi-object processes into a single Case ID causes two fatal errors:
  1. **Convergence**: Artificially duplicating events for multiple objects.
  2. **Divergence**: Conflating distinct independent object lifecycles into a tangled web.

### The Celonis OCPM Solution:
Celonis pioneered **Object-Centric Process Mining (OCPM)** and the **OCEL (Object-Centric Event Log)** format:
* Events can be linked to **multiple objects simultaneously** (e.g. Event `Pack Box` relates to `Order #1`, `Item #A`, `Item #B`, and `Package #99`).
* Graphs model the true relational business execution fabric across the entire supply chain.

---

## 4. Process Query Language (PQL)
PQL is Celonis's domain-specific query language tailored for graph and process analytics over columnar data.
* Example calculation:
  ```sql
  CALC_THROUGHPUT(
      FIRST_OCCURRENCE['Receive Order'] TO LAST_OCCURRENCE['Clear Invoice'], 
      REMAP_TIMESTAMPS(DAYS)
  )
  ```
* Evaluated dynamically in-memory without materializing the graph ahead of time, allowing users to filter by vendor, region, or value instantly.
"""
}

# =============================================================================
# MODULE 04: Candidate Resume Grilling
# =============================================================================
modules_data["04_Candidate_Resume_Grilling"] = {
    "title": "04: Resume Defense & Trap Neutralization",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Process Mining & OCPM",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: Event Ingestion LLD",
    "markdown": """# 04: Resume Defense & Trap Neutralization

## 1. Candidate Strategic Alignment: Adarsh Saurabh

```
Adarsh Saurabh (NIT Rourkela Roll: 225EC6021)
├── M.Tech: Signal and Image Processing (NIT Rourkela) | CGPA: 8.28
└── B.Tech: Computer Science & Engineering (Guru Ghasidas University) | CGPA: 8.5
```

### The "Elevator Pitch" for Celonis Associate Engineer
> *"I bring a unique dual background: a core Computer Science engineering foundation covering operating systems, distributed computing, and database internals, coupled with specialized Masters research at NIT Rourkela in advanced mathematical modeling, algorithmic optimization, and computational efficiency. Whether it is engineering high-speed heuristic graph traversal in Warehouse PathMapper or building multi-tenant SaaS backends with database conflict resolution in Apna Gold Solutions, my focus is always on scalable, deterministic system performance."*

---

## 2. Deep Project Defenses for Celonis

### Project 1: IBYD Technology — Warehouse PathMapper (MANDATORY PROJECT)
* **What You Built**: A high-performance spatial heuristic routing engine mapping multi-dimensional warehouse topologies into optimized graph representations.
* **Key Metric**: Scaled across $10,000 \\times 10,000$ spatial grids, computing optimal paths through 10,000+ points in $<0.5$s on a single CPU core.
* **Celonis Connection**:
  > *"Warehouse PathMapper solved the exact same mathematical problem Celonis faces in process discovery: transforming discrete, high-dimensional coordinate points into an optimized graph topology, finding optimal paths while eliminating bottlenecks, and maintaining sub-second execution bounds without consuming excessive memory."*

### Project 2: Apna Gold Solutions — Multi-Tenant SaaS Platform
* **What You Built**: Scalable multi-tenant B2B SaaS platform with custom JWT authentication, database concurrency conflict resolution, and real-time status tracking.
* **Celonis Connection**:
  > *"Celonis EMS is a multi-tenant enterprise cloud platform where enterprise customers demand strict data isolation, zero cross-tenant contamination, and high-throughput API endpoints. In Apna Gold Solutions, I implemented database-level tenant isolation, optimized query indexes, and handled concurrent state updates with transactional integrity."*

### Project 3: Alternative Data Radar
* **What You Built**: Automated ingestion pipeline extracting public web signals across target firms, synthesizing signals into a 0–100 corporate health index stored in SQL with interactive dashboards.
* **Celonis Connection**:
  > *"This maps directly to Celonis's ingestion and KPI monitoring architecture: parsing unstructured event streams, executing multi-factor aggregation metrics, storing relational snapshots in SQL, and powering real-time monitoring visualizations."*

---

## 3. High-Risk Trap Questions & Optimal Neutralizations

### Trap 1: "Your M.Tech is in Signal and Image Processing, not CSE. Why are you applying for a backend software engineering role at Celonis?"
* **Flawed Answer**: *"I like coding more than signal processing, so I switched."* (Shows inconsistency).
* **Optimal Answer**:
  > *"My undergraduate degree is in Computer Science and Engineering, where I built rigorous foundations in Data Structures, OS concurrency, Database Systems, and Software Architecture. I specifically pursued Signal Processing for my Masters to master high-performance numerical computation, linear algebra, and mathematical optimization. At Celonis, systems like the PQL engine and graph discovery aren't just CRUD applications—they are high-throughput computational engines where algorithmic complexity and mathematical vectorization determine performance. My background bridges both worlds seamlessly."*

### Trap 2: "In Warehouse PathMapper, why didn't you just use standard A* or Dijkstra? Why custom heuristics?"
* **Optimal Answer**:
  > *"Standard Dijkstra has $\\mathcal{O}(V \\log V + E)$ complexity and requires maintaining a full priority queue across $10,000 \\times 10,000 = 10^8$ possible states. In a physical warehouse, aisles impose Manhattan-constrained corridors. By decomposing the layout into hierarchical sub-graphs and utilizing Euclidean pre-computed bounding heuristics, we pruned 94% of non-viable branches, allowing us to hit sub-0.5s execution on a commodity CPU."*
"""
}

# =============================================================================
# MODULE 05: System Design or LLD
# =============================================================================
modules_data["05_System_Design_or_HIL"] = {
    "title": "05: Event Log Ingestion Engine LLD",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Resume Defense & Traps",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Culture & Values",
    "markdown": """# 05: Event Log Ingestion Engine LLD

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
"""
}

# =============================================================================
# MODULE 06: Managerial and HR
# =============================================================================
modules_data["06_Managerial_and_HR"] = {
    "title": "06: Culture, Values & Behavioral Interview",
    "prev_link": "05_System_Design_or_HIL.html",
    "prev_title": "05: Event Ingestion LLD",
    "next_link": "07_Quick_Reference.html",
    "next_title": "07: Process Mining CheatSheet",
    "markdown": """# 06: Culture, Values & Behavioral Interview

## 1. Celonis Core Cultural Values
To clear the final managerial and HR rounds, candidates must demonstrate authentic alignment with Celonis's four core organizational values:

1. **We Own It**: Take complete accountability from design to deployment. No excuses, no hand-waving. If something breaks in production, own the fix.
2. **Customer First**: Every algorithm, feature, and optimization must produce measurable business value for the enterprise client.
3. **Best Team Wins**: Radical collaboration over individual egos. Champion diverse perspectives and mentor peers.
4. **Always Moving Forward**: Relentless curiosity and continuous technical improvement.

---

## 2. Structured STAR Behavioral Answers for Adarsh Saurabh

### Question: "Tell me about a time you had to deal with a major technical setback or unexpected obstacle."
* **Situation**: During the **Hack4CG Hackathon**, our team was building a real-time facial emotion recognition pipeline. With 6 hours remaining before final evaluation, our inference model was consuming 98% GPU memory and dropping frames on live camera feeds.
* **Task**: As team lead, I had to ensure our prototype delivered smooth, sub-second inference on standard evaluation laptops without crashing.
* **Action**: I initiated a rapid profiling session and discovered our OpenCV video feed was maintaining uncompressed image buffers in memory. I restructured the capture pipeline using vectorized cropping and quantized the model weights, dropping memory consumption by 65% and boosting frame rates to 30 FPS.
* **Result**: We secured **Rank 1 out of 50+ competing teams**, and our project was praised for zero-latency live demonstration.

### Question: "Why Celonis over other software firms?"
* **Optimal Response**:
  > *"Celonis isn't just another enterprise SaaS company building standard CRUD forms; Celonis created the entire category of Process Mining and transformed how Global Fortune 500 companies execute. What excites me most as an engineer is the sheer scale and mathematical beauty of the problem: processing billions of unstructured ERP event logs, reconstructing directed graphs dynamically, and executing queries on custom columnar engines in sub-seconds. With my background in Computer Science and mathematical signal optimization, Celonis offers the perfect engineering crucible to solve deep systems challenges."*
"""
}

# =============================================================================
# MODULE 07: Quick Reference
# =============================================================================
modules_data["07_Quick_Reference"] = {
    "title": "07: Process Mining & Systems CheatSheet",
    "prev_link": "06_Managerial_and_HR.html",
    "prev_title": "06: Culture & Values",
    "next_link": "README.html",
    "next_title": "3-Day Study Roadmap",
    "markdown": """# 07: Process Mining & Systems CheatSheet

## 1. High-Yield Process Mining Concepts

| Concept | Definition in 1 Line |
| :--- | :--- |
| **Event Log** | A tabular dataset with minimum 3 columns: `case_id`, `activity`, and `timestamp`. |
| **Case ID** | The discrete business instance being tracked (e.g., invoice number, claim ID). |
| **Happy Path** | The most frequent, ideal execution sequence with zero rework or delays. |
| **Process Variant** | A distinct permutation of activity sequences observed in real data. |
| **Throughput Time** | The total elapsed duration from process start to termination. |
| **Rework / Loop** | Repeating the exact same activity multiple times within a single case. |
| **Bottleneck** | A transition step where cases spend disproportionately long waiting times. |
| **Conformance** | Quantifying how well real execution matches pre-defined business policy. |
| **OCPM** | Object-Centric Process Mining: tracking multiple interrelated entities concurrently. |

---

## 2. Big-O Complexity Reference for Signature OA Algorithms

| Algorithm | Best Time | Average Time | Worst Time | Space | Signature Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kahn's Topological Sort** | $\\mathcal{O}(V + E)$ | $\\mathcal{O}(V + E)$ | $\\mathcal{O}(V + E)$ | $\\mathcal{O}(V + E)$ | Process deadlock detection |
| **Dijkstra with Min-Heap** | $\\mathcal{O}(E \\log V)$ | $\\mathcal{O}(E \\log V)$ | $\\mathcal{O}(E \\log V)$ | $\\mathcal{O}(V)$ | Minimum throughput pathfinding |
| **Sliding Window (Two-Pointer)**| $\\mathcal{O}(N)$ | $\\mathcal{O}(N)$ | $\\mathcal{O}(N)$ | $\\mathcal{O}(1)$ | Peak event ingestion detection |
| **Monotonic Queue** | $\\mathcal{O}(N)$ | $\\mathcal{O}(N)$ | $\\mathcal{O}(N)$ | $\\mathcal{O}(K)$ | Window minimum / maximum queries |

---

## 3. Concurrency Rules in 5 Bullets
1. **Never synchronize on `String` literals** or boxed primitives in Java (`synchronized("lock")` creates JVM-wide contention).
2. **Always lock in a consistent global order** when acquiring multiple locks to eliminate deadlocks.
3. **Double-Checked Locking requires `volatile`** to prevent out-of-order instruction execution during object construction.
4. **Use CAS (Compare-And-Swap) for high-contention counters** instead of heavy mutexes.
5. **Thread pools must never have unbounded queues**; always configure explicit rejection policies (`CallerRunsPolicy` or `AbortPolicy`).
"""
}

# =============================================================================
# MODULE: README (Study Roadmap)
# =============================================================================
modules_data["README"] = {
    "title": "3-Day Accelerated Study Roadmap · Celonis",
    "prev_link": "07_Quick_Reference.html",
    "prev_title": "07: Quick Reference",
    "next_link": "index.html",
    "next_title": "Overview & Hub",
    "markdown": """# 3-Day Accelerated Study Roadmap · Celonis Associate Engineer

## 📅 Day 1: Algorithmic Mastery & Core CS (Sept 21 – 22)
* **Morning (09:00 – 13:00)**:
  * Master **Graph Traversal & Topological Sort** (Kahn's Algorithm with cycle detection).
  * Solve 3 LeetCode Mediums: *Course Schedule I & II*, *Alien Dictionary*, *Minimum Time to Finish All Tasks*.
* **Afternoon (14:00 – 18:00)**:
  * Operating Systems revision: Multithreading, Mutex vs Semaphore, Race Conditions, Deadlocks (Coffman conditions).
  * Implement Producer-Consumer pattern in C++ and Java with condition variables.
* **Evening (19:00 – 22:00)**:
  * SQL Window Functions: `LEAD()`, `LAG()`, `ROW_NUMBER()`, `DENSE_RANK()`, `PARTITION BY`.
  * Solve event log duration query from Module 01.

---

## 📅 Day 2: Process Mining & Low-Level Design (Sept 23 – 24)
* **Morning (09:00 – 13:00)**:
  * Read **Module 03: Process Mining & OCPM Deep Dive**.
  * Understand Event Logs, Alpha/Inductive Miners, Conformance Checking, and PQL.
* **Afternoon (14:00 – 18:00)**:
  * Low-Level Design (LLD): Code the **High-Throughput Event Ingestion Engine** adhering to SOLID principles.
  * Implement a Thread-Safe In-Memory LRU Cache with TTL.
* **Evening (19:00 – 21:00)**:
  * Attend the **Celonis Pre-Placement Talk (PPT)** on 24th September.
  * Note exact speaker names, specific Bangalore product initiatives, and tech stack mentions.

---

## 📅 Day 3: Online Test & Interview Defense (Sept 25 – 27)
* **Friday, 25th September**:
  * **Celonis Online Assessment (OA)**: Execute the strategy in Module 01. Stay calm, test edge cases (empty lists, cycles).
* **Weekend (Sept 26 – 27)**:
  * Rehearse **Module 04: Candidate Resume Grilling**.
  * Perfect the defense for **Warehouse PathMapper**, **Apna Gold Solutions**, and your M.Tech Signal Processing degree.
  * Rehearse STAR stories for Celonis values in **Module 06**.
* **Monday, 28th September**:
  * **Personal Interviews**: Confident delivery, clean code, vocal thought process.
"""
}

# =============================================================================
# INDEX HTML CONTENT (PORTAL HUB)
# =============================================================================
index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display:inline-flex; align-items:center; gap:6px; padding:4px 12px; border-radius:9999px; background:rgba(37,99,235,0.12); border:1px solid #2563eb; color:#2563eb; font-size:12px; font-weight:700; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:12px;">
    <span>⚡ On-Campus Recruitment Drive 2027</span>
  </div>
  <h1 style="margin:0 0 10px 0; font-size:2.2rem; font-weight:800; letter-spacing:-0.03em;">Celonis Interview Preparation Portal</h1>
  <p style="font-size:16px; color:var(--text-secondary); max-width:820px; margin:0 0 20px 0;">
    Comprehensive, mobile-optimized intelligence suite engineered for <strong>Adarsh Saurabh</strong> (NIT Rourkela). Covers signature Online Assessment (OA) graph problems, core systems & concurrency, Process Mining domain architecture, Low-Level Design (LLD), and candidate resume defense.
  </p>

  <!-- Key Metrics Row -->
  <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:12px; margin-bottom:28px;">
    <div style="padding:16px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color);">
      <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); margin-bottom:4px;">Target CTC</div>
      <div style="font-size:22px; font-weight:800; color:#2563eb;">₹22.00 LPA</div>
      <div style="font-size:12px; color:var(--text-muted);">16.2L Base + 1.8L Bonus + 4L Sign-on</div>
    </div>
    <div style="padding:16px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color);">
      <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); margin-bottom:4px;">Drive Timeline</div>
      <div style="font-size:20px; font-weight:800; color:var(--text-primary);">Sept 24 – 28</div>
      <div style="font-size:12px; color:var(--text-muted);">OA: 25 Sept · Interviews: 28 Sept</div>
    </div>
    <div style="padding:16px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color);">
      <div style="font-size:11px; font-weight:700; text-transform:uppercase; color:var(--text-muted); margin-bottom:4px;">Core Focus</div>
      <div style="font-size:20px; font-weight:800; color:var(--text-primary);">Graph DSA & Systems</div>
      <div style="font-size:12px; color:var(--text-muted);">Concurrency, LLD & Process Mining</div>
    </div>
  </div>
</div>

<!-- Modules Grid -->
<h2 style="font-size:18px; font-weight:800; margin-bottom:16px;">Preparation Curriculum</h2>
<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">

  <a href="00_START_HERE.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 00</span>
      <span style="font-size:18px;">🏢</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Company & Role Intel</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">$13B Decacorn profile, EMS architecture, Bangalore engineering hub, and full placement drive schedule.</p>
  </a>

  <a href="01_Online_Test.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 01</span>
      <span style="font-size:18px;">💻</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Signature OA Problems</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Process Variant Topological Sort, Cycle Detection, Sliding Window Event Burst, and SQL Window analytics.</p>
  </a>

  <a href="02_Technical_Rounds.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 02</span>
      <span style="font-size:18px;">⚙️</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Concurrency & Core Systems</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Thread safety, Producer-Consumer queues, Mutexes vs CAS Atomics, and PostgreSQL MVCC / index internals.</p>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 03</span>
      <span style="font-size:18px;">📊</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Process Mining & OCPM</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Event Logs, Alpha & Inductive Miners, Conformance Checking, Object-Centric Process Mining, and PQL.</p>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 04</span>
      <span style="font-size:18px;">🛡️</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Resume Defense & Traps</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Defending Warehouse PathMapper, Apna Gold Solutions, and M.Tech Signal Processing dual background.</p>
  </a>

  <a href="05_System_Design_or_HIL.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 05</span>
      <span style="font-size:18px;">🏗️</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Event Ingestion Engine LLD</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Production-grade Python & C++ LLD for batching event buffers, backpressure, and SOLID architecture.</p>
  </a>

  <a href="06_Managerial_and_HR.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 06</span>
      <span style="font-size:18px;">🤝</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Culture & Values</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Celonis Core Values ("We Own It", "Customer First"), and STAR-format leadership story defenses.</p>
  </a>

  <a href="07_Quick_Reference.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">MODULE 07</span>
      <span style="font-size:18px;">⚡</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">Process Mining CheatSheet</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Zero-fluff formulas, Big-O tables, concurrency rules, SQL templates, and 10-point interview checklist.</p>
  </a>

  <a href="README.html" style="display:block; padding:18px; border-radius:12px; background:var(--bg-card); border:1px solid var(--border-color); text-decoration:none; color:inherit; transition:transform 0.15s ease, border-color 0.15s ease;" onmouseover="this.style.borderColor='var(--accent-primary)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.borderColor='var(--border-color)'; this.style.transform='translateY(0)';">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:11px; font-weight:700; padding:2px 8px; border-radius:6px; background:var(--accent-light); color:var(--accent-primary);">ROADMAP</span>
      <span style="font-size:18px;">📅</span>
    </div>
    <div style="font-size:16px; font-weight:700; margin-bottom:6px; color:var(--text-primary);">3-Day Study Roadmap</div>
    <p style="font-size:13px; color:var(--text-secondary); margin:0;">Hour-by-hour preparation schedule leading up to OA on Sept 25 and Interviews on Sept 28.</p>
  </a>

</div>
"""

# =============================================================================
# BUILD EXECUTION
# =============================================================================
if __name__ == "__main__":
    print("Generating Celonis Interview Preparation Suite...")

    for key, mod in modules_data.items():
        md_file = os.path.join(BASE_DIR, f"{key}.md")
        html_file = os.path.join(BASE_DIR, f"{key}.html")

        # 1. Write Markdown file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(mod["markdown"])
        print(f"  [MD] Created {key}.md")

        # 2. Render Markdown to HTML
        body_html = markdown.markdown(
            mod["markdown"],
            extensions=["fenced_code", "tables", "nl2br"]
        )

        # Wrap tables in responsive table-wrapper
        body_html = body_html.replace("<table>", '<div class="table-wrapper"><table>').replace("</table>", '</table></div>')

        full_html = render_celonis_page(
            title=mod["title"],
            active_page=f"{key}.html",
            content_html=body_html,
            prev_link=mod["prev_link"],
            prev_title=mod["prev_title"],
            next_link=mod["next_link"],
            next_title=mod["next_title"]
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  [HTML] Rendered {key}.html")

    # Render index.html hub page
    index_file = os.path.join(BASE_DIR, "index.html")
    index_full_html = render_celonis_page(
        title="Overview & Hub · Celonis Interview Preparation",
        active_page="index.html",
        content_html=index_html_content,
        prev_link="../index.html",
        prev_title="All Companies Hub",
        next_link="00_START_HERE.html",
        next_title="00: Company Deep Dive"
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_full_html)
    print("  [HUB] Rendered index.html")

    print("\nAll Celonis interview preparation modules generated successfully!")
