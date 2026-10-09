# Module 00: Company & Role Intelligence · Solumn AI

## 1. Executive Summary & Corporate Identity

* **Entity Name:** **Solumn AI** (also operating under the engineering banner **BrainBrowser**)
* **Headquarters:** Dubai, United Arab Emirates (Operating globally with distributed engineering across India, UAE, and US)
* **Founding Team:**
  * **Samiksha Shrawgi:** Alumna of **IIT Kharagpur** and **Indian School of Business (ISB)**; previously Strategy Consultant at **Boston Consulting Group (BCG)**.
  * **Ashish Arpit:** Alumnus of **IIT Roorkee** and **IIM Calcutta**; previously Engagement Manager at **McKinsey & Company**.
* **Corporate DNA:** An elite blend of **top-tier management consulting rigor** (extreme structured thinking, milestone orientation, output velocity) and **frontier AI systems engineering** (falsifiable tests, Docker sandboxing, deterministic verifiers).
* **The Foundations Programme:** An applied 6-week industrial engagement for final-year engineering students (Batch 2027) with a **₹2,00,000 stipend**, remote format, and a direct merit-based **Pre-Placement Offer (PPO)** conversion track.

---

## 2. Why Solumn AI Exists: The Frontier AI Assurance Layer

### The Macro Shift: Capabilities vs. Deployment Gates
Frontier AI laboratories—specifically **Anthropic, Google DeepMind, Amazon, OpenAI, and Meta**—are training foundation models whose parameter scale and agentic capabilities advance exponentially. However, regulatory frameworks and internal governance have shifted fundamentally in 2025–2026:

$$\text{Model Capability alone } \cancel{\implies} \text{ Deployment}$$
$$\text{Deployment Gate} = \text{Empirical Safety Proof} \;\land\; \text{Falsifiable Verification}$$

Under binding policies such as **Anthropic's Responsible Scaling Policy (RSP Version 3.2)**, labs make explicit public and legal commitments:
> *"Maintaining our commitment not to train or deploy models unless we have implemented adequate safeguards."*

When a model reaches **AI Safety Level 3 (ASL-3)** or **ASL-4** thresholds (autonomous cyber-offense, self-exfiltration, biological hazard assistance, unmonitored tool privilege escalation), safety teams cannot rely on:
1. **Subjective prompt evaluations** (vibes, human RLHF raters grading conversational warmth).
2. **Static academic benchmarks** (MMLU, HumanEval, GSM8K)—which are contaminated, non-interactive, and test memorization rather than execution under stress.

### Solumn's Business Model
Solumn operates as a specialized **Evaluation Foundry and Red-Teaming Infrastructure Partner**. Frontier laboratories pay premium enterprise bounties to external verification foundries like Solumn to build the ground-truth benchmark environments against which models must be audited before releasing checkpoints.

```
+-------------------------------------------------------------------------+
|                        Frontier AI Laboratory                           |
|       (Anthropic Claude 3.7 / OpenAI o3 / Google Gemini 2.5 Pro)        |
+-------------------------------------------------------------------------+
                                    |
          Demands External, Falsifiable Safety Evidence (RSP Gates)
                                    v
+-------------------------------------------------------------------------+
|                       Solumn AI Evaluation Foundry                      |
|                                                                         |
|  [ Workstream 1: Agentic RLEs ]   Containerized Docker environments     |
|  [ Workstream 2: Vulnerability ]   Real CVE exploits + regression tests  |
|  [ Workstream 3: Adversarial ]    MCP & tool-calling attack suites      |
+-------------------------------------------------------------------------+
                                    |
                 Deterministic Graders Output PASS / FAIL
                                    v
+-------------------------------------------------------------------------+
|                  Frontier Safety Gate: Audit Approved                   |
+-------------------------------------------------------------------------+
```

---

## 3. The Three Core Live Workstreams

| Workstream | Core Problem Statement | Technical Stack | Primary Deliverable |
| :--- | :--- | :--- | :--- |
| **1. Agentic Environments** | Building sandboxed environments that place an autonomous coding agent under pressure, with a deterministic test harness judging whether it held the line. | Docker, Python, Bash, Pytest, Linux cgroups | Containerized scenario packages, repository fixtures, reference solutions, pass/fail grading scripts. |
| **2. Vulnerability Datasets** | Curating find-and-fix software security tasks derived from real-world CVEs across open-source codebases. | C/C++, Python, Git, Fuzzers, Patch parsers | Reproducible exploit reproduction script + deterministic unit-test harness that passes only after genuine patch application. |
| **3. Adversarial Evaluation** | Stress-testing tool-calling interfaces and **Model Context Protocol (MCP)** deployments against prompt injections and privilege escalation. | Python, LangGraph/LiteLLM, JSON-RPC, MCP Servers | Attack suites evaluating jailbreaks, unauthorized API calls, and data exfiltration against structured harm taxonomies. |

---

## 4. Programme Deliverables, Metrics & Milestones

The Foundations Programme is explicitly **production-driven**:

* **Baseline Quota:** **250 Reinforcement Learning Environments (RLEs)** over 6 weeks.
  * *Daily Velocity Required:* $250 \div 42 \text{ days} \approx \mathbf{6\text{ environments / day}}$ (or $\approx 3\text{ to } 4\text{ hours/day}$).
* **Founders' Recognition Tier:** Candidates delivering **>500 verified environments** receive a formal **Letter of Recommendation from the Founders**.
* **Research Fellowship Track:** Top performers who formulate and pitch a novel evaluation harness or benchmark graduate to the **Solumn Research Fellowship**—fully funded research with named co-authorship on peer-reviewed papers.
* **Pre-Placement Offer (PPO):** Converted on merit at close, benchmarked to global frontier AI research roles (typical market package: ₹25 – ₹45+ LPA equivalent or tax-free Dubai packages).

---

## 5. Selection Process & Tight Timetable

```
[Oct 8, 11:59 PM]   ---> [Oct 9, 11:00 AM]   ---> [Oct 9, 12:00 PM]   ---> [Oct 10, 09:00 AM]  ---> [Oct 11]
Campus Application        CV Shortlisting          Practical Take-Home      Take-Home Submission     Technical
Form Closes               Closes                   Assignment Released      Closes (21h Window)      Interviews
```

* **Stage 1 (CV Shortlisting):** Automated and manual review prioritizing evidence of shipped software, containers, systems projects, and reproducible benchmarks.
* **Stage 2 (Practical Assignment - 21 Hours):** Released Friday Oct 9 at 12:00 PM; due Saturday Oct 10 at 09:00 AM. Involves building Dockerized scenario packages, task descriptions, and deterministic grading harnesses in Python.
* **Stage 3 (Technical Interview - Sunday Oct 11):** 45-minute technical conversation drilling into your assignment design, handling flaky tests, Python subprocess concurrency, and candidate project architectures.
