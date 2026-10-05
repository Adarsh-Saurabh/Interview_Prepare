# modules_part1.py: Modules 00, 01, 02

modules_part1 = {}

# =============================================================================
# MODULE 00: Company & Role Intel
# =============================================================================
modules_part1["00_START_HERE"] = {
    "title": "00: Media.net Company & Role Intelligence",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Media.net Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Media.net** (A Directi legacy company, founded by Divyank Turakhia; acquired by Miteno / Starry Media for $900M; leading global ad-tech giant).
* **Campus Placement Drive**: National Institute of Technology, Rourkela (Batch 2027).
* **Internship Model**: **6 Months Internship + Pre-Placement Offer (PPO) Conversion**.
* **Offered Job Role**: **Software Development Engineer (SDE) Intern**
* **Compensation Structure**:
  * **Monthly Stipend**: **₹1,00,000 / month (1 LPM)**
  * **CTC on PPO Conversion**: **18L Fixed + 4L One-Time Bonus + 16L Additional Bonus** (~38 LPA total compensation).
* **Eligible Branches & Degrees**: B.Tech, M.Tech, Dual Degree, Int MSc — All Branches (CGPA $\\ge 6.0$, No active backlogs).
* **Major Engineering Centers**:
  * **Mumbai**: Directiplex, Andheri East (Core ad-serving engine, RTB infrastructure, low-latency DSP/SSP platforms).
  * **Bengaluru**: Global Technology Park, Bellandur (Contextual AI/ML matching, analytics, publisher growth).
  * **International HQs**: Dubai (Global HQ), New York (US HQ), Zurich, Los Angeles.

---

## 2. Media.net's Core Engineering & Ad-Tech Scale

Media.net is not a conventional web-application company. It operates one of the highest-throughput, lowest-latency distributed systems on the internet:

```
                  ┌──────────────────────────────────────────────┐
                  │          Media.net Ad-Tech Scale             │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│  500,000+ Sites  │           │   Sub-50ms SLA   │           │ Contextual Brain │
│ Publishers across│           │ Hard timeout on  │           │ Keyword NLP &    │
│ global internet  │           │ RTB auction bids │           │ Page Semantics   │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

1. **Contextual Advertising Pioneer**: Media.net pioneered deep contextual analysis without relying on third-party cookie tracking. It analyzes page content, natural language tokens, user intent, and publisher taxonomies in real-time to match high-value ads.
2. **Yahoo! Bing Network Partnership**: Media.net exclusively powers the Yahoo! Bing Network contextual ads program, monetizing publisher traffic with search and native intent.
3. **The Sub-50ms RTB Constraint**: When an ad slot loads on Forbes or CNN, an auction request triggers across hundreds of DSPs (Demand-Side Platforms). The whole pipeline—bid request serialization, network transport, DSP bid evaluation, second-price auction resolution, fraud filtering, and creative delivery—must complete in **under 50 milliseconds**.
4. **Engineering Stack**:
   * **Core Languages**: Java, C++, Python, Scala.
   * **Real-Time Streaming**: Apache Kafka (millions of events/sec), Apache Flink, Apache Spark.
   * **In-Memory & Storage**: Redis, Aerospike, MySQL, Elasticsearch, HDFS.
   * **Cloud & Edge**: Kubernetes, Docker, Bare-metal edge clusters in tier-1 data centers worldwide.

---

## 3. The 4 Recruitment Stages & Exact Evaluation Criteria

The on-campus selection pipeline is renowned for having one of the highest technical bars in India:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Stage 1: OA   │ ──► │  Round 1: DSA   │ ──► │ Round 2: Tech & │ ──► │  Round 3: HR &  │
│  InterviewBit   │     │  Live Coding &  │     │ CS Core + Proj  │     │   Culture Fit   │
│  (90 Minutes)   │     │  Unassisted CP  │     │  & AI Judgement │     │  (20 Minutes)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stage 1: Online Assessment (90 Minutes)
* **Platform**: Usually **InterviewBit** or **HackerEarth**.
* **Structure**: 3 Competitive Programming (CP) problems (Medium to Hard).
* **Core Topics**: Dynamic Programming (DP on grids, bitmask, knapsack), Graph Traversals (Dijkstra, Topological Sort, Shortest Path with constraints), Disjoint Set Union (DSU), Segment Trees, Binary Search on Answer, Bit Manipulation.
* **Plagiarism Filter**: **Extremely aggressive automated plagiarism detection**. Code structure, AST similarities, and identical variable patterns result in immediate disqualification. Write clean, authentic, unassisted code.

### Stage 2: Technical Round 1 — Problem Solving & Live Coding (60 Minutes)
* **Format**: 1-on-1 interview on a shared collaborative editor (Google Docs or Codeshare, no autocomplete or IDE assistance).
* **Focus**: 1 to 2 Hard/Medium DSA problems.
* **Expectations**:
  1. Clarify constraints and edge cases immediately before writing code.
  2. Explain the brute-force baseline ($O(N^2)$ or $O(2^N)$), then systematically optimize to $O(N \\log N)$ or $O(N)$.
  3. Write production-quality, bug-free C++ or Python code with descriptive naming and modular helper functions.
  4. Rigorously trace edge cases: empty inputs, single element, large numbers ($10^9$), duplicates, and negative numbers.

### Stage 3: Technical Round 2 — CS Fundamentals, Projects & AI Judgement (60 Minutes)
* **Format**: 60 minutes with a Senior Architect / Engineering Manager.
* **Core CS Fundamentals**:
  * **Operating Systems**: Process vs Thread memory layouts, context switching overhead, virtual memory, paging & page tables, mutex vs semaphore, deadlocks (Coffman conditions), condition variables.
  * **Computer Networks**: TCP vs UDP in real-time ad bidding, 3-way handshake, TCP connection teardown (TIME_WAIT state), socket exhaustion, HTTP/1.1 vs HTTP/2 multiplexing, DNS lookup steps.
  * **DBMS**: B+ Tree indexing mechanics, Clustered vs Non-Clustered index, composite index left-to-right rule, ACID transactions, isolation levels (Dirty Read, Phantom Read), Write-Ahead Logging (WAL), SQL window functions (`DENSE_RANK()`).
* **Project Deep Dive & Engineering Judgement**:
  * Deep defense of candidate projects: **Warehouse PathMapper** (heuristic routing), **Uplan** (adversarial multi-agent intelligence), and **Alternative Data Radar** (automated scraping & SQL health score).
  * **The AI Tools Evaluation Directive**: The JD states explicitly:
    > *"Interviews and the online assessment evaluate unassisted problem-solving. Your fluency with AI tools is assessed separately, through how you talk about the projects you've built with them."*
  * Interviewers will grill whether you genuinely understand your project's low-level mechanics or merely pasted prompts into an LLM.

### Stage 4: HR & Cultural Fit Round (20 Minutes)
* **Format**: Behavioral assessment with HR or Engineering Director.
* **Focus**: Directi/Media.net values: Ownership, intellectual curiosity, resilience under pressure, learning from mistakes, and handling high-scale engineering challenges.

---

## 4. Key Strengths to Project in Interviews

1. **Unassisted Algorithmic Agility**: Prove you can derive optimal algorithms from first principles without Copilot or IDE suggestions.
2. **Systems-First Mental Model**: Relate high-level code to hardware realities—CPU cache lines, memory locality, socket limits, and disk I/O.
3. **Engineering Judgement with AI**: Discuss AI as a multiplier (rapid prototyping, synthetic data generation, test harness generation), while emphasizing personal ownership of verification, mathematical deterministic rule engines, and code reliability.
"""
}

# =============================================================================
# MODULE 01: Signature OA Coding Problems
# =============================================================================
modules_part1["01_Online_Test"] = {
    "title": "01: Signature OA & Live Coding Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company & Role Intel",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: Systems, Memory, OS & Networks",
    "markdown": """# 01: Signature OA & Live Coding Problems

Media.net's Online Assessment (InterviewBit) and Technical Round 1 demand unassisted, bug-free implementations of non-trivial algorithmic problems under strict time constraints. Below are 5 signature algorithmic problems derived from real Media.net recruitment drives, complete with optimal Python and C++ implementations, complexity proofs, and edge-case test suites.

---

## Problem 1: Real-Time Bidding Top-K Vickrey Second-Price Auction

### Problem Statement
In an ad exchange auction, $N$ DSPs submit bids for $K$ available ad placements ($1 \\le K \\le N$). Each bid contains:
* `dsp_id` (string)
* `bid_price` (float in USD CPM)
* `timestamp_ms` (integer timestamp)

An ad unit is cleared using a **Generalized Second-Price (GSP) Auction**:
1. The top $K$ highest bidders win the slots.
2. Ties in bid price are broken by earliest `timestamp_ms`. If timestamps match, alphabetical order of `dsp_id`.
3. The $i$-th winner ($1 \\le i < K$) pays the bid price of the $(i+1)$-th bidder (second price).
4. The $K$-th winner pays the reserve price $R$ (or $(K+1)$-th bid if available, whichever is higher).

Return the list of winning DSPs with their assigned clearing prices.

### Algorithmic Approach
* **Brute Force**: Full sorting of $N$ bids takes $O(N \\log N)$. When $N = 10^6$ and $K \\ll N$ (e.g. $K=5$), sorting the entire stream wastes memory and CPU cache.
* **Optimal Approach**: Maintain a Min-Heap of size $K+1$. For each incoming bid, push into heap; if size exceeds $K+1$, pop the smallest.
* **Complexity**:
  * **Time**: $O(N \\log K)$ time.
  * **Space**: $O(K)$ space.

### Python 3 Production Solution
```python
import heapq
from typing import List, Tuple, Dict, Any

class Bid:
    def __init__(self, dsp_id: str, price: float, timestamp_ms: int):
        self.dsp_id = dsp_id
        self.price = price
        self.timestamp_ms = timestamp_ms

    def __lt__(self, other: 'Bid') -> bool:
        # Min-heap comparison: lower price is evicted first.
        # Tie breaker: later timestamp evicted first.
        if abs(self.price - other.price) > 1e-6:
            return self.price < other.price
        if self.timestamp_ms != other.timestamp_ms:
            return self.timestamp_ms > other.timestamp_ms
        return self.dsp_id > other.dsp_id

def resolve_gsp_auction(bids_data: List[Tuple[str, float, int]], K: int, reserve_price: float) -> List[Dict[str, Any]]:
    \"\"\"
    Resolves Generalized Second-Price (GSP) auction for K slots.
    Time Complexity: O(N log K)
    Space Complexity: O(K)
    \"\"\"
    if not bids_data or K <= 0:
        return []

    # Filter bids below reserve price
    valid_bids = [Bid(dsp, price, ts) for dsp, price, ts in bids_data if price >= reserve_price]
    if not valid_bids:
        return []

    # Maintain top K + 1 bids in min-heap to determine K-th slot clearing price
    heap = []
    for bid in valid_bids:
        heapq.heappush(heap, bid)
        if len(heap) > K + 1:
            heapq.heappop(heap)

    # Extract all elements from heap (ascending order)
    top_candidates = []
    while heap:
        top_candidates.append(heapq.heappop(heap))
    
    # Reverse to get descending order: index 0 is 1st place
    top_candidates.reverse()

    winners_count = min(K, len(top_candidates))
    results = []

    for i in range(winners_count):
        winner = top_candidates[i]
        if i + 1 < len(top_candidates):
            clearing_price = max(top_candidates[i + 1].price, reserve_price)
        else:
            clearing_price = reserve_price
            
        results.append({
            "rank": i + 1,
            "dsp_id": winner.dsp_id,
            "bid_price": winner.price,
            "clearing_price": round(clearing_price, 4)
        })

    return results

if __name__ == '__main__':
    sample_bids = [
        ("DSP_Alpha", 4.50, 100),
        ("DSP_Beta", 6.20, 105),
        ("DSP_Gamma", 6.20, 95),   # Same price as Beta, earlier timestamp
        ("DSP_Delta", 2.10, 110),
        ("DSP_Epsilon", 5.80, 102)
    ]
    winners = resolve_gsp_auction(sample_bids, K=2, reserve_price=3.00)
    for w in winners:
        print(w)
```

### C++20 Optimal Implementation
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
#include <iomanip>

struct Bid {
    std::string dsp_id;
    double price;
    int64_t timestamp_ms;

    // Strict weak ordering for Min-Heap (lowest priority on top)
    bool operator>(const Bid& other) const {
        if (std::abs(price - other.price) > 1e-6)
            return price > other.price;
        if (timestamp_ms != other.timestamp_ms)
            return timestamp_ms < other.timestamp_ms; // earlier timestamp is higher priority
        return dsp_id < other.dsp_id;
    }
};

struct AuctionResult {
    int rank;
    std::string dsp_id;
    double bid_price;
    double clearing_price;
};

std::vector<AuctionResult> resolveGSPAuction(
    const std::vector<Bid>& bids, int K, double reserve_price) {
    
    std::priority_queue<Bid, std::vector<Bid>, std::greater<Bid>> min_heap;

    for (const auto& bid : bids) {
        if (bid.price < reserve_price) continue;
        min_heap.push(bid);
        if (min_heap.size() > static_cast<size_t>(K + 1)) {
            min_heap.pop();
        }
    }

    std::vector<Bid> sorted_bids;
    while (!min_heap.empty()) {
        sorted_bids.push_back(min_heap.top());
        min_heap.pop();
    }
    std::reverse(sorted_bids.begin(), sorted_bids.end());

    std::vector<AuctionResult> results;
    int winners_count = std::min(K, static_cast<int>(sorted_bids.size()));

    for (int i = 0; i < winners_count; ++i) {
        double clearing = (i + 1 < static_cast<int>(sorted_bids.size())) 
                          ? std::max(sorted_bids[i + 1].price, reserve_price)
                          : reserve_price;
        results.push_back({i + 1, sorted_bids[i].dsp_id, sorted_bids[i].price, clearing});
    }
    return results;
}
```

---

## Problem 2: Contextual Keyword Matching with Inverted Index & Wildcard Trie

### Problem Statement
Media.net processes millions of publisher articles and extracts key phrases. Advertisers bid on keyword patterns which may contain wildcard operators:
* `?`: Matches exactly one arbitrary character.
* `*`: Matches zero or more arbitrary characters.

Given a dictionary of advertiser target patterns and article tokens, design a high-throughput matching engine returning all campaign IDs matching a given article keyword.

### Algorithmic Approach
* **Data Structure**: Prefix Trie with wildcard branch resolution.
* **Time Complexity**:
  * Pattern insertion: $O(L)$ where $L$ is pattern length.
  * Search: $O(2^L)$ worst case for degenerate `*`, but $O(L)$ average case with pruning.

### Python 3 Production Solution
```python
from typing import Dict, List, Set

class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.campaign_ids: List[int] = []

class ContextualPatternMatcher:
    def __init__(self):
        self.root = TrieNode()

    def insert_pattern(self, pattern: str, campaign_id: int):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.campaign_ids.append(campaign_id)

    def search_matches(self, word: str) -> List[int]:
        results: Set[int] = set()

        def dfs(node: TrieNode, word_idx: int):
            if word_idx == len(word):
                for cid in node.campaign_ids:
                    results.add(cid)
                if '*' in node.children:
                    dfs(node.children['*'], word_idx)
                return

            char = word[word_idx]

            # 1. Exact match
            if char in node.children:
                dfs(node.children[char], word_idx + 1)

            # 2. '?' single character wildcard
            if '?' in node.children:
                dfs(node.children['?'], word_idx + 1)

            # 3. '*' multi-character wildcard
            if '*' in node.children:
                star_node = node.children['*']
                # Case A: match 0 characters
                dfs(star_node, word_idx)
                # Case B: match 1+ characters
                dfs(star_node, word_idx + 1)

        dfs(self.root, 0)
        return sorted(list(results))

if __name__ == '__main__':
    matcher = ContextualPatternMatcher()
    matcher.insert_pattern("cloud*", 101)
    matcher.insert_pattern("cl?ud", 102)
    matcher.insert_pattern("hosting", 103)
    matcher.insert_pattern("*server*", 104)

    print("Matches for 'cloud':", matcher.search_matches("cloud"))   # [101, 102]
    print("Matches for 'cloudy':", matcher.search_matches("cloudy")) # [101]
```

---

## Problem 3: Sliding Window Rate Limiter & Frequency Capper

### Problem Statement
In digital ad delivery, **Frequency Capping** limits how often a specific advertisement is shown to the same user within a rolling time window $W$ (e.g., at most $M$ impressions per 60 seconds). Implement an in-memory frequency capper supporting:
`record_and_check(user_id: str, campaign_id: str, timestamp_sec: int) -> bool`

### Algorithmic Approach
* **Data Structure**: Hash Map mapping `(user_id, campaign_id)` to a double-ended queue storing timestamps.
* **Complexity**:
  * Evict timestamps $< (timestamp - W)$.
  * If queue size $< M$: append timestamp, return `True`.
  * Amortized Time: $O(1)$ per query.
  * Space: $O(U \\times M)$.

### C++20 Thread-Safe Implementation
```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <deque>
#include <mutex>

class FrequencyCapper {
private:
    const int max_impressions_;
    const int window_seconds_;
    std::unordered_map<std::string, std::deque<int64_t>> records_;
    mutable std::mutex mtx_;

public:
    FrequencyCapper(int max_impressions, int window_seconds)
        : max_impressions_(max_impressions), window_seconds_(window_seconds) {}

    bool recordAndCheck(const std::string& user_id, const std::string& campaign_id, int64_t current_time) {
        std::lock_guard<std::mutex> lock(mtx_);
        std::string key = user_id + "#" + campaign_id;
        auto& dq = records_[key];

        int64_t window_start = current_time - window_seconds_;

        while (!dq.empty() && dq.front() <= window_start) {
            dq.pop_front();
        }

        if (static_cast<int>(dq.size()) < max_impressions_) {
            dq.push_back(current_time);
            return true;
        }
        return false;
    }
};
```

---

## Problem 4: Maximum Revenue Non-Overlapping Ad Slot Scheduling

### Problem Statement
An online publisher has $N$ advertiser campaigns bidding for exclusive display on their homepage banner. Each campaign $i$ specifies:
* `start_time` $S_i$, `end_time` $E_i$, `revenue` $V_i$.
Maximize total non-overlapping revenue.

### Mathematical Formulation
**Weighted Interval Scheduling**:
1. Sort campaigns by `end_time` ascending.
2. For each campaign $i$, binary search for latest compatible campaign $p(i)$ where $E_{p(i)} \\le S_i$.
3. Recurrence:
   $$DP[i] = \\max\\left(DP[i-1], V_i + DP[p(i)]\\right)$$
4. Complexity: Time $O(N \\log N)$, Space $O(N)$.

### Python 3 Solution
```python
import bisect
from typing import List, Tuple

def max_ad_campaign_revenue(campaigns: List[Tuple[int, int, int]]) -> int:
    if not campaigns:
        return 0

    sorted_campaigns = sorted(campaigns, key=lambda x: x[1])
    n = len(sorted_campaigns)
    end_times = [c[1] for c in sorted_campaigns]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        curr_start, curr_end, curr_val = sorted_campaigns[i - 1]
        idx = bisect.bisect_right(end_times, curr_start)
        dp[i] = max(dp[i - 1], curr_val + dp[idx])

    return dp[n]
```

---

## Problem 5: Ad Delivery DAG Cycle Detection & Critical Path Latency

### Problem Statement
In an ad-rendering pipeline, $N$ enrichment tasks form a directed acyclic graph. Each task has latency $L_i$ ms. Detect cycles and find the maximum latency path (Critical Path).

### C++20 Optimal Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

struct PipelineAnalysis {
    bool has_cycle;
    int critical_path_latency_ms;
    std::vector<int> topo_order;
};

PipelineAnalysis analyzeAdPipeline(int n, const std::vector<int>& latencies, const std::vector<std::pair<int, int>>& dependencies) {
    std::vector<std::vector<int>> adj(n);
    std::vector<int> in_degree(n, 0);

    for (const auto& [u, v] : dependencies) {
        adj[u].push_back(v);
        in_degree[v]++;
    }

    std::queue<int> q;
    std::vector<int> completion_time = latencies;

    for (int i = 0; i < n; ++i) {
        if (in_degree[i] == 0) q.push(i);
    }

    std::vector<int> topo_order;
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        topo_order.push_back(curr);

        for (int neighbor : adj[curr]) {
            completion_time[neighbor] = std::max(
                completion_time[neighbor], 
                completion_time[curr] + latencies[neighbor]
            );
            if (--in_degree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }

    if (static_cast<int>(topo_order.size()) < n) {
        return {true, -1, {}}; // Cycle detected
    }

    int max_latency = 0;
    for (int t : completion_time) max_latency = std::max(max_latency, t);

    return {false, max_latency, topo_order};
}
```
"""
}

# =============================================================================
# MODULE 02: Systems, Memory, OS, Networks & DBMS
# =============================================================================
modules_part1["02_Technical_Rounds"] = {
    "title": "02: Systems, Memory, OS, Networks & DBMS",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Coding Problems",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Ad-Tech & RTB Systems",
    "markdown": """# 02: Systems, Memory, OS, Networks & DBMS

Technical Round 2 at Media.net is famous for deep architectural grilling on core Computer Science fundamentals. You will not pass by reciting textbook definitions—interviewers probe memory layout, latency trade-offs, kernel boundaries, and concurrency pitfalls.

---

## 1. Operating Systems: Deep Mechanics

```
┌─────────────────────────────────────────────────────────────────┐
│                    Virtual Address Space                        │
├──────────────┬──────────────┬──────────────┬────────────────────┤
│  Text / Code │ Data (BSS)   │  Heap (▲)    │  Stack (▼)         │
│  (Read-Only) │ Global / Var │  malloc / new│  Local / Ptrs / RA │
└──────────────┴──────────────┴──────────────┴────────────────────┘
```

### A. Process vs. Thread: Low-Level Reality
* **Process**: An independent instance of an executing program with its own isolated **Virtual Address Space**, page tables, file descriptor tables, and Process Control Block (PCB).
  * Context switch cost: High (typically 1–3 $\\mu s$). Forces invalidation of CPU Translation Lookaside Buffer (TLB), triggering cache misses and pipeline stalls.
* **Thread**: A unit of CPU execution within a process. Threads of the same process share the text, data, and heap segments, file descriptors, and socket handles, but possess their own **Program Counter (PC)**, registers, and private **Stack**.
  * Context switch cost: Low (~100–300 ns). Page tables remain mapped; TLB entries remain valid.

### B. Virtual Memory, Paging & TLB
* **Virtual Address Translation**: When CPU issues a virtual memory address, the Memory Management Unit (MMU) uses the CR3 register to traverse the multi-level page table (e.g., 4-level paging on x86-64: PML4 $\\to$ PDP $\\to$ PD $\\to$ PT $\\to$ Physical Frame).
* **Translation Lookaside Buffer (TLB)**: An ultra-fast hardware cache of virtual-to-physical address mappings.
* **Page Fault**: Triggered by hardware interrupt when a virtual page is accessed that is either unmapped or paged out to swap disk. The kernel suspends the thread, loads the 4KB page from disk into RAM, updates the page table, and resumes execution.

### C. Concurrency: Mutex vs. Spinlock vs. Semaphore
| Mechanism | Blocking Behavior | When to Use at Media.net |
| :--- | :--- | :--- |
| **Mutex** | Puts waiting thread into kernel sleep (`futex` wait); yields CPU. | Critical sections lasting $> 500$ ns or involving I/O. |
| **Spinlock** | Busy-loops in user space burning CPU cycles (`PAUSE` instruction). | Ultra-low-latency in-memory RTB locks lasting $< 50$ ns. |
| **Counting Semaphore** | Maintains an integer counter; permits up to $N$ concurrent threads. | Resource pool throttling (e.g., maximum 50 concurrent DSP connections). |

### D. Deadlocks: The 4 Coffman Conditions
A deadlock can occur **if and only if** all four conditions hold simultaneously:
1. **Mutual Exclusion**: Resources cannot be shared.
2. **Hold and Wait**: Process holding a resource requests another.
3. **No Preemption**: Resources cannot be forcibly revoked.
4. **Circular Wait**: $P_1$ waits for $P_2$, ..., $P_n$ waits for $P_1$.
* **Deadlock Prevention Strategy**: Enforce a strict **global lock acquisition hierarchy** (always acquire Lock A before Lock B) to break Circular Wait.

---

## 2. Computer Networks: Real-Time Bidding Protocol Mechanics

```
Client / Browser             Media.net Edge SSP                 DSP Partner
     │                                │                              │
     │─── HTTP GET /ad_request ──────►│                              │
     │                                │─── TCP Handshake (SYN) ─────►│
     │                                │◄── SYN-ACK ──────────────────│
     │                                │─── ACK + OpenRTB Bid Req ───►│ (Hard 25ms timer)
     │                                │◄── OpenRTB Bid Response ─────│
     │◄── Ad Markup (HTML/JS) ────────│                              │
```

### A. TCP vs. UDP in Low-Latency Ad Bidding
* **Why RTB uses TCP**: Even though UDP has zero handshake overhead, financial transactions (ad impressions costing millions of dollars) require guaranteed packet delivery and data integrity. Losing bid responses causes revenue discrepancy and billing disputes.
* **Mitigating TCP Latency**: Media.net uses **Long-Lived Persistent TCP Connections (Keep-Alive)** and HTTP/2 connection pooling with DSPs. The 3-way handshake is performed once at startup, eliminating the 1-RTT handshake penalty during real-time auctions.

### B. TCP Connection Teardown & The `TIME_WAIT` Danger
* **The 4-Way FIN Handshake**: Initiator sends `FIN` $\\to$ Responder sends `ACK` $\\to$ Responder sends `FIN` $\\to$ Initiator sends `ACK` $\\to$ Initiator enters `TIME_WAIT`.
* **Duration**: $2 \\times \\text{MSL}$ (Maximum Segment Life, typically 60 seconds).
* **The Danger at Scale**: In an SSP processing 50,000 req/sec, closing connections naively creates tens of thousands of sockets trapped in `TIME_WAIT`. This exhausts the ephemeral port range ($1024 - 65535$), throwing `EADDRNOTAVAIL` (connection refused).
* **Production Fix**: Enable `SO_REUSEADDR`, implement connection pooling, and tune `net.ipv4.tcp_tw_reuse = 1`.

### C. HTTP/1.1 vs. HTTP/2 in Ad Exchanges
* **HTTP/1.1**: Suffers from **Head-of-Line (HoL) Blocking** at the application layer. Each HTTP request must wait for the previous response unless multiple TCP connections are opened.
* **HTTP/2**: Introduces **Binary Framing** and **Stream Multiplexing**. Hundreds of bid requests and responses travel concurrently over a single TCP connection, interleaved in independent streams with stream prioritization.

---

## 3. Database Management Systems (DBMS) Internals

### A. B-Tree vs. B+ Tree Indexing
Media.net relies heavily on MySQL (InnoDB) and custom distributed indexes.
* **Why B+ Trees Beat B-Trees for Disk & SSD Storage**:
  1. **Higher Fan-out**: Internal nodes in a B+ Tree store only keys and child pointers (no row data). This allows thousands of keys to fit into a single 16KB disk page, keeping the tree height shallow ($h \\le 3$ for millions of rows).
  2. **Sequential Leaf Traversal**: All leaf nodes are linked in a bidirectional doubly-linked list. Range scans (e.g., `WHERE timestamp BETWEEN t1 AND t2`) require one $O(\\log N)$ tree traversal to find the start, then linear linked-list traversal, avoiding costly random I/O.

### B. Clustered vs. Secondary (Non-Clustered) Index
* **Clustered Index**: The leaf pages *are* the actual data pages. The physical table rows are sorted and stored in primary key order. A table can have **only one** clustered index.
* **Secondary Index**: Leaves store the indexed column value plus the primary key pointer.
* **Double Lookup (Bookmark Lookup)**: Querying by a secondary index (`WHERE email = ?`) first navigates the secondary index to find the primary key, then navigates the clustered index to retrieve full row data.
* **Covering Index Optimization**: If a secondary index includes all required columns (`SELECT user_id, campaign_id FROM impressions WHERE user_id = ?`), the engine avoids the second lookup entirely.

### C. ACID Properties & Isolation Levels
* **Dirty Read**: Reading uncommitted data that is later rolled back.
* **Non-Repeatable Read**: Re-reading the same row returns different values because another transaction committed an `UPDATE`.
* **Phantom Read**: Re-running a range query returns newly inserted rows committed by another transaction.

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Mechanism |
| :--- | :---: | :---: | :---: | :--- |
| **Read Uncommitted** | Yes | Yes | Yes | Dirty reads allowed; no shared locks. |
| **Read Committed** | No | Yes | Yes | MVCC snapshot read per statement. |
| **Repeatable Read** (MySQL default) | No | No | No (MVCC) | MVCC snapshot read created at first query; Next-Key locking. |
| **Serializable** | No | No | No | Strict 2-Phase Locking (2PL); shared locks on ranges. |

---

## 4. High-Yield SQL Interview Queries

### Query 1: Find the $N$-th Highest Bidder Price
```sql
-- Using Window Function DENSE_RANK()
WITH RankedBids AS (
    SELECT 
        bidder_id,
        bid_price,
        DENSE_RANK() OVER (ORDER BY bid_price DESC) as price_rank
    FROM dsp_bids
)
SELECT DISTINCT bid_price 
FROM RankedBids 
WHERE price_rank = 3; -- 3rd highest price
```

### Query 2: Publisher Click-Through-Rate (CTR) and eCPM Aggregation
```sql
SELECT 
    publisher_id,
    COUNT(impression_id) AS total_impressions,
    COUNT(click_id) AS total_clicks,
    ROUND((COUNT(click_id) * 100.0) / NULLIF(COUNT(impression_id), 0), 2) AS ctr_percentage,
    ROUND((SUM(clearing_price) / NULLIF(COUNT(impression_id), 0)) * 1000.0, 4) AS ecpm_usd
FROM ad_logs
WHERE event_date = CURRENT_DATE
GROUP BY publisher_id
HAVING total_impressions >= 1000
ORDER BY ecpm_usd DESC;
```
"""
}
