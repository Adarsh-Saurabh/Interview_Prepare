# IBM ISDL Signature Online Assessment (OA) Problems

> **Platform:** HackerRank  
> **Format:** 2 Coding Problems (60–90 Mins) + 15 Core Computer Science MCQs  
> **Target Difficulty:** LeetCode Medium to Medium-Hard with high edge-case sensitivity  

---

## Overview of OA Question Archetypes

IBM Systems (ISDL) tests algorithmic proficiency through a systems-oriented lens. Rather than abstract, highly theoretical dynamic programming on trees, problems commonly model **resource allocation, sliding-window telemetry buffers, bitmask manipulations, and graph routing across hardware topologies**.

---

## Problem 1: Sliding Window Server Telemetry Outlier Counter

### Problem Statement
An IBM Power10 server telemetry agent collects CPU utilization spikes every second as an integer array `metrics` of length $N$. You are given an integer window size $K$ and an anomaly threshold $T$. For every contiguous sliding window of size $K$, identify the maximum telemetry value. If that maximum value exceeds or equals $T$, the window is flagged as an "Anomaly Window". 

Return the total number of Anomaly Windows across the entire telemetry stream, followed by an array containing the maximum value of each window.

### Mathematical & Complexity Formulation
- **Input:** `metrics = [12, 45, 78, 34, 89, 90, 23, 11]`, $K = 3$, $T = 75$
- **Total Windows:** $N - K + 1 = 8 - 3 + 1 = 6$
- **Naive Solution:** Compute maximum of each subarray of length $K$ in $O(K)$ time $	o$ Total Time $O(N \cdot K)$. For $N = 10^5, K = 10^4$, operations $pprox 10^9$ (Time Limit Exceeded).
- **Optimal Approach:** Maintain a **Monotonic Decreasing Deque** storing indices whose values are strictly decreasing.
  - Front of deque always holds the index of the maximum element in current window.
  - Discard indices outside the current window $[i - K + 1, i]$.
  - Pop smaller elements from back before inserting current index.
  - **Time Complexity:** $O(N)$ because each index is pushed and popped at most once.
  - **Space Complexity:** $O(K)$ for the deque.

### Production C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <deque>

struct TelemetryResult {
    int anomaly_count;
    std::vector<int> window_maxima;
};

TelemetryResult detectTelemetryAnomalies(const std::vector<int>& metrics, int k, int threshold) {
    int n = metrics.size();
    if (n == 0 || k <= 0 || k > n) {
        return {0, {}};
    }

    std::deque<int> dq; // Stores indices of candidate maximum elements
    std::vector<int> window_maxima;
    int anomaly_count = 0;

    for (int i = 0; i < n; ++i) {
        // 1. Remove elements outside current sliding window
        if (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }

        // 2. Maintain monotonic decreasing order (remove smaller elements from back)
        while (!dq.empty() && metrics[dq.back()] <= metrics[i]) {
            dq.pop_back();
        }

        // 3. Push current index
        dq.push_back(i);

        // 4. Once window reaches size k, record the maximum
        if (i >= k - 1) {
            int current_max = metrics[dq.front()];
            window_maxima.push_back(current_max);
            if (current_max >= threshold) {
                anomaly_count++;
            }
        }
    }

    return {anomaly_count, window_maxima};
}

int main() {
    std::vector<int> metrics = {12, 45, 78, 34, 89, 90, 23, 11};
    int k = 3;
    int threshold = 75;

    TelemetryResult res = detectTelemetryAnomalies(metrics, k, threshold);
    std::cout << "Total Anomaly Windows: " << res.anomaly_count << "\n";
    std::cout << "Window Maxima: ";
    for (int v : res.window_maxima) std::cout << v << " ";
    std::cout << "\n";
    return 0;
}
```

### Optimal Python 3 Solution
```python
from collections import deque
from typing import List, Tuple

def detect_telemetry_anomalies(metrics: List[int], k: int, threshold: int) -> Tuple[int, List[int]]:
    if not metrics or k <= 0 or k > len(metrics):
        return 0, []
    
    dq = deque()  # stores indices
    window_maxima = []
    anomaly_count = 0
    
    for i, val in enumerate(metrics):
        # Evict indices outside current window
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # Maintain monotonic decreasing invariant
        while dq and metrics[dq[-1]] <= val:
            dq.pop()
            
        dq.append(i)
        
        # When first full window is reached
        if i >= k - 1:
            curr_max = metrics[dq[0]]
            window_maxima.append(curr_max)
            if curr_max >= threshold:
                anomaly_count += 1
                
    return anomaly_count, window_maxima
```

---

## Problem 2: Bitmask Memory & Buddy Allocator Simulator

### Problem Statement
In IBM PowerVM firmware memory virtualization, memory is divided into blocks of power-of-two sizes ($2^K$ bytes). A 64-bit integer `memory_bitmap` represents 64 contiguous base pages of size 4KB. A bit value of `0` indicates a free page; `1` indicates an allocated page.

Given an allocation request of size $S \in \{1, 2, 4, 8, 16, 32, 64\}$ pages, the allocator must find the lowest aligned offset where $S$ contiguous bits are `0`. If found, mark them `1` and return the starting block offset; otherwise, return `-1`. When freeing, given an offset and size $S$, clear those bits back to `0`.

### Bitwise Formulation
- Alignment requirement: An allocation of size $S$ must start at an index where `offset % S == 0`.
- Mask construction: A contiguous run of $S$ set bits is `mask = (1ULL << S) - 1ULL`.
- To check if a block at offset `idx` is free: `(bitmap & (mask << idx)) == 0`.
- To allocate: `bitmap |= (mask << idx)`.
- To free: `bitmap &= ~(mask << idx)`.

### Production C++17 Implementation
```cpp
#include <iostream>
#include <cstdint>

class BuddyBitmapAllocator {
private:
    uint64_t bitmap; // 64 pages (0 = Free, 1 = Allocated)

public:
    BuddyBitmapAllocator() : bitmap(0ULL) {}

    int allocate(int size) {
        if (size <= 0 || (size & (size - 1)) != 0 || size > 64) {
            return -1; // Size must be a power of 2 <= 64
        }

        uint64_t block_mask = (size == 64) ? ~0ULL : ((1ULL << size) - 1ULL);

        for (int offset = 0; offset <= 64 - size; offset += size) {
            uint64_t shifted_mask = block_mask << offset;
            if ((bitmap & shifted_mask) == 0ULL) {
                // Found contiguous aligned free block
                bitmap |= shifted_mask;
                return offset;
            }
        }
        return -1; // Out of memory
    }

    bool free(int offset, int size) {
        if (offset < 0 || offset + size > 64 || (offset % size) != 0) {
            return false; // Invalid offset or alignment
        }

        uint64_t block_mask = (size == 64) ? ~0ULL : ((1ULL << size) - 1ULL);
        uint64_t shifted_mask = block_mask << offset;

        // Verify the block was actually allocated
        if ((bitmap & shifted_mask) != shifted_mask) {
            return false; // Double free or corrupted state
        }

        bitmap &= ~shifted_mask;
        return true;
    }

    uint64_t getRawBitmap() const { return bitmap; }
};
```

---

## Problem 3: Fault-Tolerant Enterprise Network Routing

### Problem Statement
An IBM z16 compute drawer interconnects $N$ processor nodes labeled $0$ to $N-1$ via bidirectional PCIe/optical links with given transmission latencies. Due to dynamic hardware faults, certain links can fail. Given an adjacency list of links $(u, v, w)$, a source node $S$, a destination node $D$, and a dynamic list of failed edges `failed_links = [(u1, v1), ...]`, determine the minimum latency path from $S$ to $D$ that bypasses all failed links. If no route exists, return `-1`.

### Complexity & Algorithmic Strategy
- **Graph:** Undirected weighted graph with $V$ nodes and $E$ edges.
- **Dynamic Filter:** Store failed links in a hash set of ordered pairs `std::unordered_set<uint64_t>` where key is `((uint64_t)min(u,v) << 32) | max(u,v)`.
- **Dijkstra with Min-Heap:** Priority queue storing pairs `(distance, u)`.
- **Time Complexity:** $O((V + E) \log V)$ using binary min-heap.
- **Space Complexity:** $O(V + E)$ for adjacency graph and distance arrays.

### Production C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <cstdint>

struct Edge {
    int to;
    int weight;
};

uint64_t makeEdgeKey(int u, int v) {
    if (u > v) std::swap(u, v);
    return ((uint64_t)u << 32) | (uint32_t)v;
}

int routeAroundFaults(int n, const std::vector<std::vector<int>>& edges, 
                       int src, int dest, 
                       const std::vector<std::pair<int, int>>& failed_links) {
    // 1. Hash failed edges for O(1) lookup
    std::unordered_set<uint64_t> failed_set;
    for (const auto& fl : failed_links) {
        failed_set.insert(makeEdgeKey(fl.first, fl.second));
    }

    // 2. Build adjacency list excluding failed edges
    std::vector<std::vector<Edge>> adj(n);
    for (const auto& e : edges) {
        int u = e[0], v = e[1], w = e[2];
        if (failed_set.find(makeEdgeKey(u, v)) == failed_set.end()) {
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
    }

    // 3. Dijkstra's Algorithm
    const int INF = 1e9;
    std::vector<int> dist(n, INF);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<>> pq;

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();

        if (d > dist[u]) continue;
        if (u == dest) return d;

        for (const auto& edge : adj[u]) {
            if (dist[u] + edge.weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + edge.weight;
                pq.push({dist[edge.to], edge.to});
            }
        }
    }

    return (dist[dest] == INF) ? -1 : dist[dest];
}
```

---

## Problem 4: Thread-Safe Priority Task Scheduler

### Problem Statement
In IBM Systems firmware and device driver queues, asynchronous hardware interrupt tasks must be consumed by worker threads based on priority (highest priority integer first) and timestamp (earliest submitted first in case of priority tie). Implement a thread-safe task queue class supporting concurrent producers and consumers without deadlocks or race conditions.

### Concurrency Primitives Required
- `std::mutex` for exclusive synchronization of the underlying heap.
- `std::condition_variable` to suspend consumer threads when the queue is empty, eliminating CPU-burning busy waiting.
- Graceful shutdown signal to unblock all sleeping consumer threads during system shutdown.

### Production C++17 Implementation
```cpp
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <chrono>

struct Task {
    int id;
    int priority;
    uint64_t timestamp;

    bool operator<(const Task& other) const {
        if (priority == other.priority) {
            return timestamp > other.timestamp; // Earlier timestamp has higher precedence
        }
        return priority < other.priority; // Higher priority integer on top
    }
};

class ThreadSafeTaskQueue {
private:
    std::priority_queue<Task> pq;
    mutable std::mutex mtx;
    std::condition_variable cv;
    bool shutdown_flag = false;

public:
    void push(int id, int priority, uint64_t timestamp) {
        {
            std::lock_guard<std::mutex> lock(mtx);
            pq.push({id, priority, timestamp});
        }
        cv.notify_one(); // Wake up one sleeping consumer thread
    }

    bool pop(Task& out_task) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [this]() { return !pq.empty() || shutdown_flag; });

        if (shutdown_flag && pq.empty()) {
            return false; // Queue has been terminated
        }

        out_task = pq.top();
        pq.pop();
        return true;
    }

    void shutdown() {
        {
            std::lock_guard<std::mutex> lock(mtx);
            shutdown_flag = true;
        }
        cv.notify_all(); // Wake up all waiting worker threads to exit cleanly
    }
};
```
