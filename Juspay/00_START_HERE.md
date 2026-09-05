# 00: Company & Role Deep Dive ? Juspay Technologies

---

## 1. Juspay Enterprise Architecture & Scale

Juspay is India's preeminent payment orchestration infrastructure company, functioning as a Tier-1 Technology Service Provider (TSP) connecting merchants, payment aggregators, banks, and the National Payments Corporation of India (NPCI).

### 1.1 Scale & Operating Metrics
- **Daily Volume**: 350 Million+ daily digital transactions.
- **Annualized TPV**: Exceeds $1 Trillion Total Payment Volume.
- **System Availability**: 99.999% uptime SLA ("five nines" represents <5.26 minutes of downtime per calendar year across all services).
- **Core Ecosystem Inventions**:
  - Developed the **UPI Common Library SDK** and **BHIM App** in partnership with NPCI.
  - Designed the **UPI Common PIN Page**, serving every single UPI transaction executed across India.
  - Open-Source Foundations: **HyperSwitch** (the "Linux for Payments" written in Rust), **HyperSDK**, **HyperCheckout**.
  - Sovereign Initiatives: **OCEN / HyperCredit** (Open Credit Enablement Network), **ONDC / Namma Yatri** (decentralized open mobility platform powered by the Beckn protocol).

---

## 2. In-House Technology Stack & Centers of Excellence (CoEs)

### 2.1 Functional Programming (PureScript, Haskell, Rust, Clojure)
- **Why Functional Programming?** At $1T TPV, mutable state is an active financial liability. In OOP, mutable object encapsulation permits race conditions and unrepresentable intermediate states.
- **Algebraic Data Types (ADTs)**: Closed sum and product types mathematically restrict business logic to valid states:
  $$\text{PaymentState} = \text{Initialized} \mid \text{PendingGateway}(\text{Ref}) \mid \text{Success}(\text{AuthCode}, \text{BankRef}) \mid \text{Failed}(\text{Err})$$
  No code path can execute a `Success` state without compiler-enforced provision of both `AuthCode` and `BankRef`.
- **Side-Effect Boundary**: Pure mathematical state transitions $f: (\text{State}, \text{Event}) \to (\text{State}, [\text{SideEffects}])$. Network I/O and database mutations are isolated to monad interpreters (`IO` / `Aff`).

### 2.2 KvDB (In-House High-Throughput Write-Back Database)
- **Problem**: Flash sales (e.g., Flipkart Big Billion Days, IRCTC Tatkal surges) generate 100x traffic spikes that instantly saturate traditional relational connection pools and random disk I/O.
- **KvDB Design**:
  - Memory-first write-back architecture.
  - Sub-millisecond latency via append-only memory-mapped Write-Ahead Logs (WAL) replicated across cluster quorum.
  - Asynchronous background flush to cold persistence, ensuring zero customer-facing latency degradation.

### 2.3 Dynamic Routing Core: Control-Theoretic & Bandit Steering
- Published Research: *"A Control-Theoretic Approach to Dynamic Payment Routing for Success Rate Optimization"*.
- Rather than naive moving averages (which introduce catastrophic group delay $\tau_g = \frac{N-1}{2}$), Juspay models payment routing across banking gateways as a **closed-loop feedback control system** (PID + Multi-Armed Bandits).
- Dynamically allocates traffic based on real-time success rate state estimators (Kalman filters), preventing hunting oscillations (thundering herds) across partner banks.

### 2.4 Deep-Tech Flagship Initiatives
1. **Xyne Spaces**:
   - AI-native enterprise workspace unifying fragmented enterprise signals (tickets, pull requests, conversation streams) into an intelligence context layer ("Org Brain").
   - Employs multi-agent orchestration, dynamic semantic knowledge graphs, and deterministic rule validation.
2. **JusTrust**:
   - India's nationwide federated fraud management and digital trust infrastructure.
   - Real-time fraud detection (<100ms scoring budget), edge touch telemetry decomposition, explainable ML models, and autonomous agentic case investigations.
3. **Namma Cloud**:
   - Sovereign cloud infrastructure platform governed by **Namma DSL**, a Rust-based declarative infrastructure language serving as a real-time digital twin of the data center from bare-metal to Kubernetes.

---

## 3. NIT Rourkela On-Campus Selection Pipeline & CTC

### 3.1 Compensation Structure (SDE On-Campus NIT Rourkela)
- **Total Compensation Package**: **?21 LPA to ?27 LPA** (depending on tier and role profile).
  - **Base Salary**: ?13 LPA ? ?16 LPA (direct monthly fixed pay).
  - **Joining / Retention Bonus**: ?2 LPA ? ?3 LPA.
  - **Stock Grants (ESOPs)**: ?6 LPA ? ?8 LPA vested over 4 years.
  - **Internship Stipend (if applicable)**: ?40,000 ? ?50,000 per month.

### 3.2 The 3-Stage Selection Workflow
1. **OA Round 1 (3 Graph DSA Problems, 90 mins)**: Maximum Weight Node, Nearest Meeting Cell, Largest Sum Cycle. 100% test case pass rate required.
2. **OA Round 2 (The Hackathon / Tree of Space, 120-180 mins)**: Thread-Safe N-ary Tree Locking (`lock`, `unlock`, `upgradeLock`) with ancestor and descendant synchronization under concurrent queries.
3. **Technical Round 1 (60 mins)**: Advanced Data Structures, Graph Algorithms, Concurrency, Operating Systems, Thread Safety, Mutexes, Atomic CAS operations.
4. **Technical Round 2 (60 mins)**: LLD & System Design of a Payment Gateway, state machines, idempotency keys, distributed locks (Redis/Redlock), webhook retry policies.
5. **Managerial & Culture Fit (30-45 mins)**: 24/7 payment outage simulations, Samaaj-Sarkaar-Bazaar alignment, extreme ownership.
