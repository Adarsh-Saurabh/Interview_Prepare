# Module 04: Candidate Resume Grilling & Project Defense

Wabtec technical interviewers are known to dig deeply into every claim on your resume. Here is your battle-tested defense strategy.

---

## 1. Project 1: IBYD Technology — Warehouse PathMapper (Lead Defense)

### The Elevator Pitch (30 Seconds)
> *"In Warehouse PathMapper, I built a high-performance heuristic routing and spatial mapping engine for dynamic warehouse environments. The system translates physical logistics layout constraints into an optimized graph representation, computing collision-free paths across 10,000×10,000 coordinate grids through 10,000+ points in under 0.5 seconds on standard CPU hardware."*

### Probable Grilling Questions & Rebuttals

#### Q1: "How does a 2D warehouse routing engine relate to railway networks?"
* **Answer**: *"Both problems belong to the domain of constrained spatial routing over discrete topological networks. In warehouse routing, you manage aisle width, turn penalties, and dynamic obstacles. In a railway network, you manage track topology, turnouts/switches, speed restrictions, and train momentum. The core algorithmic challenge—computing minimum-cost paths over large sparse graphs with non-Euclidean turn costs—is identical to Wabtec's dispatch optimization and yard management engines."*

#### Q2: "How did you achieve <0.5s for 10,000 points on an i5 CPU?"
* **Answer**: *"Standard $O(V^2)$ or unoptimized $O(V \log V)$ algorithms fail on a $10,000 	imes 10,000$ grid ($10^8$ potential nodes). I introduced three key architectural optimizations:
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
