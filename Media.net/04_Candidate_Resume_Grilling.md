# 04: Candidate Resume Grilling & Traps

Media.net interviewers conduct surgical deep dives into your resume projects. They specifically verify that you possess **first-principles understanding** and did not simply rely on AI coding assistants or surface-level tutorials.

---

## 1. Candidate Baseline Profile Summary
* **Candidate**: Adarsh Saurabh (Roll Number: `225EC6021`)
* **Education**:
  * **M.Tech in Signal and Image Processing**, NIT Rourkela (CGPA: **8.28**)
  * **B.Tech in Computer Science and Engineering**, Guru Ghasidas University (CGPA: **8.5**)
* **Core Projects on Tailored Resume**:
  1. `Uplan — Adversarial Document Intelligence Pipeline` (LangGraph, Gemini 2.5 Pro, Streamlit, 2025)
  2. `Alternative Data Radar` (Python, Next.js, SQL, REST APIs, Bright Data, LLM APIs, 2026)
  3. `IBYD Technology — Warehouse PathMapper` (Python, Algorithms, Data Structures, 2023)

---

## 2. Deep Project Defense & Trap Scenarios

### Project 1: Warehouse PathMapper (IBYD Technology)
> *"You built a heuristic pathfinding engine on a 10,000 x 10,000 grid running in under 0.5s. How does this relate to Media.net's engineering?"*

#### The Interview Trap
* If you say: *"It was just Dijkstra / A* algorithm on a grid,"* the interviewer will ask: *"On a $10,000 \times 10,000$ grid ($10^8$ nodes), Dijkstra will timeout or run out of memory. How did it finish in $< 0.5$ seconds?"*

#### The Master Defense
> *"In a raw $10^8$ state-space, standard Dijkstra is unusable due to $O(V \log V + E)$ overhead. In real industrial warehouses, 95% of space consists of fixed rack aisles and transit corridors.
> 1. **Topological Graph Abstraction**: Instead of searching pixel-by-pixel, I precomputed a hierarchical topological waypoint graph connecting aisle intersections and picking bays (~1,500 nodes).
> 2. **Bidirectional A* with Manhattan Distance Heuristic**: I used an admissible heuristic $h(n) = |x_1 - x_2| + |y_1 - y_2|$ running from both start and target simultaneously, terminating when search frontiers met.
> 3. **Spatial Memory Locality**: I stored waypoint coordinates in contiguous array buffers (cache-line friendly) rather than linked node pointers, eliminating pointer chasing and CPU L1/L2 cache misses.
> 4. **Relevance to Media.net**: This is directly analogous to ad routing in an SSP—rather than evaluating every DSP linearly, we use hierarchical clustering and topological pruning to evaluate target criteria in microseconds."*

---

### Project 2: Uplan — Adversarial Document Intelligence Pipeline
> *"You used LangGraph and Gemini 2.5 Pro for adversarial document validation. The Media.net JD states: 'Interviews evaluate unassisted problem-solving. Fluency with AI tools is assessed separately.' Did you write the core logic, or did LLMs do the thinking?"*

#### The Interview Trap
* If you say: *"The LLM figured out if the document had errors,"* you will be rejected for lack of engineering ownership and deterministic reasoning.

#### The Master Defense
> *"I designed Uplan around the principle that **LLMs must never be trusted with deterministic mathematical validation**.
> 1. **Deterministic Rule Engine First**: LLMs suffer from stochastic hallucination when comparing numerical financial data. I engineered a zero-hallucination mathematical verification engine in Python that validates bank statements, salary credits, and tax amounts against hard Boolean rules.
> 2. **Structural Encoding & 98% Token Compression**: Sending raw multi-page PDFs to an LLM introduces unacceptable latency and token cost. I used Gemini Flash as an extraction compiler to distill page metadata into a typed semantic JSON graph, cutting prompt tokens by 98%.
> 3. **Adversarial LangGraph Topology**: I created two specialized roles: a Proposer agent that checks visa compliance, and an Adversary agent tasked with actively finding edge-case contradictions. Their state was orchestrated via a deterministic Directed Acyclic Graph in LangGraph.
> 4. **AI as an Accelerator**: I wrote the state graphs, type definitions, and rule engines myself. I used AI developer tools to rapidly generate edge-case validation test suites and fuzzing fixtures."*

---

### Project 3: Alternative Data Radar
> *"You scraped web signals and calculated corporate health scores stored in a SQL database. How did you handle anti-scraping, rate limits, and SQL concurrency?"*

#### The Interview Trap
* *"How did you prevent database lock contention when scraping multiple corporate data sources concurrently?"*

#### The Master Defense
> *"1. **Proxy Rotation & Fingerprint Emulation**: Target corporate websites use Cloudflare and Akamai bot protection. I routed traffic via Bright Data Web Unlocker, managing HTTP/2 TLS fingerprint rotation and automated exponential backoff with jitter on HTTP 429/503 responses.
> 2. **Asynchronous Scraping Worker Pool**: Instead of synchronous blocking HTTP requests, I used an asynchronous worker architecture (`asyncio` and worker queues), streaming parsed signals directly into an ingestion pipeline.
> 3. **SQL Indexing & Concurrency**: Corporate scoring metrics required frequent inserts and analytical queries. I isolated analytical aggregation queries using Read Committed isolation, created composite indexes on `(company_id, metric_date DESC)` for fast dashboard lookups, and batched inserts inside database transactions to eliminate row lock contention."*

---

## 3. Defending Your Dual Background: M.Tech Signal Processing + B.Tech CSE

> *"Your undergraduate degree is CSE, but your Master's is Signal and Image Processing. Why are you applying for a Core SDE role at Media.net?"*

#### The Winning Narrative
> *"My dual background is a deliberate technical advantage for high-scale systems:
> 1. **B.Tech in CSE**: Gave me foundational mastery in Data Structures, Algorithms, Operating Systems, Database Internals, and Computer Networks.
> 2. **M.Tech in Signal Processing at NIT Rourkela**: Trained me in high-dimensional linear algebra, Fourier analysis, statistical signal filtering, and real-time streaming pipelines.
> 3. **Application to Ad-Tech**: Real-time ad bidding is fundamentally a high-frequency digital signal stream:
>    * Click fraud detection uses statistical anomaly filtering (Kalman filtering and noise cancellation).
>    * Contextual ad semantic matching relies on high-dimensional vector embeddings and cosine projections.
>    * Low-latency RTB requires microsecond timing budgeting, which mirrors real-time digital signal processing constraints."*
