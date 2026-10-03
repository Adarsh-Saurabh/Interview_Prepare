# 04: Candidate Resume Defense & Project Traps

Interviews for Citi's SWE track will probe your technical authenticity, architectural trade-offs, and how your academic background bridges into high-reliability financial systems.

---

## 1. Candidate Strategic Positioning: Adarsh Saurabh

### Profile Summary
* **Academic Foundation**: M.Tech in Signal and Image Processing (NIT Rourkela, CGPA: 8.28) + B.Tech in Computer Science and Engineering (Guru Ghasidas University, CGPA: 8.5).
* **The Interview Pivot**:
  * *Question*: *"Why are you applying for a Software Engineering Apprenticeship at Citi when your Master's is in Signal and Image Processing?"*
  * *Winning Defense*:
    > "My dual foundation gives me a unique advantage: my B.Tech in CSE established my core software engineering discipline — data structures, object-oriented design, databases, and microservice architecture. My M.Tech in Signal Processing added deep mathematical rigor in statistical modeling, linear algebra, time-series analysis, and algorithmic optimization.
    > In modern banking and FinTech, high-frequency transaction streams, fraud detection algorithms, and low-latency order routing are fundamentally streaming signal processing problems. My background enables me to write optimal, cache-friendly code that processes massive transaction pipelines with minimal latency."

---

## 2. In-Depth Defense of Master Resume Projects

### Project 1: Warehouse PathMapper (IBYD Technology)
* **The Core Tech**: Spatial coordinate routing engine handling warehouses up to $10,000 \times 10,000$ spatial units; sub-0.5s computation through 10,000+ points on standard CPU.
* **Citi FinTech Mapping**:
  * *Technical Link*: Explain how spatial graph routing mirrors financial transaction routing across liquidity pools and multi-hop clearing networks.
* **Interviewer Trap 1**: *"Did you use Dijkstra or A*? How did you scale to 10,000 nodes without running out of memory?"*
  * **Answer**:
    > "Standard Dijkstra expands equally in all directions, evaluating $\mathcal{O}(V \log V + E)$ nodes, which causes excessive memory allocations and cache misses on large grids.
    > I engineered a heuristic-based A* pathfinding engine with an admissible Manhattan distance metric on a spatial grid graph. To ensure sub-0.5s execution, I avoided allocating dynamic heap objects during traversal by using flat, contiguous 1D array representations for node states and a custom min-heap indexed by node IDs."

---

### Project 2: Uplan — Adversarial Document Intelligence Pipeline
* **The Core Tech**: Multi-agent workflow in LangGraph with Gemini 2.5 Pro specialists; 98% token compression into typed semantic graphs; zero-hallucination mathematical verification engine.
* **Citi FinTech Mapping**:
  * *Technical Link*: Automated validation of international trade finance documents (Letters of Credit, Bills of Lading, KYC records, compliance sanction checks).
* **Interviewer Trap 2**: *"LLMs are notorious for hallucinations. How can a bank rely on your pipeline for compliance?"*
  * **Answer**:
    > "We designed an adversarial dual-agent architecture where the LLM is restricted strictly to semantic extraction and structured JSON schema generation.
    > Crucially, all rule checks, cross-field validations, dates, and currency totals are evaluated by a deterministic, zero-hallucination mathematical engine written in Python. If numeric fields fail programmatic validation, the failure is returned to the agent for rebuttal, eliminating generative hallucination in regulatory checks."

---

### Project 3: K-HOG Unsupervised Keyframe Identifier (K-HUKI)
* **The Core Tech**: Keyframe extraction using Histogram of Oriented Gradients (HOG) and unsupervised clustering; $11\times$ faster than deep neural network (ResNet) alternatives.
* **Citi FinTech Mapping**:
  * *Technical Link*: Demonstrates the ability to achieve high analytical precision using lightweight mathematical feature extraction rather than bloated, resource-heavy black-box models.

---

### Project 4: Apna Gold Solutions — Multi-Tenant SaaS Platform
* **The Core Tech**: Multi-tenant B2B2C SaaS platform with Django REST API, React Vite, JWT authentication, and secure database isolation.
* **Citi FinTech Mapping**:
  * *Technical Link*: Multi-tenant enterprise banking platforms, client segregation, role-based access control (RBAC), and stateless JWT session handling.
* **Interviewer Trap 3**: *"How did you enforce multi-tenant security in your database? What prevented Tenant A from reading Tenant B's data?"*
  * **Answer**:
    > "We implemented tenant isolation at both the middleware and database layer. Every incoming HTTP request required a verified JWT containing the encrypted `tenant_id` claim.
    > Our database access layer automatically scoped every query with a global tenant filter (`WHERE tenant_id = current_tenant`). Foreign keys and unique indexes were compound-keyed on `(tenant_id, record_id)` to prevent cross-tenant data leaks."
