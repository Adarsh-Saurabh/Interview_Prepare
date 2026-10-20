# Module 05: Candidate Resume Grilling & Defensive Strategies

## 1. Candidate Background Defense: M.Tech Signal Processing + B.Tech CSE

As **Adarsh Saurabh** (Roll: `225EC6021`), you hold an exceptionally synergistic combination:
* **M.Tech in Signal and Image Processing (NIT Rourkela, 2025–2027, CGPA: 8.28)**: Provides rigorous mathematical grounding in spatial frequency, 2D continuous/discrete convolution, image gradient orientation, Fourier/Laplace analysis, and structural pattern recognition.
* **B.Tech in Computer Science and Engineering (GGU Bilaspur, 2020–2024, CGPA: 8.5)**: Provides algorithmic optimization, data structures, graph theory, multi-threading, and systems engineering.

### Expected Strategic Trap: "Why apply for Visual Reasoning SME instead of traditional SWE?"
* **Flawed Answer**: *"I just need an internship and this role looked interesting."* (Instant rejection).
* **Winning Pivot**:
  > *"Traditional SWE builds CRUD pipelines; the frontier bottleneck of modern AI is evaluation and multimodal reasoning. In this role, my Signal and Image Processing research background at NIT Rourkela allows me to dissect complex engineering artifacts—schematics, spatial diagrams, and CAD drawings—at the mathematical and structural level. Combined with my B.Tech CSE foundation, I don't just solve problems manually; I can design deterministic programmatic verifiers and synthetic evaluation harnesses that scale Innodata's benchmark throughput for frontier labs."*

---

## 2. Project Defense 1: Uplan — Adversarial Document Intelligence Pipeline

### The Project Reality
* **Stack**: Python, Gemini API, LangGraph, Streamlit.
* **Core Achievement**: Architected an adversarial multi-agent workflow in LangGraph utilizing Gemini 2.5 Pro specialists to check visa document coherence; reduced manual verification workload by 85% with detailed failure rebuttal generation.
* **Key Innovation**: Designed structural encoding system using Gemini 2.0 Flash to compile page-level document metadata into a typed semantic graph (98% token compression) and integrated a zero-hallucination mathematical rule check engine.

### Interview Grilling & Defense
* **Q: "How does Uplan's typed semantic graph translate to Innodata's visual benchmark tasks?"**
  * **Defense**: *"In Uplan, raw document images are filled with high-dimensional noise. Rather than feeding raw OCR dumps into a model, I engineered a structural encoding pipeline that translated visual geometry (headers, signatures, stamps, tables) into typed semantic graph nodes with spatial relational edges (e.g., `ABOVE`, `CONTAINS`, `CROSS_REFERENCES`). This exact paradigm is required when converting CAD blueprints or P&IDs into verified ground-truth DAGs for multimodal AI benchmarking."*
* **Q: "What do you mean by 'zero-hallucination mathematical rule check engine'?"**
  * **Defense**: *"LLMs are notorious for arithmetic drift when computing date durations or balance reconciliations. In Uplan, I decoupled reasoning from calculation: the language model was strictly restricted to extracting symbolic variables into a typed Pydantic schema, while an external deterministic Python rule engine executed all mathematical validations. In benchmark authoring, this ensures that the ground-truth worked proof trace is mathematically irrefutable."*

---

## 3. Project Defense 2: Warehouse PathMapper (IBYD Technology)

### The Project Reality
* **Stack**: Python, Algorithms, Data Analysis.
* **Core Achievement**: Delivered a dynamic warehouse mapping solution as a freelance engagement, translating operational pathfinding needs into a heuristic-based routing system. Scaled the engine to warehouses as large as $10,000 \times 10,000$ units, computing optimal paths through 10,000+ locations in under 0.5s on a standard CPU.

### Interview Grilling & Defense
* **Q: "Innodata evaluates CAD floorplans and architectural layouts. How did you model physical constraints in PathMapper?"**
  * **Defense**: *"A continuous $10,000 \times 10,000$ coordinate grid is too computationally expensive for exhaustive search ($10^8$ cells). I abstracted the physical floorplan into a sparse topological adjacency graph where only allowable transit corridors, rack intersections, and docking gates became vertices. Obstacles, one-way aisle rules, and AGV turning radius clearances were encoded as dynamic edge weights and directional constraints. When benchmarking VLMs on floorplans, this allows me to instantly test whether a model's predicted navigation path violates physical wall boundaries."*

---

## 4. Project Defense 3: K-HUKI (Unsupervised Keyframe Identifier)

### The Project Reality
* **Stack**: Python, Computer Vision, Machine Learning.
* **Core Achievement**: Built keyframe extraction system with HOG (Histogram of Oriented Gradients) features and unsupervised learning achieving 96.45% accuracy; developed preprocessing architecture 11x faster than ResNet-based approaches.

### Interview Grilling & Defense
* **Q: "Why did you choose HOG features over deep learning embeddings like ResNet or ViT?"**
  * **Defense**: *"Deep neural networks like ResNet-50 require heavy matrix multiplications and GPU acceleration, introducing massive latency. HOG captures edge and corner structural orientations directly from image gradient vectors ($\nabla I_x, \nabla I_y$). In industrial diagrams, line geometry and orientation matter far more than texture or semantic color. HOG provided 11x faster preprocessing with zero GPU dependency while capturing the structural contours of the visual artifact with 96.45% accuracy."*
