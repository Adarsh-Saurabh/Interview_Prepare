# 04: Candidate Resume Defense

Tailored defense strategies for **Adarsh Saurabh** (M.Tech Signal & Image Processing @ NIT Rourkela, B.Tech CSE). Interviewers at Swiggy will probe project scalability, algorithmic limits, and theoretical connections to hyperlocal food delivery.

---

## 1. Project Defense: IBYD Technology — Warehouse PathMapper (Mandatory)

### Elevator Pitch to Swiggy
> *"In Warehouse PathMapper, I developed a high-throughput spatial routing engine for industrial facilities. I modeled massive topological grids ($10,000 \times 10,000$) as directed spatial graphs, executing multi-point heuristic trajectory optimization through 10,000+ coordinates simultaneously in under 0.5 seconds on standard CPU. This directly mirrors Swiggy’s logistics challenges: both Instamart’s in-store dark-store pick routing and city-scale multi-drop dispatch batching over hexagonal H3 spatial grids."*

### Trap 1: "A 2D warehouse grid is simple. City road networks are directed, non-planar, and experience dynamic traffic. How does your grid heuristic apply to Swiggy?"
- **Candidate Defense:**
  1. **Direct Application to Instamart:** Instamart dark stores are literally high-density warehouse grids where pickers must collect multi-SKU orders within 150 seconds. My algorithm solves the exact NP-hard Traveling Salesperson Problem (TSP) with obstacle avoidance for store aisles.
  2. **Hierarchical Abstraction on City Graphs:** For city-level routing, raw road networks (OSRM) are too expensive to compute globally in real-time dispatch loops. Swiggy aggregates road coordinates into Uber H3 hexagonal grid cells (Resolution 8/9). The inter-cell transitions form a grid-graph topology where heuristic search algorithms (A*, Jump Point Search, Contraction Hierarchies) prune search spaces by $>95\%$.

### Trap 2: "What heuristics did you use, and did you guarantee admissibility?"
- **Candidate Defense:**
  - For Euclidean distance $h(u, v) = \sqrt{(x_u - x_v)^2 + (y_u - y_v)^2}$, the heuristic is strictly admissible ($h(u, v) \le d^*(u, v)$) and monotonic/consistent, ensuring that the first time a node is expanded in A*, its optimal path is found without reopening nodes.
  - To achieve $<0.5$s execution across 10,000 coordinates, I implemented **Hierarchical Pathfinding (HPA\*)**: partitioning the $10,000 	imes 10,000$ grid into $64 	imes 64$ macro-clusters, precomputing border-to-border transitions, and executing heuristic search on the abstracted macro-graph before refining local paths.

---

## 2. Project Defense: Autobot Robotics (ML Intern)

### Trap: "You processed robotic sensor telemetry. How does that relate to delivery partner mobile signals?"
- **Candidate Defense:**
  - Both domains suffer from **noisy, high-frequency spatial telemetry**. Delivery executive mobile GPS in urban Indian cities (e.g. Bangalore, Mumbai) suffers from severe multipath interference, satellite shadow between skyscrapers, and battery-saver GPS throttling.
  - At Autobot Robotics, I handled sensor noise filtering using **Discrete Kalman Filters** and moving window variance thresholds.
  - At Swiggy, this exact mathematical foundation is required for **Map Matching**: taking raw, jittery GPS coordinates $(lat, lon)$ and projecting them onto the underlying directed road graph using Hidden Markov Models (HMM) with emission and transition probabilities based on road speed limits.

---

## 3. Project Defense: Alternative Data Radar

### Connection to Swiggy
- Scraped corporate and pricing signals mapped directly to:
  - Competitive price scraping of rival food delivery and quick commerce catalogs.
  - Detecting restaurant menu price inflation on delivery platforms vs in-store dining.
  - Real-time indexing of local events, concerts, and weather alerts that cause sudden localized demand surges.

---

## 4. Academic Background: M.Tech Signal Processing Advantage

### Trap: "You are an M.Tech in Signal & Image Processing. Why should Swiggy hire you over a pure Computer Science graduate for Data Science?"
- **Candidate Defense:**
  - *"Machine Learning at scale is applied statistical estimation. In Signal Processing, we treat telemetry not as static database rows, but as continuous, non-stationary stochastic signals.
  - Concepts like **Fourier & Wavelet analysis** provide deep mathematical grounding for decomposing seasonal demand into trend, daily cycles, and high-frequency noise.
  - **Kalman Filtering and State-Space Models** are the optimal estimators for tracking real-time delivery rider trajectories and battery-efficient location extrapolation.
  - Combined with my B.Tech in Computer Science, I possess both the low-level systems engineering capability (DSA, C++, SQL) and advanced mathematical rigor (linear algebra, probability, optimization) necessary for production Data Science at Swiggy."*
