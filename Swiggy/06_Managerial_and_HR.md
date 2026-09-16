# 06: Life at Swiggy & Cultural Values

Swiggy assesses cultural alignment through its **Core Leadership Values**. Candidates must demonstrate a founder's mindset, customer empathy, and comfort with rapid experimentation.

---

## 1. Swiggy's Core Leadership Values

1. **Consumer Comes First:** In any conflict between short-term monetization and customer trust, customer trust wins. (e.g. accurate ETAs are better than unrealistically short ETAs that cause frustration).
2. **Always Curious, Always Learning:** Relentlessly experimenting with new AI architectures (GNNs, two-tower embeddings, LLM agentic search).
3. **Bias for Action:** In fast-paced hyperlocal markets, speed is of the essence. Perfect is the enemy of good. Deploy, measure, and iterate.
4. **Displaying Founder's Mentality:** Taking extreme ownership. If deliveries fail during torrential rain, you don't blame the weather; you optimize geospatial routing.
5. **Think Win-Win:** Balancing the delicate three-sided marketplace: Customers, Delivery Partners, and Restaurant Partners.
6. **Honest, Transparent Communication:** Being intellectually honest about model flaws and evaluation metrics.

---

## 2. STAR Behavioral Defense Scenarios for Adarsh Saurabh

### Question 1: "Tell me about a time you faced ambiguous technical requirements and had to deliver on a deadline."
- **Situation:** During the development of *Uplan* (Multi-Agent System for Document Verification), our goal was to verify complex cross-document constraints, but there was no labeled dataset or standard ground truth benchmark.
- **Task:** I needed to architect an automated, reliable verification pipeline within the 48-hour hackathon timeframe.
- **Action:** Instead of chasing complex fine-tuning without data, I exercised a strong *Bias for Action*. I architected an adversarial multi-agent system using LangGraph: one agent acted as an extraction specialist, while an auditor agent checked for mathematical consistency and hallucination flags. To ensure deterministic accuracy, I engineered a graph-encoding layer that compressed metadata into semantic representations.
- **Result:** Cut manual auditing overhead by 85% with explainable failure rebuttals, winning recognition at the AMD Developer Hackathon.

### Question 2: "Describe a situation where you had to make a trade-off between model accuracy and system latency."
- **Situation:** In *Warehouse PathMapper*, calculating the exact globally optimal TSP trajectory across 10,000 coordinates using mixed-integer linear programming (MILP) took several minutes per calculation, making it useless for real-time interactive routing.
- **Task:** Balance the path optimality against a sub-second execution requirement.
- **Action:** I replaced exhaustive MILP solving with a multi-level hierarchical heuristic: partitioning the grid into coarse clusters, computing cluster-to-cluster transfers using precomputed lookup tables, and using local A* search for fine-grained steps.
- **Result:** Path length was within 2.3% of the theoretical global optimum, while computation time dropped from 3 minutes to $<0.5$ seconds—a $360	imes$ speedup that enabled real-time deployment.
