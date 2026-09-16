# 00: CRED Company & Role Deep Dive

## 1. Executive Intelligence & Founding Thesis
CRED was founded in 2018 by **Kunal Shah** with a contrarian thesis on Indian economic friction:
- **The Low-Trust Deficit:** India historically operates as an asymmetric, low-trust economy. High verification costs, fraud risks, and regulatory friction lead to high borrowing rates and punitive terms for honest individuals.
- **The Flywheel of Creditworthiness:** CRED builds an exclusive, closed-loop network of India's top creditworthy individuals (traditionally requiring an Experian/CRIF credit score $\ge 750$). By aggregating affluent, high-trust users, CRED creates superior distribution power for financial institutions, luxury brands, and payment networks.
- **The Core Philosophy:** Reward good financial behavior, eliminate archaic friction, and scale a virtuous community where trust is mathematically and economically reinforced.

---

## 2. Business Ecosystem & Monetization
CRED operates across interconnected business verticals that generate immense financial and transactional telemetry:

| Vertical | Core Offering | Monetization & Unit Economics | ML / Data Science Touchpoint |
| :--- | :--- | :--- | :--- |
| **CRED Pay** | In-app UPI, card bill payments, and merchant 1-click checkout | Merchant Discount Rate (MDR) & interchange settlement fees | Real-time payment routing, transaction categorization, dynamic latency optimization |
| **CRED Cash** | Pre-approved, instant revolving personal credit lines | Revenue-share on lending interest & distribution fees with partner NBFCs (e.g. IDFC First Bank) | Probability of Default (PD), Exposure at Default (EAD), dynamic credit limit decisioning |
| **CRED Flash** | Buy-Now-Pay-Later (BNPL) for store checkout and utility bills | Merchant subsidy fees and late repayment charges | Sub-second micro-underwriting, checkout abandonment prediction |
| **CRED Garage** | Vehicle lifecycle management, FASTag recharge, traffic challans, insurance | FASTag interchange commission, vehicle insurance lead distribution | Document OCR & parsing, insurance renewal propensity modeling |
| **CRED Mint** | Peer-to-peer (P2P) investment lending platform with LiquiLoans | Platform spread / management fee between lenders and borrowers | Risk-adjusted matching algorithms, credit risk diversification |
| **CRED Store** | Curated member-exclusive D2C e-commerce marketplace | Merchant commission and sponsored discovery placement | Recommendation engines, dynamic pricing, user lifetime value (LTV) |

---

## 3. Scale Metrics & Technical Architecture

```
                               ┌───────────────────────────────────────────────┐
                               │            CRED Mobile Client (Flutter)       │
                               └───────────────────────┬───────────────────────┘
                                                       │ HTTPS / gRPC (Envoy)
                                                       ▼
                               ┌───────────────────────────────────────────────┐
                               │           API Gateway & Auth Service          │
                               └───────────────────────┬───────────────────────┘
                                                       │
                           ┌───────────────────────────┴───────────────────────────┐
                           ▼                                                       ▼
               ┌───────────────────────┐                               ┌───────────────────────┐
               │ Payment & Core Engine │                               │  ML Real-Time Engine  │
               │   (Go / Kotlin)       │                               │   (Python / Triton)   │
               └───────────┬───────────┘                               └───────────┬───────────┘
                           │ Event Stream                                          ▲
                           ▼                                                       │ Features (<10ms)
               ┌──────────────────────────────────────────────────┐                │
               │               Apache Kafka Event Bus             │                │
               └───────────┬───────────────────────────┬──────────┘                │
                           │                           │                           │
                           ▼                           ▼                           │
               ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────┴───────────┐
               │    Real-Time Stream   │   │     Data Lakehouse    │   │  Feast Feature Store  │
               │  (Apache Flink/Kafka) │   │ (Snowflake/ClickHouse)│   │     (Redis Cache)     │
               └───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

- **Member Base:** 13M+ affluent Indian consumers (~30–40% of all credit card bill payments in India).
- **Transaction Volume:** >$100B+ annualized Total Payment Volume (TPV); 350M+ annual card bills processed.
- **Latency SLAs:** Sub-15ms p99 SLA for real-time risk decisioning, payment fraud scoring, and transaction routing.
- **Core Technology Stack:**
  - **Languages:** Go (microservices), Kotlin/Java (payment state machines), Python (Data Science, ML training, Triton serving).
  - **Event Bus & Streaming:** Apache Kafka, Apache Flink for real-time event aggregation.
  - **Storage:** Amazon DynamoDB (low-latency key-value), PostgreSQL (ACID ledger/financial records), Redis (feature cache & distributed locks), ClickHouse & Snowflake (OLAP analytics & historical training data).
  - **ML Infrastructure:** Triton Inference Server, PyTorch, XGBoost/LightGBM, Feast Feature Store, MLflow, Evidently AI (model monitoring).

---

## 4. On-Campus Placement Details (NIT Rourkela)

- **Role:** Data Science and MLE Intern
- **Structure:** 6 Months Internship + Pre-Placement Offer (PPO)
- **Stipend:** ₹1,10,000 / month (1.1 LPM)
- **Full-Time Compensation (CTC):** ₹24.00 LPA (Tentative)
- **Eligible Batch & Degree:** Batch 2027, M.Tech (CS, EC, EE), CGPA $\ge 6.0$
- **Deadline:** 11:59 AM, 17th September 2026

---

## 5. The Exact On-Campus Hiring Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Resume Shortlisting                                                                      │
│    • Keyword matching: Data pipelines, ML deployment, LLMs/GenAI, low-latency algorithms    │
│    • Mandatory inclusion: Warehouse PathMapper, Uplan, Alternative Data Radar               │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 2. Online Assessment (OA) — HackerRank (90–105 Mins)                                        │
│    • 2–3 DSA / Algorithmic Coding Problems (Graphs, Monotonic Deque, Bitmask DP)             │
│    • Technical MCQs (Probability, Bayes Rule, Bias-Variance, Tree Split Math)                │
│    • 1–2 SQL Window Function Challenges (DENSE_RANK, LAG, Rolling Spend Growth)              │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 3. Technical Round 1: DSA + Machine Coding / Clean Code (60–90 Mins)                         │
│    • Live In-Memory Object-Oriented System Implementation (e.g. Feature Store Registry)     │
│    • Focus: SOLID principles, thread-safety, modular design, clean separation of concerns   │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 4. Technical Round 2: Data Science & ML Pipeline Architecture (60 Mins)                     │
│    • Deep grilling on resume projects: Mathematical formulation, latency, and tradeoffs    │
│    • Core ML: Loss functions, handling imbalanced fraud classes, feature selection           │
│    • System Design: Real-time credit underwriting / fraud detection architecture            │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 5. Managerial & HR Round: "Life at CRED" (45 Mins)                                          │
│    • Kunal Shah's leadership tenets: First-principles thinking, high autonomy               │
│    • "No designations": Ability to work through ambiguity and own business outcomes         │
│    • 4 STAR behavioral stories defending candidate engineering decisions                    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```
