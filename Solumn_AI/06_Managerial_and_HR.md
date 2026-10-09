# Module 06: Founder Mindset, High-Velocity Culture & PPO Conversion

## 1. Deconstructing the Founders' Mindset

Solumn AI was founded by **Samiksha Shrawgi (IIT Kharagpur, ISB, ex-BCG)** and **Ashish Arpit (IIT Roorkee, IIM Calcutta, ex-McKinsey)**. Understanding the consulting-and-engineering hybrid culture is essential for clearing the interview and converting to a full-time Pre-Placement Offer (PPO).

### Core Cultural Tenets at Solumn AI
1. **Hypothesis-Driven & Structured Communication:** In interviews, never ramble. Structure every answer in the McKinsey/BCG pyramid principle: **Top-line conclusion first**, followed by 2–3 structured mutually exclusive, collectively exhaustive (MECE) supporting points.
2. **Output Obsession Over Activity:** "I worked hard for 8 hours" means zero. "I built 7 deterministic environments, each with automated CVE repros and zero flaky tests" is the language they respect.
3. **Falsifiability & Intellectual Honesty:** A verifier that cannot fail is useless. If a test harness has a corner case where it might pass on incorrect code, proactively call it out and explain how you fixed it.
4. **Autonomous Ownership:** You will be working remotely with asynchronous reviews. The founders do not micromanage; they measure the commit log, environment throughput, and review acceptance rate.

---

## 2. High-Frequency Behavioral & Situational Questions

### Q1: "The delivery target is 250 environments in 6 weeks (~6 per day). How will you realistically balance this alongside your M.Tech research at NIT Rourkela?"
> **Model Answer (Structured & Crisp):**
> "I approach this through systematic pipeline automation rather than manual brute-force:
> 1. **Scaffolding Automation:** I will build Python CLI generators that automate boilerplate repository fixtures, Dockerfiles, and pytest test harness structures in seconds.
> 2. **Time-Boxing:** I dedicate a dedicated 3.5-hour block every evening (8:00 PM to 11:30 PM) specifically for environment authoring. In my M.Tech research on signal processing, I already manage high-compute GPU experiments in batch jobs, so my university work and this engagement operate on orthogonal schedules.
> 3. **Batch Verification:** I write and test verifiers locally in parallel batches of 5 using local Docker daemon scripts, ensuring I hit 6–8 verified environments per day consistently."

### Q2: "Tell me about a time a test harness or automated verification system you built produced a false positive. How did you diagnose and remediate it?"
> **Model Answer (STAR Format):**
> * **Situation:** "In my project Uplan, while testing our mathematical rule engine against parsed visa asset statements, the engine occasionally passed invalid applicant profiles."
> * **Task:** "I had to determine why the rule engine falsely verified financial coherence when values were logically incompatible."
> * **Action:** "I extracted the raw execution traces and discovered a floating-point truncation bug in currency conversions across multi-currency tables. The parser was casting string amounts to IEEE-754 floats without fixed precision, causing precision loss on large decimal amounts that bypassed our boundary condition assertions."
> * **Result:** "I refactored the verification pipeline to utilize Python's `decimal.Decimal` module with strict rounding modes, completely eliminating the false positive and restoring 100% deterministic assertion fidelity."

### Q3: "Why choose AI Safety and evaluation infrastructure over building consumer AI apps or working at Big Tech?"
> **Model Answer:**
> "Consumer AI apps are building interfaces on top of capabilities. But the existential blocker for frontier AI today is safety verification—if labs cannot prove a model won't write autonomous zero-days or exfiltrate credentials under Anthropic RSP gates, the model does not ship. Building the evaluation foundry layer puts me at the absolute frontier where models are audited against ground-truth reality. It is higher leverage, mathematically harder, and has an immediate impact on global deployment standards."

---

## 3. The PPO Conversion Playbook (Week 1 to Week 6)

| Phase | Target Deliverable | PPO Conversion Multiplier |
| :--- | :--- | :--- |
| **Weeks 1–2** | Onboard, master internal Docker harness schemas, deliver first 60 environments with **>95% review acceptance rate**. | Establishes baseline reliability; proves zero hand-holding required. |
| **Weeks 3–4** | Accelerate throughput to 10 environments/day; cross the **200 environment milestone**. | Enters top 10% of the entire university cohort. |
| **Week 5** | Cross the **250 environment quota**; draft a formal 2-page Research Proposal on **Model Context Protocol (MCP) Tool-Use Security Evaluation**. | Triggers evaluation for the **Solumn Research Fellowship** and direct Founder visibility. |
| **Week 6** | Push total environments beyond **400+**; submit research proposal for peer review. | **Converts Pre-Placement Offer (PPO)** for Core AI Safety Engineer / Research Fellow. |
