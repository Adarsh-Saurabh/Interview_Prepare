# 02: Core Systems, Concurrency, C++ Internals & OS

## 1. C++ Language Internals for Systems Engineers

### 1.1 Virtual Tables (`vtable`) & Virtual Pointers (`vptr`)
* **How Polymorphism Works at Assembly Level**:
  * Every class with at least one virtual function has a hidden compiler-generated lookup table called the **vtable**.
  * Each object instance of that class contains a hidden 8-byte pointer (**vptr**) placed at offset 0 pointing to its class's vtable.
  * When calling `obj->process()`, the compiler generates: `(*obj->vptr[index])(obj)`.
* **Cost of Virtual Dispatch**:
  * Additional memory: 8 bytes per object instance (`vptr`) + one static table per polymorphic class (`vtable`).
  * Branch prediction penalty: Indirect jump via function pointer prevents inline optimization and causes CPU pipeline stalls if mispredicted.
* **Why Virtual Destructors are Mandatory**:
  * Deleting a derived class instance through a base pointer (`Base* p = new Derived(); delete p;`) without a virtual destructor causes **Undefined Behavior** and memory leaks (only `~Base()` executes; `~Derived()` is skipped).

### 1.2 Memory Layout & Structure Alignment
* **Memory Alignment Rule**: A variable of size $N$ bytes must reside at a memory address divisible by $N$.
* **Padding Demonstration**:
```cpp
struct UnalignedTransceiver {
    char status;     // 1 byte
    // 3 bytes padding
    int channel_id;  // 4 bytes
    double power;    // 8 bytes
}; // Total: 16 bytes (instead of 13)

struct OptimizedTransceiver {
    double power;    // 8 bytes
    int channel_id;  // 4 bytes
    char status;     // 1 byte
    // 3 bytes padding at end
}; // Total: 16 bytes, but cache lines pack more predictably
```
* **Hardware Cache Line Awareness**: CPU caches transfer data in **64-byte chunks** (cache lines). Group related telemetry fields together to ensure they hit the same L1 cache line.

### 1.3 Move Semantics & RAII
* **Lvalue vs Rvalue**: An lvalue has an identifiable memory location (name/address). An rvalue is a temporary value that does not persist beyond the expression.
* **Move Constructor Idiom**:
```cpp
class TelemetryBuffer {
    float* data_;
    size_t size_;
public:
    // Move Constructor: Steals resources without memory copy
    TelemetryBuffer(TelemetryBuffer&& other) noexcept 
        : data_(other.data_), size_(other.size_) {
        other.data_ = nullptr;
        other.size_ = 0;
    }
    ~TelemetryBuffer() { delete[] data_; }
};
```
* **Smart Pointers**:
  * `std::unique_ptr`: Zero-cost abstraction over raw pointers. Exclusive ownership.
  * `std::shared_ptr`: Reference-counted ownership. Allocates a **Control Block** (contains ref-count, weak-count, custom deleter). `std::make_shared` combines object and control block into a single contiguous memory allocation for cache locality.
  * `std::weak_ptr`: Non-owning observer that does not increment ref count. Breaks circular reference memory leaks.

---

## 2. Operating Systems, Concurrency & Multithreading

### 2.1 Synchronization Primitives Comparison

| Primitive | Mechanism | Kernel Transition? | Best Used For |
| :--- | :--- | :---: | :--- |
| **Mutex (`std::mutex`)** | Sleeping lock; thread yields CPU if contested | Yes | Long critical sections (>几 microseconds) |
| **Spinlock (`std::atomic_flag`)** | Busy-waits in a tight loop checking condition | No | Ultra-short critical sections (< cache miss time) |
| **Read-Write Lock (`shared_mutex`)** | Multiple concurrent readers, exclusive single writer | Yes | Read-heavy configuration tables |
| **Condition Variable** | Thread sleeps until signaled by another thread | Yes | Producer-Consumer pipelines & queues |

### 2.2 The 4 Coffman Deadlock Conditions & Prevention
1. **Mutual Exclusion**: Resources cannot be shared. (Mitigation: use lock-free read structures where possible).
2. **Hold and Wait**: Thread holding resource A requests resource B. (Mitigation: request all locks atomically via `std::scoped_lock(m1, m2)`).
3. **No Preemption**: Resources cannot be forcibly taken.
4. **Circular Wait**: Cycle in resource dependency graph. (Mitigation: **Global Lock Ordering** — always acquire lock with lower memory address first).

### 2.3 False Sharing & Cache Thrashing
* When two threads on different CPU cores modify two distinct variables that happen to share the same **64-byte cache line**, the MESI cache coherency protocol forces cores to repeatedly invalidate and reload each other's L1 cache lines.
* **Solution**: `alignas(64)` hardware padding:
```cpp
struct alignas(64) WorkerStats {
    uint64_t processed_frames;
};
```

---

## 3. Linux Systems Programming & Networking Sockets

### 3.1 Socket Programming Essentials
```cpp
// Non-blocking TCP server snippet
int server_fd = socket(AF_INET, SOCK_STREAM, 0);
int flags = fcntl(server_fd, F_GETFL, 0);
fcntl(server_fd, F_SETFL, flags | O_NONBLOCK);

sockaddr_in address{};
address.sin_family = AF_INET;
address.sin_addr.s_addr = INADDR_ANY;
address.sin_port = htons(8080);
bind(server_fd, (struct sockaddr*)&address, sizeof(address));
listen(server_fd, 128);
```

### 3.2 `epoll` vs `select`
* `select()`: $\mathcal{O}(N)$ scan over file descriptor set on every event. Limited to 1024 FDs.
* `epoll()`: $\mathcal{O}(1)$ event readiness notifications via Linux kernel red-black tree and ready list. Scalable to $100,000+$ persistent optical device telemetry connections.

### 3.3 Linux Debugging Toolkit
* **GDB**: `gdb ./firmware`, `break main.cpp:45`, `run`, `backtrace full`, `info registers`, `print *transceiver`.
* **Valgrind**: `valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./firmware`.
* **Perf**: `perf record -g ./firmware` followed by `perf report` for CPU profiling and cache miss analysis.
