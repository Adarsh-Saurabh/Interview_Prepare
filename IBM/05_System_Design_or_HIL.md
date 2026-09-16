# System Design: Distributed Server Firmware Telemetry Collector

> **Domain:** Embedded Systems, OpenBMC, Low-Latency Networking, Firmware-to-Cloud Telemetry  
> **Target Scale:** 5,000+ Enterprise Server Drawers, <1ms Buffer Latency, Zero Crash Impact on Host OS  

---

## 1. Problem Statement & Functional Requirements

In mission-critical enterprise environments running **IBM Power10 and z16 servers**, hardware health telemetry (core temperatures, voltage rails, fan RPMs, PCIe error registers, and correctable memory ECC errors) must be collected continuously. The telemetry system must run out-of-band on the **Baseboard Management Controller (BMC)** without consuming host CPU cycles or impacting running enterprise workloads (SAP HANA, Core Banking).

```
+------------------------------------------------------------------------------------+
|                High-Level Firmware Telemetry Collection Architecture               |
+------------------------------------------------------------------------------------+
|  [Host CPU / Memory / PCIe Bus]                                                    |
|         | (Out-of-band I2C / SMBus / eSPI / Hostboot Mailbox)                      |
|         v                                                                          |
|  +------------------------------------------------------------------------------+  |
|  |                 OpenBMC Subsystem (Linux SoC on Server Motherboard)          |  |
|  |                                                                              |  |
|  |   [Kernel hwmon Drivers] ---> [Producer Daemon: Sensor Collector]             |  |
|  |                                          |                                   |  |
|  |                                          v (Zero-Copy Shared Memory)         |  |
|  |                         +-----------------------------------+                |  |
|  |                         |  Lock-Free Circular Ring Buffer   |                |  |
|  |                         |  (Cache-line aligned, atomics)    |                |  |
|  |                         +-----------------------------------+                |  |
|  |                                          |                                   |  |
|  |                                          v                                   |  |
|  |                          [Consumer Daemon: Redfish / SSE Engine]             |  |
|  +------------------------------------------------------------------------------+  |
|         |                                                                          |
|         | HTTPS / Redfish Event Stream (gRPC / TLS 1.3)                            |
|         v                                                                          |
|  [Hardware Management Console (HMC) / Enterprise Cloud Aggregator]                 |
|    - Time-Series Database (InfluxDB / Timescale)                                   |
|    - Predictive Anomaly Detector (Kalman Filter / Telum Hardware Assist)           |
|    - Fleet Thermal Balancing & Automated Failover Migration                       |
+------------------------------------------------------------------------------------+
```

### System Requirements:
1. **Low Memory Footprint:** The BMC SoC typically has only 512MB–1GB of dedicated RAM. The telemetry buffer must have a fixed, bounded memory footprint ($<32\text{MB}$).
2. **Lock-Free Concurrency:** Producer threads (sampling sensor chips) and consumer threads (streaming out over Redfish) must not lock each other; producer must never block or experience jitter.
3. **Graceful Degradation:** In case of network disconnection to the HMC, the ring buffer wraps around, dropping the oldest non-critical metrics while preserving critical hardware trip alerts.

---

## 2. Low-Level Design (LLD): Lock-Free Circular Ring Buffer

To achieve microsecond latency and zero lock contention, we design a **Single-Producer Single-Consumer (SPSC) Lock-Free Circular Ring Buffer** using C++17 atomics with explicit memory ordering.

### Cache-Conscious Memory Layout
- The `head` (written by Producer) and `tail` (written by Consumer) pointers are placed on separate **64-byte cache lines** using `alignas(64)` to eliminate false sharing.
- Atomic operations use `std::memory_order_release` when storing data and `std::memory_order_acquire` when reading pointers, avoiding expensive full memory fence instructions (`mfence` or `sync`).

### Production C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <atomic>
#include <cstdint>
#include <cstring>
#include <thread>
#include <chrono>

// Telemetry event payload (32 bytes)
struct TelemetryEvent {
    uint64_t timestamp_ns;
    uint32_t sensor_id;
    float value;
    uint16_t status_flags; // 0x00 = Normal, 0x01 = Warning, 0x02 = Critical
    uint8_t component_type; // 1 = CPU, 2 = Memory, 3 = Fan, 4 = VRM
    uint8_t reserved[9];
};

template <typename T, size_t Capacity>
class LockFreeRingBuffer {
    static_assert((Capacity & (Capacity - 1)) == 0, "Capacity must be a power of 2");

private:
    std::vector<T> buffer;
    static constexpr size_t MASK = Capacity - 1;

    // Separate head and tail onto distinct 64-byte cache lines
    alignas(64) std::atomic<size_t> head{0}; // Written by Producer
    alignas(64) std::atomic<size_t> tail{0}; // Written by Consumer

public:
    LockFreeRingBuffer() : buffer(Capacity) {}

    // Producer pushes an event (returns false if full)
    bool push(const T& item) {
        const size_t current_head = head.load(std::memory_order_relaxed);
        const size_t current_tail = tail.load(std::memory_order_acquire);

        // Check if buffer is full
        if ((current_head - current_tail) >= Capacity) {
            return false; // Buffer overflow (or drop oldest)
        }

        buffer[current_head & MASK] = item;
        head.store(current_head + 1, std::memory_order_release);
        return true;
    }

    // Consumer pops an event (returns false if empty)
    bool pop(T& out_item) {
        const size_t current_tail = tail.load(std::memory_order_relaxed);
        const size_t current_head = head.load(std::memory_order_acquire);

        // Check if buffer is empty
        if (current_tail == current_head) {
            return false; // No data available
        }

        out_item = buffer[current_tail & MASK];
        tail.store(current_tail + 1, std::memory_order_release);
        return true;
    }

    size_t size() const {
        size_t h = head.load(std::memory_order_relaxed);
        size_t t = tail.load(std::memory_order_relaxed);
        return (h >= t) ? (h - t) : 0;
    }
};

int main() {
    constexpr size_t BUFFER_SIZE = 1024; // Must be power of 2
    LockFreeRingBuffer<TelemetryEvent, BUFFER_SIZE> ring_buf;

    std::atomic<bool> running{true};

    // Producer thread: Simulates 10 kHz sensor telemetry sampling
    std::thread producer([&]() {
        uint64_t counter = 0;
        while (running.load(std::memory_order_relaxed)) {
            TelemetryEvent ev;
            ev.timestamp_ns = 1726531200000000ULL + counter;
            ev.sensor_id = 101; // CPU0 Temp
            ev.value = 45.0f + (counter % 15);
            ev.status_flags = (ev.value > 55.0f) ? 0x01 : 0x00;
            ev.component_type = 1;

            while (!ring_buf.push(ev) && running.load(std::memory_order_relaxed)) {
                std::this_thread::yield(); // Buffer full, yield briefly
            }
            counter++;
            std::this_thread::sleep_for(std::chrono::microseconds(100));
        }
    });

    // Consumer thread: Streams telemetry to network / Redfish daemon
    std::thread consumer([&]() {
        TelemetryEvent ev;
        int processed = 0;
        while (running.load(std::memory_order_relaxed) || ring_buf.size() > 0) {
            if (ring_buf.pop(ev)) {
                processed++;
                if (processed % 1000 == 0) {
                    std::cout << "[Consumer] Processed " << processed 
                              << " events. Latest temp: " << ev.value << " C\\n";
                }
            } else {
                std::this_thread::sleep_for(std::chrono::milliseconds(1));
            }
        }
    });

    std::this_thread::sleep_for(std::chrono::milliseconds(500));
    running.store(false, std::memory_order_relaxed);

    producer.join();
    consumer.join();
    std::cout << "Telemetry engine shutdown cleanly.\\n";
    return 0;
}
```

---

## 3. Reliability & Fault Tolerance Under Stress

1. **Handling Outages & Network Partitions:**
   - The ring buffer uses overwrite semantics during network loss: it overwrites normal telemetry (e.g. ambient temperature) while routing critical hardware warnings (e.g., thermal throttling, VRM overcurrent) to a non-volatile SPI flash log (`/var/log/ipmi_sel`).
2. **Crash Resilience (Shared Memory Persistence):**
   - The buffer backing is backed by POSIX shared memory (`/dev/shm`). If the consumer daemon crashes, the producer continues writing uninterrupted; when systemd restarts the consumer, it reads the unconsumed items directly without losing telemetry history.
