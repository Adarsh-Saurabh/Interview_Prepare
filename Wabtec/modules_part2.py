# modules_part2.py - Wabtec LEAD Modules 03, 04, 05

modules_part2 = {
    "03_Domain_Deep_Dive": {
        "title": "Module 03: Rail Technology, Trip Optimizer & Digital Systems",
        "tag": "Domain",
        "desc": "Positive Train Control (PTC), Trip Optimizer autonomous physics engine, Distributed Power wireless sync, and edge computer vision in rail inspection.",
        "content": """# Module 03: Rail Technology, Trip Optimizer & Digital Systems

To excel in Wabtec interviews, you must demonstrate fluent understanding of the physical-digital intersection: how heavy rail machinery is automated, synchronized, and safeguarded by real-time software.

---

## 1. Positive Train Control (PTC): The Safety Shield

### A. What is PTC?
Positive Train Control is a federally mandated, fail-safe safety system designed to automatically stop a train before human-factor accidents occur. Specifically, PTC prevents:
1. Train-to-train collisions.
2. Derailments caused by excessive speed.
3. Unauthorized train movements into active work zones.
4. Passage through misaligned track switches.

```
+-----------------------------------------------------------------------------------+
|                           PTC ARCHITECTURE & SUBSYSTEMS                           |
+-----------------------------------------------------------------------------------+
| 1. Onboard Segment : Locomotive computer, GPS receiver, wheel tachometer,        |
|                      CAN bus brake interface, and onboard track database.         |
| 2. Wayside Segment : Electronic sensors and transponders monitoring track switches|
|                      and railway signal aspects along the physical tracks.        |
| 3. Comm Segment    : 220 MHz digital wireless radios, cellular, and Wi-Fi.        |
| 4. Back Office     : Central dispatch server dispatching Movement Authorities.     |
+-----------------------------------------------------------------------------------+
```

### B. Fail-Safe Braking Curve Calculation
* The locomotive onboard computer continuously calculates a dynamic **Braking Enforcement Curve**:
  $$ D_{brake} = \frac{V^2}{2 \cdot a_{decel}(W, L, G, B_{pressure})} + V \cdot t_{reaction} + D_{margin} $$
  * $V$: Current train velocity.
  * $W$: Total train weight (can exceed 18,000 tons!).
  * $L$: Train length (up to 2 to 3 miles).
  * $G$: Track grade/elevation (gravity assistance or resistance).
  * $B_{pressure}$: Brake pipe air pressure dynamics.
* If the engineer fails to brake within the warning interval, PTC overrides manual control and commands an **Emergency Air Brake Penalty Application**.

---

## 2. Trip Optimizer: Autonomous Train Cruise Control

### A. The Core Optimization Challenge
A heavy freight train is not a rigid block; it is an elastic chain of 150+ cars connected by couplers (spring draft gears). Improper throttle or brake application causes severe **in-train coupler forces (slack run-in / run-out)**, leading to broken knuckles or derailments.

### B. How Trip Optimizer Works
1. **Inputs**: Track profile (grades, curves, speed limits), train make-up (locomotive horsepower, tonnage per car, empty vs. loaded cars), and scheduled arrival deadline.
2. **Real-Time Physics Simulation**: Computes the optimal speed and fuel curve using dynamic programming and optimal control theory.
3. **Closed-Loop Actuation**: Directly controls the locomotive throttle (Notch 1 to Notch 8) and dynamic electrical brakes without human intervention.
4. **Impact**: Delivers **10% to 15% net fuel savings** across global railroads and reduces carbon emissions by millions of tons annually.

---

## 3. Distributed Power (DP): 2-Mile Wireless Synchronization

```
[Lead Locomotive] ════ (Freight Cars) ════ [Remote Loco 1] ════ (Freight Cars) ════ [Remote Loco 2]
       │                                         │                                        │
       └── Radio Link (450 MHz Telemetry) ───────┴── Radio Link (450 MHz Telemetry) ──────┘
```

* **The Problem**: In ultra-long trains, air brake propagation from the front to the caboose takes up to 30 seconds via pneumatic pipes. Applying brakes only from the front causes rear cars to slam into the front cars.
* **The Solution**: Distributed Power places remote locomotives in the middle and rear of the train. The lead locomotive wirelessly transmits throttle and brake commands to remote engines simultaneously, ensuring instantaneous uniform braking and traction.
* **Software Safety Challenge**: What happens during **Radio Link Loss** inside a mountain tunnel?
  * The remote locomotive runs a deterministic watchdog timer. If telemetry heartbeat is lost for $>45$ seconds, the remote engine safely transitions to idle or initiates automated safe brake application.

---

## 4. Computer Vision & Edge AI in Rail Infrastructure

```
+-----------------------------------------------------------------------------------+
|                         RAILWAY EDGE COMPUTER VISION TASKS                        |
+-----------------------------------------------------------------------------------+
| 1. Pantograph & Catenary Inspection : High-speed line scan cameras verify contact |
|                                       wire height, stagger, and carbon wear.      |
| 2. Track & Rail Defect Detection    : Edge GPUs/accelerators process video feeds  |
|                                       to detect missing fastener clips and cracks.|
| 3. Acoustic Bearing Fault Analysis  : Fast Fourier Transform (FFT) on wayside     |
|                                       microphones to detect hot axle bearings.    |
+-----------------------------------------------------------------------------------+
```

### Candidate Connection (Adarsh Saurabh)
Your M.Tech in Signal and Image Processing and your work on **K-HUKI** (11× faster feature extraction pipeline) and **Warehouse PathMapper** (high-speed routing algorithms) directly position you to contribute to these exact subsystems in the LEAD program!
"""
    },

    "04_Candidate_Resume_Grilling": {
        "title": "Module 04: Candidate Resume Grilling & Project Defense",
        "tag": "Defense",
        "desc": "Anticipated questions, aggressive project grilling, and bulletproof defenses tailored specifically for Adarsh Saurabh's canonical projects.",
        "content": """# Module 04: Candidate Resume Grilling & Project Defense

Wabtec technical interviewers are known to dig deeply into every claim on your resume. Here is your battle-tested defense strategy.

---

## 1. Project 1: IBYD Technology — Warehouse PathMapper (Lead Defense)

### The Elevator Pitch (30 Seconds)
> *"In Warehouse PathMapper, I built a high-performance heuristic routing and spatial mapping engine for dynamic warehouse environments. The system translates physical logistics layout constraints into an optimized graph representation, computing collision-free paths across 10,000×10,000 coordinate grids through 10,000+ points in under 0.5 seconds on standard CPU hardware."*

### Probable Grilling Questions & Rebuttals

#### Q1: "How does a 2D warehouse routing engine relate to railway networks?"
* **Answer**: *"Both problems belong to the domain of constrained spatial routing over discrete topological networks. In warehouse routing, you manage aisle width, turn penalties, and dynamic obstacles. In a railway network, you manage track topology, turnouts/switches, speed restrictions, and train momentum. The core algorithmic challenge—computing minimum-cost paths over large sparse graphs with non-Euclidean turn costs—is identical to Wabtec's dispatch optimization and yard management engines."*

#### Q2: "How did you achieve <0.5s for 10,000 points on an i5 CPU?"
* **Answer**: *"Standard $O(V^2)$ or unoptimized $O(V \log V)$ algorithms fail on a $10,000 \times 10,000$ grid ($10^8$ potential nodes). I introduced three key architectural optimizations:
  1. **Hierarchical Graph Abstraction**: Clustered local walkable aisles into macro-nodes, reducing active search space by over 90%.
  2. **Heuristic Pruning with Euclidean-Manhattan Hybrid**: Used an admissible and consistent heuristic that tightens lower-bound distance estimations.
  3. **Memory-Conscious Flat Arrays**: Replaced nested pointer nodes with contiguous memory 1D arrays, maximizing CPU L1/L2 cache hits and eliminating dynamic heap allocations during path execution."*

---

## 2. Project 2: K-HOG Unsupervised Keyframe Identifier (K-HUKI)

### The Elevator Pitch (30 Seconds)
> *"K-HUKI is an unsupervised visual stream summarization pipeline. It combines Histogram of Oriented Gradients (HOG) feature descriptors with clustering algorithms to condense surveillance/inspection video into essential keyframes with 96.45% accuracy, running 11× faster than deep learning baselines with zero GPU dependency."*

### Probable Grilling Questions & Rebuttals

#### Q1: "Why did you use HOG and Unsupervised Learning instead of YOLO or a fine-tuned ResNet?"
* **Answer**: *"Deep convolutional networks like ResNet-50 require substantial GPU acceleration and consume significant wattage—resources that are severely constrained in edge industrial systems. In railroad condition monitoring (e.g., inspecting overhead catenary wires or rail track beds), algorithms must execute in real time on low-power onboard embedded microprocessors. HOG captures critical structural edges and gradient orientations with minimal CPU cycles, allowing our pipeline to run 11× faster while retaining 96.45% keyframe fidelity."*

#### Q2: "How would this deploy to a Wabtec track inspection car?"
* **Answer**: *"On a track inspection vehicle traveling at 80 km/h, cameras generate hundreds of frames per second. Storing or streaming all raw footage is bandwidth-prohibitive. K-HUKI acts as an edge triage filter: it discards redundant, static rail frames and only flags anomalous frames (e.g., track fractures, misaligned switches, foreign debris) for high-resolution processing and telemetry transmission."*

---

## 3. Project 3: Uplan — Document Intelligence Pipeline

### The Elevator Pitch (30 Seconds)
> *"Uplan is an adversarial multi-agent workflow built with LangGraph and Gemini models to verify complex document compliance. It compresses page metadata into a typed semantic graph (98% token compression) and pairs LLM semantic extraction with deterministic, zero-hallucination mathematical verification engines to reduce verification workload by 85%."*

### Probable Grilling Questions & Rebuttals

#### Q1: "Isn't generative AI too unreliable and hallucinatory for safety-critical railway engineering?"
* **Answer**: *"I completely agree that raw LLMs must never directly control safety-critical actuators or brake systems. In Uplan, we explicitly addressed this by architecting a **hybrid dual-layer validation system**:
  * Layer 1 uses the LLM solely as a semantic extractor to parse unstructured documents into structured JSON schema.
  * Layer 2 passes that data through a **deterministic mathematical rule check engine** where no neural network is involved.
  * In industrial manufacturing and railway maintenance, this architecture ensures that compliance checks against operating standards (like IEEE or EN 50128) remain 100% deterministic and auditable."*

---

## 4. Defending the Dual Background: M.Tech + B.Tech

```
+-----------------------------------------------------------------------------------------+
|                  THE INTERVIEW CLOSER: WHY HIRE ADARSH SAURABH?                         |
+-----------------------------------------------------------------------------------------+
| "Most software applicants only know abstract web stacks and LeetCode problems;          |
|  most hardware applicants only know circuits and control equations.                     |
|  My B.Tech in CSE gives me the high-performance C++, OS, and algorithmic rigor,         |
|  while my M.Tech in Signal Processing gives me the mathematical foundation of           |
|  filtering, real-time sensor processing, and computer vision.                           |
|  In the Wabtec LEAD program, that dual capability means I can contribute immediately     |
|  across embedded firmware, sensor telemetry, and autonomous algorithms."               |
+-----------------------------------------------------------------------------------------+
```
"""
    },

    "05_System_Design_or_HIL": {
        "title": "Module 05: Low-Level Design (LLD) & High-Level System Architecture (HLD)",
        "tag": "Architecture",
        "desc": "Production C++20 Finite State Machine for train signals (LLD) and scalable 10,000-locomotive fleet telemetry platform (HLD).",
        "content": """# Module 05: Low-Level Design (LLD) & High-Level System Architecture (HLD)

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
                  << " -> " << newState->getName() << "\\n";
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
        std::cout << ">>> [VITAL SAFETY ACTION] EMERGENCY BRAKES DEPLOYED! <<\\n";
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
            std::cout << "Warning: Speed exceeded in Green Zone. Sounding cab alarm.\\n";
        }
    }
};

class ApproachYellowState : public TrainSignalState {
public:
    std::string getName() const override { return "APPROACH_YELLOW"; }
    void onSignalAspect(TrainControlContext& ctx, int aspect) override;
    void onSpeedExceeded(TrainControlContext& ctx, double speed) override {
        if (speed > 45.0) {
            std::cout << "Warning: Speed exceeded 45 km/h in Yellow Zone. Penalty countdown initiated.\\n";
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
        std::cout << "Locked in Emergency State until complete stop and dispatcher reset.\\n";
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
        std::cout << "VIOLATION: Passing Red Signal above restriction speed!\\n";
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
* Total Event Volume: $10,000 \times 200 \times 10 = \mathbf{20\text{ Million events/second}}$.
* Telemetry must be ingested, checked for immediate safety anomalies within $<500\text{ ms}$, and archived for predictive fleet maintenance.

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
   Runs sliding time-window aggregations ($30\text{-second windows}$). If bearing temperature exceeds $110^\circ\text{C}$ while wheel vibration variance increases by $3\sigma$, an automated maintenance ticket is generated.
"""
    }
}
