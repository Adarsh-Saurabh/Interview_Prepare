# Module 07: Rapid Recall CheatSheet & Technical Flash Cards

Keep this quick-reference sheet open for 10-minute rapid recall before entering your online test or interview round.

---

## 1. C++20 Core Rules Flash Sheet

```
+-----------------------------------------------------------------------------------------+
|                                  C++ RAPID RECALL                                       |
+-----------------------------------------------------------------------------------------+
| Virtual Destructors | ALWAYS mark base class destructor 'virtual' if class has virtual  |
|                     | methods, otherwise deleting derived via base pointer leaks derived|
|                     | member variables!                                                 |
| vtable & vptr       | vptr is 8 bytes at offset 0 of the object; points to array of     |
|                     | function pointers (vtable). Overhead: 1 indirect dereference.     |
| unique_ptr<T>       | sizeof(unique_ptr) == sizeof(raw pointer). Zero overhead. Move    |
|                     | only (deleted copy constructor). Use std::make_unique<T>().       |
| shared_ptr<T>       | 16 bytes: 8 bytes ptr + 8 bytes ptr to control block (atomic ref  |
|                     | count + weak count + custom deleter). Overhead: atomic ops.       |
| Rule of 5           | If you define Destructor, also define: Copy Constructor,          |
|                     | Copy Assignment, Move Constructor, Move Assignment.               |
| static_cast vs      | static_cast: Compile-time check (fast, no RTTI).                  |
| dynamic_cast        | dynamic_cast: Runtime type check (safe, requires RTTI/vtable, slow)|
+-----------------------------------------------------------------------------------------+
```

---

## 2. OS & RTOS Formulas CheatSheet

* **Rate Monotonic Scheduling (RMS) Utilization**:
  $$ U = \sum_{i=1}^{N} rac{C_i}{T_i} \le N (2^{1/N} - 1) $$
  * $N = 1 \implies 100\%$
  * $N = 2 \implies 82.8\%$
  * $N = 3 \implies 77.9\%$
  * $N 	o \infty \implies 69.3\%$
* **Earliest Deadline First (EDF) Utilization**:
  $$ U = \sum_{i=1}^{N} rac{C_i}{T_i} \le 1.0 \quad (100\%) $$
* **Deadlock 4 Conditions**: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.
* **Context Switch**: Thread switch does NOT flush the TLB. Process switch FLUSHES the TLB.

---

## 3. CAN Bus (Controller Area Network) Quick Spec

* **Two-Wire Differential**: $	ext{CAN\_High}$ and $	ext{CAN\_Low}$.
* **Bit States**:
  * **Dominant (Logic 0)**: $	ext{CAN\_H} pprox 3.5	ext{V}$, $	ext{CAN\_L} pprox 1.5	ext{V}$ ($\Delta V pprox 2.0	ext{V}$). Overrides recessive!
  * **Recessive (Logic 1)**: Both lines at $2.5	ext{V}$ ($\Delta V pprox 0	ext{V}$).
* **Arbitration**: Lowest ID number has the most leading dominant zeros, winning the bus without losing a single bit!

---

## 4. Adarsh Saurabh: Verified Project Metrics Flash Sheet

| Project | Core Domain | Key Metric 1 | Key Metric 2 | Architecture |
| :--- | :--- | :--- | :--- | :--- |
| **Warehouse PathMapper** | Heuristic Graph Routing | **10,000×10,000 Grid** | **<0.5s Compute Time** on i5 CPU | Flat 1D Cache Arrays, Euclidean-Manhattan Hybrid |
| **K-HUKI** | Computer Vision / Signals | **11× Faster** than ResNet | **96.45% Accuracy** in keyframe extraction | HOG Features + Unsupervised Clustering |
| **Uplan** | Multi-Agent / AI Safety | **85% Manual Reduction** in verification | **98% Token Compression** into typed graph | LangGraph, Gemini 2.5 Pro + Math Rule Engine |

---

## 5. Compensation & Program Fast Facts

* **Role**: Leadership Expertise & Accelerated Development (LEAD) Program
* **Fixed CTC**: **₹15.50 LPA (CS & EC)** | ₹14.50 LPA (ME & EE)
* **Variable**: 7.5% annual performance bonus (~₹1.16 LPA)
* **Monthly In-Hand**: **~₹1,05,000 / month** net after tax & PF
* **Location**: Bengaluru (WITEC)
* **Structure**: 2 Years, 4 Rotations (6 months each), roll-off to Lead Engineer.
