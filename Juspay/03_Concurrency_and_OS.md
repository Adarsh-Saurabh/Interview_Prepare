# 03: Concurrency, OS Internals & Multithreading ? Juspay Technologies

---

## 1. Concurrency Axioms & Hardware Architecture

At Juspay's scale (350M+ transactions/day), multi-core CPU architectures and memory subsystems dictate latency and safety.

### 1.1 Data Race vs. Race Condition
- **Data Race (Hardware/Language Level)**: Two concurrent memory accesses to the exact same memory location without synchronization, where at least one access is a write. In C/C++, a data race invokes Undefined Behavior (UB), allowing compiler optimizations to reorder instructions unpredictably.
- **Race Condition (Application/Logic Level)**: A flaw in execution sequencing where the correctness of a program depends on the non-deterministic relative timing of threads (e.g., check-then-act, double-spending in payments).

### 1.2 CPU Caching, False Sharing & MESI Protocol
- Modern x86-64 and ARM CPUs organize memory into L1/L2/L3 caches in **64-byte cache lines**.
- **MESI Protocol States**:
  - `M` (Modified): Line present only in current core cache, dirty (not written to RAM).
  - `E` (Exclusive): Line present only in current core cache, clean (matches RAM).
  - `S` (Shared): Line present in multiple core caches, clean.
  - `I` (Invalid): Line does not contain valid data.
- **False Sharing**: Two threads running on Core 0 and Core 1 independently modify two unrelated variables that reside within the *same 64-byte cache line*. Writing to variable A transitions Core 1's cache line to `Invalid`, forcing Core 1 to reload from L3/RAM?degrading performance by 10x?50x!
  - **Mitigation**: Cache line alignment (`alignas(64)` in C++).

```
False Sharing Scenario:
?????????????????????????????????????????????????????????????????
?                   64-Byte Cache Line                          ?
?  [ Thread 0 Variable: counter_A ]  [ Thread 1: counter_B ]   ?
?????????????????????????????????????????????????????????????????
Core 0 writes counter_A ??? Invalidate line on Core 1! ??? Cache Thrashing
```

### 1.3 Memory Barriers & Acquire-Release Semantics
Compilers and Out-of-Order (OoO) CPUs aggressively reorder reads and writes unless constrained by memory fences.
- `memory_order_relaxed`: Guarantees atomicity of the single variable, but permits arbitrary reordering with surrounding instructions.
- `memory_order_acquire`: Ensures that *no subsequent reads or writes* in the current thread can be reordered *before* this load.
- `memory_order_release`: Ensures that *no previous reads or writes* in the current thread can be reordered *after* this store.
- `memory_order_seq_cst`: Full sequential consistency. Enforces a single globally agreed-upon total order across all threads at high CPU cycle cost.

---

## 2. Synchronization Primitives: Internals & Trade-offs

| Primitive | Mechanism | CPU Behavior | Latency / Context Switch Cost | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Mutex (`std::mutex`)** | Futex (`SYS_futex` in Linux) | Spins briefly in userspace, then puts thread to sleep via kernel wait queue | ~1.2 to 2.5 $\mu$s (kernel context switch penalty) | Long-running critical sections, I/O operations. |
| **Spinlock (`pthread_spinlock_t`)** | Atomic CAS tight loop (`PAUSE` instruction) | 100% CPU utilization on core; never deschedules thread | ~10 to 30 nanoseconds | Microsecond critical sections, interrupt handlers. |
| **Reader-Writer Lock (`shared_mutex`)** | Shared read counter + exclusive write lock | Permits multiple concurrent readers; blocks writers | Moderate overhead (counter updates) | Read-heavy configs, routing tables (99% reads, 1% writes). |
| **Atomic CAS (`std::atomic`)** | Hardware `LOCK CMPXCHG` instruction | Hardware bus lock / cache coherence lock | ~5 to 15 nanoseconds | Lock-free counters, sequence numbers, state transitions. |

### 2.1 The Futex Architecture (Fast Userspace Mutex)
Traditional POSIX mutexes required a kernel system call on every lock/unlock. The Linux **Futex** optimizes this:
1. An integer in userspace represents the lock state (`0 = unlocked`, `1 = locked`, `2 = locked with waiters`).
2. An uncontended lock acquisition is a single userspace atomic CAS instruction (`0 -> 1`). Zero kernel transition overhead.
3. If contended, the thread issues the `SYS_futex` syscall with `FUTEX_WAIT`, descheduling the thread until the owner invokes `FUTEX_WAKE`.

---

## 3. Deadlock Analysis & Prevention in Payments

### 3.1 The 4 Coffman Conditions
A deadlock can occur if and only if all four conditions hold simultaneously:
1. **Mutual Exclusion**: Resources cannot be shared simultaneously.
2. **Hold and Wait**: A process currently holding at least one resource requests additional resources.
3. **No Preemption**: A resource cannot be forcibly taken from a process holding it.
4. **Circular Wait**: A closed chain of processes exists, where each process holds one resource and waits for the next.

### 3.2 The Classic Double-Account Transfer Deadlock
Scenario: Thread 1 transfers $100 from Account A to Account B. Thread 2 transfers $50 from Account B to Account A.
- Thread 1 locks Account A, attempts to lock Account B.
- Thread 2 locks Account B, attempts to lock Account A.
- Result: **Permanent Coffman Circular Wait Deadlock**.

```
Thread 1 (Txn: A -> B):  Holds Lock(A) ??waiting for??? Lock(B)
                               ?                           ?
                               ?                           ?
Thread 2 (Txn: B -> A):  Lock(A) ???waiting for?? Holds Lock(B)
```

### 3.3 The Strict Canonical Order Solution
Break Condition 4 (Circular Wait) by establishing a **Global Total Order** on lock acquisition:

```cpp
void transferMoney(Account& acc1, Account& acc2, double amount) {
    if (&acc1 == &acc2) return; // Prevent self-transfer deadlocks

    // Always acquire lock on smaller memory address / account ID first
    Account& first = (acc1.id < acc2.id) ? acc1 : acc2;
    Account& second = (acc1.id < acc2.id) ? acc2 : acc1;

    std::unique_lock<std::mutex> lock1(first.mtx);
    std::unique_lock<std::mutex> lock2(second.mtx);

    // Critical section: atomic debit and credit
    acc1.balance -= amount;
    acc2.balance += amount;
}
```

---

## 4. Lock-Free Programming & Atomic Compare-And-Swap (CAS)

### 4.1 The CAS Primitive & The ABA Problem
- `compare_exchange_strong(expected, desired)` atomically checks if current value equals `expected`. If true, sets it to `desired`.
- **The ABA Problem**: Thread 1 reads value $A$. Thread 2 changes $A \to B$, and then back to $A$. Thread 1 executes CAS, observes $A$, assumes nothing changed, and corrupts state (e.g., node memory reallocated in lock-free freelists).
- **Mitigation**: **Tagged Pointers / Version Counters** ? combine value with a monotonically increasing sequence counter:
  $$\langle \text{Pointer}, \text{Version} \rangle$$
