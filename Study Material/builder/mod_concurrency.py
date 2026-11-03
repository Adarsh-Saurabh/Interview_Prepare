# mod_concurrency.py - Concurrency & Parallelism Module Generator
# Conforms to instruction.md Part 7.1 Specification (P0 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Concurrency Fundamentals"),
        ("primitives-matrix", "⚖️ Primitives Selection Matrix"),
        ("memory-models", "🧠 Memory Models & Happens-Before"),
        ("thread-sizing", "📐 Thread Pool Sizing & Latency"),
        ("language-comparison", "🌐 Multi-Language Concurrency Matrix"),
        ("classic-problems", "🧵 Classic Coordination Problems Code"),
        ("thread-safe-structures", "🏗️ Production Thread-Safe Data Structures"),
        ("lock-free-internals", "🚀 Lock-Free & Atomics Deep Dive"),
        ("debugging-concurrency", "🔍 Race Detectors & Concurrency Debugging"),
        ("interview-flashcards", "🎯 32 Top Tech Interview Q&As")
    ]

    # SVG 1: Happens-Before and CPU Memory Reordering
    svg_happens_before = """
    <svg viewBox="0 0 880 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="conc-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="sync-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Thread 1 Column -->
      <rect x="50" y="20" width="340" height="290" rx="10" fill="#111827" stroke="#1e293b" stroke-width="1.5" />
      <text x="220" y="50" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">THREAD 1 (Producer / Writer)</text>
      
      <rect x="80" y="75" width="280" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1" />
      <text x="220" y="100" fill="#f1f5f9" font-size="12" font-family="monospace" text-anchor="middle">data = 42; (Normal Write)</text>

      <line x1="220" y1="120" x2="220" y2="155" stroke="#64748b" stroke-width="2" marker-end="url(#conc-arrow)" />
      <text x="230" y="142" fill="#94a3b8" font-size="10">Program Order</text>

      <rect x="80" y="160" width="280" height="45" rx="6" fill="rgba(52, 211, 153, 0.15)" stroke="#34d399" stroke-width="2" />
      <text x="220" y="182" fill="#34d399" font-size="12" font-weight="700" font-family="monospace" text-anchor="middle">ready.store(true, release);</text>
      <text x="220" y="197" fill="#a7f3d0" font-size="10" text-anchor="middle">Release Barrier: flushes writes before</text>

      <!-- Synchronization Edge across threads -->
      <path d="M 360 182 C 430 182, 450 182, 510 182" fill="none" stroke="#34d399" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#sync-arrow)" />
      <text x="440" y="172" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Synchronizes-With</text>

      <!-- Thread 2 Column -->
      <rect x="490" y="20" width="340" height="290" rx="10" fill="#111827" stroke="#1e293b" stroke-width="1.5" />
      <text x="660" y="50" fill="#a855f7" font-size="14" font-weight="800" text-anchor="middle">THREAD 2 (Consumer / Reader)</text>

      <rect x="520" y="160" width="280" height="45" rx="6" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="2" />
      <text x="660" y="182" fill="#38bdf8" font-size="12" font-weight="700" font-family="monospace" text-anchor="middle">while (!ready.load(acquire));</text>
      <text x="660" y="197" fill="#bae6fd" font-size="10" text-anchor="middle">Acquire Barrier: prevents reads moving up</text>

      <line x1="660" y1="210" x2="660" y2="245" stroke="#64748b" stroke-width="2" marker-end="url(#conc-arrow)" />
      <text x="670" y="232" fill="#94a3b8" font-size="10">Program Order</text>

      <rect x="520" y="250" width="280" height="40" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1" />
      <text x="660" y="275" fill="#34d399" font-size="12" font-family="monospace" text-anchor="middle">assert(data == 42); // GUARANTEED</text>
    </svg>
    """

    # SVG 2: Striped Locks vs Coarse Mutex in Concurrent HashMap
    svg_striped_lock = """
    <svg viewBox="0 0 880 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Coarse Lock (Left) -->
      <rect x="40" y="20" width="360" height="230" rx="8" fill="#111827" stroke="#f43f5e" stroke-width="1.5" />
      <text x="220" y="45" fill="#f43f5e" font-size="13" font-weight="800" text-anchor="middle">COARSE-GRAINED LOCK (Single Global Mutex)</text>
      
      <rect x="60" y="65" width="320" height="40" rx="6" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" />
      <text x="220" y="90" fill="#fca5a5" font-size="11" font-weight="700" text-anchor="middle">Global std::mutex mtx; (Severe Contention)</text>

      <g transform="translate(60, 120)">
        <rect x="0" y="0" width="70" height="110" fill="#1e293b" stroke="#475569" />
        <text x="35" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Bucket 0</text>
        <rect x="80" y="0" width="70" height="110" fill="#1e293b" stroke="#475569" />
        <text x="115" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Bucket 1</text>
        <rect x="160" y="0" width="70" height="110" fill="#1e293b" stroke="#475569" />
        <text x="195" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Bucket 2</text>
        <rect x="240" y="0" width="80" height="110" fill="#1e293b" stroke="#475569" />
        <text x="280" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Bucket N</text>
      </g>

      <!-- Striped Lock (Right) -->
      <rect x="480" y="20" width="360" height="230" rx="8" fill="#111827" stroke="#34d399" stroke-width="1.5" />
      <text x="660" y="45" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">LOCK STRIPING (e.g., 16 Independent Mutexes)</text>

      <g transform="translate(500, 70)">
        <!-- Stripe 0 -->
        <rect x="0" y="0" width="155" height="35" rx="4" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" />
        <text x="77" y="22" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Mutex 0 (Protects 0, 16, 32...)</text>
        
        <!-- Stripe 1 -->
        <rect x="170" y="0" width="155" height="35" rx="4" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" />
        <text x="247" y="22" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Mutex 1 (Protects 1, 17, 33...)</text>
      </g>

      <g transform="translate(500, 120)">
        <rect x="0" y="0" width="70" height="110" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
        <text x="35" y="55" fill="#34d399" font-size="11" text-anchor="middle">Bucket 0</text>
        <text x="35" y="75" fill="#64748b" font-size="9" text-anchor="middle">(Stripe 0)</text>

        <rect x="80" y="0" width="70" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
        <text x="115" y="55" fill="#38bdf8" font-size="11" text-anchor="middle">Bucket 1</text>
        <text x="115" y="75" fill="#64748b" font-size="9" text-anchor="middle">(Stripe 1)</text>

        <rect x="160" y="0" width="70" height="110" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
        <text x="195" y="55" fill="#34d399" font-size="11" text-anchor="middle">Bucket 16</text>
        <text x="195" y="75" fill="#64748b" font-size="9" text-anchor="middle">(Stripe 0)</text>

        <rect x="240" y="0" width="80" height="110" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
        <text x="280" y="55" fill="#38bdf8" font-size="11" text-anchor="middle">Bucket 17</text>
        <text x="280" y="75" fill="#64748b" font-size="9" text-anchor="middle">(Stripe 1)</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Concurrency is about structure (dealing with lots of things at once); parallelism is about execution (doing lots of things at once on multiple cores). Asynchrony is about non-blocking handoffs without burning an OS thread.")}

    <p>Concurrency exists because processors have multiple execution cores, memory subsystems have latency ladders (1ns L1 vs 100ns RAM), and I/O devices are orders of magnitude slower than CPUs. High-concurrency systems must coordinate access to shared state without data corruption, deadlock, or convoy starvation.</p>

    {table(
        headers=["Failure Mode", "Formal Definition", "Minimal Reproducible Example", "Engineering Mitigation"],
        rows=[
            ["Data Race", "Two threads access the same memory location concurrently, at least one write, without synchronization.", "Thread 1: <code>x++</code>, Thread 2: <code>x++</code> simultaneously.", "<code>std::atomic&lt;T&gt;</code>, Mutex lock, Memory Barriers."],
            ["Race Condition", "Flaw in timing/interleaving where program output depends on non-deterministic scheduling.", "Check-then-act: <code>if (!map.contains(k)) map.put(k, v);</code>", "Atomic compound operations, Synchronized blocks."],
            ["Deadlock", "Two or more threads blocked forever, each holding a resource the other needs.", "T1 holds Lock A, wants Lock B. T2 holds Lock B, wants Lock A.", "Strict global lock ordering, <code>std::lock(m1, m2)</code>."],
            ["Livelock", "Threads actively change state in response to each other without making forward progress.", "Two polite threads releasing locks repeatedly when seeing contention.", "Exponential backoff with randomized jitter."],
            ["Starvation", "A runnable thread is perpetually denied CPU time or locks due to unfair scheduling.", "Low priority thread waiting behind endless stream of high-priority threads.", "FIFO queue fairness, aging, ticket locks."],
            ["Priority Inversion", "Low-priority thread holds lock needed by high-priority thread; mid-priority thread preempts low.", "Mars Pathfinder anomaly: Information bus mutex held by meteorology task.", "Priority Inheritance Protocol (PIP)."]
        ]
    )}

    {callout(
        title="Spurious Wakeups: Why condition variables MUST use a while loop",
        body="A thread waiting on a condition variable can wake up even if no thread signaled it (OS scheduler preemption, signal interrupts, or another thread woke up first and consumed the predicate). If you write <code>if (!ready) cv.wait(lock);</code>, the thread proceeds on spurious wakeup with invalid state! Always write <code>while (!ready) cv.wait(lock);</code> or <code>cv.wait(lock, [&amp;]{{ return ready; }});</code>.",
        kind="trap"
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Concurrency Fundamentals", s1_body, pill="Core Mechanics", pill_color="indigo"))

    # Section 2: Primitives Matrix
    s2_body = f"""
    <p>Interviews evaluate your ability to select the <em>cheapest synchronization primitive</em> that satisfies correctness guarantees without over-locking.</p>

    {decision_matrix(
        title="Synchronization Primitives Selection",
        options=[
            ("std::mutex", "Mutual exclusion for critical sections with unpredictable duration or complex object mutation.", "Sub-microsecond hot paths (high kernel context switch cost); read-heavy workloads."),
            ("Spinlock", "Ultra-short critical sections (≤ 50 CPU cycles) where thread sleep/wakeup latency (>2µs) dominates.", "Single-core CPUs; critical sections that perform I/O, allocate memory, or yield."),
            ("std::shared_mutex (RW Lock)", "Workloads with &gt;90% reads and infrequent writes where multiple concurrent readers boost throughput.", "Write-heavy workloads; very short reads where atomic refcount cache contention exceeds lock savings."),
            ("Counting Semaphore", "Resource pool throttling (e.g., maximum 10 concurrent database connections or bounded queues).", "Simple mutual exclusion (mutex is cleaner and has ownership semantics)."),
            ("Condition Variable", "Thread coordination based on state changes (Producer-Consumer buffer empty/full).", "Stateless synchronization (use events/latches); atomic flags."),
            ("std::atomic<T>", "Single primitive variable updates (counters, boolean flags, pointers) without locking.", "Multi-variable invariant updates (e.g., updating balance AND transaction log together).")
        ]
    )}

    {svg_card(svg_striped_lock, "Coarse-Grained Global Mutex vs Lock Striping (16 Independent Mutex Buckets)")}
    """
    content.append(section("primitives-matrix", "⚖️ Primitives Selection Matrix", s2_body, pill="Decision Matrix", pill_color="blue"))

    # Section 3: Memory Models
    s3_body = f"""
    <p>Modern out-of-order CPUs (x86, ARM64) and optimizing compilers aggressively reorder instructions as long as single-threaded semantics are preserved. Without memory barriers, writes on Core 0 may become visible to Core 1 out of order.</p>

    {svg_card(svg_happens_before, "Happens-Before Relationship via Release-Acquire Synchronization Barrier")}

    {table(
        headers=["Memory Order", "Guarantees", "Cost on x86-64", "Cost on ARM64 / PowerPC", "Canonical Use-Case"],
        rows=[
            ["<code>memory_order_relaxed</code>", "Atomicity only. Zero ordering or synchronization guarantees.", "0 cycles (plain mov)", "0 cycles (plain ldr/str)", "Incrementing statistics counters, metrics."],
            ["<code>memory_order_acquire</code>", "Prevents memory reads/writes after this load from being reordered before it.", "0 cycles (x86 loads already acquire)", "DMB barrier instruction (~5-15 cycles)", "Reading flags, Consumer lock acquisition."],
            ["<code>memory_order_release</code>", "Prevents memory reads/writes before this store from being reordered after it.", "0 cycles (x86 stores already release)", "DMB barrier instruction (~5-15 cycles)", "Publishing shared data, Producer release."],
            ["<code>memory_order_acq_rel</code>", "Combined acquire and release barrier for Read-Modify-Write operations.", "0 cycles (except LOCK prefix)", "Full memory barrier (~15-30 cycles)", "CAS loops, reference counting (fetch_sub)."],
            ["<code>memory_order_seq_cst</code>", "Sequential consistency. Single global total order visible across all cores.", "LOCK prefix / MFENCE (~20-40 cycles)", "Full DMB ISH barrier (~20-40 cycles)", "Default atomic operations; critical algorithms."]
        ]
    )}

    {callout(
        title="Why 'volatile' does NOT mean thread-safe in C++ and Java",
        body="In C/C++, <code>volatile</code> tells the compiler not to optimize away reads/writes to memory-mapped hardware registers. It provides <strong>zero atomicity and zero memory barriers</strong>! In Java, <code>volatile</code> provides visibility and acquire-release ordering, but still no atomicity for compound operations like <code>i++</code>.",
        kind="trap"
    )}
    """
    content.append(section("memory-models", "🧠 Memory Models & Happens-Before", s3_body, pill="Low-Latency", pill_color="indigo"))

    # Section 4: Thread Sizing
    s4_body = f"""
    {formula_box(
        katex_display=r"$$N_{\text{threads}} = N_{\text{CPU}} \times \left(1 + \frac{\text{Wait Time}}{\text{Compute Time}}\right)$$",
        reading="Optimal pool threads equals CPU core count multiplied by one plus ratio of I/O wait time to compute time.",
        symbols=[
            ("N_threads", "Target thread pool worker count"),
            ("N_CPU", "Available hardware execution threads / CPU cores"),
            ("Wait Time", "Time spent waiting for socket I/O, disk read, or database response"),
            ("Compute Time", "Time spent executing CPU instructions (parsing, hashing, serialization)")
        ],
        meaning="For purely CPU-bound tasks (matrix multiply), set pool size = N_CPU (extra threads cause context-switch thrashing). For I/O-bound tasks with 90% wait time (wait/compute = 9), pool size = 10 * N_CPU."
    )}

    {worked_example(
        title="Deriving Thread Count for a High-Throughput REST Gateway",
        steps=[
            ("Identify Workload Metrics", "A server has 16 vCPU cores. Profiling reveals average request processing takes 5ms of CPU JSON serialization and 45ms of database socket wait time."),
            ("Compute Wait-to-Compute Ratio", r"$$\frac{\text{Wait}}{\text{Compute}} = \frac{45\text{ms}}{5\text{ms}} = 9$$"),
            ("Apply Sizing Formula", r"$$N_{\text{threads}} = 16 \times (1 + 9) = 160\text{ worker threads}$$")
        ],
        answer="Setting the thread pool to 160 threads achieves maximum hardware utilization without CPU starvation. If set to 16, 90% of cores remain idle during network stalls."
    )}
    """
    content.append(section("thread-sizing", "📐 Thread Pool Sizing & Latency", s4_body, pill="Capacity", pill_color="emerald"))

    # Section 5: Multi-Language Comparison
    s5_body = f"""
    {table(
        headers=["Language / Runtime", "Threading Model", "Memory Isolation", "GIL / Runtime Lock", "Optimal Workload Pattern"],
        rows=[
            ["C++ (std::thread)", "1:1 Native OS Threads.", "Shared address space; manual synchronization.", "None. True CPU hardware parallelism.", "High-Frequency Trading, Game Engines, Systems."],
            ["Python (CPython)", "1:1 OS Threads under GIL.", "Shared memory across threads; separate in multiprocessing.", "CPython Global Interpreter Lock (GIL).", "AsyncIO for I/O bounds; Multiprocessing for CPU."],
            ["Java (JVM / Loom)", "Platform Threads (1:1) + Virtual Threads (M:N).", "Shared heap with garbage collector.", "JVM HotSpot object monitors.", "Enterprise microservices, high-concurrency web."],
            ["Go (Goroutines)", "M:N User-space Scheduler (GMP model).", "Shared heap; channels promote shared-nothing.", "No GIL. Cooperative preemption at function prologue.", "Cloud-native services, Kubernetes, microservices."]
        ]
    )}
    """
    content.append(section("language-comparison", "🌐 Multi-Language Concurrency Matrix", s5_body, pill="Cross-Platform", pill_color="teal"))

    # Section 6: Classic Coordination Problems
    s6_body = f"""
    <p>These coordination problems are the verbatim coding challenges asked in Anthropic, OpenAI, and Apple concurrency rounds.</p>

    {subsection("classic-foobar", "1. Print FooBar Alternately (C++ Condition Variables & Semaphores)")}
    {code(
        src=r"""#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

class FooBar {
private:
    int n;
    std::mutex mtx;
    std::condition_variable cv;
    bool foo_turn = true;

public:
    FooBar(int n) : n(n) {}

    void foo() {
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this]() { return foo_turn; });
            std::cout << "foo";
            foo_turn = false;
            cv.notify_one();
        }
    }

    void bar() {
        for (int i = 0; i < n; i++) {
            std::unique_lock<std::mutex> lock(mtx);
            cv.wait(lock, [this]() { return !foo_turn; });
            std::cout << "bar";
            foo_turn = true;
            cv.notify_one();
        }
    }
};""",
        lang="cpp",
        title="FooBar Coordination in C++"
    )}

    {subsection("classic-h2o", "2. Building H2O Molecule Coordination (Python Condition Variables)")}
    {code(
        src=r"""import threading

class H2O:
    def __init__(self):
        self.lock = threading.Lock()
        self.cv = threading.Condition(self.lock)
        self.h_count = 0

    def hydrogen(self, releaseHydrogen):
        with self.cv:
            while self.h_count == 2:
                self.cv.wait()
            self.h_count += 1
            releaseHydrogen()
            self.cv.notify_all()

    def oxygen(self, releaseOxygen):
        with self.cv:
            while self.h_count < 2:
                self.cv.wait()
            releaseOxygen()
            self.h_count = 0
            self.cv.notify_all()""",
        lang="python",
        title="Building H2O Molecule Synchronization"
    )}
    """
    content.append(section("classic-problems", "🧵 Classic Coordination Problems Code", s6_body, pill="Coding Drills", pill_color="rose", depth="deep"))

    # Section 7: Thread-Safe Data Structures
    s7_body = f"""
    {subsection("struct-bounded-queue", "1. Thread-Safe Bounded Blocking Queue")}
    {code(
        src=r"""#include <queue>
#include <mutex>
#include <condition_variable>

template <typename T>
class BoundedBlockingQueue {
private:
    std::queue<T> queue_;
    size_t capacity_;
    std::mutex mtx_;
    std::condition_variable not_full_;
    std::condition_variable not_empty_;

public:
    explicit BoundedBlockingQueue(size_t capacity) : capacity_(capacity) {}

    void push(T value) {
        std::unique_lock<std::mutex> lock(mtx_);
        not_full_.wait(lock, [this] { return queue_.size() < capacity_; });
        queue_.push(std::move(value));
        not_empty_.notify_one();
    }

    T pop() {
        std::unique_lock<std::mutex> lock(mtx_);
        not_empty_.wait(lock, [this] { return !queue_.empty(); });
        T value = std::move(queue_.front());
        queue_.pop();
        not_full_.notify_one();
        return value;
    }
};""",
        lang="cpp",
        title="Production Bounded Blocking Queue"
    )}

    {followup_chain(
        root_question="What is the bottleneck in this BoundedBlockingQueue when scaled to 64 threads?",
        chain=[
            ("Both push() and pop() contend on the same std::mutex mtx_, causing core cache-line invalidation.", "Split into two distinct locks: one head_mutex_ for pops and one tail_mutex_ for pushes, using a dummy node."),
            ("Now push and pop operate independently, but how do they coordinate capacity without locking both?", "Use an std::atomic<size_t> count_ with acquire-release ordering or separate producer/consumer semaphores."),
            ("When does this two-lock queue still degrade?", "Under extreme load, false sharing occurs if head_mutex_ and tail_mutex_ share the same 64-byte L1 cache line. Fix with alignas(64).")
        ]
    )}
    """
    content.append(section("thread-safe-structures", "🏗️ Production Thread-Safe Data Structures", s7_body, pill="Systems Design", pill_color="purple", depth="deep"))

    # Section 8: Lock-Free Internals
    s8_body = f"""
    <p>Lock-free programming guarantees that <em>at least one thread makes progress</em> in a finite number of steps, eliminating priority inversion and deadlock. However, it requires meticulous memory ordering to avoid the ABA problem and cache thrashing.</p>

    {code(
        src=r"""#include <atomic>
#include <cstddef>
#include <new>

template <typename T, size_t Capacity>
class LockFreeSPSCQueue {
    static_assert((Capacity & (Capacity - 1)) == 0, "Capacity must be power of 2");
private:
    T buffer_[Capacity];
    
    // Align to separate 64-byte cache lines to eliminate False Sharing
    alignas(64) std::atomic<size_t> tail_{0}; // Written by Producer
    alignas(64) std::atomic<size_t> head_{0}; // Written by Consumer

public:
    bool push(const T& item) {
        size_t current_tail = tail_.load(std::memory_order_relaxed);
        size_t current_head = head_.load(std::memory_order_acquire);
        
        if (current_tail - current_head >= Capacity) return false; // Full
        
        buffer_[current_tail & (Capacity - 1)] = item;
        tail_.store(current_tail + 1, std::memory_order_release);
        return true;
    }

    bool pop(T& item) {
        size_t current_head = head_.load(std::memory_order_relaxed);
        size_t current_tail = tail_.load(std::memory_order_acquire);
        
        if (current_head == current_tail) return false; // Empty
        
        item = buffer_[current_head & (Capacity - 1)];
        head_.store(current_head + 1, std::memory_order_release);
        return true;
    }
};""",
        lang="cpp",
        title="Lock-Free Single-Producer Single-Consumer (SPSC) Ring Buffer"
    )}

    {see_also([
        ("cpp_systems.html", "atomic-memory", "C++ Atomics & Memory Ordering"),
        ("coa.html", "false-sharing", "COA False Sharing & alignas(64)"),
        ("os.html", "sync-primitives", "OS Futexes & Spinlocks")
    ])}
    """
    content.append(section("lock-free-internals", "🚀 Lock-Free & Atomics Deep Dive", s8_body, pill="HFT Depth", pill_color="indigo", depth="deep"))

    # Section 9: Debugging Concurrency
    s9_body = f"""
    {table(
        headers=["Debugging Tool", "Technology & Mechanism", "Overhead", "Detection Capability"],
        rows=[
            ["ThreadSanitizer (TSan)", "Compiler instrumentation (Clang/GCC <code>-fsanitize=thread</code>). Intercepts every memory access.", "5×-15× CPU, 5×-10× RAM", "Data races, deadlocks, lock-order inversions."],
            ["Valgrind Helgrind", "Binary dynamic instrumentation. Tracks POSIX pthread API calls.", "20×-50× slowdown", "POSIX mutex misuse, lock order cycles, data races."],
            ["Deterministic Replay", "Records scheduler decisions and thread inter-leavings to replay elusive bugs.", "Moderate", "Heisenbugs (bugs that disappear under debugging/print statements)."]
        ]
    )}

    {callout(
        title="The Heisenbug Trap in Concurrency Debugging",
        body="Adding <code>printf</code> or <code>std::cout</code> to debug a concurrency race condition almost always hides the bug. Console logging performs system calls and acquires internal I/O mutexes, adding tens of thousands of CPU cycles of latency and forcing memory barriers that serialize the threads. Always debug with TSan or lock-free ring-buffer trace logs.",
        kind="trap"
    )}
    """
    content.append(section("debugging-concurrency", "🔍 Race Detectors & Concurrency Debugging", s9_body, pill="Tooling", pill_color="amber", depth="deep"))

    # Section 10: 32 Interview Flashcards
    qa_list = [
        ("Concurrency vs Parallelism — explain in one sentence each.",
         "Concurrency is about handling multiple tasks by interleaving their execution over time (structural); parallelism is about executing multiple tasks simultaneously across physically separate hardware cores (computational).",
         ["Fundamentals"], "Easy", ["Anthropic", "Apple"]),
        ("What is the difference between a Data Race and a Race Condition?",
         "A Data Race occurs when two threads access the same memory location concurrently without synchronization and at least one is a write (Undefined Behavior in C++). A Race Condition is a higher-level semantic timing flaw where valid operations occur in an unexpected sequence (e.g. check-then-act).",
         ["Core CS"], "Medium", ["OpenAI", "Google"]),
        ("Why must condition_variable wait() ALWAYS be placed inside a while loop?",
         "Because of spurious wakeups (the OS kernel may unblock the thread without an explicit notification) and stolen wakes (another thread may wake up first and invalidate the predicate before this thread acquires the mutex).",
         ["POSIX"], "Easy", ["Qualcomm", "Pace"]),
        ("What is a Livelock? Give an example that is not a deadlock.",
         "A state where threads continuously change their states in response to each other without making forward progress. Example: Two ethernet nodes detecting collision and repeatedly attempting retransmission at the exact same fixed time interval, or two courteous threads repeatedly releasing locks to let the other pass.",
         ["Failures"], "Medium", ["Microsoft"]),
        ("Explain the ABA problem in Compare-And-Swap (CAS) lock-free algorithms.",
         "Thread 1 reads pointer value A. Thread 2 preempts, changes A to B, and then changes it back to A. Thread 1 resumes and executes CAS(A, C), succeeding because the memory address is still A, unaware that the underlying node or state was mutated. Mitigation: Tagged pointers with monotonic version counters (Double-CAS).",
         ["Lock-Free"], "Hard", ["Pace (₹41L)", "Jane Street"]),
        ("What is Priority Inversion and how does Priority Inheritance solve it?",
         "When a high-priority thread H is blocked waiting for a lock held by low-priority thread L, and a medium-priority thread M preempts L because M has higher priority than L, preventing L from finishing and releasing the lock for H. Priority Inheritance dynamically elevates L's priority to H's level until L releases the lock.",
         ["Real-Time"], "Medium", ["Apple", "Texas Instruments"]),
        ("How do you size a thread pool for CPU-bound vs I/O-bound workloads?",
         "For CPU-bound tasks: N_threads = N_CPU (or N_CPU + 1 to absorb page faults). For I/O-bound tasks: N_threads = N_CPU * (1 + Wait_Time / Compute_Time).",
         ["Architecture"], "Medium", ["Amazon", "Palantir"]),
        ("Why does adding more threads sometimes make a multi-threaded application slower?",
         "Due to Amdahl's law serial bottlenecks, excessive OS context switching overhead, thread scheduling quantum preemption, and severe CPU cache coherence traffic (cache-line bouncing and false sharing).",
         ["Performance"], "Medium", ["Meta", "Netflix"]),
        ("What is False Sharing and how do you prevent it in C++?",
         "When two threads running on different cores modify independent variables that reside within the same 64-byte L1 cache line, forcing continuous cache invalidation traffic (MESI protocol bouncing). Prevent by padding variables using alignas(64) or std::hardware_destructive_interference_size.",
         ["Hardware"], "Hard", ["Pace", "Nvidia"]),
        ("What is the difference between memory_order_relaxed and memory_order_seq_cst?",
         "memory_order_relaxed guarantees only atomicity of the single operation with zero synchronization or ordering guarantees relative to other memory accesses. memory_order_seq_cst enforces a single total globally consistent order of all operations across all cores.",
         ["Atomics"], "Hard", ["Qualcomm", "Apple"]),
        ("Why is double-checked locking broken without memory barriers / volatile?",
         "Because instruction reordering allows memory allocation and pointer assignment (instance = raw_ptr) to execute before the object constructor completes. A concurrent thread can see instance != nullptr and access uninitialized memory.",
         ["Patterns"], "Medium", ["Google", "Adobe"]),
        ("What is a Futex in Linux and why is it faster than a classic kernel semaphore?",
         "A Fast Userspace Mutex. On uncontended lock acquisition/release, it executes purely in user space via atomic CAS instructions without any system call. It only enters the Linux kernel (sys_futex) to put the thread to sleep when real contention occurs.",
         ["Linux"], "Hard", ["Qualcomm", "Pace"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s10_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 32 Top Tech Interview Q&As", s10_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
