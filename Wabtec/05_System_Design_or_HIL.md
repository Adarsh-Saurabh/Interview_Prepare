# Module 05: Low-Level Design (LLD) & High-Level System Architecture (HLD)

This module covers the systems architecture challenges frequently presented in Wabtec technical rounds.

---

## Part 1: Low-Level Design (LLD) — Positive Train Control (PTC) Signal State Machine

### Design Requirements
Design a robust, extensible **Finite State Machine (FSM)** in C++20 for an onboard train signaling system:
* States: `CLEAR_GREEN`, `APPROACH_YELLOW`, `RESTRICTED_RED`, `EMERGENCY_BRAKE`.
* Transitions: Event-driven by wayside transponder signals, speed violations, and engineer acknowledgments.
* Pattern: Use the **State Pattern** (GoF) with strict encapsulation.

```cpp
#include <iostream>
#include <memory>
#include <string>

// Forward declaration
class TrainControlContext;

// Abstract State Interface
class TrainSignalState {
public:
    virtual ~TrainSignalState() = default;
    virtual void onSignalAspect(TrainControlContext& ctx, int aspect) = 0;
    virtual void onSpeedExceeded(TrainControlContext& ctx, double speed) = 0;
    virtual std::string getName() const = 0;
};

// Concrete Context
class TrainControlContext {
private:
    std::unique_ptr<TrainSignalState> currentState;
    double currentSpeed = 0.0;
    double maxSpeedLimit = 100.0; // km/h

public:
    TrainControlContext(std::unique_ptr<TrainSignalState> initialState)
        : currentState(std::move(initialState)) {}

    void transitionTo(std::unique_ptr<TrainSignalState> newState) {
        std::cout << "[STATE TRANSITION] " << currentState->getName() 
                  << " -> " << newState->getName() << "\n";
        currentState = std::move(newState);
    }

    void handleSignal(int aspect) { currentState->onSignalAspect(*this, aspect); }
    void handleSpeed(double speed) { 
        currentSpeed = speed; 
        currentState->onSpeedExceeded(*this, speed); 
    }

    void setSpeedLimit(double limit) { maxSpeedLimit = limit; }
    double getSpeedLimit() const { return maxSpeedLimit; }
    void applyEmergencyBrakes() {
        std::cout << ">>> [VITAL SAFETY ACTION] EMERGENCY BRAKES DEPLOYED! <<\n";
    }
};

// Concrete States
class ClearGreenState;
class ApproachYellowState;
class RestrictedRedState;
class EmergencyBrakeState;

class ClearGreenState : public TrainSignalState {
public:
    std::string getName() const override { return "CLEAR_GREEN"; }
    void onSignalAspect(TrainControlContext& ctx, int aspect) override;
    void onSpeedExceeded(TrainControlContext& ctx, double speed) override {
        if (speed > ctx.getSpeedLimit() + 5.0) {
            std::cout << "Warning: Speed exceeded in Green Zone. Sounding cab alarm.\n";
        }
    }
};

class ApproachYellowState : public TrainSignalState {
public:
    std::string getName() const override { return "APPROACH_YELLOW"; }
    void onSignalAspect(TrainControlContext& ctx, int aspect) override;
    void onSpeedExceeded(TrainControlContext& ctx, double speed) override {
        if (speed > 45.0) {
            std::cout << "Warning: Speed exceeded 45 km/h in Yellow Zone. Penalty countdown initiated.\n";
        }
    }
};

class RestrictedRedState : public TrainSignalState {
public:
    std::string getName() const override { return "RESTRICTED_RED"; }
    void onSignalAspect(TrainControlContext& ctx, int aspect) override;
    void onSpeedExceeded(TrainControlContext& ctx, double speed) override;
};

class EmergencyBrakeState : public TrainSignalState {
public:
    std::string getName() const override { return "EMERGENCY_BRAKE"; }
    void onSignalAspect(TrainControlContext& ctx, int aspect) override {
        std::cout << "Locked in Emergency State until complete stop and dispatcher reset.\n";
    }
    void onSpeedExceeded(TrainControlContext& ctx, double speed) override {}
};

// Transition Implementations
void ClearGreenState::onSignalAspect(TrainControlContext& ctx, int aspect) {
    if (aspect == 1) { // Yellow
        ctx.setSpeedLimit(45.0);
        ctx.transitionTo(std::make_unique<ApproachYellowState>());
    } else if (aspect == 2) { // Red
        ctx.setSpeedLimit(15.0);
        ctx.transitionTo(std::make_unique<RestrictedRedState>());
    }
}

void ApproachYellowState::onSignalAspect(TrainControlContext& ctx, int aspect) {
    if (aspect == 0) { // Green
        ctx.setSpeedLimit(100.0);
        ctx.transitionTo(std::make_unique<ClearGreenState>());
    } else if (aspect == 2) { // Red
        ctx.setSpeedLimit(15.0);
        ctx.transitionTo(std::make_unique<RestrictedRedState>());
    }
}

void RestrictedRedState::onSignalAspect(TrainControlContext& ctx, int aspect) {
    if (aspect == 0) {
        ctx.setSpeedLimit(100.0);
        ctx.transitionTo(std::make_unique<ClearGreenState>());
    }
}

void RestrictedRedState::onSpeedExceeded(TrainControlContext& ctx, double speed) {
    if (speed > 15.0) {
        std::cout << "VIOLATION: Passing Red Signal above restriction speed!\n";
        ctx.applyEmergencyBrakes();
        ctx.transitionTo(std::make_unique<EmergencyBrakeState>());
    }
}

int main() {
    TrainControlContext train(std::make_unique<ClearGreenState>());
    train.handleSignal(1); // Transitions to Yellow
    train.handleSignal(2); // Transitions to Red
    train.handleSpeed(25.0); // Violation in Red -> Triggers Emergency Brake!
    return 0;
}
```

---

## Part 2: High-Level System Architecture (HLD) — Scalable Fleet Telemetry & Predictive Analytics Platform (`EdgeLINC`)

### Problem Scenario
Wabtec monitors over **10,000 locomotives** across North America, Australia, and India.
* Each locomotive has **200+ onboard sensors** (engine RPM, oil pressure, motor temperature, vibration, GPS coordinates).
* Sensor sampling rate: 10 Hz per sensor.
* Total Event Volume: $10,000 	imes 200 	imes 10 = \mathbf{20	ext{ Million events/second}}$.
* Telemetry must be ingested, checked for immediate safety anomalies within $<500	ext{ ms}$, and archived for predictive fleet maintenance.

### System Architecture Diagram
```
[10,000 Locomotives]
   │ (Edge Aggregation & Compression via EdgeLINC)
   ▼ (Cellular / SatCom UDP & MQTT)
[API Gateway & Load Balancer Cluster (Envoy)]
   │
   ▼
[Apache Kafka Message Ingestion Layer]
   │ (Partitioned by Locomotive_ID)
   ├───► [Apache Flink Real-Time Anomaly Stream Engine] ──► [Emergency Alert Dispatcher (<500ms)]
   │                                                               │ (WebSockets to Operations Center)
   ▼                                                               ▼
[Kafka Connect Sinks]                                   [Operator Dashboard]
   ├───► [TimescaleDB / InfluxDB (Time-Series Metric Storage - 90 Days Hot)]
   └───► [AWS S3 / Apache Parquet (Long-Term Cold Lake for ML Model Retraining)]
```

### Key Architectural Decisions
1. **Edge Compression at the Locomotive**:
   Locomotives don't send raw floats; they buffer 1-second chunks, apply delta-encoding (saving >70% bandwidth), and transmit via MQTT over TLS.
2. **Kafka Partitioning Strategy**:
   Partition topics strictly by `hash(Locomotive_ID)`. This guarantees that telemetry from a single train is processed in strict chronological order by the downstream Flink worker.
3. **Stream Processing with Apache Flink**:
   Runs sliding time-window aggregations ($30	ext{-second windows}$). If bearing temperature exceeds $110^\circ	ext{C}$ while wheel vibration variance increases by $3\sigma$, an automated maintenance ticket is generated.
