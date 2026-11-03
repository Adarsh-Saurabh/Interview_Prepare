# mod_cpp_systems.py - C++ Internals & Low-Latency Systems Generator
# Conforms to instruction.md Part 6.8 Specification (P1 Track B - Pace Stock Broking Focus)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: OOP Internals, Move & Memory Orders"),
        ("vtable-memory-svg", "📊 VTable Layout, Smart Pointers & Control Blocks"),
        ("move-perfect-forwarding", "⚡ Move Semantics, Universal References & Forwarding"),
        ("lockfree-spsc-buffer", "🚀 Lock-Free SPSC Ring Buffer & Memory Models"),
        ("hft-low-latency-toolkit", "⚡ Low-Latency & HFT Systems Toolkit (Pace ₹41L)"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: VTable Memory Layout
    svg_vtable = """
    <svg viewBox="0 0 860 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="vptr-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>
      <!-- Object in Memory -->
      <rect x="30" y="30" width="220" height="210" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="140" y="55" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Derived Object (Stack/Heap)</text>

      <!-- Hidden __vptr -->
      <rect x="45" y="70" width="190" height="40" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="140" y="92" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">*__vptr (8 Bytes)</text>
      <text x="140" y="105" fill="#bae6fd" font-size="8" text-anchor="middle">Hidden pointer at offset 0</text>

      <!-- Member int x -->
      <rect x="45" y="120" width="190" height="30" rx="4" fill="#334155" />
      <text x="140" y="140" fill="#f1f5f9" font-size="11" text-anchor="middle">int x (Base member)</text>

      <!-- Member int y -->
      <rect x="45" y="160" width="190" height="30" rx="4" fill="#334155" />
      <text x="140" y="180" fill="#f1f5f9" font-size="11" text-anchor="middle">int y (Derived member)</text>

      <line x1="235" y1="90" x2="330" y2="90" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#vptr-arrow)" />

      <!-- VTable in .rodata -->
      <rect x="340" y="30" width="230" height="210" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
      <text x="455" y="55" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">Derived VTable (.rodata segment)</text>

      <!-- Slot 0: typeinfo -->
      <rect x="355" y="70" width="200" height="30" rx="4" fill="#1e293b" />
      <text x="455" y="90" fill="#94a3b8" font-size="10" text-anchor="middle">[0]: RTTI typeinfo pointer</text>

      <!-- Slot 1: virtual funcA() -->
      <rect x="355" y="110" width="200" height="35" rx="4" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
      <text x="455" y="128" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[1]: &amp;Derived::funcA()</text>
      <text x="455" y="140" fill="#a7f3d0" font-size="8" text-anchor="middle">Overridden Derived Function</text>

      <!-- Slot 2: virtual ~Destructor() -->
      <rect x="355" y="155" width="200" height="35" rx="4" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
      <text x="455" y="173" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">[2]: &amp;Derived::~Derived()</text>
      <text x="455" y="185" fill="#fecdd3" font-size="8" text-anchor="middle">Virtual Destructor</text>

      <text x="600" y="110" fill="#94a3b8" font-size="11" font-weight="600">Dynamic Dispatch Cost:</text>
      <text x="600" y="130" fill="#38bdf8" font-size="10">1. Dereference obj->__vptr</text>
      <text x="600" y="150" fill="#38bdf8" font-size="10">2. Index into vtable[slot]</text>
      <text x="600" y="170" fill="#38bdf8" font-size="10">3. Indirect function call (Prevents inlining!)</text>
    </svg>
    """

    # SVG 2: std::shared_ptr Control Block Memory Layout
    svg_control_block = """
    <svg viewBox="0 0 880 240" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="860" height="220" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
      
      <!-- shared_ptr object on Stack (16 bytes) -->
      <rect x="30" y="30" width="220" height="120" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="140" y="55" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">std::shared_ptr&lt;T&gt; (16 Bytes)</text>
      
      <rect x="45" y="70" width="190" height="30" rx="4" fill="#0369a1" />
      <text x="140" y="90" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Pointer to Object T* (8 Bytes)</text>

      <rect x="45" y="105" width="190" height="30" rx="4" fill="#0f766e" />
      <text x="140" y="125" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Pointer to Control Block* (8 Bytes)</text>

      <!-- Arrows -->
      <line x1="235" y1="85" x2="350" y2="85" stroke="#38bdf8" stroke-width="2" />
      <line x1="235" y1="120" x2="350" y2="150" stroke="#34d399" stroke-width="2" />

      <!-- Managed Object T on Heap -->
      <rect x="350" y="30" width="200" height="80" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <text x="450" y="55" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Managed Object T (Heap)</text>
      <text x="450" y="80" fill="#94a3b8" font-size="10" text-anchor="middle">Raw Data: int, string, buffer...</text>

      <!-- Control Block on Heap -->
      <rect x="350" y="125" width="480" height="90" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="2" />
      <text x="590" y="145" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Dynamic Control Block (Heap)</text>

      <g transform="translate(365, 155)">
        <rect x="0" y="0" width="140" height="45" rx="4" fill="#064e3b" />
        <text x="70" y="20" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Strong RefCount (atomic)</text>
        <text x="70" y="35" fill="#a7f3d0" font-size="8" text-anchor="middle">Number of shared_ptrs</text>

        <rect x="155" y="0" width="140" height="45" rx="4" fill="#065f46" />
        <text x="225" y="20" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Weak RefCount (atomic)</text>
        <text x="225" y="35" fill="#a7f3d0" font-size="8" text-anchor="middle">Number of weak_ptrs</text>

        <rect x="310" y="0" width="140" height="45" rx="4" fill="#334155" />
        <text x="380" y="20" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">Custom Deleter &amp; Alloc</text>
        <text x="380" y="35" fill="#94a3b8" font-size="8" text-anchor="middle">Virtual destructor slot</text>
      </g>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P1 Track B", "indigo"), ("Systems & HFT", "rose"), ("Pace ₹41L Target", "amber"), ("15-Min Sprint", "teal")])
        + callout(
            "C++ Systems & Low-Latency Ground Rules",
            "Targeting high-frequency trading (HFT) and core systems engineering firms (Pace Stock Broking ₹41L, Texas Instruments, Qualcomm, Apple) requires mastery over hardware-software boundaries: zero dynamic heap allocation on the hot path, atomic memory ordering without cache-line bouncing, lock-free ring buffers, cache alignment (`alignas(64)`), and compile-time template metaprogramming.",
            "important"
        )
        + numbers_card("C++ Microarchitecture & Latency Magnitudes", [
            ("L1 Cache Access", "~1 ns (4 cycles)", "L1 hit latency on modern x86/ARM cores"),
            ("Uncontended Atomic Load/Store", "~2 - 5 ns", "Atomic operation with relaxed / acquire-release ordering"),
            ("Contended Atomic CAS / RFO Bounce", "~20 - 40 ns", "Cross-core bus cache line invalidation cycle"),
            ("Virtual Function Call Overhead", "~2 - 5 ns", "Indirect branch misprediction + vptr dereference"),
            ("malloc() / free() Hot Path", "~30 - 100 ns", "Heap allocator locks & thread cache traversal (Strictly Banned in HFT!)"),
            ("Cache Line Size", "64 Bytes", "Standard hardware block transferred between cache and RAM")
        ])
        + subsection(
            "smart-pointers-matrix",
            "Smart Pointers Master Comparison: Memory & Mechanics",
            table(
                ["Smart Pointer", "Size on 64-bit", "Ownership Model", "Atomic Overhead?", "Interview Gotcha / Trap"],
                [
                    ["`std::unique_ptr<T>`", "8 Bytes (zero overhead!)", "Exclusive ownership. Move-only type.", "Zero atomic overhead", "Custom deleter as function pointer inflates size to 16 bytes! Use stateless lambda."],
                    ["`std::shared_ptr<T>`", "16 Bytes (Raw T* + ControlBlock*)", "Shared reference-counted ownership.", "Yes: RefCount increment/decrement uses atomic CAS", "Atomic ref count protects control block ONLY! The pointee T is NOT thread-safe!"],
                    ["`std::weak_ptr<T>`", "16 Bytes (Raw T* + ControlBlock*)", "Non-owning observer. Breaks reference cycles.", "Yes: atomic weak refcount", "Cannot access object directly. Must call `.lock()` which returns a `shared_ptr`."]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "memory-orders-matrix",
            "C++11 Memory Models & Atomic Orderings",
            table(
                ["Memory Order", "Ordering Guarantee", "Hardware Cost on x86-64", "Primary Production Use Case"],
                [
                    ["`memory_order_relaxed`", "Atomicity only; ZERO synchronization or ordering constraints", "Free: standard CPU instruction", "Atomic performance counters, metrics"],
                    ["`memory_order_consume`", "Data-dependency ordering (discouraged; compilers promote to acquire)", "Free", "Rarely used in practice"],
                    ["`memory_order_acquire`", "No memory reads/writes in current thread can be reordered BEFORE this load", "Free on x86! (x86 hardware enforces Total Store Order / TSO)", "Acquiring mutex, consumer reading lock-free queue head"],
                    ["`memory_order_release`", "No memory reads/writes in current thread can be reordered AFTER this store", "Free on x86!", "Releasing mutex, producer updating lock-free queue tail"],
                    ["`memory_order_acq_rel`", "Both Acquire and Release combined on Read-Modify-Write", "Free on x86 (except for locked instructions)", "Atomic `fetch_add`, `compare_exchange` locks"],
                    ["`memory_order_seq_cst`", "Sequentially Consistent: globally agreed total order across all threads", "Costly: requires `MFENCE` or locked `XCHG` on x86!", "Default `std::atomic` operations when unsure"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "raii-rule-of-5",
            "RAII & The Rule of 5 / Rule of 0",
            callout(
                "The Rule of 5 for Resource-Managing Classes",
                "If a class manages an acquired resource (raw pointer, file handle, socket, mutex), you must explicitly declare or delete all FIVE special member functions:\n"
                "1. **Destructor**: `~MyClass()` — releases resource.\n"
                "2. **Copy Constructor**: `MyClass(const MyClass&)` — deep copy.\n"
                "3. **Copy Assignment**: `MyClass& operator=(const MyClass&)`.\n"
                "4. **Move Constructor**: `MyClass(MyClass&&) noexcept` — steals pointer, zeroes source.\n"
                "5. **Move Assignment**: `MyClass& operator=(MyClass&&) noexcept`.\n"
                "**Rule of Zero**: Prefer classes that manage NO raw resources directly (use `std::string`, `std::vector`, `std::unique_ptr`). The compiler auto-generates all 5 correctly!",
                "important"
            ),
            depth="sprint"
        )
    )

    # Section 2: VTable & Smart Pointer Architecture
    vtable_html = (
        subsection(
            "vtable-internals",
            "VTable Internal Layout & Virtual Destructors",
            svg_card("C++ Virtual Table (VTable) Layout in Memory", svg_vtable)
            + callout(
                "Why Base Classes MUST Have a Virtual Destructor",
                "If a derived object is deleted through a pointer to its base class (`Base* ptr = new Derived(); delete ptr;`):\n"
                "• If `~Base()` is **NOT virtual**: The compiler resolves the destructor statically to `Base::~Base()`. The `Derived` destructor is NEVER invoked! Any resources allocated by `Derived` (heap memory, sockets, file locks) leak immediately. Undefined Behaviour under C++ standard.\n"
                "• If `~Base()` is **virtual**: The destructor is called dynamically via the vtable, executing `Derived::~Derived()` first, then chaining to `Base::~Base()` cleanly.",
                "important"
            )
            + svg_card("std::shared_ptr Control Block Architecture", svg_control_block),
            depth="deep"
        )
        + subsection(
            "make-shared-vs-new",
            "std::make_shared vs std::shared_ptr(new T)",
            decision_matrix(
                "shared_ptr Allocation Strategies",
                [
                    ("std::make_shared<T>()", "Allocates Managed Object T and Control Block in a SINGLE contiguous heap chunk. 1 allocation instead of 2. Cache friendly.", "If large weak_ptrs outlive shared_ptrs, the entire combined memory block cannot be deallocated until all weak_ptrs die!"),
                    ("std::shared_ptr<T>(new T())", "Need custom deleters, or when object T is massive and weak_ptrs persist for a long time.", "Performs TWO separate heap allocations (`new T` and control block). Slower and fragments memory.")
                ]
            ),
            depth="deep"
        )
    )

    # Section 3: Move Semantics & Perfect Forwarding
    move_html = (
        subsection(
            "move-semantics",
            "Move Semantics & Universal References (Forwarding References)",
            callout(
                "What std::move Actually Compiles To (The Big Interview Secret)",
                "`std::move` generates **ZERO assembly instructions** and moves absolutely nothing at runtime!\n"
                "It is purely a compile-time `static_cast<T&&>(x)` that unconditionally casts an lvalue to an rvalue (xvalue), allowing the compiler to select the move constructor instead of the copy constructor.",
                "tip"
            )
            + callout(
                "Universal References & Reference Collapsing Rules",
                "A template parameter `T&&` in a type-deducing context is a **Forwarding Reference** (Universal Reference), NOT an rvalue reference!\n"
                "Reference Collapsing Rules:\n"
                "• `&` + `&` → `&`\n"
                "• `&` + `&&` → `&`\n"
                "• `&&` + `&` → `&`\n"
                "• `&&` + `&&` → `&&` (Only rvalue + rvalue collapses to rvalue!)\n"
                "`std::forward<T>(arg)` conditionally casts to rvalue only if `T` was deduced as a non-reference (preserving original argument category).",
                "important"
            )
            + code(r"""#include <utility>
#include <memory>

// Perfect-Forwarding Factory Function
template <typename T, typename... Args>
std::unique_ptr<T> make_custom(Args&&... args) {
    // std::forward preserves whether each argument was lvalue or rvalue
    return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
}""", "cpp", "perfect_forwarding_factory.cpp"),
            depth="deep"
        )
    )

    # Section 4: Lock-Free SPSC Ring Buffer
    lockfree_html = (
        subsection(
            "spsc-ring-buffer",
            "Lock-Free Single-Producer Single-Consumer (SPSC) Ring Buffer",
            callout(
                "The Holy Grail of Low-Latency Systems (Pace / HFT Core)",
                "An SPSC ring buffer enables communication between a network-polling thread and a trading-logic thread with ZERO mutex locks, ZERO context switches, and sub-10ns latency using acquire-release atomics and cache-line padding.",
                "tip"
            )
            + code(r"""#include <atomic>
#include <cstddef>
#include <new>

template <typename T, size_t Capacity>
class LockFreeSPSCQueue {
    static_assert((Capacity & (Capacity - 1)) == 0, "Capacity must be power of 2");

    alignas(64) T buffer_[Capacity]; // Cache-line aligned buffer

    // Head (Reader index) padded to separate 64-byte cache line
    alignas(64) std::atomic<size_t> head_{0};

    // Tail (Writer index) padded to separate 64-byte cache line to prevent False Sharing!
    alignas(64) std::atomic<size_t> tail_{0};

public:
    // Producer pushes element into queue (Lock-Free)
    bool push(const T& item) {
        const size_t current_tail = tail_.load(std::memory_order_relaxed);
        const size_t current_head = head_.load(std::memory_order_acquire);

        if ((current_tail - current_head) == Capacity) {
            return false; // Queue full
        }

        buffer_[current_tail & (Capacity - 1)] = item;
        // Release ordering guarantees item write is visible before tail is updated!
        tail_.store(current_tail + 1, std::memory_order_release);
        return true;
    }

    // Consumer pops element from queue (Lock-Free)
    bool pop(T& item) {
        const size_t current_head = head_.load(std::memory_order_relaxed);
        const size_t current_tail = tail_.load(std::memory_order_acquire);

        if (current_head == current_tail) {
            return false; // Queue empty
        }

        item = buffer_[current_head & (Capacity - 1)];
        // Release ordering guarantees item read before head update is visible to writer
        head_.store(current_head + 1, std::memory_order_release);
        return true;
    }
};""", "cpp", "lockfree_spsc_queue.hpp"),
            depth="deep"
        )
    )

    # Section 5: Low-Latency Toolkit
    hft_html = (
        subsection(
            "hft-optimizations",
            "Low-Latency Toolkit: Kernel Bypass, CPU Pinning & Memory Pools",
            table(
                ["Optimization Technique", "Mechanism / Linux Tool", "Latency Impact"],
                [
                    ["CPU Core Pinning & Isolation", "`pthread_setaffinity_np` + Linux boot param `isolcpus=2,3`", "Eliminates OS scheduler context switches and core migrations (~1 µs saved)"],
                    ["Kernel Bypass (DPDK / Solarflare)", "Direct user-space access to network card NIC rings without OS network stack", "Bypasses kernel socket overhead: reduces packet ingress latency from 5 µs to < 800 ns!"],
                    ["Busy Polling (Spinloop)", "Continuous polling on network ring buffer without `epoll()` sleep", "Zero interrupt latency; CPU runs at 100% pinned core utilization"],
                    ["Custom Arena / Pool Allocators", "Pre-allocate fixed block chunks at startup; bump pointer allocation", "Reduces allocation latency from 100 ns (`malloc`) to < 2 ns (pointer add)"],
                    ["Branch Hints", "`[[likely]]` / `[[unlikely]]` or `__builtin_expect`", "Guides compiler instruction layout for fall-through branch prediction"]
                ]
            ),
            depth="deep"
        )
    )

    # Section 6: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield C++ Systems Interview Flashcards",
        flashcard(
            "What happens if a virtual function is called inside a C++ constructor?",
            "During base class construction, the derived class members have NOT yet been constructed! The C++ runtime temporarily sets the object's `__vptr` to the **Base class VTable**. Calling a virtual function inside the constructor resolves to the **Base class implementation**, NOT the derived class override! Polymorphic dispatch is intentionally disabled during object construction to prevent accessing uninitialized derived member variables.",
            "P1 C++ Classic Weed-Out"
        )
        + flashcard(
            "Why is 'return std::move(x);' an anti-pattern when returning a local object by value?",
            "Returning a local object by value allows the compiler to perform **Named Return Value Optimization (NRVO)**, constructing the object directly in the caller's stack frame with **ZERO copies and ZERO moves**! If you write `return std::move(x);`, you explicitly cast `x` to an rvalue reference, which forces the compiler to disable NRVO and invoke the move constructor instead! Only use `std::move` when returning a function parameter or class member.",
            "P1 Modern C++ Trap"
        )
        + flashcard(
            "What is Object Slicing and how do you prevent it?",
            "Object Slicing occurs when an instance of a Derived class is assigned or passed by value to an object of Base class type (`Base b = derived;`). The compiler copies only the Base slice of the object, slicing away all derived member variables and resetting the `__vptr` to the Base vtable! Polymorphism is completely lost. Prevention: Always pass polymorphic objects by pointer or reference (`const Base&`).",
            "P1 OOP Internals"
        )
        + flashcard(
            "Why does High-Frequency Trading (HFT) strictly ban malloc/free on the hot path?",
            "1. **Non-Deterministic Latency**: `malloc()` acquires internal heap bucket mutex locks and may trigger the `mmap`/`brk` kernel system call if the arena is exhausted, causing unpredictable latency spikes of up to 10 microseconds.\n2. **Memory Fragmentation**: Dynamic allocations scatter memory across non-contiguous heap addresses, causing severe L1/L2 cache misses.\n3. **HFT Strategy**: Pre-allocate all data structures at startup in contiguous static buffers or fixed-size pool allocators.",
            "P1 HFT Architecture (Pace ₹41L)"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: OOP Internals, Move & Memory Orders", sprint_html)
        + section("vtable-memory-svg", "📊 VTable Layout, Smart Pointers & Control Blocks", vtable_html)
        + section("move-perfect-forwarding", "⚡ Move Semantics, Universal References & Forwarding", move_html)
        + section("lockfree-spsc-buffer", "🚀 Lock-Free SPSC Ring Buffer & Memory Models", lockfree_html)
        + section("hft-low-latency-toolkit", "⚡ Low-Latency & HFT Systems Toolkit (Pace ₹41L)", hft_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
