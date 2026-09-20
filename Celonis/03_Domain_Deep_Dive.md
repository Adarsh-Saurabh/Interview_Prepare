# 03: Process Mining & OCPM Deep Dive

## 1. What is Process Mining?
Process Mining is an analytical discipline that sits at the intersection of **Data Science** and **Business Process Management (BPM)**. It discovers, monitors, and improves real processes by extracting knowledge from event logs readily available in corporate IT systems.

```
Traditional BI (What happened?):    "Revenue fell 12% in Q3."
Process Mining (WHY did it happen?): "In 34% of orders, credit approval took 14 days due to manual paperwork loops between sales and finance."
```

---

## 2. The Three Pillars of Process Mining

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     1. Process Discovery        │   │    2. Conformance Checking      │   │     3. Process Enhancement      │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ Takes raw event log and outputs │   │ Compares real event log against │   │ Uses discovered bottlenecks to  │
│ an accurate, data-driven        │   │ a pre-defined standard model to │   │ optimize, automate, or redesign │
│ process model without human bias│   │ flag compliance violations.     │   │ operational execution steps.    │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```

### Signature Discovery Algorithms:
1. **Alpha Miner**: The foundational algorithm based on footprint causal dependencies ($a \rightarrow b$, $a \# b$, $a \parallel b$). Generates Petri nets but struggles with noise and loops.
2. **Heuristics Miner**: Uses frequency thresholds to filter out rare outliers and noisy paths, making it practical for real-world enterprise data.
3. **Inductive Miner**: The state-of-the-art discovery algorithm. Recursively splits the event log using process trees (sequence, choice, parallel, loop cuts), guaranteeing a deadlock-free model.

---

## 3. Object-Centric Process Mining (OCPM)

### The Legacy Problem: The 2D Case ID Limitation
In traditional process mining, every row must be tied to a single `case_id`. For example:
* If Case ID = `Order`, where does `Invoice` belong?
* One Purchase Order can contain **5 Order Lines**, which are delivered across **2 Shipments**, and billed in **3 separate Invoices**.
* Forcing multi-object processes into a single Case ID causes two fatal errors:
  1. **Convergence**: Artificially duplicating events for multiple objects.
  2. **Divergence**: Conflating distinct independent object lifecycles into a tangled web.

### The Celonis OCPM Solution:
Celonis pioneered **Object-Centric Process Mining (OCPM)** and the **OCEL (Object-Centric Event Log)** format:
* Events can be linked to **multiple objects simultaneously** (e.g. Event `Pack Box` relates to `Order #1`, `Item #A`, `Item #B`, and `Package #99`).
* Graphs model the true relational business execution fabric across the entire supply chain.

---

## 4. Process Query Language (PQL)
PQL is Celonis's domain-specific query language tailored for graph and process analytics over columnar data.
* Example calculation:
  ```sql
  CALC_THROUGHPUT(
      FIRST_OCCURRENCE['Receive Order'] TO LAST_OCCURRENCE['Clear Invoice'], 
      REMAP_TIMESTAMPS(DAYS)
  )
  ```
* Evaluated dynamically in-memory without materializing the graph ahead of time, allowing users to filter by vendor, region, or value instantly.
