# modules_part2.py: Modules 03, 04, 05

modules_part2 = {}

# =============================================================================
# MODULE 03: Domain Deep Dive - Ad-Tech & RTB Systems
# =============================================================================
modules_part2["03_Domain_Deep_Dive"] = {
    "title": "03: Ad-Tech & RTB Systems Architecture",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: Systems, Memory, OS & Networks",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Candidate Resume Grilling",
    "markdown": """# 03: Ad-Tech & RTB Systems Architecture

Media.net is an industry pioneer in **Sell-Side Platforms (SSP)** and **Contextual Advertising**. To excel in technical and managerial interviews, you must understand how billions of dollars flow through programmatic ad pipelines within millisecond latency budgets.

---

## 1. The Programmatic Advertising Ecosystem

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          Digital Ad Supply Chain                                │
├─────────────────┬──────────────────────┬──────────────────────┬─────────────────┤
│   Publishers    │   Supply-Side (SSP)  │   Ad Exchange / RTB  │ Demand-Side(DSP)│
│ Forbes, CNN, NYT│   Media.net Engine   │   OpenRTB Auction    │ Trade Desk, DV36│
│ Generates Supply│ Aggregates Inventory │ Matches Buyers & Sell│ Buys on Target  │
└─────────────────┴──────────────────────┴──────────────────────┴─────────────────┘
```

1. **Publisher (Supply)**: Websites and mobile apps providing ad real estate (banners, native widgets, video players).
2. **Supply-Side Platform (SSP) — Media.net's Core Business**: Software used by publishers to automate the selling of their advertising impressions to maximize yield.
3. **Demand-Side Platform (DSP)**: Software used by advertisers and agencies (Nike, Uber, Samsung) to automatically purchase inventory across multiple ad exchanges based on audience targeting and bidding algorithms.
4. **Data Management Platform (DMP)**: Warehouses audience demographic, behavioral, and intent data to enrich bid requests.
5. **Ad Server**: The final decision authority on the publisher page that renders the winning ad creative.

---

## 2. Real-Time Bidding (RTB) Protocol & The 50ms Latency Budget

When a user opens an article on a publisher website, an RTB auction executes before the browser paints the viewport. The entire pipeline operates under a **hard 50ms SLA**:

| Step | Operation | Latency Budget | Technology / Mechanism |
| :---: | :--- | :---: | :--- |
| **1** | Client Browser $\\to$ Edge SSP Request | 10 ms | HTTP/2, Anycast DNS routing to closest edge PoP |
| **2** | Contextual NLP & Keyword Extraction | 5 ms | In-memory Trie matcher, cached page semantic vector |
| **3** | OpenRTB Bid Request Serialization & DSP Dispatch | 2 ms | Protocol Buffers / zero-copy JSON serializer |
| **4** | DSP Bid Computation (Parallel Wait) | 25 ms | Hard timeout timer; DSPs failing to respond are dropped |
| **5** | Auction Resolution (Second-Price Vickrey) | 3 ms | Min-Heap / QuickSelect top-K selection & pricing |
| **6** | Winning Ad Creative Serialization & Response | 5 ms | Asynchronous event logging to Kafka; return HTML/JS |
| **Total**| **End-to-End Auction Pipeline** | **50 ms** | **Sub-50ms SLA Guaranteed** |

### The OpenRTB 2.5 Bid Request Spec (Simplified JSON)
```json
{
  "id": "auction-83921-prod-mumbai",
  "imp": [
    {
      "id": "1",
      "banner": { "w": 300, "h": 250, "pos": 1 },
      "bidfloor": 1.25,
      "bidfloorcur": "USD"
    }
  ],
  "site": {
    "id": "forbes-tech-102",
    "domain": "forbes.com",
    "cat": ["IAB19-1", "IAB19-18"],
    "keywords": "cloud computing, enterprise security, kubernetes"
  },
  "device": {
    "ip": "203.0.113.195",
    "geo": { "country": "IND", "region": "MH", "city": "Mumbai" }
  },
  "tmax": 35
}
```

---

## 3. Header Bidding (Prebid.js) vs. Traditional Waterfall

Historically, publishers used the **Waterfall (Daisy-Chaining)** model:
```
Publisher Ad Server ──► SSP 1 ($5 Floor) [Passback] ──► SSP 2 ($3 Floor) [Passback] ──► AdSense ($1)
```
* **Problems with Waterfall**:
  1. High latency (sequential network hops accumulating 500ms–1500ms).
  2. Inefficient yield (SSP 2 might have a $6 buyer, but SSP 1 passes it back because its own floor was unmet).

```
                      ┌─────────────────────────────────┐
                      │    Client Browser (Prebid.js)   │
                      └────────────────┬────────────────┘
                                       │ (Parallel Requests)
               ┌───────────────────────┼───────────────────────┐
               ▼                       ▼                       ▼
      ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
      │ Media.net (SSP) │     │   AppNexus/Xandr│     │   Rubicon/Magnite
      │   Bids: $4.50   │     │   Bids: $3.80   │     │   Bids: $4.10   │
      └────────┬────────┘     └────────┬────────┘     └────────┬────────┘
               │                       │                       │
               └───────────────────────┼───────────────────────┘
                                       ▼
                      ┌─────────────────────────────────┐
                      │ Media.net Wins ($4.50 Clearing) │
                      └─────────────────────────────────┘
```
* **Header Bidding Revolution**: Media.net embeds a lightweight JavaScript adapter (`Prebid.js`) in the publisher's page `<head>`. Before the ad server is called, the script dispatches **concurrent asynchronous requests** to multiple SSPs. All bids arrive within 200ms and compete in a unified, transparent auction, maximizing publisher revenue by 30–50%.

---

## 4. High-Scale Data Structures in Ad-Tech

### A. Frequency Capping via Redis Bitmaps & Sliding Windows
* Advertisers cap user exposure to avoid banner blindness.
* **Storage Optimization**: Storing timestamps naively consumes gigabytes of memory.
* **Bitmaps Solution**: For daily frequency caps, maintain a Redis Bitmap per user where bit index represents hour or time slot. `BITCOUNT` checks impressions in $O(1)$ operations with only a few bytes of storage per user.

### B. HyperLogLog for Unique Daily Audience Counting
* An ad campaign reports "How many unique users viewed this Nike ad today?"
* Across 100 million impressions, storing user IDs in a hash set would require gigabytes of RAM.
* **HyperLogLog (HLL)** estimates the cardinality of billions of items using **only 1.5 KB of memory** with a standard error of $\\approx 0.81\\%$. It analyzes the distribution of leading zeros in the hash values of elements.

### C. Bloom Filters for Click Fraud Prevention
* Malicious bots generate automated click fraud to drain advertiser budgets.
* Edge proxies check incoming click signatures against a **Bloom Filter** of known malicious IP ranges and bot user-agents in $< 10$ microseconds before passing the request to the billing engine.
"""
}

# =============================================================================
# MODULE 04: Candidate Resume Grilling (Adarsh Saurabh Defense)
# =============================================================================
modules_part2["04_Candidate_Resume_Grilling"] = {
    "title": "04: Candidate Resume Grilling & Traps",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Ad-Tech & RTB Systems",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: LLD & Low-Latency System Design",
    "markdown": """# 04: Candidate Resume Grilling & Traps

Media.net interviewers conduct surgical deep dives into your resume projects. They specifically verify that you possess **first-principles understanding** and did not simply rely on AI coding assistants or surface-level tutorials.

---

## 1. Candidate Baseline Profile Summary
* **Candidate**: Adarsh Saurabh (Roll Number: `225EC6021`)
* **Education**:
  * **M.Tech in Signal and Image Processing**, NIT Rourkela (CGPA: **8.28**)
  * **B.Tech in Computer Science and Engineering**, Guru Ghasidas University (CGPA: **8.5**)
* **Core Projects on Tailored Resume**:
  1. `Uplan — Adversarial Document Intelligence Pipeline` (LangGraph, Gemini 2.5 Pro, Streamlit, 2025)
  2. `Alternative Data Radar` (Python, Next.js, SQL, REST APIs, Bright Data, LLM APIs, 2026)
  3. `IBYD Technology — Warehouse PathMapper` (Python, Algorithms, Data Structures, 2023)

---

## 2. Deep Project Defense & Trap Scenarios

### Project 1: Warehouse PathMapper (IBYD Technology)
> *"You built a heuristic pathfinding engine on a 10,000 x 10,000 grid running in under 0.5s. How does this relate to Media.net's engineering?"*

#### The Interview Trap
* If you say: *"It was just Dijkstra / A* algorithm on a grid,"* the interviewer will ask: *"On a $10,000 \\times 10,000$ grid ($10^8$ nodes), Dijkstra will timeout or run out of memory. How did it finish in $< 0.5$ seconds?"*

#### The Master Defense
> *"In a raw $10^8$ state-space, standard Dijkstra is unusable due to $O(V \\log V + E)$ overhead. In real industrial warehouses, 95% of space consists of fixed rack aisles and transit corridors.
> 1. **Topological Graph Abstraction**: Instead of searching pixel-by-pixel, I precomputed a hierarchical topological waypoint graph connecting aisle intersections and picking bays (~1,500 nodes).
> 2. **Bidirectional A* with Manhattan Distance Heuristic**: I used an admissible heuristic $h(n) = |x_1 - x_2| + |y_1 - y_2|$ running from both start and target simultaneously, terminating when search frontiers met.
> 3. **Spatial Memory Locality**: I stored waypoint coordinates in contiguous array buffers (cache-line friendly) rather than linked node pointers, eliminating pointer chasing and CPU L1/L2 cache misses.
> 4. **Relevance to Media.net**: This is directly analogous to ad routing in an SSP—rather than evaluating every DSP linearly, we use hierarchical clustering and topological pruning to evaluate target criteria in microseconds."*

---

### Project 2: Uplan — Adversarial Document Intelligence Pipeline
> *"You used LangGraph and Gemini 2.5 Pro for adversarial document validation. The Media.net JD states: 'Interviews evaluate unassisted problem-solving. Fluency with AI tools is assessed separately.' Did you write the core logic, or did LLMs do the thinking?"*

#### The Interview Trap
* If you say: *"The LLM figured out if the document had errors,"* you will be rejected for lack of engineering ownership and deterministic reasoning.

#### The Master Defense
> *"I designed Uplan around the principle that **LLMs must never be trusted with deterministic mathematical validation**.
> 1. **Deterministic Rule Engine First**: LLMs suffer from stochastic hallucination when comparing numerical financial data. I engineered a zero-hallucination mathematical verification engine in Python that validates bank statements, salary credits, and tax amounts against hard Boolean rules.
> 2. **Structural Encoding & 98% Token Compression**: Sending raw multi-page PDFs to an LLM introduces unacceptable latency and token cost. I used Gemini Flash as an extraction compiler to distill page metadata into a typed semantic JSON graph, cutting prompt tokens by 98%.
> 3. **Adversarial LangGraph Topology**: I created two specialized roles: a Proposer agent that checks visa compliance, and an Adversary agent tasked with actively finding edge-case contradictions. Their state was orchestrated via a deterministic Directed Acyclic Graph in LangGraph.
> 4. **AI as an Accelerator**: I wrote the state graphs, type definitions, and rule engines myself. I used AI developer tools to rapidly generate edge-case validation test suites and fuzzing fixtures."*

---

### Project 3: Alternative Data Radar
> *"You scraped web signals and calculated corporate health scores stored in a SQL database. How did you handle anti-scraping, rate limits, and SQL concurrency?"*

#### The Interview Trap
* *"How did you prevent database lock contention when scraping multiple corporate data sources concurrently?"*

#### The Master Defense
> *"1. **Proxy Rotation & Fingerprint Emulation**: Target corporate websites use Cloudflare and Akamai bot protection. I routed traffic via Bright Data Web Unlocker, managing HTTP/2 TLS fingerprint rotation and automated exponential backoff with jitter on HTTP 429/503 responses.
> 2. **Asynchronous Scraping Worker Pool**: Instead of synchronous blocking HTTP requests, I used an asynchronous worker architecture (`asyncio` and worker queues), streaming parsed signals directly into an ingestion pipeline.
> 3. **SQL Indexing & Concurrency**: Corporate scoring metrics required frequent inserts and analytical queries. I isolated analytical aggregation queries using Read Committed isolation, created composite indexes on `(company_id, metric_date DESC)` for fast dashboard lookups, and batched inserts inside database transactions to eliminate row lock contention."*

---

## 3. Defending Your Dual Background: M.Tech Signal Processing + B.Tech CSE

> *"Your undergraduate degree is CSE, but your Master's is Signal and Image Processing. Why are you applying for a Core SDE role at Media.net?"*

#### The Winning Narrative
> *"My dual background is a deliberate technical advantage for high-scale systems:
> 1. **B.Tech in CSE**: Gave me foundational mastery in Data Structures, Algorithms, Operating Systems, Database Internals, and Computer Networks.
> 2. **M.Tech in Signal Processing at NIT Rourkela**: Trained me in high-dimensional linear algebra, Fourier analysis, statistical signal filtering, and real-time streaming pipelines.
> 3. **Application to Ad-Tech**: Real-time ad bidding is fundamentally a high-frequency digital signal stream:
>    * Click fraud detection uses statistical anomaly filtering (Kalman filtering and noise cancellation).
>    * Contextual ad semantic matching relies on high-dimensional vector embeddings and cosine projections.
>    * Low-latency RTB requires microsecond timing budgeting, which mirrors real-time digital signal processing constraints."*
"""
}

# =============================================================================
# MODULE 05: LLD & Low-Latency System Design
# =============================================================================
modules_part2["05_System_Design_or_HIL"] = {
    "title": "05: LLD & Low-Latency System Design",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Candidate Resume Grilling",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Culture & Ownership",
    "markdown": """# 05: LLD & Low-Latency System Design

Media.net evaluates candidates on both **Low-Level Design (Machine Coding)**—producing clean, runnable object-oriented code—and **High-Level Distributed System Design** under extreme scale and strict latency SLAs.

---

## 1. Machine Coding (LLD): Thread-Safe In-Memory Cache with TTL & LRU

### Problem Requirements
Implement an industrial-grade in-memory cache supporting:
1. `put(key, value, ttl_ms)`: Inserts or updates key with a Time-To-Live in milliseconds.
2. `get(key)`: Returns value if key exists and has not expired; updates LRU access order.
3. Eviction Policy: If capacity $C$ is reached, evict the **Least Recently Used (LRU)** non-expired element.
4. **Thread Safety**: Fully safe under high concurrent reader/writer threads.

### C++20 Production Implementation
```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <list>
#include <mutex>
#include <chrono>
#include <optional>

template <typename K, typename V>
class LRUCacheWithTTL {
private:
    struct CacheItem {
        K key;
        V value;
        std::chrono::steady_clock::time_point expiry;
    };

    const size_t capacity_;
    std::list<CacheItem> lru_list_; // Front = Most Recently Used, Back = Least Recently Used
    
    // Hash map from Key to list iterator for O(1) lookups
    std::unordered_map<K, typename std::list<CacheItem>::iterator> map_;
    mutable std::mutex mtx_;

    bool isExpired(const typename std::list<CacheItem>::iterator& it) const {
        return std::chrono::steady_clock::now() > it->expiry;
    }

    void evictExpiredOrLRU() {
        // First check if tail is expired; if so, remove it
        if (!lru_list_.empty()) {
            auto it = std::prev(lru_list_.end());
            map_.erase(it->key);
            lru_list_.pop_back();
        }
    }

public:
    explicit LRUCacheWithTTL(size_t capacity) : capacity_(capacity) {}

    std::optional<V> get(const K& key) {
        std::lock_guard<std::mutex> lock(mtx_);
        auto it = map_.find(key);
        if (it == map_.end()) {
            return std::nullopt;
        }

        // Check TTL
        if (isExpired(it->second)) {
            lru_list_.erase(it->second);
            map_.erase(it);
            return std::nullopt;
        }

        // Move accessed node to front of LRU list (Most Recently Used)
        lru_list_.splice(lru_list_.begin(), lru_list_, it->second);
        return it->second->value;
    }

    void put(const K& key, const V& value, int64_t ttl_ms) {
        std::lock_guard<std::mutex> lock(mtx_);
        auto expiry = std::chrono::steady_clock::now() + std::chrono::milliseconds(ttl_ms);

        auto it = map_.find(key);
        if (it != map_.end()) {
            // Key exists: update value, expiry and move to front
            it->second->value = value;
            it->second->expiry = expiry;
            lru_list_.splice(lru_list_.begin(), lru_list_, it->second);
            return;
        }

        // Evict if capacity exceeded
        if (map_.size() >= capacity_) {
            evictExpiredOrLRU();
        }

        lru_list_.push_front({key, value, expiry});
        map_[key] = lru_list_.begin();
    }

    size_t size() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return map_.size();
    }
};

// Verification Driver
int main() {
    LRUCacheWithTTL<std::string, std::string> cache(2);

    cache.put("campaign_1", "Nike_Shoes", 1000); // 1 sec TTL
    cache.put("campaign_2", "Apple_MacBook", 5000);

    auto v1 = cache.get("campaign_1");
    if (v1) std::cout << "Found: " << *v1 << std::endl;

    // Insert 3rd item -> triggers LRU eviction of campaign_2 (since campaign_1 was recently accessed)
    cache.put("campaign_3", "Sony_Headphones", 5000);

    auto v2 = cache.get("campaign_2");
    std::cout << "Campaign 2 (Evicted?): " << (v2 ? *v2 : "null") << std::endl;

    return 0;
}
```

---

## 2. High-Level Design (HLD): Scalable Real-Time Contextual Ad Exchange

```
                       ┌─────────────────────────────────────┐
                       │   Client Browser / Publisher App    │
                       └──────────────────┬──────────────────┘
                                          │ HTTP GET /bid (Sub-50ms)
                                          ▼
                       ┌─────────────────────────────────────┐
                       │       Edge Ingestion Gateway        │
                       │    (Envoy Proxy / Nginx + C++)      │
                       └──────────────────┬──────────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
       ┌──────────────────────┐                       ┌──────────────────────┐
       │ Inverted Index Match │                       │ Redis Frequency Cap  │
       │ Contextual Keyword   │                       │ User Impression Cap  │
       │ Extraction & Target  │                       │ & Bot Fraud Filter   │
       └──────────┬───────────┘                       └──────────┬───────────┘
                  │                                               │
                  └───────────────────────┬───────────────────────┘
                                          ▼
                       ┌─────────────────────────────────────┐
                       │     Auction Coordinator Service     │
                       │   (OpenRTB Dispatcher / Wait Pool)  │
                       └──────────────────┬──────────────────┘
                                          │ 25ms Timeout
               ┌──────────────────────────┼──────────────────────────┐
               ▼                          ▼                          ▼
      ┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐
      │  DSP 1 (Amazon)  │       │  DSP 2 (Google)  │       │  DSP 3 (Criteo)  │
      │  Bid: $2.40      │       │  Bid: $3.10      │       │  Bid: $2.85      │
      └────────┬─────────┘       └────────┬─────────┘       └────────┬─────────┘
               │                          │                          │
               └──────────────────────────┼──────────────────────────┘
                                          ▼
                       ┌─────────────────────────────────────┐
                       │   Second-Price Clearing Engine      │
                       │   Winner: DSP 2 @ $2.85 Clearing    │
                       └──────────────────┬──────────────────┘
                                          │
                     ┌────────────────────┴────────────────────┐
                     ▼                                         ▼
         ┌───────────────────────┐                 ┌───────────────────────┐
         │ Return Ad Markup (JS) │                 │ Async Kafka Log Bus   │
         │ to Publisher Viewport │                 │ Analytics & Billing   │
         └───────────────────────┘                 └───────────────────────┘
```

### Key Architectural Pillars
1. **Edge Anycast & Connection Pooling**: Edge gateways terminate TLS close to users and maintain persistent keep-alive TCP pools with registered DSPs, saving 30ms of connection latency.
2. **Contextual Tokenizer**: Caches pre-extracted semantic tags for popular publisher URLs in Aerospike/Redis with sub-millisecond lookup.
3. **Auction Coordinator**: Dispatches non-blocking async HTTP/2 requests to all matching DSPs simultaneously with a **hard 25ms timeout**. Any DSP that fails to respond in 25ms is excluded from the auction.
4. **Second-Price Clearing Engine**: Computes the winning bid and sets the clearing price to $(2nd\\_highest\\_bid + \\$0.01)$ or reserve floor.
5. **Decoupled Billing & Analytics via Kafka**: All winning impression logs and tracking pixel clicks are emitted asynchronously to an Apache Kafka topic, isolating analytical ingestion from real-time auction latency.
"""
}
