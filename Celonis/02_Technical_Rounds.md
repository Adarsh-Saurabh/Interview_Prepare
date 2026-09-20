# 02: Concurrency & Core Systems

## 1. Concurrency, Multithreading & Race Conditions
Celonis backend systems process millions of real-time event logs simultaneously. Interviewers frequently probe deep into thread safety, synchronization primitives, and lock contention.

### Core Concurrency Primitives
| Concept | Mechanism | Overhead | Use Case in Celonis |
| :--- | :--- | :--- | :--- |
| **Mutex / Lock** | Mutual exclusion; blocks thread execution until lock acquired | Kernel context switch on contention | Protecting shared process variant state |
| **Reader-Writer Lock** | Multiple concurrent readers, exclusive single writer | Moderate | Heavy read traffic on static process models |
| **Spinlock** | Busy-wait loop checking atomic flag | Burns CPU cycles | Ultra-short critical sections in hot loops |
| **Atomic Operations** | Hardware-level atomic instructions (CAS: Compare-And-Swap) | Zero context switch | Lock-free metrics & event counters |
| **Condition Variable** | Sleep thread until signaled by another thread | Low | Producer-consumer event ingestion queues |

---

## 2. Production Producer-Consumer Pattern in C++

```cpp
#include <iostream>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <vector>

template <typename T>
class ThreadSafeEventQueue {
private:
    std::queue<T> queue_;
    mutable std::mutex mutex_;
    std::condition_variable not_empty_;
    std::condition_variable not_full_;
    size_t capacity_;
    bool stopped_{false};

public:
    explicit ThreadSafeEventQueue(size_t capacity) : capacity_(capacity) {}

    void push(T item) {
        std::unique_lock<std::mutex> lock(mutex_);
        not_full_.wait(lock, [this]() { return queue_.size() < capacity_ || stopped_; });
        if (stopped_) return;
        queue_.push(std::move(item));
        not_empty_.notify_one();
    }

    bool pop(T& item) {
        std::unique_lock<std::mutex> lock(mutex_);
        not_empty_.wait(lock, [this]() { return !queue_.empty() || stopped_; });
        if (queue_.empty() && stopped_) return false;
        item = std::move(queue_.front());
        queue_.pop();
        not_full_.notify_one();
        return true;
    }

    void stop() {
        std::lock_guard<std::mutex> lock(mutex_);
        stopped_ = true;
        not_empty_.notify_all();
        not_full_.notify_all();
    }
};
```

---

## 3. Java Concurrency Essentials (Frequently Asked)
1. **Volatile Keyword**: Guarantees visibility across threads (prevents CPU core caching of stale values), but does **not** guarantee atomicity for compound actions like `count++`.
2. **Synchronized vs ReentrantLock**:
   * `synchronized`: Implicit language keyword, automatically releases lock on exception, no timeout capability.
   * `ReentrantLock`: Explicit lock management with `tryLock(timeout)`, fairness policies, and multiple `Condition` variables.
3. **Thread Pool Tuning Formula**:
   $$\text{Optimal Threads} = \text{Number of CPU Cores} \times \left(1 + \frac{\text{Wait Time}}{\text{Compute Time}}\right)$$
   * For CPU-bound tasks (e.g. Graph mining): `Runtime.getRuntime().availableProcessors() + 1`.
   * For I/O-bound tasks (e.g. Database queries, SAP REST calls): Significantly higher thread count (e.g., $10 \times \text{Cores}$).

---

## 4. Database Storage & Transaction Internals
* **B+ Trees vs LSM Trees**:
  * PostgreSQL uses B+ Trees for indices: Fast $O(\log N)$ point reads, balanced height, efficient range scans.
  * Ingestion-heavy systems often use LSM Trees (Log-Structured Merge Trees) for ultra-fast sequential disk writes.
* **ACID Isolation Levels & Anomalies**:
  * **Read Committed** (Default in PostgreSQL): Prevents dirty reads.
  * **Repeatable Read**: Prevents non-repeatable reads using MVCC snapshots.
  * **Serializable**: Guarantees serial execution; detects read/write conflicts using serialization graphs.
