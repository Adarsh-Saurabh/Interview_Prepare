# 02: Systems, Memory Management & OS Internals

Apple engineers build software close to the metal. Whether you are applying for **AI & ML SDE** or **SDET**, technical interviews at Apple rigorously probe memory layout, concurrency primitives, synchronization, and operating system mechanics.

---

## 1. Memory Management: ARC vs GC vs RAII

Apple platforms (iOS, macOS) utilize **Automatic Reference Counting (ARC)** rather than tracing Garbage Collection (like Java or Go).

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ Feature                 │ ARC (Swift / Objective-C│ Tracing GC (Java/Go)    │ C++ RAII                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Deallocation Timing     │ Deterministic (Instant) │ Non-deterministic (Stop-│ Deterministic (Scope    │
│                         │ when count hits 0       │ the-world pauses)       │ exit)                   │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Runtime CPU Overhead    │ Zero GC pauses; atomic  │ Periodic CPU spikes for │ Zero runtime tracking   │
│                         │ ref count increments    │ mark-and-sweep          │ overhead                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Memory Footprint        │ Minimal; immediate      │ Higher; delayed memory  │ Strict, explicit cache  │
│                         │ reclamation             │ reclamation             │ locality                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Retain Cycle Risk       │ High (needs weak/unowned│ Low (GC automatically   │ Prevented by clean      │
│                         │ references)             │ collects cyclic graphs) │ ownership & weak_ptr    │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Retain Cycles & Reference Types
* **Strong Reference**: Increments the reference count by 1. Object remains in memory as long as strong count $> 0$.
* **Weak Reference**: Does **not** increment the reference count. When the referenced object deallocates, the pointer is automatically zeroed out (`nil`). In Swift/Obj-C, a weak reference is always an optional.
* **Unowned Reference**: Does not increment reference count, but assumes the object will never be deallocated while accessed. Accessing a deallocated unowned reference results in an immediate crash (equivalent to a raw dangling pointer).

### C++ Smart Pointers Internals
1. `std::unique_ptr<T>`:
   * Exclusive ownership model.
   * Exactly the size of a raw pointer (zero memory overhead).
   * Non-copyable, only movable (`std::move`). Destroys object when out of scope.
2. `std::shared_ptr<T>`:
   * Shared ownership model.
   * Stores two pointers (16 bytes on 64-bit): Pointer to raw object, and pointer to the **Control Block**.
   * The Control Block contains:
     - Strong Reference Count (`std::atomic<long>`)
     - Weak Reference Count (`std::atomic<long>`)
     - Custom Deleter / Allocator
   * Thread Safety: Modifying the reference count is atomic and thread-safe. Modifying the underlying object itself is **not** thread-safe.
3. `std::weak_ptr<T>`:
   * Non-owning observer. Does not keep the object alive.
   * Can be promoted to `std::shared_ptr` via `.lock()` if the object is still alive. Used to break circular dependencies.

---

## 2. C++ Object Memory Layout & Virtual Tables (`vtable`)

When a class declares or inherits at least one virtual function, the C++ compiler injects runtime polymorphism machinery:

```
[Stack / Heap Object Instance]
┌─────────────────────────────────┐
│  vptr (Virtual Table Pointer)   │ ──► [Virtual Table (vtable) in .rodata]
├─────────────────────────────────┤     ┌───────────────────────────────────┐
│  member_var_1                   │     │  &Derived::virtual_method_1()     │
├─────────────────────────────────┤     ├───────────────────────────────────┤
│  member_var_2                   │     │  &Derived::virtual_method_2()     │
└─────────────────────────────────┘     └───────────────────────────────────┘
```

### Essential Virtual Concepts to Defend
1. **Virtual Destructor**: If a class has virtual methods, its destructor **must** be marked `virtual`. If you delete a derived class object through a base class pointer without a virtual destructor, only the base destructor runs, causing resource/memory leaks.
2. **Object Slicing**: Occurs when you assign a derived class instance to a base class object **by value** (instead of pointer or reference). The derived portion is sliced off, and polymorphic behavior is lost because `vptr` points to the base class table.
3. **Struct Padding & Memory Alignment**:
   * Hardware reads memory in words (4 or 8 bytes). Data must be aligned to addresses that are multiples of its size.
   * Order matters: Placing a `char` (1 byte), `double` (8 bytes), and `int` (4 bytes) sequentially results in 24 bytes due to padding. Reordering as `double` (8), `int` (4), `char` (1) results in 16 bytes.

---

## 3. Concurrency, Synchronization & Multi-Threading

### Processes vs Threads
* **Process**: An isolated execution environment with its own dedicated virtual memory space, file descriptor table, and page tables. Context switching between processes requires invalidating or swapping Translation Lookaside Buffer (TLB) entries, making it expensive ($1000+$ CPU cycles).
* **Thread**: A lightweight execution stream within a process. Threads share the same address space, heap, static data, and open file descriptors, but each thread has its own **Stack**, **Program Counter (PC)**, and **Registers**. Context switching is faster ($100-200$ CPU cycles).

### Synchronization Primitives & Trade-Offs

```
┌──────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Primitive        │ How It Works                    │ Best Use Case                   │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Mutex            │ Puts thread to sleep via OS     │ Long critical sections; I/O     │
│                  │ scheduler if lock unavailable   │ or disk operations.             │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Spinlock         │ Busy-waits in a tight CPU loop  │ Ultra-short critical sections   │
│                  │ (`while(test_and_set)`)         │ where sleep context switch is   │
│                  │                                 │ more expensive than waiting.    │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Semaphore        │ Integer counter controlling     │ Resource pools (e.g., max 10    │
│                  │ access to $N$ shared resources  │ database connections).          │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ `std::atomic`    │ Hardware-enforced atomic        │ Single variable counters, lock- │
│                  │ instructions (e.g., CMPXCHG)    │ free ring buffers, flags.       │
└──────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

### False Sharing & Cache Lines
* Modern CPUs access memory in **Cache Lines** (typically 64 bytes on ARM Apple Silicon and x86).
* **False Sharing**: Occurs when two threads running on different CPU cores modify completely independent variables that happen to reside on the same 64-byte cache line. The CPU cache coherence protocol (MESI/MOESI) invalidates the cache line back and forth, degrading multi-threaded throughput.
* **Fix**: Force data alignment to separate cache lines using `alignas(64)` in C++.

---

## 4. Networking Protocols & Socket I/O Multiplexing

### TCP 3-Way Handshake & 4-Way Teardown
```
Client                              Server
  │               SYN                 │
  ├──────────────────────────────────►│  1. Client sends SYN (seq = x)
  │             SYN-ACK               │
  │◄──────────────────────────────────┤  2. Server responds SYN-ACK (seq = y, ack = x + 1)
  │               ACK                 │
  ├──────────────────────────────────►│  3. Client sends ACK (ack = y + 1) -> ESTABLISHED
  │                                   │
  │               FIN                 │
  ├──────────────────────────────────►│  1. Initiator sends FIN
  │               ACK                 │
  │◄──────────────────────────────────┤  2. Receiver acknowledges ACK
  │               FIN                 │
  │◄──────────────────────────────────┤  3. Receiver finishes sending data, sends FIN
  │               ACK                 │
  ├──────────────────────────────────►│  4. Initiator sends ACK -> Enters TIME_WAIT (2MSL)
```
* **Why TIME_WAIT is 2MSL (Maximum Segment Lifetime)**: Ensures the final ACK is reliably delivered to the receiver. If the ACK is lost, the receiver will retransmit its FIN, which the client can still acknowledge during TIME_WAIT, preventing stray packets from corrupting new connections.

### I/O Multiplexing: `select` vs `epoll` vs `kqueue`
* `select()` / `poll()`: $O(N)$ scanning over the entire file descriptor list on every event. Unscalable for high concurrency.
* `epoll()` (Linux): $O(1)$ event notification using red-black trees and ready lists in the kernel.
* `kqueue()` (macOS / Darwin / iOS): Apple's kernel event notification mechanism. Handles file descriptors, signals, timers, and asynchronous I/O with $O(1)$ complexity.
