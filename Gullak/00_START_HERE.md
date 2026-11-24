# Module 00: Executive Intel & Interview Blueprint

## 1. Executive Summary & Opportunity Snapshot

* **Target Company:** Gullak Technologies (`gullak.money`)
* **Role:** Backend Engineer (SDE-1 / Core Systems)
* **Target Batch:** Batch of 2027 (On-Campus NIT Rourkela)
* **Compensation Structure:** 
  * **Stipend (Internship):** ₹50,000 / month (6 Months)
  * **Full-Time Compensation (CTC):** ₹20.00 LPA on PPO Conversion
* **Office Locations:** Bengaluru, Karnataka (HQ / Tech Hub)
* **Candidate Profile Alignment:** Adarsh Saurabh (M.Tech Signal Processing @ NIT Rourkela, B.Tech CSE @ GGU Bilaspur, 8.5 CGPA, Roll: `225EC6021`).

---

## 2. Gullak Origin Story & Founding Team Pedigree

Gullak is an early-stage, Y Combinator-backed (YC S22) consumer fintech revolutionizing wealth accumulation for ordinary Indians through digital gold micro-savings and automated SIPs.

### The Problem They Solve
* **The \$5 Trillion Idle Asset:** Indian households collectively hoard over 25,000 tonnes of physical gold (worth upwards of \$5 Trillion), primarily resting unproductive in bank lockers and home cupboards.
* **Friction in Micro-Savings:** Traditional physical gold purchases suffer from 3% GST, 10–25% jeweler making charges, purity verification risks, and high capital thresholds (minimum gram purchase).
* **The Gullak Solution:** A frictionless mobile-first rails where users save in 24K 99.9% pure digital gold (partnered with Augmont / MMTC-PAMP) starting with as little as ₹10, daily round-up savings on UPI spends, automated daily/weekly gold SIPs, and gold leasing yielding extra annual interest.
* **Scale Achieved:** In less than 3 years, Gullak has processed over **₹2,000+ Crore in gold savings across 500,000+ active customers**.

### The Founding Team & The Juspay DNA
To ace an engineering interview at Gullak, you must understand their founding team's engineering lineage:
* **Dilip Jain (Co-Founder & Head of Engineering):** Formerly Head of Engineering at **Juspay**. Key architect behind India's cloud-based UPI PSP stack (processing billions of monthly transactions across Google Pay, Amazon Pay, CRED, and Swiggy). He also contributed extensively to national digital public infrastructure (DPI) initiatives with **iSPIRT** (UPI, Account Aggregator, OCEN, and Beckn).
* **Manthan Shah (Co-Founder & Product):** Former Product Lead at Juspay, spearheading high-conversion checkout flows.
* **Naimisha Rao (Co-Founder & Growth):** Consumer psychology and rapid growth architect who scaled 40+ consumer brands.

> **Engineering Takeaway:** Gullak’s tech leadership comes from the crucible of Juspay's engineering culture. They value **first-principles thinking, extreme latency sensitivity, functional programming patterns, and anti-fragile distributed systems**. They do not want generic framework users; they want engineers who understand how Linux executes syscalls, how databases lock rows, and how payment gateways guarantee zero double-spends.

---

## 3. Engineering Stack & Architectural Philosophy

| Layer | Technologies & Tools | Key Architectural Decisions |
| :--- | :--- | :--- |
| **Backend Languages** | **Golang (Primary)**, Python, Java | Go goroutines for lightweight concurrent request handling and sub-millisecond final-mile API latencies. |
| **Databases** | **PostgreSQL**, MySQL, **DynamoDB**, ClickHouse | Relational PostgreSQL for double-entry financial ledgers and strict ACID guarantees; NoSQL DynamoDB for high-throughput stream ingestion. |
| **Caching & In-Memory** | **Redis**, Redis Cluster | Distributed locks (Redlock), session caching, real-time gold price feed ticker, rate-limiting. |
| **Asynchronous Queues** | **Kafka**, RabbitMQ | Decoupling webhook ingestion from payment verification; asynchronous bank settlement queues with dead-letter topics. |
| **Infrastructure** | **AWS (ECS/EKS, S3, RDS)**, Docker, Kubernetes | Cloud-native containerized microservices, zero-downtime rolling deployments, VPC isolation for financial security. |
| **Payment Rails** | **Juspay HyperUPI SDK**, NPCI BBPS, Banking APIs | In-app UPI intent without switching to third-party UPI apps; under 3-second payment confirmation. |

---

## 4. The 3-Stage Interview Process & Evaluation Rubric

Based on verified campus recruitment debriefs at premier NITs/IITs, the Gullak interview evaluation follows three rigorous technical filters:

```
[Round 1: Problem Solving & DSA / Puzzles (45-60 Mins)]
         │
         ▼
[Round 2: Core CS, DBMS & Fintech System Design (45-60 Mins)]
         │
         ▼
[Round 3: Founder / Leadership & Culture Fit (30-45 Mins)]
```

### Round 1: Problem Solving, Data Structures & Puzzles (45–60 Mins)
* **What Interviewers Probe:** Live coding in your language of choice (C++ / Python / Go). They test your ability to write clean, modular code and think aloud on mathematical corner cases.
* **Core Topics:**
  * Prefix sum arrays and two-pointer reconciliation (e.g., matching debit and credit streams).
  * Sliding window and heap-based streaming aggregations (Top-K savers).
  * Mathematical logic and number theory puzzles (e.g., the 100-Locker problem, class average score adjustments).
  * Graph traversal or cycle detection for cyclic money transfers.

### Round 2: Core CS Fundamentals, Databases & System Design (45–60 Mins)
* **What Interviewers Probe:** Deep first-principles computer science intuition.
* **Core Topics:**
  * **Database Internals:** PostgreSQL MVCC, transaction isolation anomalies (Dirty Read vs Repeatable Read vs Serialization Anomaly), B-Tree vs Hash index layouts, Optimistic vs Pessimistic concurrency control.
  * **Concurrency & OS:** Threads vs Processes, race conditions, atomic CAS (Compare-And-Swap), mutexes vs spinlocks, epoll vs select, connection pooling.
  * **Fintech System Design:** Designing the signature **QR-Code Web Login** system (WhatsApp Web flow), or designing an **Automated Daily Round-Up Micro-Savings Ledger** with idempotency keys.

### Round 3: Leadership, High Agency & Culture Fit (30–45 Mins)
* **What Interviewers Probe:** Founder or Director of Engineering discussion on ownership, autonomy, debugging production fire-drills, and culture.
* **Key Evaluation Criteria:**
  * Do you take initiative without being handheld? (Gullak explicitly seeks people who "initiate projects, make decisions, and drive outcomes").
  * Do you understand fintech security, compliance, and user trust?
  * Can you defend every line on your resume with genuine engineering trade-offs?

---

## 5. Candidate Alignment & Superpower Strategy (Adarsh Saurabh)

You enter this interview with a decisive, unmatched advantage that 99% of candidates do not possess:

```
                     ┌──────────────────────────────────────────────┐
                     │          ADARSH'S GULLAK ADVANTAGE           │
                     └──────────────────────┬───────────────────────┘
                                            │
    ┌───────────────────────────────────────┼───────────────────────────────────────┐
    ▼                                       ▼                                       ▼
[Direct Gold Fintech Domain]      [Algorithmic Rigor & Scale]        [Strong Computer Science Dual Base]
• Apna Gold Solutions SaaS         • Warehouse PathMapper              • B.Tech Computer Science (8.50)
• Multi-tenant gold platform       • 10k x 10k grid in < 0.5 sec       • M.Tech Signal Processing (8.28)
• B2B2C seller KYC & plans         • Heuristic graph optimization      • Low-level systems, algorithms,
• DB conflict resolution & JWT     • Memory cache-locality & latency   • OS, concurrency & DB mastery
```

1. **`Apna Gold Solutions` Is Your Golden Ticket:** You have literally built a multi-tenant B2B2C gold platform with seller registration, customer subscription plans, JWT security, and database conflict resolution. Anchor your database and backend answers in this project!
2. **`Warehouse PathMapper` Proves Low-Latency Rigor:** Handling 10,000+ points on a 10,000×10,000 grid in under 0.5s on a standard CPU proves you understand algorithmic complexity, memory layout, and CPU cache-friendliness.
3. **Turn the M.Tech Signal Processing Background into a Superpower:** You have a B.Tech in CSE (algorithms, OS, DBMS) combined with an M.Tech in Signal Processing (mathematical optimization, stochastic processes, low-latency DSP pipelines). You are equipped to build mathematically rigorous, high-throughput financial systems.
