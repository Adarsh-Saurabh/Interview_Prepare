# 01: Signature OA Coding Problems & Online Assessment

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
        std::cout << "Popped sample: Rx Power = " << popped->rx_power_dbm << " dBm
";
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
        std::cout << "No continuous wavelength available.
";
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
    std::cout << "Received 102: Released " << r1.size() << " frames.
";

    auto r2 = reassembler.receive_packet(100, "Payload_100");
    std::cout << "Received 100: Released " << r2.size() << " frames (seq " << r2[0].first << ").
";

    auto r3 = reassembler.receive_packet(101, "Payload_101");
    std::cout << "Received 101: Released " << r3.size() << " frames.
";
    for (const auto& p : r3) {
        std::cout << "  Released seq " << p.first << ": " << p.second << "
";
    }
    return 0;
}
```

---

## 5. Signature Problem 4: Bitwise Transceiver Register Configuration & CRC-8

### Problem Statement
In Nokia optical transceivers, a 32-bit hardware register packs:
* Bits `0..7`: Laser Output Power in units of $0.1\,	ext{dBm}$ (Signed 8-bit).
* Bits `8..11`: Modulation Format (`0`: BPSK, `1`: QPSK, `2`: 16-QAM, `3`: 64-QAM).
* Bits `12..23`: ITU Grid Channel Frequency Index ($12\,	ext{bits}$).
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
        std::cout << "Validated! Power = " << (power / 10.0f) << " dBm, Mod = " << (int)mod << ", Freq = " << freq << "
";
    } else {
        std::cout << "Corrupted register!
";
    }
    return 0;
}
```
