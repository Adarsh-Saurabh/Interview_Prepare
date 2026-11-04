# Module 02: Core CS, OS, RTOS & C++ Internals

In Wabtec's technical rounds, interviewers place intense scrutiny on your fundamental understanding of computer systems, memory management, and concurrent programming.

---

## 1. Operating Systems & Real-Time Systems (RTOS)

### A. Process vs. Thread: Deep Memory Architecture
* **Process**: An isolated execution unit with its own virtual address space, containing:
  * **Text Segment**: Machine code instructions (read-only).
  * **Data & BSS**: Initialized and uninitialized global/static variables.
  * **Heap**: Dynamic memory managed by `malloc`/`new`.
  * **Stack**: Local variables, stack frames, return pointers.
  * *Each process has a unique Page Directory and Process Control Block (PCB).*
* **Thread**: A lightweight execution stream inside a process.
  * Shares: Text, Data, BSS, Heap, and open file descriptors.
  * Private: Its own Program Counter (PC), Register state, and Stack!
  * *Context Switch Overhead*: Thread context switches are significantly faster than process context switches because threads share the same virtual address mapping—**no TLB (Translation Lookaside Buffer) invalidation** occurs!

### B. Real-Time Operating Systems (RTOS) vs. General Purpose OS (GPOS)
* **GPOS (Linux/Windows)**: Optimizes for **average throughput** and fairness. Cannot guarantee hard timing deadlines.
* **RTOS (VxWorks, FreeRTOS, QNX)**: Optimizes for **deterministic latency** and bounded worst-case execution time (WCET). If an emergency brake task misses its 10ms deadline, catastrophic failure occurs.

```
+-----------------------------------------------------------------------------------------+
|                  REAL-TIME SCHEDULING ALGORITHMS (CRUCIAL FOR WABTEC)                   |
+-----------------------------------------------------------------------------------------+
| 1. Rate Monotonic Scheduling (RMS) | Static Priority based on Period:                   |
|                                    | Shorter Period = Higher Priority.                  |
|                                    | Utilization Bound for N tasks:                     |
|                                    | U = sum(C_i / T_i) <= N * (2^(1/N) - 1)            |
|                                    | As N -> inf, U_bound approaches 69.3%.             |
| 2. Earliest Deadline First (EDF)   | Dynamic Priority: Task with nearest deadline wins. |
|                                    | Achieves 100% theoretical CPU utilization bound!   |
+-----------------------------------------------------------------------------------------+
```

### C. Concurrency Primitives: When to Use Which?
1. **Mutex (Mutual Exclusion)**:
   * Sleeping lock with ownership. Only the thread that acquired the mutex can unlock it.
   * Use case: Protecting shared state during long operations (> a few microseconds).
2. **Spinlock**:
   * Busy-waiting loop checking an atomic flag (`test_and_set`).
   * Use case: In low-latency interrupt service routines (ISRs) or kernel code where critical sections take only a few CPU cycles.
3. **Semaphore**:
   * Signaling mechanism with an integer counter. No ownership concept.
   * `Counting Semaphore`: Manages a pool of $N$ identical resources.
   * `Binary Semaphore`: Often used for task synchronization (Task A signals Task B upon completing sensor DMA transfer).

### D. Priority Inversion & The Mars Pathfinder Flaw
* **The Problem**: A Low-Priority Task (L) acquires a shared mutex. A High-Priority Task (H) arrives and blocks waiting for the mutex. A Medium-Priority Task (M) with no need for the mutex preempts L. Consequently, Task H is indirectly blocked by Task M!
* **The Solution (Priority Inheritance Protocol - PIP)**:
  * When Task H blocks on a mutex held by Task L, Task L temporarily inherits the high priority of Task H until it releases the mutex.

### E. Deadlocks & The 4 Coffman Conditions
Deadlock occurs if and only if all 4 conditions hold simultaneously:
1. **Mutual Exclusion**: Resource cannot be shared.
2. **Hold and Wait**: Process holding resources requests additional ones.
3. **No Preemption**: Resources cannot be forcibly revoked.
4. **Circular Wait**: Process $P_1$ waits for $P_2$, which waits for $P_1$.
* **Deadlock Prevention in Locomotive Software**: Enforce a strict **global lock hierarchy**. Locks must always be acquired in increasing order of their numerical IDs!

---

## 2. Modern C++ & Object-Oriented Internals

### A. The Virtual Table (`vtable`) and Virtual Pointer (`vptr`)
When a class defines a `virtual` method:
1. The compiler creates a static table of function pointers (`vtable`) for that class.
2. Every object instance of that class contains an invisible pointer (`vptr`) placed at offset 0 pointing to its class's `vtable`.
3. When calling `obj->run()`, the runtime executes:
   $$	ext{call } *( *(obj->vptr) + 	ext{method\_offset} )$$
* *Performance cost*: Indirect memory dereference + CPU branch prediction penalty.

```cpp
class LocomotiveSubsystem {
public:
    virtual ~LocomotiveSubsystem() = default; // Essential! Prevents undefined behavior
    virtual void step() = 0; // Pure virtual -> Abstract class
};

class BrakeController : public LocomotiveSubsystem {
public:
    void step() override {
        // Concrete brake logic
    }
};
```

### B. RAII & Smart Pointer Semantics
* **Resource Acquisition Is Initialization (RAII)**: Bind the life cycle of a resource (heap memory, socket, mutex lock) to the lifetime of a stack object. Destructors run deterministically upon exiting scope.
* **`std::unique_ptr<T>`**: Exclusive ownership. Zero runtime memory overhead (same size as raw pointer). Cannot be copied, only moved.
* **`std::shared_ptr<T>`**: Shared ownership via an atomic reference count control block.
* **`std::weak_ptr<T>`**: Non-owning observer of a `shared_ptr`. Breaks cyclic reference memory leaks!

### C. Move Semantics & Rvalue References
```cpp
// Move constructor avoids deep copy of telemetry buffers!
class TelemetryPacket {
    double* data;
    size_t size;
public:
    // Move Constructor
    TelemetryPacket(TelemetryPacket&& other) noexcept 
        : data(other.data), size(other.size) {
        other.data = nullptr;
        other.size = 0;
    }
    
    // Move Assignment
    TelemetryPacket& operator=(TelemetryPacket&& other) noexcept {
        if (this != &other) {
            delete[] data;
            data = other.data;
            size = other.size;
            other.data = nullptr;
            other.size = 0;
        }
        return *this;
    }
};
```

---

## 3. Computer Networks & Industrial Communication

```
+-----------------------------------------------------------------------------------+
|                        CAN BUS (CONTROLLER AREA NETWORK)                          |
+-----------------------------------------------------------------------------------+
| Topology     : Multi-master differential two-wire bus (CAN_H, CAN_L).             |
| Signaling    : Recessive (Logic 1, 2.5V diff 0V), Dominant (Logic 0, diff ~2V).   |
| Arbitration  : Non-destructive bitwise arbitration by Message ID.                |
|              : LOWER numerical ID = HIGHER priority!                              |
| Safety       : Cyclic Redundancy Check (15-bit CRC), Frame Bit Stuffing,          |
|              : Automatic Error Confinement (Bus-off state on fault nodes).        |
+-----------------------------------------------------------------------------------+
```

### TCP vs. UDP in Railroad Telemetry
* **TCP**: Guaranteed delivery, congestion control. Used for non-vital diagnostics and cloud fleet sync.
* **UDP**: Minimal packet overhead, no retransmission delays. Used for high-frequency sensor telemetry where latest state is more important than stale retransmissions.
