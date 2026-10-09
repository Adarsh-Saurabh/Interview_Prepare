# Module 04: Candidate Resume Defense & Technical Grilling (Adarsh Saurabh)

## 1. Candidate Strategic Positioning

In the technical interview, the interviewers will scrutinize your background:
* **Academic Profile:** **M.Tech in Signal and Image Processing (NIT Rourkela)** + **B.Tech in Computer Science and Engineering (Guru Ghasidas University, 8.5 CGPA)**.
* **The Strategic Pivot:** How does an M.Tech Signal Processing + B.Tech CSE student fit into an AI Safety Foundry?
  * *The Pitch:* "Signal processing is fundamentally about mathematical precision, noise filtering, and deterministic transform verification. Combining rigorous mathematical rigor from signal analysis with low-level systems programming in CSE gives me the exact mindset needed for AI safety: treating model outputs as noisy signals that must be strictly audited by deterministic, zero-tolerance verification filters."

---

## 2. Flagship Project 1 Defense: Uplan (Adversarial Multi-Agent Verifier)

* **Repository:** `https://huggingface.co/spaces/ksk76/AMDDeveloperHackathon`
* **Technologies:** Python, LangGraph, Gemini 2.5 Pro, Multi-Agent Systems, Adversarial Evaluation.

### Expected Grilling Questions & Model Answers

#### Q1: "You claim an adversarial multi-agent workflow in Uplan. How did you prevent the agents from colluding or falling into endless agreement loops?"
> **Model Defense:** "In multi-agent LLM setups, agents naturally exhibit sycophancy. In Uplan, we structured the critic-agent relationship with **asymmetric reward objectives and strict JSON schemas**. The primary generator agent was tasked with extracting coherent visa profiles, while the critic agent was initialized with an adversarial prompt explicitly incentivized to discover factual contradictions and missing evidentiary links. Crucially, the final arbiter was not another LLM, but a **deterministic mathematical rule check engine**. If the agent asserted an applicant met income thresholds, the rule engine validated that against raw document metadata. The loop terminated deterministically after a maximum of 3 iterations if convergence was not reached."

#### Q2: "How did your structural encoding achieve a 98% token compression with Gemini 2.0 Flash?"
> **Model Defense:** "Raw PDF documents have immense whitespace and redundant structural tokens. We used Gemini 2.0 Flash as an extractor to parse raw text into a typed semantic graph (nodes representing entities like names, dates, amounts; directed edges representing relationships like 'issued_by', 'amount_paid'). By stripping natural language fluff and compiling only the relational adjacency matrix into a typed JSON schema, we reduced the context payload by 98% while preserving 100% of the mathematical and logical constraints required for downstream verification."

---

## 3. Flagship Project 2 Defense: Amazon ML Challenge 2026 (24.2M Records)

* **Repository:** `https://github.com/Adarsh-Saurabh/AmazonMl2026`
* **Key Metric:** **Macro F0.5 = 0.9719** across 24.2 Million records using Polars and GPU CatBoost.

### Expected Grilling Questions & Model Answers

#### Q1: "How does high-throughput entity resolution relate to building 250 evaluation environments for Solumn?"
> **Model Defense:** "Both problems require high-velocity, memory-efficient data processing without runtime bottlenecks. In the Amazon challenge, processing 24.2 million records sequentially in Pandas would have taken 14 hours and crashed RAM. By migrating to Polars with multi-view blocking and GPU-accelerated gradient boosting, we parallelized pipeline execution down to minutes. At Solumn, producing 6 verified environments per day requires the exact same engineering discipline: writing automated scaffolding scripts, validating schemas in micro-seconds, and never relying on slow, un-parallelized code."

---

## 4. Flagship Project 3 Defense: Warehouse PathMapper (Deterministic Routing)

* **Video Proof:** `https://youtu.be/nTAbJAMX3GY`
* **Key Metric:** Heuristic routing across a **10,000 × 10,000 grid** with 10,000+ locations in **<0.5s on a standard CPU**.

### Expected Grilling Questions & Model Answers

#### Q1: "How does PathMapper demonstrate skills relevant to Reinforcement Learning Environments?"
> **Model Defense:** "An RLE is fundamentally a state-space Markov Decision Process (MDP) with deterministic transition rules and reward boundaries. PathMapper demonstrates my ability to engineer discrete spatial grids, design heuristic objective functions, and enforce strict execution constraints. Scaling to 10,000 nodes in sub-0.5s proves I understand algorithmic complexity ($O(N \log N)$ vs $O(N^2)$), spatial partitioning, and benchmark determinism—ensuring our test harnesses execute in milliseconds without adding latency to the model evaluation loop."

---

## 5. How to Defend Profile Gaps

### Gap: "You don't have public CTF rankings or published CVE disclosures."
> **Crisp Defense:** "While my primary background has been systems engineering, machine learning pipelines, and multi-agent workflows, software security at an evaluation foundry is fundamentally applied test design. I understand the OWASP Top 10 for LLMs, directory traversal, prompt injections, and container sandboxing. More importantly, I have a proven track record of writing deterministic verifiers that catch edge cases. I treat security not as abstract penetration testing, but as rigorous unit-test assertions that make failure states 100% reproducible."
