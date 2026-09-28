#!/usr/bin/env python3
"""
build_all_modules.py
Generates all Markdown (.md) and HTML (.html) modules for Nokia
Associate Engineer (Optical Networking) Interview Preparation Portal.
"""

import os
import markdown
from template import render_nokia_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modules_data = {}

# =============================================================================
# MODULE 00: Company & Role Intel
# =============================================================================
modules_data["00_START_HERE"] = {
    "title": "00: Nokia Optical Networks Company & Role Intel",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Nokia Optical Networks Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Nokia Corporation** (Headquartered in Espoo, Finland; global B2B networking and telecommunications innovation leader).
* **Business Unit**: **Network Infrastructure (NI) — Optical Networks**.
* **Global Standing**: Global top-tier market leader in optical transport, high-capacity long-haul, subsea networks, and data center interconnects (DCI).
* **Major Engineering Center**: **Bangalore R&D Hub (Manyata Embassy Business Park)** — core site for optical hardware-software co-design, control plane engineering, high-performance C++ firmware, and AI-driven automation pipelines.
* **The "AI Super Cycle" Driver**: Explosive growth in AI compute clusters (e.g., thousands of GPUs interconnected in AI factories) requires immense data transmission bandwidth. Nokia Optical builds the ultra-high capacity, low-latency coherent optical engines (800G, 1.2T, and 1.6T per wavelength) that feed modern AI data infrastructure.

---

## 2. Core Architecture & Optical Engineering Foundation

Nokia Optical Networks builds solutions that span physical photonics, coherent digital signal processing, embedded control, and cloud-native software:

```
[Cloud Data Centers / AI GPU Clusters]
      │ High-speed Ethernet (400G / 800G Client Interfaces)
      ▼
[Nokia 1830 Photonic Service Switch (PSS) / Optical Transponder]
      │
      ├── Client Optics (QSFP-DD / OSFP Transceivers)
      ├── Embedded Linux Control Plane (C++ / Python / Netconf / YANG)
      │      └── Real-time Telemetry, Protection Switching (<50ms), Fault Recovery
      ├── FPGA / ASIC Hardware Layer (High-speed packet framing, OTN ITU-T G.709)
      ▼
[Nokia PSE-6s / PSE-V Coherent Digital Signal Processor (DSP)]
      │ (Electronic Dispersion Compensation, Carrier Phase Recovery, QAM Modulation)
      ▼
[Optical Line System (OLS) & ROADM Layer]
      │ (Wavelength Selective Switches - WSS, EDFAs, Raman Amplifiers)
      ▼
[Dense Wavelength Division Multiplexing (DWDM) Fiber Network]
(C-Band + L-Band Fibers transmitting 100+ wavelengths simultaneously over thousands of km)
```

### Signature Nokia Optical Technologies to Know:
1. **Nokia 1830 PSS (Photonic Service Switch)**: The flagship optical transport platform deployed by global telcos, cloud hyperscalers, and enterprise data centers.
2. **Nokia PSE-6s (Photonic Service Engine 6s)**: Industry-leading 5nm coherent optical engine capable of driving 1.2 Terabits per second ($1.2\,\text{Tbps}$) on a single wavelength over multi-span metro/regional networks, slashing power-per-bit by 40%.
3. **ROADM (Reconfigurable Optical Add-Drop Multiplexer)**: Software-controlled optical switching nodes that dynamically route individual optical wavelengths without expensive optical-to-electrical-to-optical (O-E-O) conversion.
4. **WaveSuite Software**: Nokia's carrier-grade SDN (Software-Defined Networking) automation platform providing intent-based network control, predictive optical maintenance, and automated path routing.

---

## 3. Placement Drive Specification (NIT Rourkela 2027 Batch)

| Parameter | Drive Specification |
| :--- | :--- |
| **Company** | **Nokia** |
| **Target Role** | **Associate Engineer (Optical Networking)** |
| **Work Location** | **Bangalore (Manyata Embassy Business Park)** |
| **Compensation (CTC)** | **M.Tech:** **₹18.00 LPA**<br>**B.Tech:** **₹16.50 LPA** |
| **Monthly Stipend** | **M.Tech:** **₹55,000 / month**<br>**B.Tech:** **₹50,000 / month** |
| **Internship Duration** | 6-Month Internship leading directly into Full-Time Employment (PPO conversion) |
| **Eligible Batches & Courses** | Batch of 2027: B.Tech & M.Tech (CS, EC, EE, EI) |
| **Eligibility Criteria** | **CGPA $\ge 6.5$**, No active backlogs |
| **Evaluation Process** | 1. Resume Shortlisting<br>2. Online Assessment (HackerEarth/AMCAT)<br>3. Technical Interview Rounds (1–2 rounds)<br>4. Assignment (if required) / Managerial HR |

---

## 4. The 4 Technical Pillars Evaluated at Nokia

```
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     1. High-Performance C++ & OOP     │   │    2. Concurrency & Linux OS Internals│
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • C++11/14/17 Modern Idioms & RAII    │   │ • Multithreading, Pthreads, `std::thread`│
│ • Virtual Tables (`vtable`/`vptr`)    │   │ • Mutexes, Semaphores, Lock-Free Queues│
│ • Object Slicing & Memory Layout      │   │ • Race Conditions & Deadlock Prevention│
│ • Smart Pointers & Custom Allocators  │   │ • Socket Programming & Linux epoll     │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     3. Optical Networking & Systems   │   │   4. Modern AI Tools & CI/CD Pipelines│
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • DWDM, Wavelength Routing & ROADM    │   │ • Python Automation & Test Frameworks │
│ • OTN Framing (ITU-T G.709) & FEC     │   │ • AI-Assisted Architecture & Code PoCs│
│ • Fiber Impairments (Loss, CD, PMD)   │   │ • Automated Validation & Unit Testing │
│ • Coherent Detection & Modulation     │   │ • Git, CMake, GDB, Linux Debugging    │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```
"""
}

# =============================================================================
# MODULE 01: Online Assessment Coding Problems
# =============================================================================
modules_data["01_Online_Test"] = {
    "title": "01: Signature OA Coding Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company & Role Intel",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: C++ & OS Internals",
    "markdown": """# 01: Signature OA Coding Problems & Online Assessment

## 1. Nokia Online Assessment Structure
* **Platform**: Typically hosted on **HackerEarth** or **AMCAT**.
* **Duration**: 90 to 120 minutes.
* **Sections**:
  1. **Quantitative & Logical Reasoning** (15-20 questions): Speed/distance, permutations, probability, series completion, logical flowcharts.
  2. **Technical MCQs** (20-30 questions):
     * *Networking*: OSI layer responsibilities, TCP sliding window, subnetting, ARP/DNS, packet routing.
     * *Operating Systems*: Process scheduling, deadlocks, semaphores vs mutexes, virtual memory paging, cache lines.
     * *C/C++ & OOP*: Pointers, memory allocation (`malloc` vs `new`), virtual inheritance, copy constructor vs move constructor, operator overloading.
  3. **Hands-on Coding Problems** (2 Questions): Medium difficulty algorithmic challenges emphasizing clean memory usage, time complexity, and data structures.

---

## 2. Signature Problem 1: High-Throughput Circular Ring Buffer for Optical Telemetry

### Problem Statement
In Nokia optical transponders, real-time telemetry frames (optical power, laser temperature, bit error rate) arrive continuously at high frequencies from hardware FPGA registers. Design a fixed-size, high-throughput **Circular Ring Buffer** supporting thread-safe push and pop operations with zero dynamic memory allocation during steady state.

### C++ Optimal Solution
```cpp
#include <iostream>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <optional>
#include <chrono>

template <typename T, size_t Capacity>
class OpticalRingBuffer {
private:
    T buffer_[Capacity];
    size_t head_ = 0; // write index
    size_t tail_ = 0; // read index
    size_t count_ = 0;
    mutable std::mutex mtx_;
    std::condition_variable not_full_;
    std::condition_variable not_empty_;

public:
    OpticalRingBuffer() = default;

    // Push optical telemetry frame (blocks if buffer is full)
    bool push(const T& item, std::chrono::milliseconds timeout = std::chrono::milliseconds(50)) {
        std::unique_lock<std::mutex> lock(mtx_);
        if (!not_full_.wait_for(lock, timeout, [this]() { return count_ < Capacity; })) {
            return false; // Buffer overflow / timeout
        }
        buffer_[head_] = item;
        head_ = (head_ + 1) % Capacity;
        ++count_;
        not_empty_.notify_one();
        return true;
    }

    // Pop telemetry frame for processing (blocks if empty)
    std::optional<T> pop(std::chrono::milliseconds timeout = std::chrono::milliseconds(50)) {
        std::unique_lock<std::mutex> lock(mtx_);
        if (!not_empty_.wait_for(lock, timeout, [this]() { return count_ > 0; })) {
            return std::nullopt; // Buffer underflow / timeout
        }
        T item = buffer_[tail_];
        tail_ = (tail_ + 1) % Capacity;
        --count_;
        not_full_.notify_one();
        return item;
    }

    size_t size() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return count_;
    }

    bool is_empty() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return count_ == 0;
    }
};

// Test driver
struct OpticalTelemetry {
    uint32_t channel_id;
    float rx_power_dbm;
    float pre_fec_ber;
};

int main() {
    OpticalRingBuffer<OpticalTelemetry, 1024> telemetry_queue;
    OpticalTelemetry sample{42, -12.4f, 1.2e-4f};
    
    if (telemetry_queue.push(sample)) {
        std::cout << "Pushed telemetry sample for channel " << sample.channel_id << std::endl;
    }
    
    auto popped = telemetry_queue.pop();
    if (popped) {
        std::cout << "Popped sample: Rx Power = " << popped->rx_power_dbm << " dBm\n";
    }
    return 0;
}
```

### Python Implementation
```python
import threading
import time
from typing import Optional, Generic, TypeVar

T = TypeVar("T")

class OpticalRingBuffer(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    def push(self, item: T, timeout: float = 0.05) -> bool:
        with self.not_full:
            if not self.not_full.wait_for(lambda: self.count < self.capacity, timeout=timeout):
                return False
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
            self.count += 1
            self.not_empty.notify()
            return True

    def pop(self, timeout: float = 0.05) -> Optional[T]:
        with self.not_empty:
            if not self.not_empty.wait_for(lambda: self.count > 0, timeout=timeout):
                return None
            item = self.buffer[self.tail]
            self.buffer[self.tail] = None
            self.tail = (self.tail + 1) % self.capacity
            self.count -= 1
            self.not_full.notify()
            return item
```

---

## 3. Signature Problem 2: Optical Routing & Wavelength Assignment (RWA)

### Problem Statement
In a Dense Wavelength Division Multiplexing (DWDM) optical mesh network, each fiber span between two nodes supports $W$ discrete wavelengths (represented as a bitmask where bit $k = 1$ indicates wavelength $k$ is idle). A lightpath between source $S$ and destination $D$ must satisfy the **Wavelength Continuity Constraint** (the exact same wavelength must be reserved across all intermediate spans on the route). Given network adjacency and span wavelength masks, compute the shortest path (minimum hops) that shares at least one common available wavelength, and return the path and chosen wavelength.

### C++ Optimal Solution (BFS with Wavelength Bitmasks)
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

struct Edge {
    int to;
    uint32_t wavelength_mask; // Bit k = 1 means wavelength k is available
};

struct RWAResult {
    bool found;
    int wavelength_id;
    std::vector<int> path;
};

RWAResult solveRWA(int num_nodes, const std::vector<std::vector<Edge>>& graph, int src, int dst, int max_wavelengths) {
    for (int w = 0; w < max_wavelengths; ++w) {
        uint32_t w_bit = (1U << w);
        std::vector<int> parent(num_nodes, -1);
        std::vector<bool> visited(num_nodes, false);
        std::queue<int> q;

        q.push(src);
        visited[src] = true;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            if (curr == dst) {
                // Reconstruct path
                std::vector<int> path;
                for (int at = dst; at != -1; at = parent[at]) {
                    path.push_back(at);
                }
                std::reverse(path.begin(), path.end());
                return {true, w, path};
            }

            for (const auto& edge : graph[curr]) {
                if (!visited[edge.to] && (edge.wavelength_mask & w_bit)) {
                    visited[edge.to] = true;
                    parent[edge.to] = curr;
                    q.push(edge.to);
                }
            }
        }
    }
    return {false, -1, {}};
}

int main() {
    int n = 4;
    std::vector<std::vector<Edge>> graph(n);
    // Node 0 -> 1 with wavelengths 0, 1 (mask: 0b0011 = 3)
    graph[0].push_back({1, 0b0011});
    // Node 1 -> 3 with wavelength 1 (mask: 0b0010 = 2)
    graph[1].push_back({3, 0b0010});
    // Node 0 -> 2 with wavelength 0 (mask: 0b0001 = 1)
    graph[0].push_back({2, 0b0001});
    // Node 2 -> 3 with wavelength 0 (mask: 0b0001 = 1)
    graph[2].push_back({3, 0b0001});

    auto res = solveRWA(n, graph, 0, 3, 4);
    if (res.found) {
        std::cout << "Lightpath established on Wavelength " << res.wavelength_id << ": ";
        for (int node : res.path) std::cout << node << " ";
        std::cout << std::endl;
    } else {
        std::cout << "No continuous wavelength available.\n";
    }
    return 0;
}
```

### Complexity Analysis
* **Time Complexity**: $\mathcal{O}(W \cdot (V + E))$ where $W$ is number of wavelengths, $V$ nodes, $E$ optical spans.
* **Space Complexity**: $\mathcal{O}(V)$ for BFS traversal structures.

---

## 4. Signature Problem 3: Sliding Window Frame Reassembly

### Problem Statement
High-speed optical transponders stripe OTN frames across parallel physical lanes. Packets arrive out of sequence. Given a stream of packets with 32-bit sequence numbers, implement an in-memory reassembly buffer that releases packets strictly in monotonic ascending sequence starting from a baseline `expected_seq`.

### C++ Solution
```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>

class FrameReassembler {
private:
    uint32_t expected_seq_;
    std::unordered_map<uint32_t, std::string> buffer_;

public:
    explicit FrameReassembler(uint32_t initial_seq) : expected_seq_(initial_seq) {}

    std::vector<std::pair<uint32_t, std::string>> receive_packet(uint32_t seq, const std::string& data) {
        std::vector<std::pair<uint32_t, std::string>> in_order_packets;

        if (seq < expected_seq_) {
            // Duplicate or stale frame, drop
            return in_order_packets;
        }

        buffer_[seq] = data;

        // Drain consecutive frames
        while (buffer_.find(expected_seq_) != buffer_.end()) {
            in_order_packets.emplace_back(expected_seq_, buffer_[expected_seq_]);
            buffer_.erase(expected_seq_);
            ++expected_seq_;
        }

        return in_order_packets;
    }
};

int main() {
    FrameReassembler reassembler(100);
    // Arriving out of order: 102, 100, 101
    auto r1 = reassembler.receive_packet(102, "Payload_102");
    std::cout << "Received 102: Released " << r1.size() << " frames.\n";

    auto r2 = reassembler.receive_packet(100, "Payload_100");
    std::cout << "Received 100: Released " << r2.size() << " frames (seq " << r2[0].first << ").\n";

    auto r3 = reassembler.receive_packet(101, "Payload_101");
    std::cout << "Received 101: Released " << r3.size() << " frames.\n";
    for (const auto& p : r3) {
        std::cout << "  Released seq " << p.first << ": " << p.second << "\n";
    }
    return 0;
}
```

---

## 5. Signature Problem 4: Bitwise Transceiver Register Configuration & CRC-8

### Problem Statement
In Nokia optical transceivers, a 32-bit hardware register packs:
* Bits `0..7`: Laser Output Power in units of $0.1\,\text{dBm}$ (Signed 8-bit).
* Bits `8..11`: Modulation Format (`0`: BPSK, `1`: QPSK, `2`: 16-QAM, `3`: 64-QAM).
* Bits `12..23`: ITU Grid Channel Frequency Index ($12\,\text{bits}$).
* Bits `24..31`: CRC-8 checksum over bytes 0, 1, and 2.

Implement encoding, decoding, and CRC-8 validation functions.

### C++ Solution
```cpp
#include <iostream>
#include <cstdint>

uint8_t compute_crc8(const uint8_t* data, size_t len) {
    uint8_t crc = 0x00;
    for (size_t i = 0; i < len; ++i) {
        crc ^= data[i];
        for (int b = 0; b < 8; ++b) {
            if (crc & 0x80)
                crc = (crc << 1) ^ 0x07; // polynomial x^8 + x^2 + x + 1
            else
                crc <<= 1;
        }
    }
    return crc;
}

uint32_t encode_transceiver_register(int8_t power_dbm_x10, uint8_t modulation, uint16_t freq_idx) {
    uint8_t bytes[3];
    bytes[0] = static_cast<uint8_t>(power_dbm_x10);
    bytes[1] = static_cast<uint8_t>((modulation & 0x0F) | ((freq_idx & 0x0F) << 4));
    bytes[2] = static_cast<uint8_t>((freq_idx >> 4) & 0xFF);

    uint8_t crc = compute_crc8(bytes, 3);
    uint32_t reg = bytes[0] | (bytes[1] << 8) | (bytes[2] << 16) | (crc << 24);
    return reg;
}

bool validate_and_decode(uint32_t reg, int8_t& out_power, uint8_t& out_mod, uint16_t& out_freq) {
    uint8_t bytes[3];
    bytes[0] = reg & 0xFF;
    bytes[1] = (reg >> 8) & 0xFF;
    bytes[2] = (reg >> 16) & 0xFF;
    uint8_t received_crc = (reg >> 24) & 0xFF;

    if (compute_crc8(bytes, 3) != received_crc) {
        return false; // Hardware checksum failure
    }

    out_power = static_cast<int8_t>(bytes[0]);
    out_mod = bytes[1] & 0x0F;
    out_freq = ((bytes[1] >> 4) & 0x0F) | (static_cast<uint16_t>(bytes[2]) << 4);
    return true;
}

int main() {
    uint32_t reg = encode_transceiver_register(-30, 2, 192); // -3.0 dBm, 16-QAM, channel 192
    std::cout << "Encoded Register: 0x" << std::hex << reg << std::dec << std::endl;

    int8_t power; uint8_t mod; uint16_t freq;
    if (validate_and_decode(reg, power, mod, freq)) {
        std::cout << "Validated! Power = " << (power / 10.0f) << " dBm, Mod = " << (int)mod << ", Freq = " << freq << "\n";
    } else {
        std::cout << "Corrupted register!\n";
    }
    return 0;
}
```
"""
}

# =============================================================================
# MODULE 02: Core Systems, C++ & OS Internals
# =============================================================================
modules_data["02_Technical_Rounds"] = {
    "title": "02: C++ & OS Internals",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Problems",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Optical Networks & DWDM",
    "markdown": """# 02: Core Systems, Concurrency, C++ Internals & OS

## 1. C++ Language Internals for Systems Engineers

### 1.1 Virtual Tables (`vtable`) & Virtual Pointers (`vptr`)
* **How Polymorphism Works at Assembly Level**:
  * Every class with at least one virtual function has a hidden compiler-generated lookup table called the **vtable**.
  * Each object instance of that class contains a hidden 8-byte pointer (**vptr**) placed at offset 0 pointing to its class's vtable.
  * When calling `obj->process()`, the compiler generates: `(*obj->vptr[index])(obj)`.
* **Cost of Virtual Dispatch**:
  * Additional memory: 8 bytes per object instance (`vptr`) + one static table per polymorphic class (`vtable`).
  * Branch prediction penalty: Indirect jump via function pointer prevents inline optimization and causes CPU pipeline stalls if mispredicted.
* **Why Virtual Destructors are Mandatory**:
  * Deleting a derived class instance through a base pointer (`Base* p = new Derived(); delete p;`) without a virtual destructor causes **Undefined Behavior** and memory leaks (only `~Base()` executes; `~Derived()` is skipped).

### 1.2 Memory Layout & Structure Alignment
* **Memory Alignment Rule**: A variable of size $N$ bytes must reside at a memory address divisible by $N$.
* **Padding Demonstration**:
```cpp
struct UnalignedTransceiver {
    char status;     // 1 byte
    // 3 bytes padding
    int channel_id;  // 4 bytes
    double power;    // 8 bytes
}; // Total: 16 bytes (instead of 13)

struct OptimizedTransceiver {
    double power;    // 8 bytes
    int channel_id;  // 4 bytes
    char status;     // 1 byte
    // 3 bytes padding at end
}; // Total: 16 bytes, but cache lines pack more predictably
```
* **Hardware Cache Line Awareness**: CPU caches transfer data in **64-byte chunks** (cache lines). Group related telemetry fields together to ensure they hit the same L1 cache line.

### 1.3 Move Semantics & RAII
* **Lvalue vs Rvalue**: An lvalue has an identifiable memory location (name/address). An rvalue is a temporary value that does not persist beyond the expression.
* **Move Constructor Idiom**:
```cpp
class TelemetryBuffer {
    float* data_;
    size_t size_;
public:
    // Move Constructor: Steals resources without memory copy
    TelemetryBuffer(TelemetryBuffer&& other) noexcept 
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }
    ~TelemetryBuffer() { delete[] data_; }
};
```
* **Smart Pointers**:
  * `std::unique_ptr`: Zero-cost abstraction over raw pointers. Exclusive ownership.
  * `std::shared_ptr`: Reference-counted ownership. Allocates a **Control Block** (contains ref-count, weak-count, custom deleter). `std::make_shared` combines object and control block into a single contiguous memory allocation for cache locality.
  * `std::weak_ptr`: Non-owning observer that does not increment ref count. Breaks circular reference memory leaks.

---

## 2. Operating Systems, Concurrency & Multithreading

### 2.1 Synchronization Primitives Comparison

| Primitive | Mechanism | Kernel Transition? | Best Used For |
| :--- | :--- | :---: | :--- |
| **Mutex (`std::mutex`)** | Sleeping lock; thread yields CPU if contested | Yes | Long critical sections (>几 microseconds) |
| **Spinlock (`std::atomic_flag`)** | Busy-waits in a tight loop checking condition | No | Ultra-short critical sections (< cache miss time) |
| **Read-Write Lock (`shared_mutex`)** | Multiple concurrent readers, exclusive single writer | Yes | Read-heavy configuration tables |
| **Condition Variable** | Thread sleeps until signaled by another thread | Yes | Producer-Consumer pipelines & queues |

### 2.2 The 4 Coffman Deadlock Conditions & Prevention
1. **Mutual Exclusion**: Resources cannot be shared. (Mitigation: use lock-free read structures where possible).
2. **Hold and Wait**: Thread holding resource A requests resource B. (Mitigation: request all locks atomically via `std::scoped_lock(m1, m2)`).
3. **No Preemption**: Resources cannot be forcibly taken.
4. **Circular Wait**: Cycle in resource dependency graph. (Mitigation: **Global Lock Ordering** — always acquire lock with lower memory address first).

### 2.3 False Sharing & Cache Thrashing
* When two threads on different CPU cores modify two distinct variables that happen to share the same **64-byte cache line**, the MESI cache coherency protocol forces cores to repeatedly invalidate and reload each other's L1 cache lines.
* **Solution**: `alignas(64)` hardware padding:
```cpp
struct alignas(64) WorkerStats {
    uint64_t processed_frames;
};
```

---

## 3. Linux Systems Programming & Networking Sockets

### 3.1 Socket Programming Essentials
```cpp
// Non-blocking TCP server snippet
int server_fd = socket(AF_INET, SOCK_STREAM, 0);
int flags = fcntl(server_fd, F_GETFL, 0);
fcntl(server_fd, F_SETFL, flags | O_NONBLOCK);

sockaddr_in address{};
address.sin_family = AF_INET;
address.sin_addr.s_addr = INADDR_ANY;
address.sin_port = htons(8080);
bind(server_fd, (struct sockaddr*)&address, sizeof(address));
listen(server_fd, 128);
```

### 3.2 `epoll` vs `select`
* `select()`: $\mathcal{O}(N)$ scan over file descriptor set on every event. Limited to 1024 FDs.
* `epoll()`: $\mathcal{O}(1)$ event readiness notifications via Linux kernel red-black tree and ready list. Scalable to $100,000+$ persistent optical device telemetry connections.

### 3.3 Linux Debugging Toolkit
* **GDB**: `gdb ./firmware`, `break main.cpp:45`, `run`, `backtrace full`, `info registers`, `print *transceiver`.
* **Valgrind**: `valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./firmware`.
* **Perf**: `perf record -g ./firmware` followed by `perf report` for CPU profiling and cache miss analysis.
"""
}

# =============================================================================
# MODULE 03: Domain Deep Dive
# =============================================================================
modules_data["03_Domain_Deep_Dive"] = {
    "title": "03: Optical Networks & DWDM",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: C++ & OS Internals",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Resume Defense & Traps",
    "markdown": """# 03: Optical Networks, DWDM & Coherent Technologies

## 1. Physics of Optical Transmission

### 1.1 Total Internal Reflection & Fiber Geometry
* Light guides through optical fiber via **Total Internal Reflection (TIR)** at the core-cladding boundary:
  $$\theta_c = \arcsin\left(\frac{n_{\text{cladding}}}{n_{\text{core}}}\right)$$
* **Single-Mode Fiber (SMF-28)**:
  * Core diameter $\approx 9\,\mu\text{m}$, cladding diameter $= 125\,\mu\text{m}$.
  * Only one electromagnetic spatial mode propagates. Eliminates modal dispersion. Standard for telecom long-haul.
* **Multi-Mode Fiber (MMF)**:
  * Core diameter $= 50\,\mu\text{m}$ or $62.5\,\mu\text{m}$.
  * Multiple light propagation paths. Severe modal dispersion. Restricted to short enterprise distances (<500m).

### 1.2 Optical Transmission Impairments

| Impairment | Physics & Impact | Engineering Solution |
| :--- | :--- | :--- |
| **Attenuation** | Loss of light power over distance due to Rayleigh scattering and OH absorption. (Min loss $\approx 0.2\,\text{dB/km}$ at $1550\,\text{nm}$). | Optical Amplifiers (EDFA, Raman) every 80-100 km. |
| **Chromatic Dispersion (CD)** | Different wavelength spectral components travel at different group velocities, causing pulse spreading. | Coherent Digital Signal Processor (DSP) electronic dispersion compensation (EDC). |
| **Polarization Mode Dispersion (PMD)**| Asymmetry in fiber core causes two orthogonal light polarizations to travel at different speeds (Differential Group Delay - DGD). | Adaptive FIR filters in DSP (Nokia PSE engine). |
| **Non-Linearities (Kerr Effect)**| Refractive index varies with light intensity at high power (Self-Phase Modulation - SPM, Cross-Phase Modulation - XPM, Four-Wave Mixing - FWM). | Constellation shaping, digital back-propagation (DBP), power optimization. |

---

## 2. Dense Wavelength Division Multiplexing (DWDM) & ROADM

### 2.1 The Optical Spectrum
* **C-Band (Conventional)**: $1530\,\text{nm} - 1565\,\text{nm}$ (Lowest attenuation window in silica fiber; aligns with EDFA amplification spectrum).
* **L-Band (Long Wavelength)**: $1565\,\text{nm} - 1625\,\text{nm}$ (Used to double fiber capacity when C-band is saturated).
* **ITU-T Grid**: Standard channel spacing of $50\,\text{GHz}$ (approx $0.4\,\text{nm}$), $100\,\text{GHz}$, or modern **Flex-Grid** (variable $12.5\,\text{GHz}$ increments allowing channel widths from $37.5\,\text{GHz}$ to $150\,\text{GHz}$ tailored to signal baud rates).

### 2.2 ROADM Architecture (Reconfigurable Optical Add-Drop Multiplexer)
* Allows network operators to remotely add, drop, or pass through optical wavelengths at fiber junctions without manual technician intervention.
* **CDC ROADM**:
  * **Colorless**: Any port can accept any wavelength.
  * **Directionless**: Any channel can be routed to any outgoing fiber direction.
  * **Contentionless**: Multiple identical wavelengths can be added/dropped simultaneously on different directions without collision.

---

## 3. Coherent Optical Transmission & Digital Signal Processing (DSP)

### 3.1 The Coherent Revolution
* Early optical transmission used **Direct Detection (On-Off Keying - OOK)**: photodiode simply measured light intensity (presence or absence of photons).
* **Coherent Detection**: Mixes the incoming weak optical signal with a stable local laser called the **Local Oscillator (LO)**:
  * Measures both **Amplitude** and **Phase** of the electromagnetic wave.
  * Employs **Dual-Polarization (DP)**: encodes two independent data streams on horizontal (H) and vertical (V) polarizations of light.
  * Enables high-order modulation schemes: **DP-QPSK** (4 bits/symbol), **DP-16QAM** (8 bits/symbol), and **DP-64QAM** (12 bits/symbol).

### 3.2 The Nokia PSE-6s Engine
* Nokia's **Photonic Service Engine 6s** is fabricated on 5nm process technology.
* Functions executed inside the coherent DSP chip:
  1. **Analog-to-Digital Conversion (ADC)**: Sampling optical waveform at $>130\,\text{GSamples/s}$.
  2. **Electronic Chromatic Dispersion Compensation**: Inverse filtering compensating thousands of ps/nm of dispersion without optical dispersion compensating fibers.
  3. **Polarization Demultiplexing & Equalization**: Multi-tap adaptive FIR filters un-mixing the crossed polarization states.
  4. **Carrier Phase & Frequency Recovery**: Eliminating phase noise between transmitter laser and local oscillator.
  5. **Soft-Decision Forward Error Correction (SD-FEC)**: Iterative decoding running close to the theoretical Shannon capacity limit.

---

## 4. Optical Transport Network (OTN - ITU-T G.709)

* Known as the "Digital Wrapper" for optical networks.
* Provides deterministic framing, multiplexing, client transparency, and end-to-end performance monitoring:
  * **OPU (Optical Payload Unit)**: Wraps raw client signals (e.g. 100GbE, 400GbE).
  * **ODU (Optical Data Unit)**: Provides path monitoring, tandem connection monitoring (TCM), and switching.
  * **OTU (Optical Transport Unit)**: Adds frame alignment bytes and Reed-Solomon / LDPC Forward Error Correction (FEC).
"""
}

# =============================================================================
# MODULE 04: Candidate Resume Grilling
# =============================================================================
modules_data["04_Candidate_Resume_Grilling"] = {
    "title": "04: Resume Defense & Traps",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Optical Networks & DWDM",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: Optical Telemetry LLD",
    "markdown": """# 04: Candidate Resume Defense & Technical Traps

## 1. Candidate Strategic Positioning: Adarsh Saurabh
* **Educational Blend**:
  * **M.Tech in Signal & Image Processing** (NIT Rourkela, CGPA: 8.28)
  * **B.Tech in Computer Science & Engineering** (Guru Ghasidas University, CGPA: 8.5)
* **The Killer Value Proposition for Nokia Optical**:
  > *"Optical networking at Nokia represents the physical meeting point of high-performance Computer Science (low-level C++, concurrency, Linux systems, routing algorithms) and Signal Processing (sampling, Fourier analysis, dispersion equalization, filter design, SNR optimization). My dual background gives me the software rigor to build carrier-grade code and the mathematical DSP foundation to understand coherent optical physical layers."*

---

## 2. Project 1 Defense: Warehouse PathMapper (IBYD Technology)

### The Interview Trap
> *"You built a 2D warehouse routing algorithm for a client. How does warehouse pathfinding have anything to do with optical networks or telecommunications?"*

### The Winning Defense
> *"Both problems fundamentally reduce to **constrained graph optimization under real-time latency deadlines**. In Warehouse PathMapper, I had to route agents through a $10,000 \times 10,000$ spatial grid visiting multiple locations while avoiding dynamic collisions, running in $<0.5$ seconds on an i5 CPU.*
> 
> *In Nokia optical networks, this directly mirrors **Routing and Wavelength Assignment (RWA)** and **Optical Restoration Path Routing**. When an optical fiber cuts, the SDN control plane must find alternate paths across a mesh graph subject to physical constraints: link latency, maximum optical reach, and wavelength continuity (ensuring an identical unused wavelength is available along all intermediate spans). Both systems require cache-friendly memory structures, priority queues, and heuristic pruning to avoid combinatorial explosion."*

### Key Deep-Dive Questions to Prepare:
* **Q: How did you achieve $<0.5$ seconds on a $10,000 \times 10,000$ grid?**
  * *Answer*: *"I used spatial partitioning (spatial hashing / grid bucket lookup) so distance queries operated in $\mathcal{O}(1)$ average time. Instead of recalculating global Dijkstra paths naively, I implemented an A* heuristic with Manhattan/Chebyshev distance bounds and flattened 2D arrays into contiguous 1D memory buffers to maximize CPU L1 cache hits."*

---

## 3. Project 2 Defense: Uplan (Adversarial Document Intelligence)

### The Interview Trap
> *"Uplan is an LLM and multi-agent pipeline. Why are you showing Generative AI on an embedded and optical transport resume?"*

### The Winning Defense
> *"Nokia's JD explicitly specifies: **'Utilizing the latest AI development tools and agile methodologies... develop code in C++/Python and design PoCs using modern AI technologies.'** Modern systems engineering teams use AI tools to accelerate requirements breakdown, generate test harnesses, and automate CI/CD pipelines.*
> 
> *In Uplan, my primary technical contribution was building a **deterministic mathematical rule check engine** and a **typed semantic graph** that compressed document structure by 98% with zero hallucinations. In optical network management, you deal with massive NETCONF/YANG device models and telemetry streaming. The core principles of compiling unstructured device data into typed semantic schemas and performing deterministic constraint checking are identical."*

---

## 4. Project 3 Defense: K-HOG Unsupervised Keyframe Identifier (K-HUKI)

### The Interview Trap
> *"Why did you use traditional HOG features and unsupervised clustering instead of a deep CNN like ResNet?"*

### The Winning Defense
> *"Because of **compute, latency, and hardware deployment constraints**. Deep neural networks like ResNet introduce significant parameter overhead and high inference latency on CPU platforms. By designing a modular, object-oriented pipeline with Histogram of Oriented Gradients (HOG) and unsupervised clustering, I achieved 96.45% accuracy while running **11 times faster** than deep learning alternatives, enabling true real-time stream processing.*
> 
> *In high-speed optical systems, you cannot run heavy neural networks on every telemetry packet arriving at 50ms intervals. You need lightweight, mathematically rigorous feature extraction that operates within microsecond budgets."*

---

## 5. Defense Against the "Optical Background Gap" Trap

### The Interview Trap
> *"Your transcript does not show a specialized optical physics or photonics laboratory course. Why should we hire you over an electronics candidate who studied optical waveguides?"*

### The Winning Defense
> *"Nokia's modern optical solutions are defined by software, embedded systems, and digital signal processing. The physical layer in coherent optics (like Nokia's PSE-6s) is essentially **discrete-time signal processing over physical media** — compensating dispersion with digital FIR filters, carrier recovery via phase-locked loops, and matrix equalization.*
> 
> *My M.Tech curriculum in Signal Processing gives me direct mastery of convolution, Fourier transforms, filter design, and error correction codes. Coupled with my B.Tech in CSE, I write production-quality, multi-threaded C++ that interacts with hardware drivers, handles Linux socket telemetry, and executes without memory leaks. I understand both the mathematics of the signal and the computer architecture running the code."*
"""
}

# =============================================================================
# MODULE 05: System Design & LLD
# =============================================================================
modules_data["05_System_Design_or_HIL"] = {
    "title": "05: Optical Telemetry LLD",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Resume Defense & Traps",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Culture & Values",
    "markdown": """# 05: Low-Level System Design (LLD): Optical Telemetry & Protection Engine

## 1. Problem Statement & Specifications
In an optical transport chassis (such as the Nokia 1830 PSS), multiple transponder cards monitor fiber health. Design an embedded software engine that:
1. Ingests high-frequency telemetry samples (Rx Optical Power, Pre-FEC Bit Error Rate, Optical Signal-to-Noise Ratio) from up to 1,000 optical transponders at $50\,\text{ms}$ intervals.
2. Maintains a running sliding-window average of signal degradation metrics.
3. Automatically triggers an **Optical Protection Switch (<50ms deadline)** to an alternate fiber path when Pre-FEC BER exceeds $1.0 \times 10^{-3}$ or Rx power drops by more than $3\,\text{dB}$.
4. Runs deterministically on embedded Linux without thread contention or memory leaks.

---

## 2. High-Level Architecture & Concurrency Model

```
[Hardware FPGA / Transponder Cards]
         │ High-speed UDP / PCIe streaming
         ▼
[Telemetry Receiver Worker Thread]
         │ Zero-copy enqueue
         ▼
[Lock-Free / Ring Buffer Queue]
         │ Dequeue batch
         ▼
[Telemetry Processing & Analytics Thread]
         ├── Moving Average Calculation (Sliding Window)
         ├── Threshold Evaluation Engine
         │      ├── Rx Power Drop > 3 dB?
         │      └── Pre-FEC BER > 1e-3?
         ▼ (If Threshold Breached)
[Protection Switch Controller State Machine]
         ├── Verify Alternate Backup Path Active
         ├── Issue Hardware Register Switch Command (<50ms)
         └── Emit High-Priority Netconf/SNMP Trap to SDN Controller
```

---

## 3. Production-Grade C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <deque>
#include <memory>
#include <chrono>
#include <mutex>
#include <thread>
#include <atomic>

// Telemetry payload received from optical transceiver
struct alignas(32) OpticalSample {
    uint32_t channel_id;
    float rx_power_dbm;
    float pre_fec_ber;
    float osnr_db;
    uint64_t timestamp_ms;
};

// Interface for Hardware Protection Switch
class IProtectionHardware {
public:
    virtual ~IProtectionHardware() = default;
    virtual bool trigger_switch(uint32_t channel_id, const std::string& reason) = 0;
};

class MockProtectionHardware : public IProtectionHardware {
public:
    bool trigger_switch(uint32_t channel_id, const std::string& reason) override {
        std::cout << "[HARDWARE PROTECTION SWITCH ACTIVATED] Channel " << channel_id 
                  << " switched to backup fiber! Reason: " << reason << std::endl;
        return true;
    }
};

// Channel Health Monitor with Sliding Window
class ChannelMonitor {
private:
    uint32_t channel_id_;
    const size_t window_size_;
    std::deque<OpticalSample> window_;
    float baseline_power_ = 0.0f;
    bool has_baseline_ = false;
    bool is_switched_ = false;

    // Thresholds
    const float MAX_BER_THRESHOLD = 1e-3f;
    const float POWER_DROP_LIMIT_DB = 3.0f;

public:
    ChannelMonitor(uint32_t channel_id, size_t window_size = 10)
        : channel_id_(channel_id), window_size_(window_size) {}

    bool evaluate_sample(const OpticalSample& sample, IProtectionHardware& hardware) {
        if (is_switched_) return false; // Already switched

        if (!has_baseline_) {
            baseline_power_ = sample.rx_power_dbm;
            has_baseline_ = true;
        }

        window_.push_back(sample);
        if (window_.size() > window_size_) {
            window_.pop_front();
        }

        // Compute running average of Pre-FEC BER
        float ber_sum = 0.0f;
        for (const auto& s : window_) {
            ber_sum += s.pre_fec_ber;
        }
        float avg_ber = ber_sum / window_.size();

        // Check 1: Sudden optical power drop (fiber bending or cut)
        if ((baseline_power_ - sample.rx_power_dbm) > POWER_DROP_LIMIT_DB) {
            is_switched_ = true;
            return hardware.trigger_switch(channel_id_, "Rx Optical Power Drop > 3 dB");
        }

        // Check 2: Pre-FEC BER degradation beyond correction capability
        if (avg_ber > MAX_BER_THRESHOLD) {
            is_switched_ = true;
            return hardware.trigger_switch(channel_id_, "Pre-FEC BER Exceeded Threshold");
        }

        return false;
    }

    uint32_t channel_id() const { return channel_id_; }
};

// Real-Time Optical Telemetry Processing Engine
class OpticalTelemetryEngine {
private:
    std::unordered_map<uint32_t, std::unique_ptr<ChannelMonitor>> channels_;
    std::shared_ptr<IProtectionHardware> hardware_;
    std::mutex mtx_;

public:
    explicit OpticalTelemetryEngine(std::shared_ptr<IProtectionHardware> hw)
        : hardware_(std::move(hw)) {}

    void register_channel(uint32_t channel_id) {
        std::lock_guard<std::mutex> lock(mtx_);
        channels_[channel_id] = std::make_unique<ChannelMonitor>(channel_id);
    }

    void ingest_sample(const OpticalSample& sample) {
        std::lock_guard<std::mutex> lock(mtx_);
        auto it = channels_.find(sample.channel_id);
        if (it != channels_.end()) {
            it->second->evaluate_sample(sample, *hardware_);
        }
    }
};

int main() {
    auto hardware = std::make_shared<MockProtectionHardware>();
    OpticalTelemetryEngine engine(hardware);

    uint32_t channel_1 = 101;
    engine.register_channel(channel_1);

    // Ingest healthy optical samples
    std::cout << "Streaming healthy optical samples...\n";
    for (int i = 0; i < 5; ++i) {
        engine.ingest_sample({channel_1, -10.0f, 1.0e-5f, 28.5f, static_cast<uint64_t>(i * 50)});
    }

    // Ingest sudden power drop sample (fiber degradation)
    std::cout << "Injecting sudden optical degradation sample...\n";
    engine.ingest_sample({channel_1, -14.2f, 8.5e-3f, 18.0f, 250});

    return 0;
}
```

---

## 4. Key Design Patterns Applied
1. **Dependency Injection**: `IProtectionHardware` interface decouples testing from physical driver registers.
2. **State Machine Pattern**: Monitored channel transitions through `NORMAL` $\rightarrow$ `DEGRADED` $\rightarrow$ `SWITCH_TRIGGERED` $\rightarrow$ `PROTECTED`.
3. **Sliding Window Filtering**: Prevents single-packet transient spikes from triggering false-positive fiber switches.
"""
}

# =============================================================================
# MODULE 06: Managerial & HR
# =============================================================================
modules_data["06_Managerial_and_HR"] = {
    "title": "06: Culture & Values",
    "prev_link": "05_System_Design_or_HIL.html",
    "prev_title": "05: Optical Telemetry LLD",
    "next_link": "07_Quick_Reference.html",
    "next_title": "07: Optical CheatSheet",
    "markdown": """# 06: Nokia Culture, Values & Behavioral Interview Defense

## 1. Nokia Core Culture & The Nokia Essentials
Nokia's corporate ethos is structured around 3 core behaviors called **The Nokia Essentials**:
1. **Open**: We respect each other and are open to diverse ideas and constructive debate. We communicate with transparency.
2. **Fearless**: We take bold risks, challenge the status quo, and learn rapidly from failures. We reject complacency.
3. **Empowered**: We take ownership, make decisions with accountability, and execute autonomously to deliver customer value.

---

## 2. Signature Behavioral Questions & Tailored STAR Responses

### Question 1: "Why Nokia, and specifically why our Optical Networking team in Bangalore?"
* **Context**: Align personal strengths with Nokia's mission.
* **Model Answer**:
  > *"Nokia is one of the few true engineering institutions pioneering the physical and software backbone of global connectivity. The Optical Networking team is at the epicenter of the AI revolution — building the high-speed coherent optics and 1830 PSS transport nodes that allow hyperscale data centers and telecom operators to move Petabits of data efficiently.*
  > 
  > *With my dual background in M.Tech Signal Processing at NIT Rourkela and B.Tech in CSE, optical networks is the ideal domain where my software engineering, low-level systems programming, and signal processing skills directly intersect. The opportunity to work alongside world-class architects on the next generation of PSE engines in Bangalore is where I want to build my career."*

### Question 2: "Tell me about a time you handled ambiguous requirements in a technical project."
* **Situation**: In my freelance engagement for **IBYD Technology (Warehouse PathMapper)**, the client had an operational warehouse routing issue but no technical specifications, formal API contracts, or mathematical bounds.
* **Task**: Define the algorithmic scope, design the data structure, and deliver an interactive routing system under tight turnaround.
* **Action**: I scheduled structured discovery discussions to identify the exact constraint: real-time routing across grids up to $10,000 \times 10,000$ in sub-second time. I built rapid iterative prototypes, demonstrating path simulations on video, gathered continuous feedback, and refined the heuristic pruning.
* **Result**: Delivered a solution computing optimal paths through 10,000+ locations in under 0.5 seconds on an ordinary laptop CPU, exceeding client expectations.

### Question 3: "Have you ever had a disagreement with a teammate or mentor regarding a technical choice?"
* **Situation**: During my **Autobot Robotics** internship, we were selecting the model architecture for a robotics vision pipeline. A team member advocated deploying a heavy deep CNN model.
* **Task**: Ensure the robot could process visual input at 30+ FPS without overheating the embedded onboard compute board.
* **Action**: Instead of an opinionated debate, I set up a quantitative benchmarking test. I profiled latency, memory footprint, and frame throughput between the heavy model and a lightweight feature extraction pipeline. The benchmark clearly demonstrated that the heavier model throttled the CPU and caused frame drops.
* **Result**: We collaboratively agreed on an optimized, lightweight model that achieved the target accuracy while maintaining smooth real-time execution. We delivered the project ahead of schedule.

### Question 4: "Tell me about a time you failed or made a mistake in code. What did you learn?"
* **STAR Response**: Mention an early multithreaded debugging experience with race conditions or dangling pointers, explaining how learning to use GDB and Valgrind taught you defensive programming, RAII, and thread safety.

---

## 3. High-Impact Questions to Ask the Nokia Interviewer
1. *"How is the Optical Networking team currently integrating modern AI tooling into the verification and FPGA validation pipeline for next-gen transponders?"*
2. *"With the rollout of the 5nm PSE-6s chipset, what are the primary software control plane challenges in managing flex-grid spectrum allocation dynamically?"*
3. *"What does a successful first 6 months look like for an Associate Engineer joining the Bangalore Optical team?"*
"""
}

# =============================================================================
# MODULE 07: Quick Reference & CheatSheet
# =============================================================================
modules_data["07_Quick_Reference"] = {
    "title": "07: Optical CheatSheet",
    "prev_link": "06_Managerial_and_HR.html",
    "prev_title": "06: Culture & Values",
    "next_link": "README.html",
    "next_title": "Study Roadmap",
    "markdown": """# 07: Optical Networks & Systems Engineering Quick Reference

## 1. Optical Network Equations & Formulas

| Metric | Formula / Relationship | Practical Meaning |
| :--- | :--- | :--- |
| **Decibel (dB)** | $\text{Loss/Gain (dB)} = 10 \log_{10}\left(\frac{P_{\text{out}}}{P_{\text{in}}}\right)$ | $3\,\text{dB} \approx$ half/double power; $10\,\text{dB} = 10\times$; $20\,\text{dB} = 100\times$. |
| **Power in dBm** | $P_{\text{dBm}} = 10 \log_{10}\left(\frac{P_{\text{mW}}}{1\,\text{mW}}\right)$ | $0\,\text{dBm} = 1.0\,\text{mW}$; $-10\,\text{dBm} = 0.1\,\text{mW}$; $+20\,\text{dBm} = 100\,\text{mW}$. |
| **Fiber Link Budget** | $P_{\text{Rx}} = P_{\text{Tx}} - (\alpha \cdot L + N_{\text{splice}} \cdot L_{\text{splice}} + M)$ | Ensures received optical power is above transceiver sensitivity. |
| **Shannon-Hartley Capacity** | $C = B \log_2(1 + \text{SNR})$ | Maximum theoretical error-free data rate over noisy channel. |
| **Chromatic Dispersion Delay** | $\Delta \tau = D \cdot L \cdot \Delta \lambda$ | Pulse spreading ($D \approx 17\,\text{ps/(nm}\cdot\text{km)}$ for SMF-28 at $1550\,\text{nm}$). |

---

## 2. Essential Optical Acronyms

* **DWDM**: Dense Wavelength Division Multiplexing
* **ROADM**: Reconfigurable Optical Add-Drop Multiplexer
* **WSS**: Wavelength Selective Switch
* **OTN**: Optical Transport Network (ITU-T G.709)
* **FEC**: Forward Error Correction (Reed-Solomon, LDPC)
* **BER**: Bit Error Rate (Pre-FEC and Post-FEC)
* **OSNR**: Optical Signal-to-Noise Ratio
* **EDFA**: Erbium-Doped Fiber Amplifier
* **QAM**: Quadrature Amplitude Modulation
* **LO**: Local Oscillator Laser

---

## 3. C++ Modern Systems CheatSheet

```cpp
// RAII Lock Guard
std::lock_guard<std::mutex> lock(mtx);

// Scoped Multi-Lock (Deadlock-Free)
std::scoped_lock lock(mtx1, mtx2);

// Unique Pointer with Custom Deleter
std::unique_ptr<int, void(*)(int*)> ptr(new int(10), [](int* p){ delete p; });

// Hardware Memory Alignment (False Sharing Prevention)
struct alignas(64) PerCoreCounter {
    std::atomic<uint64_t> counter{0};
};

// Check if move constructor is noexcept
static_assert(std::is_nothrow_move_constructible<MyClass>::value, "Must be noexcept");
```

---

## 4. Linux CLI Diagnostics CheatSheet

```bash
# GDB Basics
gdb ./app
(gdb) break main
(gdb) run
(gdb) backtrace full
(gdb) info threads
(gdb) thread apply all bt

# Memory Leaks
valgrind --leak-check=full ./app

# Network Interface & Sockets
netstat -tulpn          # List listening ports
ethtool eth0            # Physical link speed & duplex
ss -s                   # Socket summary statistics
ip route show           # Routing table

# System Profiling
top -H -p <PID>         # Monitor individual thread CPU usage
perf top                # Real-time kernel & userspace hotspots
```
"""
}

# =============================================================================
# MODULE: README (Roadmap)
# =============================================================================
modules_data["README"] = {
    "title": "3-Day Study Roadmap · Nokia Optical Prep",
    "prev_link": "07_Quick_Reference.html",
    "prev_title": "07: Optical CheatSheet",
    "next_link": "index.html",
    "next_title": "Overview & Hub",
    "markdown": """# 3-Day Intensive Study Roadmap: Nokia Associate Engineer

This tactical checklist guides your 72-hour sprint before the Nokia OA and Technical Interviews.

---

## Day 1: C++, Concurrency & Systems Fundamentals
- [ ] Review C++ Virtual Tables, memory alignment, padding, and smart pointers in [Module 02](02_Technical_Rounds.html).
- [ ] Implement and dry-run the **Circular Ring Buffer** from [Module 01](01_Online_Test.html).
- [ ] Understand Mutex vs Spinlock vs Condition Variable and the 4 Coffman deadlock conditions.
- [ ] Review POSIX socket creation, non-blocking sockets, and `epoll()` readiness mechanics.

---

## Day 2: Optical Networking Domain & Resume Defense
- [ ] Study Optical Transmission Fundamentals (SMF vs MMF, Attenuation, Dispersion, WDM) in [Module 03](03_Domain_Deep_Dive.html).
- [ ] Master the difference between Direct Detection and Coherent Detection (Nokia PSE-6s).
- [ ] Memorize the winning defenses for **Warehouse PathMapper**, **Uplan**, and **K-HUKI** in [Module 04](04_Candidate_Resume_Grilling.html).
- [ ] Practice explaining your M.Tech Signal Processing + B.Tech CSE dual background pitch.

---

## Day 3: System Design, OA Mock & Behavioral
- [ ] Walk through the **Optical Telemetry & Protection Switch LLD** in [Module 05](05_System_Design_or_HIL.html).
- [ ] Solve the **RWA Wavelength Routing** algorithm problem from [Module 01](01_Online_Test.html).
- [ ] Practice the 3 Nokia Essentials and behavioral STAR answers in [Module 06](06_Managerial_and_HR.html).
- [ ] Quick review of optical formulas and Linux GDB commands in [Module 07](07_Quick_Reference.html).
"""
}

# =============================================================================
# INDEX HUB PAGE
# =============================================================================
index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: inline-block; padding: 4px 12px; background: rgba(18, 65, 145, 0.12); border: 1px solid #124191; border-radius: 9999px; font-size: 0.85rem; font-weight: 700; color: #124191; margin-bottom: 0.75rem;">
    ON-CAMPUS RECRUITMENT · NIT ROURKELA 2027
  </div>
  <h1 style="font-size: 2.2rem; font-weight: 800; margin: 0 0 0.5rem 0; letter-spacing: -0.02em;">
    Nokia Optical Networks Preparation Portal
  </h1>
  <p style="font-size: 1.05rem; color: var(--text-muted); margin: 0;">
    Role: <strong>Associate Engineer (Optical Networking)</strong> · Bangalore R&D Center<br>
    Package: <strong>M.Tech: ₹18.00 LPA</strong> (₹55K/mo Stipend) · <strong>B.Tech: ₹16.50 LPA</strong> (₹50K/mo Stipend)
  </p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-bottom: 2.5rem;">
  <a href="00_START_HERE.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company & Role Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Nokia Optical, 1830 PSS, PSE-6s coherent DSP, and hiring drive evaluation parameters.</p>
    </div>
  </a>

  <a href="01_Online_Test.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">OA Coding Problems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">4 Signature OA problems: Circular ring buffer, RWA routing, sliding window reassembly, and bitwise registers.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">C++ & OS Internals</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Virtual tables, memory layout, alignment, move semantics, multithreading, mutexes, epoll, and GDB.</p>
    </div>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Optical Networks & DWDM</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Fiber physics, chromatic dispersion, DWDM, ROADM, coherent detection, QAM, and OTN framing.</p>
    </div>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense & Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending Warehouse PathMapper, Uplan AI tools, K-HUKI DSP, and M.Tech Signal Processing background.</p>
    </div>
  </a>

  <a href="05_System_Design_or_HIL.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Optical Telemetry LLD</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Real-time telemetry ingestion, sliding window degradation analysis, and sub-50ms protection switching.</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Culture & Values</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Nokia Essentials (Open, Fearless, Empowered), STAR behavioral answers, and high-impact questions.</p>
    </div>
  </a>

  <a href="07_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Optical CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Formulas, dB/dBm conversions, Shannon limit, C++ concurrency idioms, and Linux CLI diagnostics.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #124191; text-transform: uppercase;">Roadmap</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Study Sprint</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Structured hour-by-hour preparation schedule and readiness checklist.</p>
    </div>
  </a>
</div>
"""

# =============================================================================
# BUILD LOOP
# =============================================================================
def main():
    print("Building all Nokia Interview Preparation modules...")

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

        full_html = render_nokia_page(
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
    index_full_html = render_nokia_page(
        title="Overview & Hub · Nokia Optical Interview Preparation",
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

    print("\nAll Nokia interview preparation modules generated successfully!")

if __name__ == "__main__":
    main()
