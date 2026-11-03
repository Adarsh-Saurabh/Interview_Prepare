# ⚡ Fast Interview Study Material & Rapid Cheat Sheets

A high-yield, interview-focused preparation portal featuring **Dual-Mode Learning** (15-Minute Sprint vs 60-Minute Deep Dive), inline SVG architectural diagrams, mathematical derivations rendered with KaTeX, and **237+ GeeksforGeeks & Top Tech Interview Flashcards** with Spaced Repetition (`Got it`, `Shaky`, `No idea`) queue tracking.

Curated for **Adarsh Saurabh (NIT Rourkela — Batch 2027)** across 3 target hiring profiles:
- **AI / Machine Learning Engineer** (OpenAI, Anthropic, Apple AI, Qualcomm, DeepMind)
- **Software Engineer / Systems & Low-Latency** (Pace Stock Broking ₹41L HFT, Texas Instruments ₹43L, Apple ₹80L, Qualcomm, Media.net, Cisco)
- **Forward Deployed Engineer (FDE) / Applied AI Systems** (Palantir, AiPrise, Cred, Swiggy, Warner Bros)

---

## 🚀 Quick Launch

Open [`index.html`](./index.html) in any modern desktop or mobile browser.

- **Dual-Mode Depth Control**: Toggle between **15-Min Sprint** (`data-depth="sprint"`) for last-minute cramming and **60-Min Deep Dive** (`data-depth="deep"`) for rigorous derivations and system design. State persisted in `localStorage`.
- **Spaced Repetition Review Queue**: Click [`review.html`](./review.html) to rehearse flashcards flagged as ⚠️ *Shaky* or ❌ *No idea* with scheduled intervals.
- **Search System**: Multi-keyword fuzzy search indexed across 148+ sections in [`search_index.json`](./search_index.json).
- **Mobile-Ready UX**: Slide-out navigation drawer (`☰ Sections`), 3px reading progress bar, and fixed bottom navigation (`🏠 Hub`, `📑 Sections`, `⚡ Sprint`, `🌙 Theme`, `↑ Top`).
- **Mathematical Integrity**: KaTeX auto-rendering for all complexity classes, attention scaling, AMAT, and SVD derivations.

---

## 📚 Complete 23-Module Curriculum Roster (5 Tracks)

### Track A: Core CS Fundamentals (6 Modules)

| # | Module | File | Tier | Target Roles | Sprint | Deep | Flashcards | Highlights & Visual Diagrams (SVG) |
| :-: | :--- | :--- | :-: | :---: | :-: | :-: | :-: | :--- |
| 1 | **Data Structures & Algorithms** | [`dsa.html`](./dsa.html) | P0 | SWE, AI, FDE | 15 min | 60 min | 14 | Trigger phrase table, Constraint size guide, 9 DP state shapes, Grid=Graph, Monotonic stack, DSU. |
| 2 | **Operating Systems** | [`os.html`](./os.html) | P0 | SWE, AI | 15 min | 60 min | 9 | Process Memory Layout SVG, MMU/TLB Hardware Lookup SVG, Classic Sync problems, Gantt charts, Belady's anomaly. |
| 3 | **DBMS & Storage Internals** | [`dbms.html`](./dbms.html) | P0 | SWE, FDE | 15 min | 60 min | 8 | B+ Tree Architecture SVG, WAL/ARIES Recovery SVG, LSM Tree Write Path SVG, Isolation matrix, Write Skew. |
| 4 | **Computer Networks** | [`cn.html`](./cn.html) | P1 | SWE | 12 min | 60 min | 8 | TCP Handshake & 4-Way Teardown SVG, DNS Resolution Chain SVG, URL lifecycle, BDP formula, Sliding windows. |
| 5 | **Computer Organization & Architecture** | [`coa.html`](./coa.html) | P1 | SWE | 12 min | 60 min | 8 | 5-Stage RISC Pipeline SVG, Amdahl's Law, AMAT 3-level latency, Cache bits (Tag/Index/Offset), False Sharing, MESI. |
| 6 | **Concurrency & Parallelism** | [`concurrency.html`](./concurrency.html) | P0 | SWE, AI | 15 min | 60 min | 16 | Happens-Before Memory Ordering SVG, Striped Lock HashMap SVG, SPSC lock-free buffer, FooBar & H2O synchronization. |

### Track B: Software Engineering & Design (5 Modules)

| # | Module | File | Tier | Target Roles | Sprint | Deep | Flashcards | Highlights & Visual Diagrams (SVG) |
| :-: | :--- | :--- | :-: | :---: | :-: | :-: | :-: | :--- |
| 7 | **Low-Level Design & Patterns** | [`lld_design_patterns.html`](./lld_design_patterns.html) | P0 | SWE, FDE | 15 min | 60 min | 14 | SOLID principles, 23 GoF Design Patterns, O(1) LRU & LFU caches, Thread-safe Singleton, Parking Lot LLD. |
| 8 | **System Design & Distributed Systems** | [`system_design.html`](./system_design.html) | P0 | SWE, AI, FDE | 15 min | 60 min | 14 | Consistent Hashing Ring SVG, Scalable TinyURL SVG, CAP/PACELC trade-offs, Kafka internals, Distributed Sagas. |
| 9 | **API Design, Auth & Security** | [`api_security.html`](./api_security.html) | P1 | SWE, FDE | 15 min | 60 min | 14 | OAuth 2.0 PKCE Flow SVG, JWT Header/Signature SVG, Idempotency Keys with Redis, OWASP Top 10, Multi-tenant RLS. |
| 10 | **C++ Low-Latency & Systems** | [`cpp_systems.html`](./cpp_systems.html) | P1 | SWE | 15 min | 60 min | 8 | VTable Layout SVG, shared_ptr Control Block SVG, Lock-Free SPSC Ring Buffer, Move semantics, HFT allocator rules. |
| 11 | **Python Internals & GIL** | [`python_internals.html`](./python_internals.html) | P0 | AI, FDE | 14 min | 60 min | 14 | CPython PyObject Header, GIL Mechanics SVG, Generational Cyclic GC, `__slots__` memory savings, AsyncIO event loop. |
| 11B | **Python & OOP Complete Interview Masterclass (25-Page Print Cheat Sheet)** | [`python_oop_interview_cheatsheet.html`](./python_oop_interview_cheatsheet.html) | P0 | SWE, AI, Data Science | 29-Page Print | 105 Qs | 100+ Code | 105 Categorized Interview Questions (OOP Basics, The 4 Pillars, Gotchas, Deep Systems & AI) (Tricky Outputs, CPython Memory, MRO C3 Linearization, Descriptors, Metaclasses, GIL Concurrency, AI Agent Tool Engine, 3 Complete LLD Systems). |

### Track C: AI / Machine Learning (6 Modules)

| # | Module | File | Tier | Target Roles | Sprint | Deep | Flashcards | Highlights & Visual Diagrams (SVG) |
| :-: | :--- | :--- | :-: | :---: | :-: | :-: | :-: | :--- |
| 12 | **Math for Machine Learning** | [`math_ml.html`](./math_ml.html) | P1 | AI | 15 min | 60 min | 8 | SVD Geometric Transformation SVG, Forward vs Reverse KL SVG, Bayes' Disease worked example, MLE vs MAP L1/L2 proof. |
| 13 | **Classical ML & Deep Learning Core** | [`ml_core.html`](./ml_core.html) | P0 | AI | 15 min | 60 min | 8 | Bias-Variance Tradeoff SVG, L1 vs L2 Sparsity Geometry SVG, NumPy 2-Layer Net from scratch, XGBoost 2nd-order math, 9-Step ML Design. |
| 14 | **Computer Vision & Signal Processing** | [`ml_cv.html`](./ml_cv.html) | P1 | AI | 14 min | 60 min | 9 | CNN Feature Pyramid SVG, HOG Feature Extraction SVG (K-HUKI), ResNet skip connection gradient proof, Canny edge detection. |
| 15 | **LLM & Transformer Internals** | [`llm_internals.html`](./llm_internals.html) | P0 | AI | 15 min | 60 min | 14 | MHA vs MQA vs GQA SVG, Scaled Dot-Product Attention formula, KV Cache Memory Scaling arithmetic, SFT vs DPO vs GRPO. |
| 16 | **AI Agents, RAG & Vector DBs** | [`ai_agents.html`](./ai_agents.html) | P0 | AI, FDE | 15 min | 60 min | 9 | Advanced Modular RAG SVG, LangGraph Cyclic State Machine SVG (Uplan), Hybrid search RRF, Vector DB matrix, ReAct loops. |
| 17 | **AI Evaluation, Guardrails & LLMOps** | [`ai_evals.html`](./ai_evals.html) | P0 | AI, FDE | 15 min | 60 min | 12 | Evaluation Pyramid Hierarchy SVG, pass@k vs pass^k formula, RAG Triad, LLM-as-a-judge bias mitigation, PSI drift. |

### Track D: Data & Infrastructure (3 Modules)

| # | Module | File | Tier | Target Roles | Sprint | Deep | Flashcards | Highlights & Visual Diagrams (SVG) |
| :-: | :--- | :--- | :-: | :---: | :-: | :-: | :-: | :--- |
| 18 | **SQL & Data Engineering** | [`sql_data.html`](./sql_data.html) | P0 | SWE, AI, FDE | 15 min | 60 min | 10 | Logical Query Execution Order SVG, Window Frames, Gaps & Islands, 2nd Highest Salary, Spark skew salting. |
| 19 | **Linux CLI, Systems Debugging & Git** | [`linux_git.html`](./linux_git.html) | P1 | SWE, FDE | 14 min | 60 min | 8 | Git 4-Area Architecture SVG, Production Incident Diagnosis checklist, Merge vs Rebase, `lsof +L1` unlinked file descriptor trap. |
| 20 | **Docker, Containers & Kubernetes** | [`docker.html`](./docker.html) | P1 | SWE, FDE | 10 min | 60 min | 8 | VM vs Docker Stack SVG, OverlayFS Union Mount SVG, 16 Docker CLI commands, Kubernetes Objects, OOMKill vs CPU throttling. |

### Track E: Role-Specific & Human (3 Modules)

| # | Module | File | Tier | Target Roles | Sprint | Deep | Flashcards | Highlights & Visual Diagrams (SVG) |
| :-: | :--- | :--- | :-: | :---: | :-: | :-: | :-: | :--- |
| 21 | **Forward Deployed Engineer (FDE) Decomposition** | [`fde_decomp.html`](./fde_decomp.html) | P0 | FDE | 15 min | 60 min | 8 | 8-Phase Enterprise Decomposition SVG, Scoping question bank, Workflow Spine methodology, Mid-round constraint pivot defenses. |
| 22 | **Behavioral, Leadership & STAR Stories** | [`behavioral.html`](./behavioral.html) | P0 | SWE, AI, FDE | 15 min | 60 min | 8 | Action-Weighted STAR (60% Action) SVG, 12-Story Bank mapped to Master Resume projects (Warehouse PathMapper, Uplan, K-HUKI). |
| 23 | **Quantitative Aptitude & Interview Puzzles** | [`quant.html`](./quant.html) | P1 | SWE, AI | 15 min | 60 min | 8 | Monty Hall Bayesian Host Knowledge SVG, Linearity of Expectation, 25 Horses race puzzle, 12 Coins balance puzzle, Fermi estimation. |

---

## 🎯 Strategic Study Plans & Presets

Use the quick preset filters directly on [`index.html`](./index.html):

1. **🔥 48-Hour Cram (10 Modules — 2.5 hrs Sprint / 10 hrs Deep)**:
   `dsa`, `concurrency`, `lld`, `system_design`, `python_internals`, `ml_core`, `llm_internals`, `sql_data`, `fde_decomp`, `behavioral`.
2. **🎯 FDE Loop (7 Modules — 1.7 hrs Sprint / 7 hrs Deep)**:
   `fde_decomp`, `lld`, `api_security`, `system_design`, `sql_data`, `ai_agents`, `behavioral`.
3. **🤖 AI / ML Loop (7 Modules — 1.75 hrs Sprint / 7 hrs Deep)**:
   `math_ml`, `ml_core`, `llm_internals`, `ai_agents`, `ai_evals`, `concurrency`, `behavioral`.
4. **💻 SWE Systems Loop (7 Modules — 1.7 hrs Sprint / 7 hrs Deep)**:
   `dsa`, `os`, `concurrency`, `system_design`, `cpp_systems`, `api_security`, `behavioral`.
5. **👑 Full Mastery (23 Modules — 5.5 hrs Sprint / 23 hrs Deep)**:
   Complete coverage of all 5 tracks.

---

## 🛠️ Recompiling & Extending

All generators and components reside in [`builder/`](./builder/):

```powershell
# Recompile all 23 modules, search index, and review queue
python "Study Material\builder\build_all.py"
```

The build process emits:
- 23 modular, self-contained HTML files with KaTeX math and PrismJS syntax highlighting.
- Master dashboard [`index.html`](./index.html) with role filters, track grouping, and local progress tracking.
- Spaced Repetition hub [`review.html`](./review.html) reading `localStorage` ratings.
- Fast multi-topic search index [`search_index.json`](./search_index.json).
