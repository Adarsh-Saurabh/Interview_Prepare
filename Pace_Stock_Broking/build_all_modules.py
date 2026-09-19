#!/usr/bin/env python3
"""
build_all_modules.py
Generates all Markdown (.md) and HTML (.html) modules for Pace Stock Broking Services
Software Developer (Quantitative & Low-Latency Trading Systems) Interview Preparation.
"""

import os
import markdown
from template import render_pace_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modules_data = {}

# =============================================================================
# MODULE 00: Company & Role Intel
# =============================================================================
modules_data["00_START_HERE"] = {
    "title": "00: Pace Company & Role Deep Dive",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Pace Stock Broking — Company & Role Deep Dive

## 1. Executive Intelligence & Institutional Profile
**Pace Stock Broking Services Pvt. Ltd.** was founded in 1995 and has evolved into one of India's premier financial conglomerates with specialized operations spanning:
- **Proprietary High-Frequency Trading (HFT):** Ultra-low-latency market-making, statistical arbitrage, and quantitative algorithmic strategies on Indian and global exchanges.
- **Medium-Frequency Trading (MFT):** Statistical momentum, pairs trading, and quantitative multi-factor strategies holding positions across minutes to days.
- **Exchange Memberships:** Prominent clearing and algorithmic trading member on the National Stock Exchange of India (NSE), Bombay Stock Exchange (BSE), and Multi Commodity Exchange (MCX, where Pace has been recognized as a leading algo firm).
- **Technology Infrastructure Hub:** Technical trading operations centered around Gurgaon / New Delhi, with specialized teams from top IITs, NITs, and BITS.

---

## 2. Low-Latency Infrastructure & Co-Location Ecosystem

```
Exchange Matching Engine (NSE / BSE Colocation Rack)
         │
         │ 100 Gbps Low-Latency Optical Fiber (Solarflare NIC)
         ▼
[Kernel Bypass Layer: Solarflare OpenOnload / DPDK]
         │ (Zero-copy Direct User-Space Packet Delivery: ~300 ns)
         ▼
[Market Data Ingestion: ITCH / FAST Multicast Parser]
         │ (Unpack binary packets, maintain tick sequence)
         ▼
[In-Memory Limit Order Book (LOB) Engine: O(1) Cache-Aligned]
         │ (Compute Best Bid, Ask, Micro-Price, Order Book Imbalance)
         ▼
[Quantitative Alpha Strategy Model (C++ / SIMD AVX-512)]
         │ (Generate Signal: +1 Buy / -1 Sell / 0 Hold)
         ▼
[Pre-Trade Risk Engine: Sub-microsecond Pre-Allocated Checks]
         │ (Max Notional, Price Collar, Position Limits, Circuit Breakers)
         ▼
[Order Gateway: Binary OUCH / FIX Protocol Engine]
         │ (Serialize raw TCP order packet)
         ▼
[Exchange Venue NIC Outbound Wire: Microsecond Execution]
```

### Key Engineering Realities:
1. **The Race for Microseconds:**
   - In retail software, 100 milliseconds is fast. In HFT, **1 microsecond ($1\\,\\mu\\text{s} = 1,000\\,\\text{ns}$)** is an eternity.
   - If an arbitrage opportunity opens across NSE and BSE, 10 HFT firms detect it simultaneously. Only the firm that crosses the exchange threshold first gets filled; the remaining 9 eat rejection or slippage costs.
2. **Co-Location (Colo):**
   - Trading servers physically installed in the same exchange data center room as the matching engine (e.g., NSE Colo at BKC, Mumbai).
   - Speed-of-light in glass: $\\approx 5\\,\\text{ns}$ per meter. Cable lengths are equalized across broker racks to prevent unfair physical advantages.
3. **Hardware & Systems Stack:**
   - **Solarflare 100 Gbps NICs:** Utilizing `OpenOnload` user-space network stacks to eliminate Linux kernel context switches.
   - **Modern C++ (C++17/20):** Strict lock-free, zero-allocation architectures with CPU cache alignment (`alignas(64)`).
   - **HPC Clusters & GPUs:** Off-market statistical model training, deep backtesting of historical tick-by-tick order book data using Python (`NumPy`, `Pandas`, `PyTorch`).

---

## 3. Placement Drive Intelligence (Campus 2026)

| Parameter | Placement Drive Specification |
| :--- | :--- |
| **Target Role** | Software Developer (Quantitative & Low-Latency Trading Systems) |
| **Stipend** | **₹75,000 / month** (6-Month Internship) |
| **Full-Time CTC** | **₹41.00 LPA** (Post-PPO) |
| **Open Vacancies** | **5 – 6 Engineers** (Substantial hiring appetite) |
| **Online Test (OT)** | **Sunday, 20th September, 7:45 PM – 10:30 PM (TIIR Lab)** |
| **OT Sections** | **Aptitude** (Logic/Speed), **Mathematics** (Prob/Stats), **DSA** (4 Coding Problems) |
| **Interviews** | **Monday, 21st September** (Continuous technical rounds) |

---

## 4. The 3 Technical Pillars Tested

```
┌─────────────────────────┐   ┌─────────────────────────┐   ┌─────────────────────────┐
│   1. Algorithmic DSA    │   │  2. Low-Latency Systems │   │  3. Math & Quantitative │
├─────────────────────────┤   ├─────────────────────────┤   ├─────────────────────────┤
│ • Dynamic Programming   │   │ • Cache lines & misses  │   │ • Bayes theorem & stats │
│ • Two pointers contrib. │   │ • Struct memory padding │   │ • Expected value games  │
│ • Disjoint Set Union    │   │ • Lock-free atomics     │   │ • Combinatorics & logic │
│ • 2D Grid Pathfinding   │   │ • vtable & OOP overhead │   │ • Matrix linear algebra │
└─────────────────────────┘   └─────────────────────────┘   └─────────────────────────┘
```
"""
}

# =============================================================================
# MODULE 01: Online Test (OA)
# =============================================================================
modules_data["01_Online_Test"] = {
    "title": "01: Signature OA Coding & Math Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company Deep Dive",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: Low-Latency C++ & OS",
    "markdown": """# 01: Signature Online Assessment (OA) Problems

## 1. Test Architecture & Scoring Strategy
The Pace Stock Broking Online Test runs for **165 minutes** on HackerRank in the TIIR lab:
* **Section 1: Quantitative Aptitude & Fast Logic (approx. 20 mins):** Probability, mental arithmetic, series, and time-speed-distance.
* **Section 2: Mathematical Foundations (approx. 35 mins):** Bayes theorem, discrete probability distributions, expected value puzzles, and matrix linear algebra.
* **Section 3: Data Structures & Algorithms (approx. 110 mins):** 4 medium-to-hard coding problems requiring optimal asymptotic time and memory complexity.

---

## 2. Signature Coding Problem 1: Subarray Value Contribution (Two Pointers)

### Problem Description:
Given an array $A$ of $N$ integers, calculate the sum of $\\max(B) - \\min(B)$ across all non-empty contiguous subarrays $B$ of $A$. Return the result modulo $10^9 + 7$.
* **Constraints:** $N \\le 2 \\times 10^5$, $1 \\le A[i] \\le 10^9$.
* **HFT Significance:** Quant desks compute streaming volatility and rolling price spreads across thousands of market windows. An $O(N^2)$ solution will TLE instantly.

### Optimal Solution ($O(N)$ Time, $O(N)$ Space):
Instead of iterating through every subarray, compute how many subarrays have $A[i]$ as their maximum, and how many have $A[i]$ as their minimum using a **Monotonic Stack**.
$$\\text{Total Sum} = \\sum_{i=0}^{N-1} A[i] \\times (\\text{count\\_max}(i) - \\text{count\\_min}(i))$$

```cpp
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

long long totalSubarrayVariance(const vector<int>& arr) {
    int n = arr.size();
    long long MOD = 1e9 + 7;

    // left_max[i]: distance to previous strictly greater element
    // right_max[i]: distance to next greater or equal element
    vector<int> left_max(n), right_max(n);
    // left_min[i]: distance to previous strictly smaller element
    // right_min[i]: distance to next smaller or equal element
    vector<int> left_min(n), right_min(n);

    stack<int> s;

    // 1. Compute max contributions
    for (int i = 0; i < n; ++i) {
        while (!s.empty() && arr[s.top()] <= arr[i]) s.pop();
        left_max[i] = s.empty() ? (i + 1) : (i - s.top());
        s.push(i);
    }
    while (!s.empty()) s.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!s.empty() && arr[s.top()] < arr[i]) s.pop();
        right_max[i] = s.empty() ? (n - i) : (s.top() - i);
        s.push(i);
    }
    while (!s.empty()) s.pop();

    // 2. Compute min contributions
    for (int i = 0; i < n; ++i) {
        while (!s.empty() && arr[s.top()] >= arr[i]) s.pop();
        left_min[i] = s.empty() ? (i + 1) : (i - s.top());
        s.push(i);
    }
    while (!s.empty()) s.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!s.empty() && arr[s.top()] > arr[i]) s.pop();
        right_min[i] = s.empty() ? (n - i) : (s.top() - i);
        s.push(i);
    }

    // 3. Aggregate totals
    long long total = 0;
    for (int i = 0; i < n; ++i) {
        long long max_subarrays = (1LL * left_max[i] * right_max[i]);
        long long min_subarrays = (1LL * left_min[i] * right_min[i]);
        long long diff = (max_subarrays - min_subarrays);
        total = (total + (diff % MOD) * arr[i]) % MOD;
    }

    return (total + MOD) % MOD;
}
```

---

## 3. Signature Coding Problem 2: Dynamic Connectivity (DSU with Minimum Path)

### Problem Description:
You are given $N$ trading venues and $M$ optical communication fiber lines being constructed sequentially at timestamps $t_1, t_2, \\dots, t_M$. Each link connects venue $u$ and $v$ with propagation latency $L$. Answer $Q$ queries: *"At what earliest timestamp can venue $A$ and venue $B$ communicate with total maximum edge latency $\\le X$?"*
* **Constraints:** $N \\le 10^5$, $M \\le 2 \\times 10^5$, $Q \\le 10^5$.
* **HFT Significance:** Exchange inter-connectivity routing and dynamic risk circuit-breaker partitioning.

### Optimal C++ Solution (Disjoint Set Union with Path Compression & Union by Rank):

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> rank;

    DSU(int n) {
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        rank.assign(n + 1, 0);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]); // Path compression
    }

    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            // Union by rank
            if (rank[root_i] < rank[root_j])
                swap(root_i, root_j);
            parent[root_j] = root_i;
            if (rank[root_i] == rank[root_j])
                rank[root_i]++;
            return true;
        }
        return false;
    }
};
```

---

## 4. Mathematics & Probability Section Mastery

### Problem: The High-Frequency Coin Toss Game
**Question:** A trader flips a fair coin repeatedly. What is the expected number of flips until the pattern **HTH** appears, versus the pattern **HTT**?
* **Analytical Derivation:**
  * Let $E[\\text{HTT}]$ and $E[\\text{HTH}]$ denote the expected flips.
  * For any pattern $S$, by Conway's Leading Crosses Algorithm or Martingale Optional Stopping Theorem:
    $$E[S] = \\sum_{k=1}^{L} I(k) \\cdot 2^k$$
    where $I(k) = 1$ if the prefix of length $k$ equals the suffix of length $k$.
  * For **HTT**:
    * Prefix/Suffix matches: Length 3 (`HTT` $\\ne$ `HTT` prefix match? Only full string matches).
    * Prefix of length 1 is `H`, suffix is `T` (no).
    * Prefix of length 2 is `HT`, suffix is `TT` (no).
    * Prefix of length 3 is `HTT`, suffix is `HTT` (yes: $2^3 = 8$).
    * **$E[\\text{HTT}] = 8$ flips.**
  * For **HTH**:
    * Prefix of length 1 is `H`, suffix is `H` (match! $2^1 = 2$).
    * Prefix of length 2 is `HT`, suffix is `TH` (no).
    * Prefix of length 3 is `HTH`, suffix is `HTH` (match! $2^3 = 8$).
    * **$E[\\text{HTH}] = 8 + 2 = 10$ flips.**
  * **HFT Interviewer Follow-up:** *Why does HTH take longer on average than HTT?*
    * *Answer:* Because HTH has internal self-overlap. If you have `HT` and roll `T`, you fail and start completely over. But for `HTT`, failing on the 3rd roll gives `HTH`, which already gives you the first `H` of the next attempt!
"""
}

# =============================================================================
# MODULE 02: Technical Rounds
# =============================================================================
modules_data["02_Technical_Rounds"] = {
    "title": "02: Low-Latency C++ & Core Systems",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Problems",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Market Microstructure & LOB",
    "markdown": """# 02: Low-Latency C++ & Core Systems

## 1. The Cost of Virtual Functions (`vtable` & `vptr`)

### What happens under the hood?
When a class declares a virtual function:
1. The compiler instantiates a static **Virtual Method Table (`vtable`)** containing function pointers to the resolved methods.
2. Every instance of the class receives an invisible **Virtual Table Pointer (`vptr`)** (typically 8 bytes on a 64-bit architecture) at offset 0.
3. When calling `ptr->executeTrade()`:
   * Dereference object pointer to read `vptr`.
   * Add offset to locate `executeTrade` entry in `vtable`.
   * Dereference function pointer and branch (`call %rax`).

```
Object Instance in RAM                     Class VTable in .rodata
┌─────────────────────────┐               ┌──────────────────────────────┐
│  vptr (8 bytes)  ───────┼──────────────►│ [0] &Order::validate()       │
├─────────────────────────┤               ├──────────────────────────────┤
│  uint64_t order_id      │               │ [1] &LimitOrder::execute()   │
├─────────────────────────┤               └──────────────────────────────┘
│  double price           │
└─────────────────────────┘
```

### Why is this banned in HFT Hot-Paths?
1. **Instruction Cache (I-Cache) Eviction & Indirection:** Two pointer dereferences instead of one direct assembly `call`.
2. **Compiler Inlining Banned:** Compilers cannot inline virtual calls at compile time unless devirtualization succeeds. Inlining eliminates call-overhead and enables register allocation optimizations.
3. **Branch Prediction Penalty:** Dynamic indirect jumps confuse CPU branch target buffers (BTB), triggering expensive $\\sim 15-20$ cycle CPU pipeline flushes.

### The HFT Alternative: Curiously Recurring Template Pattern (CRTP)
Compile-time static polymorphism with zero runtime overhead:

```cpp
template <typename Derived>
class OrderHandler {
public:
    inline void processOrder() {
        static_cast<Derived*>(this)->processOrderImpl();
    }
};

class EquityHandler : public OrderHandler<EquityHandler> {
public:
    inline void processOrderImpl() {
        // Inlined directly into caller assembly without vtable lookup!
    }
};
```

---

## 2. Memory Alignment, Struct Padding & False Sharing

### Struct Layout & Cache Lines
CPUs access RAM in discrete **64-byte Cache Lines**. An unaligned variable spanning two cache lines requires two memory fetches instead of one.

```cpp
// BAD: Poor layout (Wasteful padding)
struct BadTrade {
    char exchange_code;  // 1 byte + 7 bytes padding
    double price;        // 8 bytes
    char order_type;     // 1 byte + 7 bytes padding
    uint64_t order_id;   // 8 bytes
}; // Total Size: 32 bytes (14 bytes wasted padding!)

// GOOD: Ordered by descending alignment
struct alignas(32) GoodTrade {
    double price;        // 8 bytes
    uint64_t order_id;   // 8 bytes
    char exchange_code;  // 1 byte
    char order_type;     // 1 byte
    char padding[14];    // Explicit 14 bytes pad to 32 bytes
}; // Total Size: 32 bytes (Zero implicit wasted alignment traps)
```

### Eliminating False Sharing in Multithreading
When Thread 1 (Core 1) writes to `tail` and Thread 2 (Core 2) writes to `head` located on the **same 64-byte cache line**, the CPU's cache coherence protocol (MESI) repeatedly invalidates Core 1 and Core 2 caches across the interconnect bus—degrading performance by $50\\times$.

```cpp
// Prevent False Sharing in Lock-Free Queues:
struct SPSCQueuePointers {
    alignas(64) std::atomic<uint64_t> write_tail{0}; // Core 1 writes here
    alignas(64) std::atomic<uint64_t> read_head{0};  // Core 2 reads here
};
```

---

## 3. Row-Major vs Column-Major Memory Traversal

### Benchmark Comparison:
In C and C++, 2D arrays are stored in **row-major order** (contiguous in memory row by row):

```cpp
const int N = 8192;
int matrix[N][N];

// Fast: Row-Major Traversal (Contiguous memory access)
// 1 cache line fetch loads 16 consecutive integers into L1 Cache!
for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
        sum += matrix[i][j]; // Spatial Locality: 15 cache hits per 1 miss
    }
}

// Slow: Column-Major Traversal (Stride of 8192 integers = 32 KB jump!)
// Every single iteration triggers an L1/L2 Cache Miss!
for (int j = 0; j < N; ++j) {
    for (int i = 0; i < N; ++i) {
        sum += matrix[i][j]; // Stride Thrashing: ~10x slower execution
    }
}
```
"""
}

# =============================================================================
# MODULE 03: Domain Deep Dive
# =============================================================================
modules_data["03_Domain_Deep_Dive"] = {
    "title": "03: Market Microstructure & Trading Systems",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: Low-Latency C++ & OS",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Resume Defense & Traps",
    "markdown": """# 03: Market Microstructure & Low-Latency Trading

## 1. What is an Electronic Limit Order Book (LOB)?
An exchange order book is an in-memory two-sided auction mechanism:
* **Bids (Buy Orders):** Sorted in descending order (highest willingness to pay at the top).
* **Asks / Offers (Sell Orders):** Sorted in ascending order (lowest willingness to sell at the top).
* **Top of Book (BBO - Best Bid and Offer):**
  $$\\text{Best Bid} = \\max(P_{\\text{buy}}), \\quad \\text{Best Ask} = \\min(P_{\\text{sell}})$$
* **The Spread:** $\\text{Spread} = \\text{Best Ask} - \\text{Best Bid}$.
* **Price-Time Priority (FIFO):**
  If Order A and Order B arrive at the exact same price level ₹1,500.00, Order A gets executed first if it arrived 1 nanosecond earlier.

```
       ASKS (Sell Orders)
Level 3: ₹1,501.50  (Qty: 2,500)
Level 2: ₹1,501.00  (Qty: 1,200)
Level 1: ₹1,500.50  (Qty:   400) ◄── BEST ASK
---------------------------------- SPREAD = ₹0.50
Level 1: ₹1,500.00  (Qty:   800) ◄── BEST BID
Level 2: ₹1,499.50  (Qty: 3,000)
Level 3: ₹1,499.00  (Qty: 5,400)
       BIDS (Buy Orders)
```

---

## 2. Exchange Protocol Architecture: Market Data vs Order Entry

### Market Data (Tick Dissemination): Multicast UDP
* **Exchange Side:** Exchanges multicast market events (order inserted, order canceled, trade executed) over raw UDP.
* **Why UDP?** No TCP handshake, no TCP head-of-line blocking, and 1-to-many broadcast efficiency.
* **Protocols:**
  * **NASDAQ ITCH / NSE Multicast:** Binary, fixed-length packets containing `Timestamp`, `Order_ID`, `Side`, `Shares`, `Price`.
  * **Packet Loss Recovery:** When a UDP tick packet drops, feed handlers detect missing sequence numbers and query TCP snapshot/replay recovery channels.

### Order Entry (Execution): Point-to-Point TCP
* **Broker Side:** When a strategy triggers, orders are transmitted over dedicated point-to-point TCP connections to guarantee reliable execution.
* **Protocols:**
  * **NASDAQ OUCH / NSE NEAT:** High-speed binary execution protocols.
  * **FIX (Financial Information eXchange):** Human-readable tag-value protocol (e.g., `35=D|55=RELIANCE|54=1`) used for institutional and retail trading, but avoided in ultra-HFT hot paths due to string parsing overhead.

---

## 3. Kernel Bypass Networking: Solarflare & DPDK

### The Linux Kernel Networking Bottleneck:
```
Normal Linux Socket Path:
NIC RX Wire ──► Hardware Interrupt (IRQ) ──► OS Kernel SoftIRQ 
            ──► Allocate sk_buff in Kernel ──► Copy payload across Kernel-User Boundary 
            ──► Context Switch to User Process ──► recv() returns
            [Total Latency: 1.5 - 3.5 microseconds]

Kernel Bypass (Solarflare OpenOnload / DPDK):
NIC RX Wire ──► Direct Memory Access (DMA) to Pre-Mapped User Memory Ring Buffer 
            ──► User Application polls buffer directly
            [Total Latency: 250 - 450 nanoseconds] (Zero syscalls, zero context switches)
```

### Key Trade-offs:
* **Busy Polling:** Kernel bypass threads run on dedicated isolated CPU cores pinned at 100% CPU utilization (`pthread_setaffinity_np`), spinning continuously on memory addresses rather than sleeping on interrupts.
"""
}

# =============================================================================
# MODULE 04: Candidate Resume Grilling
# =============================================================================
modules_data["04_Candidate_Resume_Grilling"] = {
    "title": "04: Adarsh's Resume Defense & Traps",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Market Microstructure & LOB",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: Limit Order Book LLD",
    "markdown": """# 04: Adarsh Saurabh — Resume Defense & Traps

## 1. Bridging Signal Processing to Quantitative Low-Latency HFT

### The Interviewer's Skeptical Opening Question:
> *"Your Master's degree from NIT Rourkela is in Signal and Image Processing. Pace is a high-frequency algorithmic trading desk. Why shouldn't we hire a pure Financial Engineering or Computer Science graduate instead?"*

### Adarsh's Winning Defense Strategy:
1. **Tick Data IS a High-Frequency Discrete Signal:**
   * Financial market tick feeds are non-stationary, noisy, discrete-time stochastic signals sampled at microsecond intervals.
   * Core concepts in Signal Processing—such as **Discrete Fourier Transforms (DFT)**, **Kalman Filters (state estimation from noisy sensors)**, **Autoregressive Moving Average (ARMA)**, and **Convolutional Feature Extraction**—are the exact mathematical foundations used by quantitative alpha researchers to model price momentum and order flow imbalance.
2. **Dual Foundation Advantage:**
   * B.Tech in CSE (GGU Bilaspur, 8.5 CGPA): Mastery of Operating Systems, Memory Architecture, Compilers, and C++ Data Structures.
   * M.Tech in Signal Processing (NIT Rourkela, 8.28 CGPA): Advanced Linear Algebra, Matrix Decompositions (SVD, Eigenvalues), and numerical algorithm optimization.

---

## 2. Deep Project Defense: Warehouse PathMapper (IBYD Technology)

### The Likely Interrogation:
> *"You claim you scaled spatial routing to $10,000 \\times 10,000$ unit spaces for 10,000+ coordinates simultaneously in under 0.5 seconds on an ordinary single CPU core. How is that possible without running out of RAM or cache thrashing?"*

### Architectural Explanation:
1. **1D Contiguous Memory Layout Over Pointer Graphs:**
   * Standard graph implementations use pointer-based adjacency lists (`vector<vector<Node*>>`). On a $10,000 \\times 10,000$ grid ($10^8$ cells), node pointers alone would consume $>800\\,\\text{MB}$ of heap, resulting in pointer chasing and L3 cache thrashing.
   * PathMapper formatted coordinates into a flat 1D byte array where cell $(x, y) = x \\cdot W + y$. Accessing neighbors utilizes direct index math with zero pointer dereferences.
2. **Heuristic Pruning & Spatial Discretization:**
   * Utilized modified A* search with Euclidean heuristic bounds and bounding-box spatial pruning, evaluating only relevant navigation corridors.
   * Used a flat array binary min-heap for the priority queue with pre-allocated storage to prevent dynamic heap reallocation during traversal.

---

## 3. Deep Project Defense: Alternative Data Radar

### The Likely Interrogation:
> *"How does your Alternative Data Radar translate into an actual trading strategy?"*

### Architectural Explanation:
1. **Pre-Earnings Asymmetric Information Ingestion:**
   * Extracted non-traditional web signals: dynamic hiring spikes, pricing shifts, and web traffic changes across target corporations.
   * Quant research relies on alternative data signals to predict earnings surprises before quarterly balance sheet releases.
2. **High-Throughput Extraction Pipeline:**
   * Handled rate limits and anti-scraping blocks through proxy session rotation.
   * Normalized disparate qualitative data into a structured numerical 0–100 corporate health score indexed in PostgreSQL for rapid SQL backtesting.

---

## 4. Deep Project Defense: K-HOG Keyframe Identifier (K-HUKI)

### The Likely Interrogation:
> *"Why did you use classical HOG and unsupervised clustering instead of a fine-tuned ResNet or Transformer?"*

### The HFT-Aligned Answer:
> *"Because in high-throughput streaming environments, latency and resource footprint dictate feasibility. A ResNet model requires billions of floating-point operations (FLOPs) and GPU acceleration, introducing massive inference latency. By engineering an unsupervised pipeline utilizing Histogram of Oriented Gradients (HOG) and geometric clustering, we captured 96.45% accuracy while running **11× faster** on a standard CPU with zero GPU dependency. This proves my engineering bias toward choosing lightweight, mathematically sound algorithms over computationally bloated neural networks."*
"""
}

# =============================================================================
# MODULE 05: System Design (LLD)
# =============================================================================
modules_data["05_System_Design_or_HIL"] = {
    "title": "05: Limit Order Book (LOB) Low-Level Design",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Resume Defense & Traps",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Prop Trading & Culture",
    "markdown": """# 05: Limit Order Book (LOB) — Low-Level System Design

## 1. System Requirements & Latency Bounds
* **Functional Requirements:**
  1. `add_order(order_id, side, price, qty)`: Insert limit order in $O(1)$ or $O(\\log N)$.
  2. `cancel_order(order_id)`: Remove existing order in $O(1)$ time.
  3. `get_bbo()`: Return Best Bid and Best Ask in $O(1)$ time.
  4. `match()`: Execute incoming market orders against the top of book.
* **Non-Functional Latency Requirements:**
  * **Zero Dynamic Allocation (`malloc`/`new`) on Hot-Path:** Pre-allocate all order structures in a memory pool.
  * **Deterministic Execution:** No unbounded iterations.

---

## 2. Low-Level Architecture & Data Structure Choice

```
Price Level Map (std::map<double, PriceLevel*> or Flat Bounded Array)
  ├── 1500.50 (Ask Level 1) ──► Doubly Linked List of Orders:
  │                             [Order 101: 200 shares] ◄──► [Order 102: 200 shares]
  ├── 1501.00 (Ask Level 2) ──► [Order 103: 500 shares]
  │
Hash Map Index (std::unordered_map<uint64_t, OrderNode*>)
  ├── Key: 101 ──► Points directly to Order 101 in Doubly Linked List ($O(1)$ Cancel)
  └── Key: 102 ──► Points directly to Order 102 in Doubly Linked List ($O(1)$ Cancel)
```

---

## 3. Production C++ Implementation (Ultra-Low Latency Order Book)

```cpp
#include <iostream>
#include <unordered_map>
#include <map>
#include <cstdint>

enum class Side { BUY, SELL };

struct Order {
    uint64_t order_id;
    Side side;
    double price;
    uint32_t qty;
    Order* prev{nullptr};
    Order* next{nullptr};
};

struct LimitLevel {
    double price;
    uint32_t total_qty{0};
    Order* head{nullptr};
    Order* tail{nullptr};

    void append(Order* order) {
        order->prev = tail;
        order->next = nullptr;
        if (tail) tail->next = order;
        else head = order;
        tail = order;
        total_qty += order->qty;
    }

    void remove(Order* order) {
        if (order->prev) order->prev->next = order->next;
        else head = order->next;

        if (order->next) order->next->prev = order->prev;
        else tail = order->prev;

        total_qty -= order->qty;
        order->prev = nullptr;
        order->next = nullptr;
    }

    bool empty() const { return head == nullptr; }
};

class LimitOrderBook {
private:
    // Buy orders: Descending order (highest bid first)
    std::map<double, LimitLevel, std::greater<double>> bids;
    // Sell orders: Ascending order (lowest ask first)
    std::map<double, LimitLevel, std::less<double>> asks;

    // Fast order lookup for O(1) cancellations
    std::unordered_map<uint64_t, Order*> order_map;

    // Static memory pool to avoid runtime heap allocations
    static constexpr size_t POOL_SIZE = 100000;
    Order pool[POOL_SIZE];
    size_t pool_idx{0};

    Order* allocate_order() {
        if (pool_idx < POOL_SIZE) return &pool[pool_idx++];
        return new Order(); // Fallback if pool exhausted
    }

public:
    void add_order(uint64_t id, Side side, double price, uint32_t qty) {
        Order* order = allocate_order();
        order->order_id = id;
        order->side = side;
        order->price = price;
        order->qty = qty;

        if (side == Side::BUY) {
            bids[price].append(order);
        } else {
            asks[price].append(order);
        }
        order_map[id] = order;
    }

    void cancel_order(uint64_t id) {
        auto it = order_map.find(id);
        if (it == order_map.end()) return;

        Order* order = it->second;
        if (order->side == Side::BUY) {
            auto level_it = bids.find(order->price);
            if (level_it != bids.end()) {
                level_it->second.remove(order);
                if (level_it->second.empty()) bids.erase(level_it);
            }
        } else {
            auto level_it = asks.find(order->price);
            if (level_it != asks.end()) {
                level_it->second.remove(order);
                if (level_it->second.empty()) asks.erase(level_it);
            }
        }
        order_map.erase(it);
    }

    double get_best_bid() const {
        return bids.empty() ? 0.0 : bids.begin()->first;
    }

    double get_best_ask() const {
        return asks.empty() ? 0.0 : asks.begin()->first;
    }
};
```
"""
}

# =============================================================================
# MODULE 06: Managerial & HR
# =============================================================================
modules_data["06_Managerial_and_HR"] = {
    "title": "06: Life at Pace & Culture Fit",
    "prev_link": "05_System_Design_or_HIL.html",
    "prev_title": "05: Limit Order Book LLD",
    "next_link": "07_Quick_Reference.html",
    "next_title": "07: Caveman Quant CheatSheet",
    "markdown": """# 06: Life at Pace & Cultural Fit

## 1. The High-Frequency Trading Mindset
Proprietary trading desks operate under fundamentally different rules than standard consumer tech firms:
* **The Bottom Line is Immediate:** In SaaS, a software bug might cause a customer ticket. In HFT, an unhandled corner case or deadlocked thread can wipe out millions of rupees in capital in 300 milliseconds.
* **Strict Performance Meritocracy:** Code is measured by latency profilers and daily PnL (Profit and Loss). If your optimization cuts 40 nanoseconds off the order loop, its impact is mathematically visible immediately.
* **Extreme Ownership & Zero Bureaucracy:** Small teams of 4–8 engineers deploy directly to live exchange colocation servers. There are no 5-tier manager approval chains.

---

## 2. Signature Behavioral Questions & Strategic Answers

### Question 1: "Why do you want to join an HFT firm like Pace instead of Big Tech (Google, Microsoft) or SaaS unicorns?"
* **Strategic Answer:**
  > *"Big Tech companies optimize for scale across millions of distributed web clients, where latency is measured in hundreds of milliseconds and constrained by network hops. HFT is the only industry that pushes software engineering to the physical limits of hardware silicon—squeezing CPU clock cycles, eliminating cache misses, and designing lock-free data structures. At Pace, I get to write modern C++ where low-level systems architecture and advanced mathematical signal modeling directly impact performance every single trading microsecond."*

### Question 2: "What would you do if you noticed a live trading strategy behaving erratically and generating unexpected orders?"
* **Strategic Answer:**
  > *"First, execute the **Emergency Kill-Switch** immediately to stop outbound order dissemination and cancel outstanding working limit orders on the exchange. Protecting trading capital always precedes debugging. Second, notify the head risk officer and quant lead with the exact timestamp and affected symbols. Third, recreate the anomalous market state in the offline backtester using the recorded tick-by-tick packet pcap to identify whether it was an exchange feed format anomaly, numerical overflow, or concurrency race condition before any redeployment."*
"""
}

# =============================================================================
# MODULE 07: Quick Reference (CheatSheet)
# =============================================================================
modules_data["07_Quick_Reference"] = {
    "title": "07: Caveman Quant CheatSheet",
    "prev_link": "06_Managerial_and_HR.html",
    "prev_title": "06: Prop Trading & Culture",
    "next_link": "README.html",
    "next_title": "3-Day Study Roadmap",
    "markdown": """# 07: Caveman Quant CheatSheet & Formula Vault

## 1. Latency Numbers Every Quant Dev Must Know

```
┌───────────────────────────────────────┬─────────────────────────┐
│ Operation                             │ Latency                 │
├───────────────────────────────────────┼─────────────────────────┤
│ CPU L1 Cache Reference                │ 0.5 - 1 ns              │
│ Branch Mispredict                     │ 3 - 5 ns                │
│ CPU L2 Cache Reference                │ 3 - 4 ns                │
│ Mutex Lock / Unlock                   │ 15 - 25 ns              │
│ CPU L3 Cache Reference                │ 10 - 20 ns              │
│ Main Memory (DRAM) Access             │ 50 - 100 ns             │
│ PCIe Bus Transfer                     │ 100 - 250 ns            │
│ Kernel Bypass Network Tick (OpenOnload)│ 250 - 450 ns           │
│ Linux OS Context Switch / Page Fault  │ 1,500 - 3,500 ns        │
│ Standard Linux Socket recv() syscall  │ 2,000 - 4,000 ns        │
│ Mumbai NSE to BKC Colo Roundtrip      │ < 10,000 ns (10 µs)     │
│ Mumbai to London Optical Fiber        │ ~ 60,000,000 ns (60 ms) │
└───────────────────────────────────────┴─────────────────────────┘
```

---

## 2. Modern C++ Low-Latency Commandments
1. **Never allocate heap memory (`new` / `malloc`) on the critical path:** Always use pre-allocated static arrays or memory pools.
2. **Eliminate dynamic polymorphism:** Replace `virtual` functions with templates (CRTP).
3. **Pass objects by `const &`:** Avoid redundant copy constructor invocations.
4. **Pad structures to 64 bytes (`alignas(64)`):** Prevent multithreaded false sharing.
5. **Never use `std::endl`:** Always use `'\n'` to avoid forcing redundant I/O buffer flushes.
6. **Prefer sequential array iteration (Row-Major):** Exploit CPU hardware prefetchers.
7. **Use `std::atomic` with relaxed or acquire-release semantics:** Avoid heavy sequential consistency barriers unless strictly necessary.

---

## 3. Mathematical Formula Vault

* **Bayes Theorem:**
  $$P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$$
* **Expected Value of Discrete Random Variable:**
  $$E[X] = \\sum_{i} x_i \\cdot P(X = x_i)$$
* **Variance & Covariance:**
  $$\\text{Var}(X) = E[X^2] - (E[X])^2, \\quad \\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$
* **Order Book Spread & Mid-Price:**
  $$\\text{Mid-Price} = \\frac{P_{\\text{best\\_ask}} + P_{\\text{best\\_bid}}}{2}$$
* **Order Book Imbalance (OBI):**
  $$\\text{OBI} = \\frac{Q_{\\text{bid}} - Q_{\\text{ask}}}{Q_{\\text{bid}} + Q_{\\text{ask}}} \\in [-1, +1]$$
"""
}

# =============================================================================
# MODULE README: 3-Day Study Roadmap
# =============================================================================
modules_data["README"] = {
    "title": "3-Day Study Roadmap for Pace Stock Broking",
    "prev_link": "07_Quick_Reference.html",
    "prev_title": "07: Caveman Quant CheatSheet",
    "next_link": "index.html",
    "next_title": "Overview & Hub",
    "markdown": """# 3-Day Accelerated Study Roadmap

## 📅 Day 1 (Saturday): Online Test (OA) Dominance
* **Morning (09:00 – 13:00): Data Structures & Algorithms**
  * Solve **Monotonic Stack** subarray contribution problems (LeetCode 907, 2104).
  * Practice **Disjoint Set Union (DSU)** with path compression and rank optimization.
  * Practice **2D Grid BFS/DFS** with constrained state transitions.
* **Afternoon (14:30 – 18:00): Mathematics & Probability**
  * Review conditional probability, Bayes theorem, coin toss state machines, and expected value games.
  * Solve mental math and numerical sequence puzzles.
* **Night (19:30 – 22:30): Mock Assessment**
  * Timed 90-minute coding sprint simulating the HackerRank environment.

---

## 📅 Day 2 (Sunday): Systems Deep Dive & Online Assessment
* **Morning (09:00 – 13:00): Low-Latency C++ & OS Internals**
  * Master the internals of `vtable`, `vptr`, and memory alignment (`alignas(64)`).
  * Understand cache lines, false sharing, and row-major vs column-major matrix traversal.
* **Afternoon (14:30 – 18:00): Limit Order Book & Market Microstructure**
  * Review the C++ implementation of the Limit Order Book from Module 05.
  * Review kernel bypass (Solarflare OpenOnload) vs Linux TCP sockets.
* **Night (19:45 – 22:30): THE ONLINE ASSESSMENT (TIIR Lab)**
  * Stay calm, read problem constraints carefully, and ensure zero off-by-one errors.

---

## 📅 Day 3 (Monday): Interview Day Execution
* **Pre-Interview Polish (07:30 – 09:00):**
  * Review Module 04: Project Defense for Warehouse PathMapper, Alternative Data Radar, and K-HOG.
  * Review Module 06: Emergency Kill-Switch and prop trading motivation.
* **Interview Rounds (Morning Onwards):**
  * Communicate thought process out loud.
  * When writing code, write clean, modern C++ with explicit consideration for time and memory complexity.
"""
}

# =============================================================================
# INDEX HUB CONTENT
# =============================================================================
index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
    <div style="width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, #10b981, #047857); display: flex; align-items: center; justify-content: center; color: white; font-weight: 900; font-size: 1.4rem;">P</div>
    <div>
      <h1 style="font-size: 1.8rem; margin: 0; padding: 0; border: none;">Pace Stock Broking Services</h1>
      <span style="font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">Quantitative & Low-Latency Trading Systems | Campus Hiring 2026</span>
    </div>
  </div>
  <p style="font-size: 0.95rem; color: var(--text-secondary); margin-top: 0.5rem; line-height: 1.6;">
    Comprehensive, mobile-optimized interview preparation suite for the <strong>Software Developer (Quantitative & Low-Latency Trading Systems)</strong> role at Pace Stock Broking Services Pvt. Ltd. CTC: <strong>₹41.00 LPA</strong> | Stipend: <strong>₹75,000/month</strong> | OT: <strong>20th Sept, 7:45 PM @ TIIR</strong>.
  </p>
</div>

<!-- Metrics Bar -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 2rem;">
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px;">
    <span style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Role Applied</span>
    <h4 style="font-size: 1rem; margin: 4px 0 0; color: var(--text-primary);">Software Developer</h4>
    <span style="font-size: 0.75rem; color: #10b981; font-weight: 700;">HFT / Quant Systems</span>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px;">
    <span style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Total CTC</span>
    <h4 style="font-size: 1rem; margin: 4px 0 0; color: var(--text-primary);">₹41.00 LPA</h4>
    <span style="font-size: 0.75rem; color: #10b981; font-weight: 700;">6M Internship + PPO</span>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px;">
    <span style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Monthly Stipend</span>
    <h4 style="font-size: 1rem; margin: 4px 0 0; color: var(--text-primary);">₹75,000 / mo</h4>
    <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600;">6-Month Duration</span>
  </div>
  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px;">
    <span style="font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700;">Online Test (OT)</span>
    <h4 style="font-size: 1rem; margin: 4px 0 0; color: var(--text-primary);">20 Sep · 7:45 PM</h4>
    <span style="font-size: 0.75rem; color: #ef4444; font-weight: 700;">TIIR Lab (165 Mins)</span>
  </div>
</div>

<!-- Modules Grid -->
<h2 style="font-size: 1.3rem; margin-bottom: 1rem;">Preparation Modules</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 2rem;">

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">00: Company & Role Intel</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Strategy</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Executive profile of Pace Stock Broking, HFT/MFT desk operations, exchange co-location topology, and placement intelligence.
    </p>
    <a href="00_START_HERE.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">01: Signature OA Problems</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Algorithms</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      HackerRank test solutions: Monotonic stack contribution technique, DSU graph connectivity, and coin toss probability derivations.
    </p>
    <a href="01_Online_Test.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">02: Low-Latency C++ & OS</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Core Systems</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      vtable/vptr overhead, static CRTP polymorphism, cache line false sharing, alignas(64), and row-major matrix optimization.
    </p>
    <a href="02_Technical_Rounds.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">03: Market Microstructure</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Architecture</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Limit Order Book mechanics, FIFO priority, ITCH/OUCH & FIX protocols, and Solarflare OpenOnload kernel bypass.
    </p>
    <a href="03_Domain_Deep_Dive.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">04: Resume Defense & Traps</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Defense</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Defending Signal Processing M.Tech for HFT, PathMapper 10k cache optimization, Alternative Data Radar, and K-HOG 11x speed.
    </p>
    <a href="04_Candidate_Resume_Grilling.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">05: Limit Order Book LLD</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">System Design</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Complete production C++ Limit Order Book implementation with O(1) order operations and pre-allocated static memory pool.
    </p>
    <a href="05_System_Design_or_HIL.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">06: Life at Pace & Culture</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Behavioral</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Proprietary trading mindset, emergency circuit breakers & kill-switch protocols, and handling high-pressure trading incidents.
    </p>
    <a href="06_Managerial_and_HR.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">07: Caveman Quant CheatSheet</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">CheatSheet</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Latency numbers every programmer must know (L1 to RAM), modern C++ commandments, and mathematical formulas vault.
    </p>
    <a href="07_Quick_Reference.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Module →</a>
  </div>

  <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
      <h3 style="font-size: 1.05rem; font-weight: 700; margin: 0;">3-Day Study Roadmap</h3>
      <span style="font-size: 0.72rem; padding: 2px 8px; border-radius: 6px; background: var(--tag-bg); border: 1px solid var(--tag-border); color: var(--tag-text); font-weight: 700;">Roadmap</span>
    </div>
    <p style="font-size: 0.84rem; color: var(--text-secondary); margin-bottom: 1rem; line-height: 1.5;">
      Structured day-by-day prep plan prioritizing Saturday algorithms/probability and Sunday systems architecture before the OT.
    </p>
    <a href="README.html" style="margin-top: auto; display: inline-flex; align-items: center; justify-content: center; gap: 6px; padding: 8px 14px; border-radius: 8px; background: var(--accent-light); color: var(--accent-primary); text-decoration: none; font-weight: 700; font-size: 0.85rem;">Read Roadmap →</a>
  </div>

</div>
"""

# =============================================================================
# BUILD EXECUTION
# =============================================================================
if __name__ == "__main__":
    print("Generating Pace Stock Broking Interview Preparation Suite...")

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

        full_html = render_pace_page(
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
    index_full_html = render_pace_page(
        title="Overview & Hub · Pace Stock Broking",
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

    print("\nAll Pace Stock Broking interview preparation modules generated successfully!")
