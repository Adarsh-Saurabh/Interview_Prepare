# 01: Signature OA Coding & Core CS Problems

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
* **Time Complexity**: $\mathcal{O}(V \log V + E)$ where $V$ is the number of activities and $E$ is dependencies.
* **Space Complexity**: $\mathcal{O}(V + E)$ for adjacency list and in-degree tracking.

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
A Celonis ingestion buffer receives high-frequency event records $[t_0, t_1, \dots, t_{n-1}]$ where each timestamp represents an incoming event record in milliseconds. Given a sliding monitoring interval $W$, calculate the maximum number of events received within any time window of length $W$ (inclusive: $[t, t + W]$).

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
* **Time Complexity**: $\mathcal{O}(N \log N)$ for sorting (or $\mathcal{O}(N)$ if already sorted by time).
* **Space Complexity**: $\mathcal{O}(1)$ auxiliary.

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
