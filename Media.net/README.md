# 3-Day Intensive Study Roadmap: Media.net SDE Intern

A focused, hour-by-hour preparation schedule designed to maximize conversion probability for Media.net's Online Assessment and Technical Interview rounds.

---

## Day 1: Algorithmic Rigor & Speedrun (OA Mastery)

### Morning (09:00 – 13:00): Core Dynamic Programming & Heaps
* **Module Review**: Study `01_Online_Test.html` (Problem 1: Top-K Vickrey Auction, Problem 4: Weighted Interval Scheduling).
* **Practice on LeetCode / InterviewBit**:
  * LeetCode 295: Find Median from Data Stream (Two Heaps pattern).
  * LeetCode 1235: Maximum Profit in Job Scheduling (Binary Search + DP).
  * LeetCode 300: Longest Increasing Subsequence ($O(N \log N)$ patience sorting).

### Afternoon (14:00 – 18:00): Graphs & Advanced Traversal
* **Module Review**: Study `01_Online_Test.html` (Problem 5: DAG Critical Path & Cycle Detection).
* **Practice**:
  * Kahn's Algorithm for Topological Sort & Cycle Detection in Directed Graphs.
  * Dijkstra's Algorithm with `std::priority_queue` and path reconstruction.
  * Disjoint Set Union (DSU) with Path Compression and Union by Rank.

### Evening (19:00 – 22:30): Strings & Wildcard Tries
* **Module Review**: Study `01_Online_Test.html` (Problem 2: Wildcard Trie Contextual Matcher).
* **Timed Mock Assessment**: Solve 3 problems in 90 minutes on InterviewBit without IDE assistance.

---

## Day 2: Systems, Memory, OS, Networks & LLD

### Morning (09:00 – 13:00): Operating Systems Internals
* **Module Review**: Study `02_Technical_Rounds.html` (Section 1: Process vs Thread, Virtual Memory, Paging, Mutex vs Spinlock).
* **Hands-On**: Write a multithreaded Producer-Consumer queue in C++ using `std::mutex` and `std::condition_variable`.
* **Deep Review**: Deadlocks (4 Coffman conditions), page fault handling, TLB hit/miss latency.

### Afternoon (14:00 – 18:00): Computer Networks & DBMS Internals
* **Module Review**: Study `02_Technical_Rounds.html` (Section 2 & 3: TCP Keep-Alive, TIME_WAIT socket exhaustion, HTTP/2 multiplexing, B+ Tree indexing, ACID isolation levels).
* **SQL Query Drill**: Write queries for $N$-th highest salary (`DENSE_RANK()`), self-joins, and aggregations.

### Evening (19:00 – 22:30): Low-Level Design (Machine Coding)
* **Module Review**: Study `05_System_Design_or_HIL.html` (Section 1: Thread-Safe LRU Cache with TTL).
* **Code from Scratch**: Write, compile, and execute an LRU cache with expiration in clean, modular C++ without looking at reference code.

---

## Day 3: Ad-Tech Architecture & Resume Defense

### Morning (09:00 – 13:00): Ad-Tech Domain & Low-Latency HLD
* **Module Review**: Study `03_Domain_Deep_Dive.html` and `05_System_Design_or_HIL.html` (OpenRTB 2.5 spec, Sub-50ms SLA budget, Header Bidding vs Waterfall, Redis Bitmaps, HyperLogLog, Bloom filters).
* **System Design Practice**: Walk through the Real-Time Bidding Auction Coordinator architecture end-to-end.

### Afternoon (14:00 – 18:00): Candidate Resume Defense & Grilling Traps
* **Module Review**: Study `04_Candidate_Resume_Grilling.html`.
* **Verbal Rehearsal**:
  * Practice the 2-minute elevator pitch for **Warehouse PathMapper** (explain why topological abstraction beats raw grid search).
  * Practice the defense of **Uplan** against the Media.net AI clause (explain deterministic mathematical validation vs LLM non-determinism).
  * Practice defending your **M.Tech Signal Processing + B.Tech CSE** dual background.

### Evening (19:00 – 21:30): Rapid Recall & Behavioral Fit
* **Module Review**: Study `06_Managerial_and_HR.html` and `07_Quick_Reference.html`.
* **Mental Rehearsal**: Review the STAR stories for production bugs, technical disagreements, and leadership under pressure.
