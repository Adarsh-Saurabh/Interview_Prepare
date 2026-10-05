# 07: Rapid Recall CheatSheet

A rapid-fire reference card for last-minute revision before Media.net online assessments and technical interviews.

---

## 1. C++ STL & Concurrency Rapid Reference

```cpp
// 1. Min-Heap for Top-K
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;

// 2. Custom Comparator Priority Queue
auto cmp = [](const auto& a, const auto& b) { return a.price > b.price; };
std::priority_queue<Bid, std::vector<Bid>, decltype(cmp)> pq(cmp);

// 3. Binary Search
auto it = std::upper_bound(vec.begin(), vec.end(), target); // first elem > target
int idx = std::distance(vec.begin(), it);

// 4. Thread-Safe Mutex & RAII Lock
std::mutex mtx;
{
    std::lock_guard<std::mutex> lock(mtx); // auto releases on scope exit
}

// 5. Condition Variable
std::condition_variable cv;
std::unique_lock<std::mutex> ulock(mtx);
cv.wait(ulock, []{ return ready; }); // releases lock, sleeps, re-acquires
cv.notify_one();
```

---

## 2. Operating Systems & Network Rapid Formulas

* **Amdahl's Law (Speedup Limit)**:
  $$S_{\text{latency}}(s) = \frac{1}{(1 - p) + \frac{p}{s}}$$
  *(Where $p$ is the parallel fraction and $s$ is the number of cores. If 10% is serial, speedup cannot exceed $10\times$ even with infinite cores).*
* **Little's Law (Queueing Theory)**:
  $$L = \lambda \times W$$
  *(Average requests in system $L$ = Throughput $\lambda$ $\times$ Average response time $W$. For 50,000 req/sec at 50ms latency, system holds $50000 \times 0.05 = 2,500$ in-flight requests).*
* **Bandwidth-Delay Product (BDP)**:
  $$\text{BDP} = \text{Bandwidth (bits/sec)} \times \text{RTT (sec)}$$
  *(Determines the optimal TCP socket receive buffer size to keep network pipe full).*

---

## 3. High-Yield SQL CheatSheet

```sql
-- 1. Nth Highest Salary using DENSE_RANK()
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rk
    FROM employees
) t WHERE rk = 2 LIMIT 1;

-- 2. Rolling 7-Day Average Revenue
SELECT date, AVG(revenue) OVER (
    ORDER BY date 
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
) as rolling_7d_avg
FROM daily_revenue;

-- 3. Self-Join to find Employees earning more than their Manager
SELECT e.name AS employee
FROM employee e
JOIN employee m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

---

## 4. Ad-Tech & RTB Rapid Glossary

* **CPM (Cost Per Mille)**: Cost per 1,000 ad impressions (standard RTB pricing metric).
* **eCPM (Effective CPM)**: $\frac{\text{Total Earnings}}{\text{Total Impressions}} \times 1000$.
* **CTR (Click-Through Rate)**: $\frac{\text{Total Clicks}}{\text{Total Impressions}} \times 100\%$.
* **Vickrey (Second-Price) Auction**: The highest bidder wins, but pays the price bid by the second-highest bidder (plus 1 cent). Ensures truthful bidding (dominant strategy).
* **Fill Rate**: $\frac{\text{Ads Rendered}}{\text{Ad Requests Dispatched}} \times 100\%$.
* **Header Bidding**: Running client-side or server-side parallel auctions with multiple SSPs via Prebid.js before querying the primary ad server.

---

## 5. Adarsh Saurabh: Candidate Project Metrics

| Project | Core Stack | Key Authentic Metric to Quote |
| :--- | :--- | :--- |
| **Warehouse PathMapper** | Python, Heuristic Routing, Data Structures | $10,000 \times 10,000$ grid computed in **$< 0.5$ seconds** on i5 CPU. |
| **Uplan** | Gemini 2.5 Pro, LangGraph, Python | **85% reduction** in manual verification; **98% token compression**. |
| **Alternative Data Radar** | Python, Next.js, SQL, Bright Data | Automated anti-bot proxy bypass; 0–100 pre-earnings corporate health score. |
