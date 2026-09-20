# 00: Celonis Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Celonis SE** (Founded 2011 in Munich, Germany, by Alexander Rinke, Bastian Nominacher, and Martin Klenk from Technical University of Munich - TUM).
* **Valuation**: **$13 Billion+ Decacorn**, backed by premier venture capital firms including 83North, Accel, Arena Holdings, and T. Rowe Price.
* **Dual Headquarters**: Munich (Germany) & New York City (USA), with major global engineering hubs in **Bengaluru (India)**, Madrid, Pristina, and Tokyo.
* **Core Product**: Pioneer and uncontested global leader in **Process Mining** and the **Execution Management System (EMS)**.
* **Enterprise Customer Base**: Over 1,400+ leading enterprises globally, including Siemens, BMW, Uber, Dell, Cisco, L'Oréal, AstraZeneca, and Johnson & Johnson.

---

## 2. Core Architecture & Engineering Foundation

Celonis bridges the gap between raw enterprise IT transaction records and real-world operational execution:

```
[Enterprise Source Systems]
(SAP ERP, Salesforce, Oracle, ServiceNow, Workday)
         │
         │ Real-time & Batch Connectors (Kafka / CDC / APIs)
         ▼
[Data Extraction & Ingestion Engine]
         │ (Extract Event Logs: Case ID, Activity, Timestamp, Resource)
         ▼
[In-Memory Columnar Database & PQL Engine]
         │ (Process Query Language: Custom vector engine optimized for graphs)
         ▼
[Process Graph & Variant Discovery Layer]
         │ (Directed Graphs, Petri Nets, Inductive / Alpha Miner)
         ▼
[Execution Management System (EMS)]
  ├── Process Analytics (Bottlenecks, Cycle Time, Deviations)
  ├── Conformance Checking (Prescribed vs Actual Execution)
  ├── Action Engine (Automated Webhooks, Alerts, RPA triggers)
  └── Process Copilot (GenAI & LLM-assisted process queries)
```

### Key Technical Concepts to Know:
1. **The Event Log**: Every process starts with 3 mandatory columns:
   * **Case ID**: The unique identifier of a process instance (e.g., Purchase Order `#450012`).
   * **Activity**: The specific step completed (e.g., `Create PO`, `Approve PO`, `Goods Receipt`, `Pay Invoice`).
   * **Timestamp**: Exact UTC epoch when the activity transpired.
2. **Process Graph**: Directed graphs reconstructed from timestamp ordering across all cases. Nodes represent activities; edges represent process transitions with throughput times and transition frequencies.
3. **PQL (Process Query Language)**: Celonis's custom in-memory query language built in C++ and Java that evaluates graph calculations (e.g., `CALC_THROUGHPUT(ALL_RUNS)`) over billions of rows at sub-second response times.
4. **Object-Centric Process Mining (OCPM)**: Next-generation process intelligence that models multiple interacting business entities simultaneously (Orders, Items, Invoices, Deliveries) eliminating legacy 2D Case ID bottlenecks.

---

## 3. Placement Drive Specification (NIT Rourkela 2027 Batch)

| Parameter | Placement Drive Details |
| :--- | :--- |
| **Target Role** | **Associate Engineer** |
| **Location** | Bengaluru Tech Hub, India |
| **Compensation (CTC)** | **₹22.00 LPA Total**<br>• Fixed Base: ₹16.20 LPA<br>• Annual Performance Bonus: ₹1.80 Lakhs<br>• Sign-on Bonus: ₹4.00 LPA |
| **Internship Duration** | 6-Month Internship leading directly into Full-Time Employment (FTE) |
| **Eligible Batches** | 2027 (B.Tech, M.Tech, Dual Degree, Int MSc - All Branches eligible) |
| **Eligibility Criteria** | **CGPA $\ge 7.0$**, No Active Backlogs |
| **Application Deadline** | **11:59 PM, 23rd September 2026** |
| **Pre-Placement Talk (PPT)** | **24th September 2026** |
| **Online Assessment (OA)** | **25th September 2026** |
| **Personal Interviews** | **28th September 2026** |

---

## 4. The 3 Technical Pillars Evaluated at Celonis

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     1. Algorithmic Graph DSA    │   │  2. Concurrency & Core Systems  │   │  3. Enterprise SaaS & Backend   │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ • Directed Graph Traversal      │   │ • Multithreading & Race Conds   │   │ • RESTful API & Microservices   │
│ • DAG Topological Sorting       │   │ • Thread Pools & Synchronization│   │ • PostgreSQL & SQL Windowing    │
│ • Cycle Detection in Workflow   │   │ • Locks, Mutexes, CAS Atomics   │   │ • Multi-Tenant Data Isolation   │
│ • Sliding Window Burst Ingestion│   │ • JVM / C++ Memory Internals    │   │ • High-Throughput Buffers & LLD │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```
