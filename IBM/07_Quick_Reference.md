# 07: Caveman & Ponytail Ultra-Dense Systems CheatSheet

Ultra-compressed technical reference for rapid revision 30 minutes before your IBM Systems (ISDL) technical and architectural interviews.

---

## 1. Caveman Mode (High Signal, Zero Fluff)

- **ISDL Numbers:** ₹18.75 LPA CTC. M.Tech: ₹40,000/mo stipend. B.Tech: ₹30,000/mo. 70% of global banking on zSystems.
- **Seven Nines:** $99.99999\%$ uptime = $< 3.15\text{s}$ unplanned downtime per year across hardware, hypervisor, and OS.
- **Telum z16:** 8 cores, $5.0+\text{GHz}$, 7nm. 32MB L2 per core. 256MB Virtual L3 (all L2s interconnected over 320 GB/s ring). 2GB Virtual L4.
- **Telum NNPA:** Integrated on-chip AI accelerator. 6 TFLOPS FP16. In-transaction inferencing $< 1\text{ms}$ (scores 100% of banking transactions for fraud in-flight).
- **POWER10:** 7nm, up to 15 SMT8 cores (120 threads). MMA (Matrix Math Accelerator). OMI (Open Memory Interface) up to $1\text{ TB/s}$ bandwidth.
- **Memory Inception:** Optical OMI cluster interconnect. Core in Chassis A reads memory in Chassis B with hardware cache coherency and sub-100ns latency.
- **Endianness:** `s390x` is Big-Endian (MSB at lowest address). `ppc64le` is Little-Endian (LSB at lowest address). Network byte order is Big-Endian (`htonl`, `ntohl`).
- **Memory Hierarchy Latencies:**
  - L1 cache hit: $\approx 1\text{ ns}$ (4 cycles)
  - L2 cache hit: $\approx 3\text{--}4\text{ ns}$ (14 cycles)
  - L3 cache hit: $\approx 10\text{--}15\text{ ns}$ (40–60 cycles)
  - Main Memory (DRAM): $\approx 60\text{--}100\text{ ns}$ (200+ cycles)
  - Cross-Socket NUMA: $\approx 150\text{--}250\text{ ns}$
  - NVMe SSD Read: $\approx 10\text{--}30\ \mu\text{s}$
- **Page Tables:** 4-level paging on Linux x86_64/ppc64le (PGD $\to$ PUD $\to$ PMD $\to$ PTE). 4KB standard page, 2MB HugePages, 1GB Transparent HugePages (THP).
- **Copy-on-Write (COW):** `fork()` duplicates page table entries marked read-only. Write triggers Page Fault (`do_wp_page`), allocating physical page copy only on mutation.
- **Mutex vs. Spinlock:**
  - Mutex: Sleep-lock via `futex`. Puts thread on wait queue, yields CPU. Use for long or variable critical sections.
  - Spinlock: Busy-wait atomic CAS. Zero context-switch cost. Never sleep with spinlock held. Wasteful under high core contention.
  - Futex: Fast Userspace Mutex. Atomic CAS in userspace for uncontended path; kernel syscall only on lock contention.
- **False Sharing:** Two threads writing to different variables located in the same 64-byte cache line. Cores bounce cache lines via MESI invalidations. Fix: `alignas(64)` padding.
- **Memory Ordering:**
  - `memory_order_seq_cst`: Full sequential consistency, slowest, default.
  - `memory_order_acquire`: Prevents subsequent reads/writes from being reordered before this load (used when reading lock/ready flag).
  - `memory_order_release`: Prevents previous reads/writes from being reordered after this store (used when committing data to shared buffer).
  - `memory_order_relaxed`: Guarantees atomicity only, no ordering constraints.
- **Essential Linux Diagnostics:**
  - `perf stat -e cycles,instructions,cache-misses,L1-dcache-load-misses ./app`: Check Instructions Per Cycle (IPC) and cache hits.
  - `perf c2c record -F 60000 -- ./app`: Profile cache line bouncing and false sharing.
  - `strace -c ./app`: System call frequency and time profile.
  - `numactl --hardware`: View NUMA topology, memory distribution, and node distance matrix.
  - `numactl --cpunodebind=0 --membind=0 ./app`: Pin execution and memory to NUMA node 0.
- **PathMapper Defense:** Contiguous 1D array eliminates pointer overhead; 64-bit bitmasks pack 100M cells into 12MB RAM; bidirectional $A^*$ routes in $<0.5\text{s}$.
- **Uplan Defense:** AST deterministic entity parser achieved 98% token reduction, eliminating timeouts while ensuring zero-hallucination formal constraint checks.

---

## 2. Ponytail Mode (Architectural Mental Models)

```
                     THE IBM SYSTEMS FULL-STACK HIERARCHY
                     
+-------------------------------------------------------------------------------+
|                       Enterprise Workloads & Applications                      |
|                  (SAP HANA, DB2, Core Banking, AI Inference)                  |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
|                           Enterprise Operating Systems                        |
|                  (Red Hat Enterprise Linux, z/OS, AIX, IBM i)                 |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
|                      Hypervisors & Virtualization Engines                     |
|                  (IBM PR/SM, PowerVM, KVM on Power / zSystems)                |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
|                         Firmware & Out-of-Band Management                     |
|            (Hostboot, OPAL / Petitboot, OpenBMC D-Bus / Redfish Daemons)      |
+-------------------------------------------------------------------------------+
                                       │
                                       ▼
+-------------------------------------------------------------------------------+
|                        Hardware & Micro-Architecture                          |
|         - IBM POWER10: SMT8, MMA Vector Engines, OMI 1TB/s Memory Fabric      |
|         - IBM Telum z16: 5+ GHz, Virtual L3/L4 Cache Rings, On-Chip NNPA      |
+-------------------------------------------------------------------------------+
```

```
                   LOCK-FREE SPSC MEMORY ORDERING MODEL
                   
     PRODUCER THREAD                             CONSUMER THREAD
  -----------------------                     -----------------------
  1. Write payload to                         
     buffer[tail & mask]                      
            │                                 
            ▼                                 
  2. atomic_store(tail, ...,                  
     memory_order_release)                    
            │                                 
            │ (Memory Barrier: Payload writes 
            │  are flushed BEFORE tail update)
            │                                 
            └───────────────────────────────> 3. atomic_load(tail, ...,
                                                 memory_order_acquire)
                                                        │
                                                        ▼
                                              4. Read payload from
                                                 buffer[head & mask]
                                                        │
                                                        ▼
                                              5. atomic_store(head, ...,
                                                 memory_order_release)
```

---

## 3. 10 Rapid-Fire Pre-Interview Q&As

1. **Q: What is the difference between Big-Endian and Little-Endian at the byte level?**
   - *A:* Big-Endian stores the Most Significant Byte (MSB) at the lowest memory address (e.g. `0x12345678` stored as `12 34 56 78` in `s390x`). Little-Endian stores the Least Significant Byte first (`78 56 34 12` in `ppc64le` and `x86_64`).
2. **Q: Why does IBM Telum use a Virtual L3 and L4 cache instead of dedicated physical on-die L3 SRAM?**
   - *A:* Dedicated physical L3 cache consumes massive silicon area. Telum turns unused private 32MB L2 caches of neighboring idle cores into a shared 256MB Virtual L3 via a 320 GB/s dual-ring bus, saving die area while retaining low latency.
3. **Q: What happens under the hood during a Linux `fork()` system call?**
   - *A:* The kernel creates a new task struct, copies the file descriptor table, and duplicates page tables marking all pages Copy-on-Write (read-only). Physical pages are only duplicated when either process executes a write instruction, triggering a page fault.
4. **Q: What is False Sharing and how do you detect and resolve it?**
   - *A:* False sharing occurs when two independent threads on different cores modify distinct variables that share the same 64-byte cache line, causing cache-coherency invalidation storms. Detected via `perf c2c` and resolved by aligning variables using `alignas(64)`.
5. **Q: Why can a spinlock never be used in Linux interrupt service routine (ISR) context without disabling local interrupts?**
   - *A:* If a thread holds a spinlock and an interrupt arrives on the same core, the ISR attempting to acquire the same spinlock will spin forever, deadlocking the core. The driver must use `spin_lock_irqsave()`.
6. **Q: What is OpenBMC and how does it communicate with the host processor?**
   - *A:* OpenBMC is an open-source Linux distribution running on an ASPEED SoC on the motherboard. It communicates with the host CPU out-of-band via I2C, SMBus, LPC, or eSPI mailboxes without consuming host CPU cycles.
7. **Q: How does Power10 Memory Inception work across server drawers?**
   - *A:* Power10 uses low-latency optical Open Memory Interface (OMI) links to extend load/store memory operations across chassis, allowing a CPU to access remote chassis memory pools as cache-coherent NUMA nodes with sub-100ns latency.
8. **Q: What is the difference between a process and a thread at the Linux kernel level?**
   - *A:* In the Linux kernel, both are represented by `struct task_struct`. The difference is controlled by flags in `clone()`: threads share the address space (`CLONE_VM`), file descriptor table (`CLONE_FILES`), and signal handlers (`CLONE_SIGHAND`), while processes do not.
9. **Q: When would you use a condition variable instead of a busy loop?**
   - *A:* A busy loop consumes 100% of CPU cycles checking a flag. A condition variable puts the waiting thread into the kernel sleep queue, yielding the CPU to other threads until explicitly woken via `notify_one()` or `notify_all()`.
10. **Q: How did you ensure the Warehouse PathMapper fit inside CPU L3 cache?**
    - *A:* I avoided pointer-based node objects. By using a contiguous 1D flat array with spatial coordinates and packing obstacle flags into 64-bit integers, 100 million nodes consumed only 12 MB of memory, residing completely within the L3 cache.
