# 02: Low-Latency C++ & Core Systems

## 1. The Cost of Virtual Functions (`vtable` & `vptr`)

### What happens under the hood?
When a class declares a virtual function:
1. The compiler instantiates a static **Virtual Method Table (`vtable`)** containing function pointers to the resolved methods.
2. Every instance of the class receives an invisible **Virtual Table Pointer (`vptr`)** (typically 8 bytes on a 64-bit architecture) at offset 0.
3. When calling `ptr->executeTrade()`:
   * Dereference object pointer to read `vptr`.
   * Add offset to locate `executeTrade` entry in `vtable`.
   * Dereference function pointer and branch (`call %rax`).

```
Object Instance in RAM                     Class VTable in .rodata
┌─────────────────────────┐               ┌──────────────────────────────┐
│  vptr (8 bytes)  ───────┼──────────────►│ [0] &Order::validate()       │
├─────────────────────────┤               ├──────────────────────────────┤
│  uint64_t order_id      │               │ [1] &LimitOrder::execute()   │
├─────────────────────────┤               └──────────────────────────────┘
│  double price           │
└─────────────────────────┘
```

### Why is this banned in HFT Hot-Paths?
1. **Instruction Cache (I-Cache) Eviction & Indirection:** Two pointer dereferences instead of one direct assembly `call`.
2. **Compiler Inlining Banned:** Compilers cannot inline virtual calls at compile time unless devirtualization succeeds. Inlining eliminates call-overhead and enables register allocation optimizations.
3. **Branch Prediction Penalty:** Dynamic indirect jumps confuse CPU branch target buffers (BTB), triggering expensive $\sim 15-20$ cycle CPU pipeline flushes.

### The HFT Alternative: Curiously Recurring Template Pattern (CRTP)
Compile-time static polymorphism with zero runtime overhead:

```cpp
template <typename Derived>
class OrderHandler {
public:
    inline void processOrder() {
        static_cast<Derived*>(this)->processOrderImpl();
    }
};

class EquityHandler : public OrderHandler<EquityHandler> {
public:
    inline void processOrderImpl() {
        // Inlined directly into caller assembly without vtable lookup!
    }
};
```

---

## 2. Memory Alignment, Struct Padding & False Sharing

### Struct Layout & Cache Lines
CPUs access RAM in discrete **64-byte Cache Lines**. An unaligned variable spanning two cache lines requires two memory fetches instead of one.

```cpp
// BAD: Poor layout (Wasteful padding)
struct BadTrade {
    char exchange_code;  // 1 byte + 7 bytes padding
    double price;        // 8 bytes
    char order_type;     // 1 byte + 7 bytes padding
    uint64_t order_id;   // 8 bytes
}; // Total Size: 32 bytes (14 bytes wasted padding!)

// GOOD: Ordered by descending alignment
struct alignas(32) GoodTrade {
    double price;        // 8 bytes
    uint64_t order_id;   // 8 bytes
    char exchange_code;  // 1 byte
    char order_type;     // 1 byte
    char padding[14];    // Explicit 14 bytes pad to 32 bytes
}; // Total Size: 32 bytes (Zero implicit wasted alignment traps)
```

### Eliminating False Sharing in Multithreading
When Thread 1 (Core 1) writes to `tail` and Thread 2 (Core 2) writes to `head` located on the **same 64-byte cache line**, the CPU's cache coherence protocol (MESI) repeatedly invalidates Core 1 and Core 2 caches across the interconnect bus—degrading performance by $50\times$.

```cpp
// Prevent False Sharing in Lock-Free Queues:
struct SPSCQueuePointers {
    alignas(64) std::atomic<uint64_t> write_tail{0}; // Core 1 writes here
    alignas(64) std::atomic<uint64_t> read_head{0};  // Core 2 reads here
};
```

---

## 3. Row-Major vs Column-Major Memory Traversal

### Benchmark Comparison:
In C and C++, 2D arrays are stored in **row-major order** (contiguous in memory row by row):

```cpp
const int N = 8192;
int matrix[N][N];

// Fast: Row-Major Traversal (Contiguous memory access)
// 1 cache line fetch loads 16 consecutive integers into L1 Cache!
for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
        sum += matrix[i][j]; // Spatial Locality: 15 cache hits per 1 miss
    }
}

// Slow: Column-Major Traversal (Stride of 8192 integers = 32 KB jump!)
// Every single iteration triggers an L1/L2 Cache Miss!
for (int j = 0; j < N; ++j) {
    for (int i = 0; i < N; ++i) {
        sum += matrix[i][j]; // Stride Thrashing: ~10x slower execution
    }
}
```
