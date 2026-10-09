# modules_part3.py - Solumn AI Modules 06, 07, README

modules_part3 = {
    "06_Managerial_and_HR": {
        "title": "Module 06: Founder Mindset & PPO · Solumn AI Foundations 2026",
        "active_page": "06_Managerial_and_HR.html",
        "prev_link": "05_System_Design_or_HIL.html",
        "prev_title": "05: Eval Foundry Architecture",
        "next_link": "07_Quick_Reference.html",
        "next_title": "07: Rapid Recall CheatSheet",
        "content_md": """# Module 06: Founder Mindset, High-Velocity Culture & PPO Conversion

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
"""
    },

    "07_Quick_Reference": {
        "title": "Module 07: Rapid Recall CheatSheet · Solumn AI Foundations 2026",
        "active_page": "07_Quick_Reference.html",
        "prev_link": "06_Managerial_and_HR.html",
        "prev_title": "06: Founder Mindset & PPO",
        "next_link": "README.html",
        "next_title": "3-Day Selection Roadmap",
        "content_md": """# Module 07: Rapid Recall CheatSheet & Syntax Vault

## 1. Python Subprocess & Sandboxing Snippets

### Secure Isolated Execution with Timeout
```python
import subprocess, signal

def run_isolated(cmd: list[str], cwd: str, timeout_sec: float = 5.0):
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False
        )
        return {"code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    except subprocess.TimeoutExpired:
        return {"code": -signal.SIGKILL, "error": "TIMEOUT_EXCEEDED"}
```

---

## 2. Docker Python SDK Essential Snippets

### Creating Sandboxed Container with Resource Constraints
```python
import docker

client = docker.from_env()

container = client.containers.run(
    image="python:3.11-slim",
    command=["pytest", "/tests"],
    volumes={"/host/repo": {"bind": "/workspace", "mode": "rw"}},
    network_mode="none",              # Total network isolation
    mem_limit="512m",                 # 512MB RAM cap
    cpu_quota=50000,                  # 0.5 CPU core (cpu_period=100000)
    pids_limit=50,                    # Fork-bomb prevention
    read_only=True,                   # Immutable root filesystem
    tmpfs={"/tmp": "rw,size=32m"},    # Ephemeral scratch space
    detach=True
)
```

---

## 3. Pytest Deterministic Assertion Patterns

```python
import pytest
import math
from decimal import Decimal

# 1. Deterministic float comparison
def test_float_tolerance():
    assert math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)

# 2. Strict timeout per test
@pytest.mark.timeout(2.0)
def test_execution_latency():
    pass

# 3. Hermetic temporary directory
def test_file_integrity(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content")
    assert p.read_text() == "content"
```

---

## 4. Frontier Safety Framework Cheat Table

| Framework | Core Metric / Level | Mandatory Gate Requirement |
| :--- | :--- | :--- |
| **Anthropic RSP v3.2** | **ASL-3** (Cyber, CBRN, Autonomous Agent tools) | Red-teaming audits, air-gapped evaluation, third-party foundry proof. |
| **Google DeepMind** | **Critical Capability Levels (CCLs)** | Continuous monitoring against self-replication and zero-day cyber tools. |
| **OpenAI / Frontier Forum** | **Preparedness Framework (High Risk)** | Model weights locked until mitigation reduces risk below Medium threshold. |
"""
    },

    "README": {
        "title": "3-Day Selection Roadmap · Solumn AI Foundations 2026",
        "active_page": "README.html",
        "prev_link": "07_Quick_Reference.html",
        "prev_title": "07: Rapid Recall CheatSheet",
        "next_link": "index.html",
        "next_title": "Overview Hub",
        "content_md": """# 3-Day Selection & Preparation Roadmap (Oct 9 – Oct 11, 2026)

## Overview & Timeline

```
[Oct 9: 11:00 AM]   CV Submissions Deadline
[Oct 9: 12:00 PM]   Practical Take-Home Assignment Released (21-Hour Clock Starts)
[Oct 10: 09:00 AM]  Assignment Submissions Close
[Oct 11: Full Day]  Technical Interviews with Founders & Core Safety Engineers
```

---

## Day-by-Day Tactical Execution Plan

### Day 1 (Friday, Oct 9): Assignment Blitz & Verifier Engineering
* **12:00 PM – 01:00 PM:** Download and dissect the take-home assignment brief. Identify whether tasks fall into **Agentic Environments**, **CVE Vulnerabilities**, or **Adversarial Tool-Use**.
* **01:00 PM – 05:00 PM:** Build the baseline repository fixtures. Ensure Docker container builds cleanly without external network dependencies.
* **05:00 PM – 09:00 PM:** Implement the reference solution in Python. Run multiple profiling iterations to confirm clean $O(N)$ execution.
* **09:00 PM – 12:00 AM:** Write the **deterministic verification harness**. Test against 5 edge-case failure inputs to verify that broken code fails with descriptive error logs.

---

### Day 2 (Saturday, Oct 10): Submission Polish & Systems Prep
* **06:00 AM – 08:30 AM:** Final review of submission package:
  - Verify `scenario.json`, `instructions.md`, `fixture/`, `solution/`, and `verifier/` match expected schemas.
  - Run a clean-room verification test in a fresh Docker container to verify zero environment leaks.
* **08:45 AM:** Submit the assignment zip archive and form response before the 09:00 AM deadline.
* **11:00 AM – 04:00 PM:** Review **Module 02 (Python & Docker Internals)** and **Module 05 (Evaluation Foundry Architecture)**.
* **06:00 PM – 09:00 PM:** Rehearse **Module 04 (Candidate Resume Defense)**: Practice explaining Uplan's multi-agent critic and PathMapper's 10k grid benchmark in under 90 seconds.

---

### Day 3 (Sunday, Oct 11): Technical Interview Mastery
* **Morning Warm-Up:** Review **Module 07 (CheatSheet)** and **Module 03 (Anthropic RSP v3.2 & ASL-3/4 gates)**.
* **During the Interview:**
  - Structure answers top-line first.
  - Highlight your dual background (M.Tech Signal Processing + B.Tech CSE) as combining mathematical rigor with low-level systems engineering.
  - Reiterate commitment to hitting the 250 environment quota and publishing novel benchmarks via the Research Fellowship.
"""
    }
}
