# Module 01: Signature Online Assessment Problems & Coding Solutions

This module provides fully implemented, production-grade solutions in both **C++20** and **Python 3** for the exact problem archetypes asked in Wabtec online tests and live coding rounds.

---

## Problem 1: Locomotive Grid Pathfinding with Dynamic Momentum & Turn Penalties

### Problem Statement
A freight locomotive navigates a 2D railway yard modeled as an $M 	imes N$ grid. Each cell is either open track (`0`), obstructed track (`1`), or an active switch (`2`).
* Changing direction (making a 90-degree turn) incurs a momentum penalty of $K$ seconds because a heavy freight train cannot turn abruptly without severe energy dissipation.
* Moving straight forward takes $1$ second. Moving through an active switch (`2`) takes an additional switch latency of $S$ seconds.
* Find the minimum time required to move from start coordinate $(r_1, c_1)$ with initial heading $D_{start}$ to destination $(r_2, c_2)$ facing any direction. If unreachable, return $-1$.

### Algorithmic Strategy
* **State Space**: Standard BFS/Dijkstra on coordinates $(r, c)$ is insufficient because time depends on the *incoming direction*.
* **Augmented State**: Model each state as $(r, c, d)$ where $d \in \{0: 	ext{North}, 1: 	ext{East}, 2: 	ext{South}, 3: 	ext{West}\}$.
* **Algorithm**: **Dijkstra's Algorithm** with a min-priority queue over the 3D state space.
* **Complexity**: $O(M \cdot N \cdot 4 \cdot \log(M \cdot N))$.

### C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

struct State {
    int time;
    int r, c, dir; // dir: 0:North, 1:East, 2:South, 3:West
    bool operator>(const State& other) const {
        return time > other.time;
    }
};

int minLocomotiveTravelTime(const vector<vector<int>>& grid, 
                            int startR, int startC, int startDir,
                            int destR, int destC, int turnPenalty, int switchDelay) {
    int R = grid.size();
    int C = grid[0].size();
    
    // dr, dc for directions [0: North, 1: East, 2: South, 3: West]
    const int dr[4] = {-1, 0, 1, 0};
    const int dc[4] = {0, 1, 0, -1};

    // dist[r][c][dir]
    const int INF = 1e9;
    vector<vector<vector<int>>> dist(R, vector<vector<int>>(C, vector<int>(4, INF)));

    priority_queue<State, vector<State>, greater<State>> pq;
    dist[startR][startC][startDir] = 0;
    pq.push({0, startR, startC, startDir});

    while (!pq.empty()) {
        auto [t, r, c, d] = pq.top();
        pq.pop();

        if (t > dist[r][c][d]) continue;
        if (r == destR && c == destC) return t;

        // Try all 4 possible movement directions
        for (int nextDir = 0; nextDir < 4; ++nextDir) {
            // Cannot instantly reverse 180 degrees (train constraint)
            if ((d + 2) % 4 == nextDir) continue;

            int nr = r + dr[nextDir];
            int nc = c + dc[nextDir];

            // Check grid bounds and obstacles
            if (nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc] != 1) {
                int cost = 1; // base move cost
                if (nextDir != d) cost += turnPenalty; // turn penalty
                if (grid[nr][nc] == 2) cost += switchDelay; // switch delay

                if (t + cost < dist[nr][nc][nextDir]) {
                    dist[nr][nc][nextDir] = t + cost;
                    pq.push({t + cost, nr, nc, nextDir});
                }
            }
        }
    }
    return -1;
}

int main() {
    vector<vector<int>> yard = {
        {0, 0, 0, 1},
        {1, 2, 0, 0},
        {0, 0, 2, 0},
        {0, 1, 0, 0}
    };
    int ans = minLocomotiveTravelTime(yard, 0, 0, 1, 3, 3, 5, 3);
    cout << "Optimal Locomotive Transit Time: " << ans << " seconds
";
    return 0;
}
```

### Python 3 Implementation
```python
import heapq

def min_locomotive_travel_time(grid, start, start_dir, dest, turn_penalty, switch_delay):
    R, C = len(grid), len(grid[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    # Priority Queue holds (time, r, c, dir)
    pq = [(0, start[0], start[1], start_dir)]
    dist = {}
    dist[(start[0], start[1], start_dir)] = 0
    
    while pq:
        t, r, c, d = heapq.heappop(pq)
        
        if (r, c) == dest:
            return t
        
        if t > dist.get((r, c, d), float('inf')):
            continue
            
        for next_dir in range(4):
            # No 180-degree reversing
            if (d + 2) % 4 == next_dir:
                continue
                
            nr, nc = r + dr[next_dir], c + dc[next_dir]
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != 1:
                cost = 1
                if next_dir != d:
                    cost += turn_penalty
                if grid[nr][nc] == 2:
                    cost += switch_delay
                    
                new_t = t + cost
                if new_t < dist.get((nr, nc, next_dir), float('inf')):
                    dist[(nr, nc, next_dir)] = new_t
                    heapq.heappush(pq, (new_t, nr, nc, next_dir))
                    
    return -1
```

---

## Problem 2: Train Velocity Advisory & Fuel Optimization (Dynamic Programming)

### Problem Statement
In Wabtec's **Trip Optimizer**, a train travels over $N$ track segments. Each segment $i$ has an uphill/downhill elevation gradient $G[i]$, a maximum legal speed limit $V_{max}[i]$, and a minimum speed $V_{min}[i]$.
* Transitioning from speed $v_1$ in segment $i-1$ to speed $v_2$ in segment $i$ costs fuel:
  $$ 	ext{Fuel} = \max(0, v_2^2 - v_1^2) + G[i] \cdot v_2 + lpha \cdot v_2 $$
* The train cannot accelerate by more than $\Delta V_{acc}$ or decelerate by more than $\Delta V_{dec}$ between adjacent segments.
* Find the speed sequence that minimizes total fuel consumption across all $N$ track segments while finishing in segment $N-1$ with speed $\ge V_{target}$.

### Algorithmic Strategy
* Let $DP[i][v]$ be the minimum fuel consumed up to segment $i$ ending at integer velocity $v$.
* State Transition:
  $$ DP[i][v] = \min_{u \in [v - \Delta V_{acc}, v + \Delta V_{dec}]} \{ DP[i-1][u] + 	ext{Cost}(u, v, G[i]) \} $$
* Bounded state space: Since train speeds are discrete integers ($0 \le v \le 120	ext{ km/h}$), DP running time is $O(N \cdot V_{max} \cdot \Delta V)$.

### C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e16;

long long optimizeFuelProfile(int N, const vector<int>& G, 
                             const vector<int>& Vmin, const vector<int>& Vmax,
                             int maxAcc, int maxDec, int alpha, int targetSpeed) {
    int maxV = 120;
    vector<long long> dp(maxV + 1, INF);

    // Initial state: start at origin at speed Vmin[0]
    for (int v = Vmin[0]; v <= Vmax[0]; ++v) {
        dp[v] = 1LL * v * v / 2 + 1LL * G[0] * v + 1LL * alpha * v;
    }

    for (int i = 1; i < N; ++i) {
        vector<long long> next_dp(maxV + 1, INF);
        for (int v = Vmin[i]; v <= Vmax[i]; ++v) {
            for (int u = max(Vmin[i-1], v - maxAcc); u <= min(Vmax[i-1], v + maxDec); ++u) {
                if (dp[u] == INF) continue;
                long long deltaKE = max(0, v * v - u * u);
                long long cost = deltaKE + 1LL * G[i] * v + 1LL * alpha * v;
                next_dp[v] = min(next_dp[v], dp[u] + cost);
            }
        }
        dp = move(next_dp);
    }

    long long minFuel = INF;
    for (int v = targetSpeed; v <= maxV; ++v) {
        minFuel = min(minFuel, dp[v]);
    }
    return (minFuel >= INF) ? -1 : minFuel;
}

int main() {
    vector<int> gradients = {2, 5, -1, 3, 0};
    vector<int> vMin = {20, 20, 15, 20, 30};
    vector<int> vMax = {60, 50, 45, 60, 70};
    cout << "Optimal Fuel Units: " << optimizeFuelProfile(5, gradients, vMin, vMax, 10, 15, 2, 35) << "
";
    return 0;
}
```

---

## Problem 3: Low-Level Endianness Swap & CAN Bus CRC Parity

### Problem Statement
In Wabtec's embedded train networks, sensor messages on the CAN Bus (Controller Area Network) arrive as big-endian 32-bit words, while the onboard ARM/x86 controller processes them as little-endian.
1. Write a function to swap the byte order (Endianness swap) of a 32-bit hexadecimal unsigned integer without using standard library conversion functions.
2. Given a 64-bit telemetry frame, compute its odd parity bit and extract an 8-bit payload embedded between bits 12 and 19.

### C++20 Implementation
```cpp
#include <iostream>
#include <iomanip>
#include <cstdint>

using namespace std;

// 1. Endianness Byte Swap using Bit Manipulation
uint32_t swapEndian32(uint32_t val) {
    return ((val & 0x000000FF) << 24) |
           ((val & 0x0000FF00) << 8)  |
           ((val & 0x00FF0000) >> 8)  |
           ((val & 0xFF000000) >> 24);
}

// 2. Extract bitfield [startBit, endBit] inclusive
uint32_t extractPayloadBits(uint64_t frame, int startBit, int endBit) {
    int length = endBit - startBit + 1;
    uint64_t mask = (1ULL << length) - 1ULL;
    return static_cast<uint32_t>((frame >> startBit) & mask);
}

// 3. Compute Odd Parity of a 64-bit frame in O(1) operations
bool computeOddParity(uint64_t x) {
    // Brian Kernighan folded XOR
    x ^= x >> 32;
    x ^= x >> 16;
    x ^= x >> 8;
    x ^= x >> 4;
    x ^= x >> 2;
    x ^= x >> 1;
    return (x & 1) == 0; // Odd parity returns true if number of 1s is even (needs 1 to make odd)
}

int main() {
    uint32_t rawCanMessage = 0x12345678;
    uint32_t converted = swapEndian32(rawCanMessage);
    cout << "Original Hex : 0x" << hex << rawCanMessage << "
";
    cout << "Converted Hex: 0x" << hex << converted << "
";

    uint64_t telemetryFrame = 0xA5A55A5A12345678ULL;
    uint32_t payload = extractPayloadBits(telemetryFrame, 12, 19);
    cout << "Extracted 8-bit Payload (bits 12-19): 0x" << hex << payload << "
";
    cout << "Odd Parity Bit Needed: " << computeOddParity(telemetryFrame) << "
";
    return 0;
}
```

---

## Problem 4: Track Segment Conflict & Dispatch Scheduling (Sweep-Line)

### Problem Statement
A single-track railway corridor is shared by $M$ trains. Each train $j$ has a designated entry time $S_j$ and exit time $E_j$. No two trains may occupy the same single-track segment simultaneously.
1. Find the minimum number of bypass sidings required so that no train is stalled.
2. Given an existing infrastructure of $K$ tracks, return the maximum number of train trips that can be scheduled without conflict.

### Algorithmic Strategy
* Part 1 is the classic **Meeting Rooms II / Minimum Platforms** problem solved in $O(M \log M)$ via sorting arrival/departure events.
* Part 2 is the **Interval Scheduling** problem solved greedily by sorting intervals by earliest end time $E_j$.

### Python 3 Implementation
```python
def min_platforms_required(arrivals, departures):
    arrivals.sort()
    departures.sort()
    
    n = len(arrivals)
    plat_needed = 1
    max_plat = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            plat_needed += 1
            max_plat = max(max_plat, plat_needed)
            i += 1
        else:
            plat_needed -= 1
            j += 1
            
    return max_plat

def max_scheduled_trains(intervals):
    # Sort by end time
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = -1
    
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
            
    return count

# Demonstration
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(f"Minimum Siding Tracks Needed: {min_platforms_required(arr, dep)}")
```

---

## Problem 5: Lock-Free Single-Producer Single-Consumer (SPSC) Ring Buffer

### Problem Statement
Locomotive acoustic and vibration sensors sample at $10	ext{ kHz}$. A high-priority interrupt thread acquires sensor values, while a lower-priority telemetry compression worker reads and transmits them. Implement a **lock-free thread-safe Ring Buffer in C++** with zero dynamic memory allocation during runtime.

### C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <atomic>
#include <optional>
#include <thread>

template <typename T, size_t Capacity>
class SPSCRingBuffer {
    static_assert((Capacity & (Capacity - 1)) == 0, "Capacity must be a power of 2!");
private:
    T buffer[Capacity];
    // Cache line padding to eliminate false sharing
    alignas(64) std::atomic<size_t> head{0};
    alignas(64) std::atomic<size_t> tail{0};

public:
    SPSCRingBuffer() = default;

    bool push(const T& item) {
        const size_t current_tail = tail.load(std::memory_order_relaxed);
        const size_t current_head = head.load(std::memory_order_acquire);

        // Check if buffer is full
        if ((current_tail - current_head) == Capacity) {
            return false; // Buffer overflow
        }

        buffer[current_tail & (Capacity - 1)] = item;
        tail.store(current_tail + 1, std::memory_order_release);
        return true;
    }

    std::optional<T> pop() {
        const size_t current_head = head.load(std::memory_order_relaxed);
        const size_t current_tail = tail.load(std::memory_order_acquire);

        // Check if buffer is empty
        if (current_head == current_tail) {
            return std::nullopt; // Buffer underflow
        }

        T item = buffer[current_head & (Capacity - 1)];
        head.store(current_head + 1, std::memory_order_release);
        return item;
    }
};

int main() {
    SPSCRingBuffer<int, 1024> sensorBuffer;
    sensorBuffer.push(120);
    sensorBuffer.push(125);

    auto v1 = sensorBuffer.pop();
    if (v1) cout << "Read Sensor Sample: " << *v1 << "
";
    return 0;
}
```
