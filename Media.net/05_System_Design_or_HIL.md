# 05: LLD & Low-Latency System Design

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
4. **Second-Price Clearing Engine**: Computes the winning bid and sets the clearing price to $(2nd\_highest\_bid + \$0.01)$ or reserve floor.
5. **Decoupled Billing & Analytics via Kafka**: All winning impression logs and tracking pixel clicks are emitted asynchronously to an Apache Kafka topic, isolating analytical ingestion from real-time auction latency.
