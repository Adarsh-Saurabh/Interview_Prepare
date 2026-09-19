# 05: Limit Order Book (LOB) — Low-Level System Design

## 1. System Requirements & Latency Bounds
* **Functional Requirements:**
  1. `add_order(order_id, side, price, qty)`: Insert limit order in $O(1)$ or $O(\log N)$.
  2. `cancel_order(order_id)`: Remove existing order in $O(1)$ time.
  3. `get_bbo()`: Return Best Bid and Best Ask in $O(1)$ time.
  4. `match()`: Execute incoming market orders against the top of book.
* **Non-Functional Latency Requirements:**
  * **Zero Dynamic Allocation (`malloc`/`new`) on Hot-Path:** Pre-allocate all order structures in a memory pool.
  * **Deterministic Execution:** No unbounded iterations.

---

## 2. Low-Level Architecture & Data Structure Choice

```
Price Level Map (std::map<double, PriceLevel*> or Flat Bounded Array)
  ├── 1500.50 (Ask Level 1) ──► Doubly Linked List of Orders:
  │                             [Order 101: 200 shares] ◄──► [Order 102: 200 shares]
  ├── 1501.00 (Ask Level 2) ──► [Order 103: 500 shares]
  │
Hash Map Index (std::unordered_map<uint64_t, OrderNode*>)
  ├── Key: 101 ──► Points directly to Order 101 in Doubly Linked List ($O(1)$ Cancel)
  └── Key: 102 ──► Points directly to Order 102 in Doubly Linked List ($O(1)$ Cancel)
```

---

## 3. Production C++ Implementation (Ultra-Low Latency Order Book)

```cpp
#include <iostream>
#include <unordered_map>
#include <map>
#include <cstdint>

enum class Side { BUY, SELL };

struct Order {
    uint64_t order_id;
    Side side;
    double price;
    uint32_t qty;
    Order* prev{nullptr};
    Order* next{nullptr};
};

struct LimitLevel {
    double price;
    uint32_t total_qty{0};
    Order* head{nullptr};
    Order* tail{nullptr};

    void append(Order* order) {
        order->prev = tail;
        order->next = nullptr;
        if (tail) tail->next = order;
        else head = order;
        tail = order;
        total_qty += order->qty;
    }

    void remove(Order* order) {
        if (order->prev) order->prev->next = order->next;
        else head = order->next;

        if (order->next) order->next->prev = order->prev;
        else tail = order->prev;

        total_qty -= order->qty;
        order->prev = nullptr;
        order->next = nullptr;
    }

    bool empty() const { return head == nullptr; }
};

class LimitOrderBook {
private:
    // Buy orders: Descending order (highest bid first)
    std::map<double, LimitLevel, std::greater<double>> bids;
    // Sell orders: Ascending order (lowest ask first)
    std::map<double, LimitLevel, std::less<double>> asks;

    // Fast order lookup for O(1) cancellations
    std::unordered_map<uint64_t, Order*> order_map;

    // Static memory pool to avoid runtime heap allocations
    static constexpr size_t POOL_SIZE = 100000;
    Order pool[POOL_SIZE];
    size_t pool_idx{0};

    Order* allocate_order() {
        if (pool_idx < POOL_SIZE) return &pool[pool_idx++];
        return new Order(); // Fallback if pool exhausted
    }

public:
    void add_order(uint64_t id, Side side, double price, uint32_t qty) {
        Order* order = allocate_order();
        order->order_id = id;
        order->side = side;
        order->price = price;
        order->qty = qty;

        if (side == Side::BUY) {
            bids[price].append(order);
        } else {
            asks[price].append(order);
        }
        order_map[id] = order;
    }

    void cancel_order(uint64_t id) {
        auto it = order_map.find(id);
        if (it == order_map.end()) return;

        Order* order = it->second;
        if (order->side == Side::BUY) {
            auto level_it = bids.find(order->price);
            if (level_it != bids.end()) {
                level_it->second.remove(order);
                if (level_it->second.empty()) bids.erase(level_it);
            }
        } else {
            auto level_it = asks.find(order->price);
            if (level_it != asks.end()) {
                level_it->second.remove(order);
                if (level_it->second.empty()) asks.erase(level_it);
            }
        }
        order_map.erase(it);
    }

    double get_best_bid() const {
        return bids.empty() ? 0.0 : bids.begin()->first;
    }

    double get_best_ask() const {
        return asks.empty() ? 0.0 : asks.begin()->first;
    }
};
```
