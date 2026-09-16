# Systems Programming & Linux/Unix Internals Deep Dive

> **Role Focus:** Low-level C/C++ Systems Engineering, Linux Kernel, Operating Systems  
> **Interview Rounds:** Technical Round 1 (DSA & Pointers) & Technical Round 2 (OS Internals & Architecture)  

---

## 1. Process Memory Layout & Address Space Virtualization

Every user-space process in Linux operates within its own **Virtual Address Space**, isolated from other processes by the Memory Management Unit (MMU) and multi-level page tables:

```
+-------------------------------------------------------------+ 0xFFFFFFFFFFFFFFFF (Kernel Space)
|                     Kernel Space (Shared)                   |
+-------------------------------------------------------------+ 0x00007FFFFFFFFFFF (Top of User Space)
|      User Stack (Grows Downward toward lower addresses)     |
|                             |                               |
|                             v                               |
+-------------------------------------------------------------+
|               Memory-Mapped Segment (mmap, shm, DSOs)       |
+-------------------------------------------------------------+
|                             ^                               |
|                             |                               |
|       Heap (Grows Upward via brk() / sbrk() syscalls)       |
+-------------------------------------------------------------+
|      BSS Segment (Uninitialized global & static variables)   |
+-------------------------------------------------------------+
|      Data Segment (Initialized global & static variables)   |
+-------------------------------------------------------------+
|      Text Segment (Compiled machine instructions, read-only)|
+-------------------------------------------------------------+ 0x0000000000400000 (Base Text Address)
```

### Key Questions Asked by ISDL Senior Engineers:
1. **What happens under the hood during `fork()`?**
   - Linux does NOT immediately copy the physical memory of the parent process.
   - It performs **Copy-on-Write (COW)**: it duplicates the parent's page table entries and marks all pages as **Read-Only**.
   - If either the parent or child attempts to write to a page, the CPU raises a **Page Fault interrupt (PF)**.
   - The kernel trap handler allocates a new physical page frame, copies the 4KB data, updates the writing process's page table entry with write permissions, and flushes the corresponding TLB entry.
2. **What is the exact distinction between `fork()`, `vfork()`, and `clone()`?**
   - `fork()` creates a child process with a COW-duplicated page table.
   - `vfork()` pauses the parent process and shares the parent's address space directly until the child calls `execve()` or `_exit()`.
   - `clone()` is the underlying Linux system call used by `pthread_create()`. It accepts flags:
     - `CLONE_VM`: Share memory virtual address space.
     - `CLONE_FS`: Share file system information (root, cwd, umask).
     - `CLONE_FILES`: Share file descriptor table.
     - `CLONE_SIGHAND`: Share signal handlers.

---

## 2. Linux Inter-Process Communication (IPC) Spectrum

ISDL designs multi-tenant, high-throughput server backends where subsystems must exchange state at microsecond latency:

| IPC Mechanism | Kernel Overhead | Throughput / Latency | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Anonymous Pipe** | Medium (2 context switches per read/write, kernel buffer) | ~1.5 GB/s, ~2 µs | Parent-child CLI piping (`|`) |
| **Named Pipe (FIFO)** | Medium (kernel buffer, filesystem path entry) | ~1.5 GB/s, ~2 µs | Unrelated processes on same host |
| **UNIX Domain Socket** | Low-Medium (socket buffers, bypasses TCP/IP stack) | ~3.0 GB/s, ~1.2 µs | D-Bus in OpenBMC, local daemons |
| **POSIX Shared Memory** | **Zero during data transfer** (direct memory access) | **~35+ GB/s (RAM speed), <0.1 µs** | High-frequency telemetry & databases |

### POSIX Shared Memory Implementation in C/C++
```cpp
#include <iostream>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <cstring>

struct SharedTelemetry {
    uint64_t timestamp;
    double cpu_temp_celsius;
    uint32_t fan_rpm;
};

// Producer writes telemetry directly to shared physical memory
void writeToSharedMemory() {
    int shm_fd = shm_open("/ibm_isdl_telemetry", O_CREAT | O_RDWR, 0666);
    ftruncate(shm_fd, sizeof(SharedTelemetry));

    SharedTelemetry* ptr = (SharedTelemetry*)mmap(
        nullptr, sizeof(SharedTelemetry), 
        PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0
    );

    ptr->timestamp = 1726531200;
    ptr->cpu_temp_celsius = 48.5;
    ptr->fan_rpm = 4200;

    munmap(ptr, sizeof(SharedTelemetry));
    close(shm_fd);
}
```

---

## 3. Virtual Memory, Paging & Cache Hierarchies

### Multi-Level Page Tables & TLB
- On 64-bit systems (x86_64 or ppc64le), 48-bit or 57-bit virtual addresses are translated into physical addresses via a 4-level or 5-level page table hierarchy (PGD $\to$ P4D $\to$ PUD $\to$ PMD $\to$ PTE).
- Each translation requires up to 4–5 memory lookups if not cached.
- **Translation Lookaside Buffer (TLB):** A hardware associative cache storing recent virtual-to-physical address mappings. A TLB hit resolves in **~0.5 ns (1 clock cycle)**; a TLB miss costs **~30–60 ns (RAM walk)**.
- **HugePages (2MB / 1GB):** By grouping memory into 2MB or 1GB pages instead of 4KB, a single TLB entry covers $512\times$ or $262,144\times$ more memory space, reducing TLB miss rates from 15% to <0.5% in enterprise database engines.

### Cache Lines & False Sharing
- CPU caches (L1, L2, L3) load memory in contiguous chunks called **Cache Lines** (typically 64 bytes on x86, up to 128 bytes on IBM POWER10).
- **False Sharing:** Occurs when two threads running on different cores modify independent variables that reside within the **same cache line**. The cache coherence protocol (MESI/MOESI) invalidates the entire cache line across cores, creating "cache line bouncing" and degrading performance by up to $10\times$.
- **Mitigation:** Force alignment using C++17 `alignas(64)` or `alignas(128)`.

```cpp
// Cache-line aligned counter structure avoiding false sharing
struct alignas(64) CoreCounter {
    std::atomic<uint64_t> count{0};
};

CoreCounter per_core_metrics[8]; // Each array element sits in an isolated 64-byte cache line
```

---

## 4. Concurrency Primitives: Mutex vs Spinlock vs Futex

1. **Mutex (`std::mutex` / `pthread_mutex_t`):**
   - When a thread fails to acquire a mutex, it yields CPU time and is moved to the kernel's wait queue by putting the thread to sleep (`TASK_INTERRUPTIBLE`).
   - Involves context switch overhead (~1–2 µs).
2. **Spinlock (`pthread_spinlock_t`):**
   - Continuously loops in a busy-wait checking an atomic flag (`test-and-set`).
   - Zero context-switch latency, but consumes 100% CPU on that core. Use ONLY for very short critical sections (< few microseconds) or inside kernel interrupt handlers where sleeping is illegal.
3. **Futex (Fast Userspace Mutex):**
   - The foundation of modern Linux synchronization (`pthread_mutex`).
   - Fast path (no contention): Handled purely in user space using atomic Compare-And-Swap (CAS) with **zero syscall overhead**.
   - Slow path (contention): Falls back to `sys_futex()` kernel syscall to put the calling thread to sleep.
