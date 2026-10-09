# 3-Day Selection & Preparation Roadmap (Oct 9 – Oct 11, 2026)

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
