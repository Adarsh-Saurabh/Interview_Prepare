# 03: Ad-Tech & RTB Systems Architecture

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
| **1** | Client Browser $\to$ Edge SSP Request | 10 ms | HTTP/2, Anycast DNS routing to closest edge PoP |
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
* **HyperLogLog (HLL)** estimates the cardinality of billions of items using **only 1.5 KB of memory** with a standard error of $\approx 0.81\%$. It analyzes the distribution of leading zeros in the hash values of elements.

### C. Bloom Filters for Click Fraud Prevention
* Malicious bots generate automated click fraud to drain advertiser budgets.
* Edge proxies check incoming click signatures against a **Bloom Filter** of known malicious IP ranges and bot user-agents in $< 10$ microseconds before passing the request to the billing engine.
