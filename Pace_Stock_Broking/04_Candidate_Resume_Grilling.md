# 04: Adarsh Saurabh — Resume Defense & Traps

## 1. Bridging Signal Processing to Quantitative Low-Latency HFT

### The Interviewer's Skeptical Opening Question:
> *"Your Master's degree from NIT Rourkela is in Signal and Image Processing. Pace is a high-frequency algorithmic trading desk. Why shouldn't we hire a pure Financial Engineering or Computer Science graduate instead?"*

### Adarsh's Winning Defense Strategy:
1. **Tick Data IS a High-Frequency Discrete Signal:**
   * Financial market tick feeds are non-stationary, noisy, discrete-time stochastic signals sampled at microsecond intervals.
   * Core concepts in Signal Processing—such as **Discrete Fourier Transforms (DFT)**, **Kalman Filters (state estimation from noisy sensors)**, **Autoregressive Moving Average (ARMA)**, and **Convolutional Feature Extraction**—are the exact mathematical foundations used by quantitative alpha researchers to model price momentum and order flow imbalance.
2. **Dual Foundation Advantage:**
   * B.Tech in CSE (GGU Bilaspur, 8.5 CGPA): Mastery of Operating Systems, Memory Architecture, Compilers, and C++ Data Structures.
   * M.Tech in Signal Processing (NIT Rourkela, 8.28 CGPA): Advanced Linear Algebra, Matrix Decompositions (SVD, Eigenvalues), and numerical algorithm optimization.

---

## 2. Deep Project Defense: Warehouse PathMapper (IBYD Technology)

### The Likely Interrogation:
> *"You claim you scaled spatial routing to $10,000 \times 10,000$ unit spaces for 10,000+ coordinates simultaneously in under 0.5 seconds on an ordinary single CPU core. How is that possible without running out of RAM or cache thrashing?"*

### Architectural Explanation:
1. **1D Contiguous Memory Layout Over Pointer Graphs:**
   * Standard graph implementations use pointer-based adjacency lists (`vector<vector<Node*>>`). On a $10,000 \times 10,000$ grid ($10^8$ cells), node pointers alone would consume $>800\,\text{MB}$ of heap, resulting in pointer chasing and L3 cache thrashing.
   * PathMapper formatted coordinates into a flat 1D byte array where cell $(x, y) = x \cdot W + y$. Accessing neighbors utilizes direct index math with zero pointer dereferences.
2. **Heuristic Pruning & Spatial Discretization:**
   * Utilized modified A* search with Euclidean heuristic bounds and bounding-box spatial pruning, evaluating only relevant navigation corridors.
   * Used a flat array binary min-heap for the priority queue with pre-allocated storage to prevent dynamic heap reallocation during traversal.

---

## 3. Deep Project Defense: Alternative Data Radar

### The Likely Interrogation:
> *"How does your Alternative Data Radar translate into an actual trading strategy?"*

### Architectural Explanation:
1. **Pre-Earnings Asymmetric Information Ingestion:**
   * Extracted non-traditional web signals: dynamic hiring spikes, pricing shifts, and web traffic changes across target corporations.
   * Quant research relies on alternative data signals to predict earnings surprises before quarterly balance sheet releases.
2. **High-Throughput Extraction Pipeline:**
   * Handled rate limits and anti-scraping blocks through proxy session rotation.
   * Normalized disparate qualitative data into a structured numerical 0–100 corporate health score indexed in PostgreSQL for rapid SQL backtesting.

---

## 4. Deep Project Defense: K-HOG Keyframe Identifier (K-HUKI)

### The Likely Interrogation:
> *"Why did you use classical HOG and unsupervised clustering instead of a fine-tuned ResNet or Transformer?"*

### The HFT-Aligned Answer:
> *"Because in high-throughput streaming environments, latency and resource footprint dictate feasibility. A ResNet model requires billions of floating-point operations (FLOPs) and GPU acceleration, introducing massive inference latency. By engineering an unsupervised pipeline utilizing Histogram of Oriented Gradients (HOG) and geometric clustering, we captured 96.45% accuracy while running **11× faster** on a standard CPU with zero GPU dependency. This proves my engineering bias toward choosing lightweight, mathematically sound algorithms over computationally bloated neural networks."*
