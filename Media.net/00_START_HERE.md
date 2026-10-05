# 00: Media.net Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Media.net** (A Directi legacy company, founded by Divyank Turakhia; acquired by Miteno / Starry Media for $900M; leading global ad-tech giant).
* **Campus Placement Drive**: National Institute of Technology, Rourkela (Batch 2027).
* **Internship Model**: **6 Months Internship + Pre-Placement Offer (PPO) Conversion**.
* **Offered Job Role**: **Software Development Engineer (SDE) Intern**
* **Compensation Structure**:
  * **Monthly Stipend**: **₹1,00,000 / month (1 LPM)**
  * **CTC on PPO Conversion**: **18L Fixed + 4L One-Time Bonus + 16L Additional Bonus** (~38 LPA total compensation).
* **Eligible Branches & Degrees**: B.Tech, M.Tech, Dual Degree, Int MSc — All Branches (CGPA $\ge 6.0$, No active backlogs).
* **Major Engineering Centers**:
  * **Mumbai**: Directiplex, Andheri East (Core ad-serving engine, RTB infrastructure, low-latency DSP/SSP platforms).
  * **Bengaluru**: Global Technology Park, Bellandur (Contextual AI/ML matching, analytics, publisher growth).
  * **International HQs**: Dubai (Global HQ), New York (US HQ), Zurich, Los Angeles.

---

## 2. Media.net's Core Engineering & Ad-Tech Scale

Media.net is not a conventional web-application company. It operates one of the highest-throughput, lowest-latency distributed systems on the internet:

```
                  ┌──────────────────────────────────────────────┐
                  │          Media.net Ad-Tech Scale             │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│  500,000+ Sites  │           │   Sub-50ms SLA   │           │ Contextual Brain │
│ Publishers across│           │ Hard timeout on  │           │ Keyword NLP &    │
│ global internet  │           │ RTB auction bids │           │ Page Semantics   │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

1. **Contextual Advertising Pioneer**: Media.net pioneered deep contextual analysis without relying on third-party cookie tracking. It analyzes page content, natural language tokens, user intent, and publisher taxonomies in real-time to match high-value ads.
2. **Yahoo! Bing Network Partnership**: Media.net exclusively powers the Yahoo! Bing Network contextual ads program, monetizing publisher traffic with search and native intent.
3. **The Sub-50ms RTB Constraint**: When an ad slot loads on Forbes or CNN, an auction request triggers across hundreds of DSPs (Demand-Side Platforms). The whole pipeline—bid request serialization, network transport, DSP bid evaluation, second-price auction resolution, fraud filtering, and creative delivery—must complete in **under 50 milliseconds**.
4. **Engineering Stack**:
   * **Core Languages**: Java, C++, Python, Scala.
   * **Real-Time Streaming**: Apache Kafka (millions of events/sec), Apache Flink, Apache Spark.
   * **In-Memory & Storage**: Redis, Aerospike, MySQL, Elasticsearch, HDFS.
   * **Cloud & Edge**: Kubernetes, Docker, Bare-metal edge clusters in tier-1 data centers worldwide.

---

## 3. The 4 Recruitment Stages & Exact Evaluation Criteria

The on-campus selection pipeline is renowned for having one of the highest technical bars in India:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Stage 1: OA   │ ──► │  Round 1: DSA   │ ──► │ Round 2: Tech & │ ──► │  Round 3: HR &  │
│  InterviewBit   │     │  Live Coding &  │     │ CS Core + Proj  │     │   Culture Fit   │
│  (90 Minutes)   │     │  Unassisted CP  │     │  & AI Judgement │     │  (20 Minutes)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stage 1: Online Assessment (90 Minutes)
* **Platform**: Usually **InterviewBit** or **HackerEarth**.
* **Structure**: 3 Competitive Programming (CP) problems (Medium to Hard).
* **Core Topics**: Dynamic Programming (DP on grids, bitmask, knapsack), Graph Traversals (Dijkstra, Topological Sort, Shortest Path with constraints), Disjoint Set Union (DSU), Segment Trees, Binary Search on Answer, Bit Manipulation.
* **Plagiarism Filter**: **Extremely aggressive automated plagiarism detection**. Code structure, AST similarities, and identical variable patterns result in immediate disqualification. Write clean, authentic, unassisted code.

### Stage 2: Technical Round 1 — Problem Solving & Live Coding (60 Minutes)
* **Format**: 1-on-1 interview on a shared collaborative editor (Google Docs or Codeshare, no autocomplete or IDE assistance).
* **Focus**: 1 to 2 Hard/Medium DSA problems.
* **Expectations**:
  1. Clarify constraints and edge cases immediately before writing code.
  2. Explain the brute-force baseline ($O(N^2)$ or $O(2^N)$), then systematically optimize to $O(N \log N)$ or $O(N)$.
  3. Write production-quality, bug-free C++ or Python code with descriptive naming and modular helper functions.
  4. Rigorously trace edge cases: empty inputs, single element, large numbers ($10^9$), duplicates, and negative numbers.

### Stage 3: Technical Round 2 — CS Fundamentals, Projects & AI Judgement (60 Minutes)
* **Format**: 60 minutes with a Senior Architect / Engineering Manager.
* **Core CS Fundamentals**:
  * **Operating Systems**: Process vs Thread memory layouts, context switching overhead, virtual memory, paging & page tables, mutex vs semaphore, deadlocks (Coffman conditions), condition variables.
  * **Computer Networks**: TCP vs UDP in real-time ad bidding, 3-way handshake, TCP connection teardown (TIME_WAIT state), socket exhaustion, HTTP/1.1 vs HTTP/2 multiplexing, DNS lookup steps.
  * **DBMS**: B+ Tree indexing mechanics, Clustered vs Non-Clustered index, composite index left-to-right rule, ACID transactions, isolation levels (Dirty Read, Phantom Read), Write-Ahead Logging (WAL), SQL window functions (`DENSE_RANK()`).
* **Project Deep Dive & Engineering Judgement**:
  * Deep defense of candidate projects: **Warehouse PathMapper** (heuristic routing), **Uplan** (adversarial multi-agent intelligence), and **Alternative Data Radar** (automated scraping & SQL health score).
  * **The AI Tools Evaluation Directive**: The JD states explicitly:
    > *"Interviews and the online assessment evaluate unassisted problem-solving. Your fluency with AI tools is assessed separately, through how you talk about the projects you've built with them."*
  * Interviewers will grill whether you genuinely understand your project's low-level mechanics or merely pasted prompts into an LLM.

### Stage 4: HR & Cultural Fit Round (20 Minutes)
* **Format**: Behavioral assessment with HR or Engineering Director.
* **Focus**: Directi/Media.net values: Ownership, intellectual curiosity, resilience under pressure, learning from mistakes, and handling high-scale engineering challenges.

---

## 4. Key Strengths to Project in Interviews

1. **Unassisted Algorithmic Agility**: Prove you can derive optimal algorithms from first principles without Copilot or IDE suggestions.
2. **Systems-First Mental Model**: Relate high-level code to hardware realities—CPU cache lines, memory locality, socket limits, and disk I/O.
3. **Engineering Judgement with AI**: Discuss AI as a multiplier (rapid prototyping, synthetic data generation, test harness generation), while emphasizing personal ownership of verification, mathematical deterministic rule engines, and code reliability.
