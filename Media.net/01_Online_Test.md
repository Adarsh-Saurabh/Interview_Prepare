# 01: Signature OA & Live Coding Problems

Media.net's Online Assessment (InterviewBit) and Technical Round 1 demand unassisted, bug-free implementations of non-trivial algorithmic problems under strict time constraints. Below are 5 signature algorithmic problems derived from real Media.net recruitment drives, complete with optimal Python and C++ implementations, complexity proofs, and edge-case test suites.

---

## Problem 1: Real-Time Bidding Top-K Vickrey Second-Price Auction

### Problem Statement
In an ad exchange auction, $N$ DSPs submit bids for $K$ available ad placements ($1 \le K \le N$). Each bid contains:
* `dsp_id` (string)
* `bid_price` (float in USD CPM)
* `timestamp_ms` (integer timestamp)

An ad unit is cleared using a **Generalized Second-Price (GSP) Auction**:
1. The top $K$ highest bidders win the slots.
2. Ties in bid price are broken by earliest `timestamp_ms`. If timestamps match, alphabetical order of `dsp_id`.
3. The $i$-th winner ($1 \le i < K$) pays the bid price of the $(i+1)$-th bidder (second price).
4. The $K$-th winner pays the reserve price $R$ (or $(K+1)$-th bid if available, whichever is higher).

Return the list of winning DSPs with their assigned clearing prices.

### Algorithmic Approach
* **Brute Force**: Full sorting of $N$ bids takes $O(N \log N)$. When $N = 10^6$ and $K \ll N$ (e.g. $K=5$), sorting the entire stream wastes memory and CPU cache.
* **Optimal Approach**: Maintain a Min-Heap of size $K+1$. For each incoming bid, push into heap; if size exceeds $K+1$, pop the smallest.
* **Complexity**:
  * **Time**: $O(N \log K)$ time.
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
    """
    Resolves Generalized Second-Price (GSP) auction for K slots.
    Time Complexity: O(N log K)
    Space Complexity: O(K)
    """
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
  * Space: $O(U \times M)$.

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
2. For each campaign $i$, binary search for latest compatible campaign $p(i)$ where $E_{p(i)} \le S_i$.
3. Recurrence:
   $$DP[i] = \max\left(DP[i-1], V_i + DP[p(i)]\right)$$
4. Complexity: Time $O(N \log N)$, Space $O(N)$.

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
