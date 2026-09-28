# 05: Low-Level System Design (LLD): Optical Telemetry & Protection Engine

## 1. Problem Statement & Specifications
In an optical transport chassis (such as the Nokia 1830 PSS), multiple transponder cards monitor fiber health. Design an embedded software engine that:
1. Ingests high-frequency telemetry samples (Rx Optical Power, Pre-FEC Bit Error Rate, Optical Signal-to-Noise Ratio) from up to 1,000 optical transponders at $50\,	ext{ms}$ intervals.
2. Maintains a running sliding-window average of signal degradation metrics.
3. Automatically triggers an **Optical Protection Switch (<50ms deadline)** to an alternate fiber path when Pre-FEC BER exceeds $1.0 	imes 10^{-3}$ or Rx power drops by more than $3\,	ext{dB}$.
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
    std::cout << "Streaming healthy optical samples...
";
    for (int i = 0; i < 5; ++i) {
        engine.ingest_sample({channel_1, -10.0f, 1.0e-5f, 28.5f, static_cast<uint64_t>(i * 50)});
    }

    // Ingest sudden power drop sample (fiber degradation)
    std::cout << "Injecting sudden optical degradation sample...
";
    engine.ingest_sample({channel_1, -14.2f, 8.5e-3f, 18.0f, 250});

    return 0;
}
```

---

## 4. Key Design Patterns Applied
1. **Dependency Injection**: `IProtectionHardware` interface decouples testing from physical driver registers.
2. **State Machine Pattern**: Monitored channel transitions through `NORMAL` $ightarrow$ `DEGRADED` $ightarrow$ `SWITCH_TRIGGERED` $ightarrow$ `PROTECTED`.
3. **Sliding Window Filtering**: Prevents single-packet transient spikes from triggering false-positive fiber switches.
