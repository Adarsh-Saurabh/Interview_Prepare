# 00: Citi Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Citigroup Inc.** (Founded 1812 in New York City, USA). One of the "Big Four" global financial institutions, operating across 160+ countries and jurisdictions.
* **Global Headcount**: Over **230,000+ dedicated employees** worldwide, serving 200+ million customer accounts.
* **Technology Workforce**: 30,000+ engineers globally, with India representing Citi's largest and most critical engineering footprint outside the United States.
* **Major India Tech Hubs (GCCs)**:
  * **Pune**: EON Free Zone, Kharadi (Major center for Treasury and Trade Solutions, Markets Technology, and Cloud Transformation).
  * **Chennai**: DLF IT Park & Ramanujan IT City (Global center for Securities Services, Payments Engine, Digital Banking, and Risk/Compliance systems).
  * **Mumbai**: First International Financial Centre (FIFC), Bandra Kurla Complex (BKC) (Corporate HQ, Institutional Clients Group, Global Markets).
* **Core Business Divisions**:
  1. **Services**:
     * **Treasury and Trade Solutions (TTS)**: Clears $4+ Trillion in corporate transactions daily across 140 currencies.
     * **Securities Services**: Custody, asset servicing, and clearing for global institutional investors.
  2. **Markets**: High-frequency electronic trading, equities, fixed income, FX, rates, and commodities.
  3. **Banking**: Investment banking, corporate lending, and capital advisory.
  4. **Wealth**: High-net-worth portfolio management and private banking.
  5. **Enterprise Technology & Cyber**: Core infrastructure, hybrid cloud (AWS/GCP), AI/ML, zero-trust security.

---

## 2. Core Architecture & Tech Stack

Citi's engineering teams are migrating monolithic banking cores into modular, event-driven microservices running on hybrid cloud infrastructure:

```
[Client Channels: Corporate Portal / Mobile / Open Banking APIs]
                        │
                        │ HTTPS / TLS 1.3 / OAuth 2.0 / MTLS
                        ▼
      [API Gateway & Distributed Rate Limiting]
                        │
      ┌─────────────────┴─────────────────┐
      ▼                                   ▼
[Frontend Apps]                   [Backend Services]
 • React.js (v18+)                 • Python (FastAPI / Flask / AsyncIO)
 • Material UI (MUI)               • Java (Spring Boot / Micronaut)
 • Redux Toolkit / Context API     • RESTful APIs / gRPC
      │                                   │
      └─────────────────┬─────────────────┘
                        ▼
          [Enterprise Event Streaming]
           • Apache Kafka / AWS Kinesis / SQS
           • Event-driven Pub/Sub Architecture
                        │
      ┌─────────────────┴─────────────────┐
      ▼                                   ▼
[Primary Data Stores]             [Cloud & DevOps Pipeline]
 • MongoDB (DocumentDB / ACID)     • AWS Serverless (Lambda, S3, CloudFront)
 • Oracle DB / PostgreSQL          • Terraform (Infrastructure as Code)
 • Redis In-Memory Cache           • Docker, Kubernetes & OpenShift
 • ElasticSearch (Audit Logs)      • CI/CD: Jenkins, GitHub Actions, TeamCity
```

### Key Technical Concepts Expected by Citi Recruiters:
1. **Frontend**: React.js with responsive components (`Material UI`), virtual DOM diffing, state lifecycles (`useEffect`, `useCallback`, `useMemo`), clean CSS/SCSS layout.
2. **Backend**: Python for microservices and data pipelines (`asyncio`, typing, modular OOP, REST API standards, idempotent execution).
3. **Databases**: MongoDB (document modeling, compound indexing, aggregation pipelines, replica sets, and multi-document ACID transactions) alongside relational SQL.
4. **Cloud Infrastructure**: AWS Serverless paradigms (API Gateway, AWS Lambda cold-starts, S3 bucket security, CloudFront CDN, DocumentDB), automated via **Terraform** scripts.

---

## 3. Placement Drive Specification (NIT Rourkela 2027 Batch)

| Parameter | Drive Details |
| :--- | :--- |
| **Target Role** | **SWE Apprenticeship (Software Engineer Apprentice)** |
| **Transition Role** | **Technology Analyst (Grade C09)** upon successful PPO conversion |
| **Duration** | 12 Months (Full-Time Apprenticeship under Govt NATS/NAPS portal) |
| **Locations** | Pune & Chennai Tech Centers |
| **Apprenticeship Stipend** | **₹50,000 / month** (₹6.00 Lakhs annual cash) |
| **Post-Conversion CTC (Est.)**| **~₹14.00 – ₹18.00 LPA Total**<br>• Fixed Base: ₹12.00 – ₹14.00 LPA<br>• Annual Performance Bonus: ₹1.50 – ₹2.50 Lakhs<br>• Retirals & Benefits: ₹1.00 – ₹1.50 Lakhs |
| **Eligible Courses & Batches**| M.Tech (CS, EC, EE / Circuital Branches) — 2026/2027 Pass-outs |
| **Academic Cutoff** | CGPA $\ge$ 6.0 or 60% aggregate; No active backlogs |
| **Special Condition** | Must **not** have prior Provident Fund (PF) history (Govt Apprenticeship Act compliance) |

---

## 4. Complete 4-Stage Recruitment Pipeline

```
[Stage 1: Resume Shortlist]
  └── ATS Screening: Focus on Python, React, MongoDB, Cloud, OOP, and High Performance.
           │
           ▼
[Stage 2: Online Assessment (OA)]
  ├── Duration: 90 - 105 Minutes (SHL / HackerRank Platform)
  ├── Section 1: Quantitative & Logical Aptitude (20 Qs)
  ├── Section 2: Computer Science MCQs (OS, DBMS, OOP, Networking, Data Structures) (20 Qs)
  └── Section 3: 2 Hands-on Coding Problems (Medium to Hard: Sliding Window, Graphs, Heaps)
           │
           ▼
[Stage 3: Technical Round 1 (Virtual / On-Campus)]
  ├── Duration: 45 - 60 Minutes
  ├── Focus: Live Coding (DSA), React.js internals, Python memory/async, MongoDB vs SQL.
  └── Deep-dive into past projects (Warehouse PathMapper heuristics, Uplan agents).
           │
           ▼
[Stage 4: Technical Round 2 & Low-Level Design (LLD)]
  ├── Duration: 45 - 60 Minutes
  ├── Focus: OOP Design Patterns, REST API Idempotency, Banking Ledger LLD, AWS Serverless.
  └── Concurrency, race conditions, database transactions (ACID vs BASE).
           │
           ▼
[Stage 5: Managerial & HR Round]
  ├── Duration: 30 - 45 Minutes
  ├── Focus: Citi Leadership Principles (Ownership, Delivering with Pride, Succeeding Together).
  └── Behavioral scenarios (STAR technique), conflict resolution, career aspirations.
```
