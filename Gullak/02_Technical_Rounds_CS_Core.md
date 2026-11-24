# Module 02: OS, Concurrency & Networking Internals

Fintech backends demand absolute precision in multi-threading, concurrency control, and socket network behavior. A single race condition in a wallet ledger can duplicate credits or create unauthorized balances.

---

## 1. Operating Systems: Process vs. Thread Memory Layout

When an API server (e.g., in Go or Python/Django) handles concurrent requests, understanding how memory is shared across execution units is fundamental.

```
+------------------------------------+------------------------------------+
|            PROCESS A               |             PROCESS B              |
|  +------------------------------+  |  +------------------------------+  |
|  | Text (Code) & Data / BSS     |  |  | Text (Code) & Data / BSS     |  |
|  | Heap (Shared across Threads) |  |  | Heap (Shared across Threads) |  |
|  +------------------------------+  |  +------------------------------+  |
|  | Thread 1 | Thread 2 | Thread3|  |  | Thread 1 | Thread 2         |  |
|  | Stack 1  | Stack 2  | Stack 3|  |  | Stack 1   | Stack 2         |  |
|  +----------+----------+--------+  |  +-----------+------------------+  |
+------------------------------------+------------------------------------+
```

### Key Distinctions
* **Process:** The unit of resource isolation. Has its own private virtual memory space (Page Tables mapped by the MMU), open file descriptors, signal handlers, and security tokens. A crash in Process A does not corrupt Process B. Context switching between processes requires invalidating the Translation Lookaside Buffer (TLB), costing hundreds of CPU cycles.
* **Thread:** The unit of CPU execution. Multiple threads within the same process share the same Text, Data, Heap, and File Descriptors, but each thread possesses its own **Registers, Program Counter (PC), and private Stack space** (typically 2MB–8MB in Linux C/C++/Java).
* **Goroutine (Golang M:N Model):** Unlike OS threads which require 2MB stack and kernel-level context switches, Go routines start with a tiny **2KB segmented/resizable stack** and are scheduled completely in user-space by the Go runtime scheduler (the $M:N$ scheduler: $M$ OS threads, $N$ goroutines, $P$ logical processors). Millions of goroutines can run simultaneously on a modest server without thread exhaustion.

---

## 2. Concurrency Primitives: Mutex, Spinlock & Atomic CAS

### What is a Race Condition?
A race condition occurs when two concurrent threads read and write to the same shared memory location without synchronization, and the final state depends on the non-deterministic interleaving of instruction execution.

**The Classic Double-Spend Race Condition in Wallet Balances:**
```python
# Thread 1 (Withdrawal of ₹500)       # Thread 2 (Withdrawal of ₹500)
balance = read_balance(user_id) # 600   balance = read_balance(user_id) # 600
if balance >= 500:                      if balance >= 500:
    new_bal = balance - 500 # 100           new_bal = balance - 500 # 100
    write_balance(user_id, new_bal)         write_balance(user_id, new_bal)
# Result: User withdrew ₹1,000 from an initial balance of ₹600!
```

### Synchronization Primitives Compared

| Primitive | Mechanism | When to Use | Trade-off / Penalty |
| :--- | :--- | :--- | :--- |
| **Atomic (CAS)** | CPU instruction (`lock cmpxchg` on x86). Compares memory with expected value; if equal, swaps with new value atomically. | Counters, simple flags, lock-free ring buffers. | Extremely fast (single instruction); cannot protect multi-step complex transactions. |
| **Spinlock** | Loops in a `while (!test_and_set())` busy-wait loop without yielding the CPU core. | Ultra-low latency kernel code, lock held for < 100 nanoseconds. | Wastes CPU cycles if lock held long; dangerous in user space under preemption. |
| **Mutex** | Puts waiting thread into sleeping/blocked state (via Linux `futex` syscall). Kernel wakes thread up when released. | Standard multi-threading where lock is held across I/O or multi-statement blocks. | Incurs OS context switch overhead (~1–3 microseconds) when contending. |
| **Read-Write Lock** | Multiple concurrent readers can acquire; single writer obtains exclusive access. | Read-heavy data (e.g., Live Gold Price Ticker read 10,000x/sec, updated 1x/sec). | Writer starvation if readers constantly stream in (solved via fair RWLocks). |

---

## 3. High-Performance I/O: Select vs. Poll vs. Epoll

Fintech microservices handling thousands of simultaneous WebSockets (e.g., live gold price charts) rely on Linux I/O multiplexing.

```
Select / Poll: O(N) Complexity                  Epoll: O(1) Complexity
-----------------------------                  ----------------------
Passes entire array of N fds                   Kernel tracks fds in a Red-Black Tree.
to kernel on every tick.                       Ready fds pushed into a Ready List.
Kernel iterates through all N fds              epoll_wait() returns ONLY the ready fds.
to find which are ready for I/O.               Cost is proportional to active events, not total fds!
```

* **Select:** Limited to a fixed maximum of 1,024 file descriptors (`FD_SETSIZE`). Must pass the full descriptor set back and forth between user-space and kernel-space every time.
* **Poll:** Overcomes the 1,024 fd limit using dynamic arrays (`pollfd`), but still requires an $O(N)$ linear scan across all descriptors.
* **Epoll (`epoll_create`, `epoll_ctl`, `epoll_wait`):** Edge-triggered and Level-triggered event notification. The kernel registers callbacks on socket state changes. When packets arrive on a NIC, the kernel pushes the corresponding socket to an event ready list. `epoll_wait()` retrieves only active connections in $O(1)$ relative to total connections. Powers **Nginx, Node.js libuv, Go runtime netpoller, and Redis**.

---

## 4. Networking: TCP 3-Way Handshake, Teardown & Socket Exhaustion

### The 3-Way Handshake
```
CLIENT                                SERVER
  │                SYN (seq=x)           │
  ├─────────────────────────────────────►│  Server enters SYN_RCVD
  │                                      │
  │           SYN-ACK (seq=y, ack=x+1)   │
  │◄─────────────────────────────────────┤  Client enters ESTABLISHED
  │                                      │
  │                ACK (ack=y+1)         │
  ├─────────────────────────────────────►│  Server enters ESTABLISHED
```

### The 4-Way Teardown & The Dangerous `TIME_WAIT` State
```
CLIENT (Initiator)                    SERVER
  │                FIN (seq=u)           │
  ├─────────────────────────────────────►│  Server enters CLOSE_WAIT
  │                ACK (ack=u+1)         │
  │◄─────────────────────────────────────┤
  │                FIN (seq=v)           │
  │◄─────────────────────────────────────┤
  │                ACK (ack=v+1)         │
  ├─────────────────────────────────────►│  Server enters CLOSED
  │                                      │
  ▼
[TIME_WAIT] (Lingers for 2 * MSL = 60s)
```

### Why Does `TIME_WAIT` Exist?
1. **Ensures Final ACK Delivery:** If the client's final ACK packet is dropped by the router, the server retransmits its FIN. If the client had immediately closed the port, it would respond with an RST error instead of completing the graceful teardown.
2. **Clears Lingering Duplicate Packets:** Prevents delayed packets from an old connection from arriving and corrupting a newly opened connection reusing the same 4-tuple `(src_ip, src_port, dst_ip, dst_port)`.

### Production Incident: Port Exhaustion Under Microservice Loads
When a backend service calls payment gateways or partner banks (Augmont, Juspay) via short-lived HTTP/1.1 connections without connection pooling:
* The backend initiates socket closure $\to$ Sockets enter `TIME_WAIT` for 60 seconds.
* Linux has ~28,000 ephemeral ports (`/proc/sys/net/ipv4/ip_local_port_range`).
* At 1,000 requests/sec, all 28,000 ports are consumed in 28 seconds, throwing `EADDRNOTAVAIL` (Cannot assign requested address).
* **The Fix:** Enable HTTP Keep-Alive connection pooling (`MaxIdleConnsPerHost`), reuse TCP connections, or tune `tcp_tw_reuse` in Linux sysctl.
