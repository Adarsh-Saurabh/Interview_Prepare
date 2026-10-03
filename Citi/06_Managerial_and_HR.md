# 06: Citi Leadership Principles & Behavioral Rounds

Citi evaluates behavioral candidates against its three universal leadership pillars: **Taking Ownership**, **Delivering with Pride**, and **Succeeding Together**.

---

## 1. Citi's Core Leadership Principles

1. **Taking Ownership**:
   * Acting with courage and personal accountability. Stepping up to resolve ambiguities and taking calculated risks while maintaining strict regulatory compliance.
2. **Delivering with Pride**:
   * Setting high quality standards in engineering. Rejecting sloppy code, ensuring test coverage, and driving execution excellence that protects client assets.
3. **Succeeding Together**:
   * Championing an inclusive, collaborative team dynamic. Helping teammates succeed, communicating transparently, and respecting diverse technical viewpoints.

---

## 2. High-Frequency Behavioral Questions (STAR Method)

### Question 1: "Tell me about a time you handled a critical technical bug under severe time pressure."
* **Situation**: During our AMD Developer Hackathon submission for Uplan, our LangGraph multi-agent pipeline began timing out during live batch testing with less than 3 hours before the code freeze.
* **Task**: As team lead, I had to identify the latency bottleneck across our Gemini 2.5 Pro and 2.0 Flash agent graph without degrading document validation accuracy.
* **Action**: I instrumented latency timers across each node in the LangGraph workflow and identified that our structural compilation agent was re-serializing the entire multi-page document on every step. I refactored the pipeline to compile document metadata into a typed semantic graph once, compressing the token footprint by 98% and caching intermediate representations.
* **Result**: Average verification latency dropped from 48 seconds down to 6.2 seconds. The pipeline passed all automated test suites, and our team finished in the top national percentile.

---

### Question 2: "Describe a situation where you had a strong technical disagreement with a team member. How did you resolve it?"
* **Situation**: While building the Warehouse PathMapper routing engine for our client, my teammate proposed using a pre-packaged graph library that required substantial boilerplate and external dependencies, while I advocated for a customized flat-array A* heuristic implementation.
* **Task**: We needed to align on an architecture that delivered sub-second response times on a standard laptop CPU without creating technical debt or timeline delays.
* **Action**: Instead of arguing hypotheticals, I established objective benchmark criteria: execution latency on a $10,000 \times 10,000$ grid, memory footprint, and maintainability. We both built quick prototypes on a $1,000 \times 1,000$ sample. The benchmark demonstrated that the flat-array approach avoided $\sim$80,000 micro-allocations and executed $7\times$ faster.
* **Result**: My teammate readily agreed with the empirical benchmark data. We co-authored the routing engine, which successfully computed 10,000+ coordinates in under 0.5s.

---

### Question 3: "Why Citi, and why a 12-month SWE Apprenticeship?"
* **Model Answer**:
  > "Citi operates at an unmatched financial engineering scale — clearing over $4 Trillion daily across 160 countries through platforms like Treasury and Trade Solutions (TTS). A systems engineer working at Citi is not building generic consumer apps; we are engineering mission-critical financial infrastructure where high throughput, sub-millisecond latency, and absolute fault tolerance directly protect the global economy.
  > The 12-month SWE Apprenticeship provides the structured runway to immerse myself in Citi's production architecture, learn banking domain standards like ISO 20022 and AWS Serverless, and deliver immediate impact in Pune or Chennai with the clear goal of converting into a full-time Technology Analyst."

---

## 3. High-Impact Questions to Ask Your Interviewer
1. *"How is Citi's Treasury and Trade Solutions (TTS) engineering team managing the ongoing transition toward event-driven serverless architectures while ensuring zero downtime across legacy core banking ledgers?"*
2. *"What are the primary metrics by which an apprentice's performance is measured over the 12 months to qualify for early C09 Technology Analyst conversion?"*
3. *"Given the global transition to ISO 20022 message formats, how are India GCC teams involved in architectural modernization?"*
