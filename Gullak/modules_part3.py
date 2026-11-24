# modules_part3.py - Gullak Technologies Backend Engineer Interview Modules Part 3

modules_part3 = {}

# ==============================================================================
# Module 06: Startup Mindset, High Agency & Behavioral Scenarios
# ==============================================================================
modules_part3["06_Managerial_and_HR_Culture"] = """# Module 06: Startup Mindset, High Agency & Behavioral Scenarios

Gullak is an early-stage, fast-moving fintech startup. The engineering leadership is not looking for corporate bureaucrats who wait for tickets; they look for **high-agency engineers with first-principles intuition who take end-to-end ownership**.

---

## 1. What Gullak Leadership Values

1. **"Coding is Art & First-Principles Thinking":** The founders and tech leads believe in deep engineering inspired by Linux, functional type-safety, and minimal abstractions that solve real user problems.
2. **Extreme Ownership:** From schema design to API deployment, monitoring Prometheus/Grafana alerts, and fixing production edge cases.
3. **Speed with Reliability:** Moving fast does not mean writing sloppy code. In fintech, moving fast means writing strongly-typed, idempotent code that is tested against failure modes before hitting production.

---

## 2. Eight Core STAR Behavioral Scenarios

### Scenario 1: Why Gullak?
* **Situation:** You are interviewing for the Backend Engineer role at Gullak with a competitive background from NIT Rourkela.
* **Task:** Convey genuine passion for the product, engineering stack, and founding team.
* **Action:**
  > "Three factors make Gullak my top choice:
  > 1. *The Engineering Pedigree:* Gullak's leadership, led by Dilip Jain, comes from Juspay's core infrastructure team that architected India's cloud UPI stack. Learning distributed systems and low-latency engineering from team leaders who built national public rails is the best possible mentorship an ambitious engineer can get.
  > 2. *The Mission & Domain:* Gold is deeply embedded in Indian culture, but hoarding ₹5 Trillion of idle gold in lockers is economically unproductive. Digitizing this asset through frictionless micro-savings, round-ups, and SIPs democratizes wealth creation. Having built `Apna Gold Solutions`, I already understand the business mechanics and nuances of gold ledgers.
  > 3. *The 0-to-1 High-Ownership Culture:* I thrive in nimble environments where engineers own releases end-to-end rather than working on minor isolated components in large legacy corporations."

### Scenario 2: Handling an Ambiguous or Undefined Requirement
* **Situation:** During the development of the Warehouse PathMapper routing engine for IBYD Technology, the client had no formal technical specifications—only raw spreadsheet coordinates and operational delays.
* **Task:** Formulate a structured engineering problem statement and deliver a working solution without handholding.
* **Action:** I initiated weekly feedback loops, formulated the problem as a graph heuristic pathfinding challenge, built an interactive visualizer in Pygame/Matplotlib to show path simulations, and iterated directly based on physical warehouse constraints.
* **Result:** Delivered an engine capable of routing 10,000+ points across a 10,000×10,000 grid in under 0.5s on a standard CPU, exceeding client benchmarks.

### Scenario 3: Debugging a High-Pressure Technical Incident
* **Situation:** In `Apna Gold Solutions`, during peak testing, concurrent transactions caused seller inventory counts to drift out of sync.
* **Task:** Identify the root cause without blaming others and fix it permanently.
* **Action:** Analyzed SQL transaction logs and discovered race conditions caused by non-atomic read-modify-write queries in Django. I refactored the checkout flow to use database row-level locking (`SELECT FOR UPDATE`) inside an atomic transaction block and added an idempotency key middleware.
* **Result:** Eliminated race conditions completely, achieving 100% data consistency across concurrent order simulations.

### Scenario 4: Mentoring and Team Leadership
* **Situation:** As a Machine Learning Intern at Autobot Robotics and later as Vice President of the Google Developer Student Club (GDSC).
* **Task:** Guide junior engineers and drive collaborative deliverables.
* **Action:** At Autobot Robotics, mentored a junior intern on data manipulation, NumPy, and Django deployment pipelines, breaking complex tasks into bite-sized architectural milestones. At GDSC, organized hands-on developer hackathons and study jams.
* **Result:** Junior intern shipped their modules ahead of schedule; established a culture of peer code reviews and shared technical documentation.

---

## 3. High-Impact Questions to Ask Gullak Interviewers

At the end of your interview, when the interviewer asks: *"Do you have any questions for us?"* Never say no. Ask one or two of these high-caliber questions:

1. **On Engineering Architecture:**
   > *"Given Gullak's rapid growth past ₹2,000 Crore in gold savings, how does the engineering team currently handle the trade-off between strict relational double-entry ledger ACID guarantees in PostgreSQL versus the high-throughput write scalability of NoSQL/DynamoDB for streaming UPI events?"*
2. **On Culture & Day-to-Day:**
   > *"The JD mentions that Gullak engineers are inspired by first-principles thinking and how Linux works. What does that philosophy look like in the day-to-day code review and architectural design process here?"*
3. **On Growth & PPO:**
   > *"What does success look like for a Backend Engineer in the first 90 days of this 6-month engagement to ensure seamless conversion into a core FTE contributor?"*
"""

# ==============================================================================
# Module 07: Rapid Recall CheatSheet & Flashcards
# ==============================================================================
modules_part3["07_Quick_Reference_CheatSheet"] = """# Module 07: Rapid Recall CheatSheet & Flashcards

Keep this sheet open for emergency 15-minute revision right before stepping into the interview call.

---

## 1. Twenty-Five Rapid-Fire Technical Flashcards

1. **What is ACID?** Atomicity (all-or-nothing via WAL), Consistency (invariants/constraints preserved), Isolation (concurrent independence via MVCC/locks), Durability (persisted to disk via fsync).
2. **What is PostgreSQL MVCC?** Multi-Version Concurrency Control where readers never block writers and writers never block readers. Rows have hidden `xmin` and `xmax` headers. Updates create new row versions.
3. **What is VACUUM in Postgres?** Reclaims dead tuples left behind by updates/deletes and freezes transaction IDs to prevent transaction wraparound.
4. **What is a Dirty Read?** Reading uncommitted data from another concurrent transaction that might subsequently rollback.
5. **What is a Non-Repeatable Read?** Re-reading the same row within a transaction and seeing modified data because another transaction committed in between.
6. **What is a Phantom Read?** Re-running a range query and seeing new rows added or deleted by another committed transaction.
7. **What is Pessimistic Locking?** Acquiring exclusive locks upfront using `SELECT ... FOR UPDATE` to block concurrent writes until commit.
8. **What is Optimistic Concurrency Control (OCC)?** Proceeding without locks, checking a `version` or timestamp column during `UPDATE`, and aborting/retrying if version changed.
9. **How does Redis implement distributed locking?** `SET key token NX PX ttl`. Released atomically via a Lua script verifying `GET(key) == token`.
10. **What is a Fencing Token in distributed locks?** A monotonically increasing number issued with each lock lease to prevent delayed/stale requests from writing after TTL expiry.
11. **What is an Idempotency Key?** A unique UUID passed in the request header allowing the client to safely retry network calls without duplicating operations (e.g., payments).
12. **What is the 3-Way TCP Handshake?** SYN $\\to$ SYN-ACK $\\to$ ACK.
13. **Why does the TCP `TIME_WAIT` state exist?** Ensures the final ACK is received by the server and allows duplicate lingering packets to die out (lasts $2 \\times \\text{MSL} \\approx 60\\text{s}$).
14. **How do you avoid socket exhaustion under high loads?** Enable HTTP Keep-Alive connection pooling (`MaxIdleConns`), reuse TCP connections, or tune `tcp_tw_reuse`.
15. **What is the difference between Epoll and Select/Poll?** Select/Poll scan all $N$ file descriptors in $O(N)$ time. Epoll uses an OS callback ready list, returning active fds in $O(1)$ time.
16. **What is an OS Process vs Thread?** Processes have private virtual address spaces and isolated resources. Threads share memory (heap, code, globals) but have private stacks and registers.
17. **What is a Goroutine?** A user-space lightweight thread managed by the Go runtime scheduler ($M:N$). Starts with only 2KB stack vs 2MB–8MB for an OS thread.
18. **What is a Mutex vs Spinlock?** A mutex puts the waiting thread to sleep via kernel futex syscalls. A spinlock busy-waits in a CPU loop, best for ultra-short critical sections.
19. **What is the Transactional Outbox Pattern?** Writing business data and event records to the same database transaction, ensuring zero loss when publishing events to Kafka/RabbitMQ.
20. **Why are financial balances stored as double-entry ledgers?** Eliminates arbitrary mutable balance updates. Balance is derived from the algebraic sum of immutable debits and credits, ensuring verifiable audits.
21. **What is B-Tree Index complexity?** Search, insert, and delete are $O(\\log N)$. Leaf nodes are linked as a doubly-linked list for fast sequential range scans.
22. **What is the 100-Locker Puzzle answer?** Lockers with numbers that are perfect squares (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) remain open because only perfect squares have an odd number of positive divisors.
23. **What is the QR-code login sequence?** Web generates UUID $\\to$ Web opens WebSocket $\\to$ Mobile scans QR $\\to$ Mobile authenticates via biometrics $\\to$ Backend verifies and pushes JWT over WebSocket to Web.
24. **How to prevent dual-scan on a QR code?** Use a Redis atomic Lua script checking `status == 'PENDING'`; if true, set `CLAIMED`, else reject immediately.
25. **What is your 30-second background pitch?** "I am an engineer with a B.Tech in CSE and M.Tech in Signal Processing at NIT Rourkela, combining deep algorithmic optimization—like routing 10,000 points in 0.5s in Warehouse PathMapper—with real-world gold fintech experience building Apna Gold Solutions."

---

## 2. HTTP Status Codes in Financial Systems

| Code | Name | Fintech Meaning |
| :--- | :--- | :--- |
| **200 OK** | OK | Synchronous operation completed successfully. |
| **202 Accepted** | Accepted | Transaction received and queued asynchronously for bank settlement. |
| **400 Bad Request** | Bad Request | Malformed payload, invalid account number or currency format. |
| **401 Unauthorized** | Unauthorized | Missing or expired JWT token. |
| **403 Forbidden** | Forbidden | Valid user, but unauthorized for this tenant or account resource. |
| **409 Conflict** | Conflict | Duplicate idempotency key or optimistic concurrency version mismatch. |
| **422 Unprocessable** | Unprocessable Entity | Valid JSON syntax, but business logic violation (e.g., balance < amount). |
| **429 Too Many Req** | Rate Limited | Exceeded API rate limit; backed off via Redis Token Bucket. |
| **502 Bad Gateway** | Bad Gateway | Upstream banking gateway or NPCI partner returned network timeout. |
| **504 Gateway Timeout**| Gateway Timeout | Downstream settlement call timed out; transaction must enter PENDING check. |
"""

# ==============================================================================
# Module: README - Emergency Study Roadmap & Morning-Of Action Plan
# ==============================================================================
modules_part3["README"] = """# Emergency Study Roadmap: Night-Before & Morning-Of Action Plan

You have interviews with **Gullak** tomorrow morning for the **Backend Engineer** role (₹20 LPA CTC / ₹50k/mo stipend). Use this disciplined, high-impact checklist to dominate tomorrow's rounds.

---

## 1. Tonight's Hour-by-Hour Battle Plan (Night Before)

```
[10:30 PM - 11:15 PM] Module 00 & 05: Company Pedigree & Resume Defense
                      • Rehearse your Apna Gold Solutions multi-tenant story.
                      • Memorize the Warehouse PathMapper numbers (10k grid, <0.5s).
                      • Internalize Dilip Jain / Juspay architectural roots.

[11:15 PM - 12:00 AM] Module 03 & 04: Databases & Fintech System Design
                      • Review the QR-Code Login flow and atomic Redis Lua script.
                      • Review PostgreSQL MVCC, Read Committed anomalies, and SELECT FOR UPDATE.
                      • Review Idempotency Keys and the Transactional Outbox Pattern.

[12:00 AM - 12:30 AM] Module 01: Signature Algorithms & Puzzles
                      • Review the 100-Locker problem proof (perfect squares / odd divisors).
                      • Walk through Fenwick Tree prefix sum ledger logic.

[12:30 AM - 07:00 AM] MANDATORY REST & SLEEP (6.5 Hours)
                      • Do NOT stay up all night. Fintech interviews require sharp mental clarity,
                        calm problem-solving, and active listening.
```

---

## 2. Tomorrow Morning: T-Minus 90 Minutes Schedule

* **T-90 Minutes (Wake-Up & Nutrition):**
  * Hydrate, take a warm shower, and eat a clean, protein-rich breakfast.
* **T-45 Minutes (Rapid Recall):**
  * Open **Module 07 (CheatSheet)**. Read through the 25 flashcards once.
* **T-20 Minutes (Hardware & Environment Check):**
  * Test camera, microphone, and internet stability.
  * Keep a clean pen and physical scratchpad ready on your desk for drawing architectures.
  * Ensure your code editor (VS Code / browser IDE) has syntax highlighting enabled for Python and C++.
* **T-5 Minutes (Power Pose & Mental Anchoring):**
  * Take 3 deep breaths.
  * Remind yourself: *You have built a real-world gold SaaS platform (`Apna Gold Solutions`). You have written high-performance algorithms (`Warehouse PathMapper`). You are the ideal match for Gullak.*

---

## 3. During the Interview: Golden Execution Rules

1. **Think Aloud Before Coding:** Never dive into writing code immediately. Re-state the problem, clarify constraints (input bounds, memory limits), state the naive approach, and then outline the optimal strategy.
2. **Anchor Answers in Production Realities:** When discussing databases or system design, don't speak in abstract generalities. Say: *"In Apna Gold Solutions, when we handled concurrent seller updates..."* This immediately proves you are a practitioner.
3. **Handle Hints Gracefully:** If the interviewer gives a hint or questions a corner case, don't get defensive. Say: *"That's a great edge case to consider. Let's trace what happens when..."*
4. **Speak with Passion:** Gullak is an early-stage startup. Show genuine excitement about digital gold, scale, and building world-class engineering systems.
"""

print("modules_part3.py ready with modules 06, 07, README.")
