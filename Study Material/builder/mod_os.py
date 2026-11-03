# mod_os.py - Operating Systems & Concurrency Module Generator
# Conforms to instruction.md Part 6.2 Specification (P0 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Process, Sync & Scheduling"),
        ("visual-memory-tlb", "📊 Memory Architecture: Layout & TLB Lookup"),
        ("sync-problems-bankers", "🔒 Synchronization, Peterson & Banker's Algorithm"),
        ("worked-numericals", "📐 Worked Numericals: Gantt Charts & Page Replacement"),
        ("memory-storage-internals", "🧠 Multi-Level Page Tables, CFS & File Systems"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: Process Memory Layout
    svg_memory = """
    <svg viewBox="0 0 800 460" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-down" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="arrow-up" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>
      <rect x="200" y="20" width="400" height="420" rx="10" fill="#0f172a" stroke="#334155" stroke-width="2" />
      <text x="120" y="45" fill="#f43f5e" font-size="11" font-family="monospace">0xFFFFFFFF (High)</text>
      <line x1="190" y1="40" x2="200" y2="40" stroke="#f43f5e" stroke-width="1.5" />

      <!-- Kernel Space -->
      <rect x="210" y="30" width="380" height="50" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
      <text x="400" y="55" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="middle">Kernel Space (1GB on 32-bit / Upper Canonical on 64-bit)</text>
      <text x="400" y="70" fill="#94a3b8" font-size="10" text-anchor="middle">Protected from User Ring 3 (Page Fault SIGSEGV on illegal access)</text>

      <!-- Stack -->
      <rect x="210" y="90" width="380" height="65" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="400" y="115" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">STACK (Local Variables, Function Call Frames, Return Addrs)</text>
      <text x="400" y="132" fill="#bae6fd" font-size="10" text-anchor="middle">Grows Downward ↓ (High → Low Memory)</text>

      <line x1="400" y1="160" x2="400" y2="190" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-down)" />

      <!-- Free / Dynamic Space -->
      <rect x="210" y="195" width="380" height="60" rx="4" fill="#090d16" stroke="#1e293b" stroke-dasharray="4" />
      <text x="400" y="230" fill="#64748b" font-size="11" font-weight="600" text-anchor="middle">↑ ↓ Dynamic Growth Zone (mmap libraries, shared memory, guard pages)</text>

      <line x1="400" y1="290" x2="400" y2="260" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-up)" />

      <!-- Heap -->
      <rect x="210" y="295" width="380" height="50" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="400" y="318" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">HEAP (malloc, new, dynamic memory)</text>
      <text x="400" y="335" fill="#a7f3d0" font-size="10" text-anchor="middle">Grows Upward ↑ (via brk / sbrk system calls)</text>

      <!-- BSS Segment -->
      <rect x="210" y="350" width="380" height="30" rx="4" fill="#1e293b" stroke="#fbbf24" stroke-width="1" />
      <text x="400" y="370" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">BSS Segment (Uninitialized / Zero-initialized Globals &amp; Statics)</text>

      <!-- Data Segment -->
      <rect x="210" y="385" width="380" height="25" rx="4" fill="#1e293b" stroke="#c084fc" stroke-width="1" />
      <text x="400" y="402" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">Data Segment (Initialized Globals &amp; Statics, e.g. int x = 42)</text>

      <!-- Text Segment -->
      <rect x="210" y="415" width="380" height="20" rx="4" fill="#334155" />
      <text x="400" y="429" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">Text / Code Segment (Read-Only Machine Binary Instructions)</text>

      <text x="120" y="430" fill="#34d399" font-size="11" font-family="monospace">0x00000000 (Low)</text>
      <line x1="190" y1="425" x2="200" y2="425" stroke="#34d399" stroke-width="1.5" />
    </svg>
    """

    # SVG 2: Paging & TLB Lookup
    svg_tlb = """
    <svg viewBox="0 0 840 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="tlb-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="tlb-red" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
        </marker>
        <marker id="tlb-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>
      <!-- Virtual Address -->
      <rect x="20" y="80" width="160" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="100" y="105" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Virtual Address</text>
      <text x="60" y="125" fill="#38bdf8" font-size="10" font-family="monospace">VPN (p)</text>
      <text x="140" y="125" fill="#94a3b8" font-size="10" font-family="monospace">Offset (d)</text>
      <line x1="100" y1="112" x2="100" y2="135" stroke="#334155" />

      <!-- TLB Unit -->
      <rect x="230" y="60" width="140" height="100" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="300" y="95" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">TLB (MMU Cache)</text>
      <text x="300" y="115" fill="#e0f2fe" font-size="10" text-anchor="middle">Latency: ~0.5 - 1 ns</text>
      <text x="300" y="135" fill="#bae6fd" font-size="9" text-anchor="middle">Fully associative HW lookup</text>

      <line x1="180" y1="110" x2="225" y2="110" stroke="#38bdf8" stroke-width="2" marker-end="url(#tlb-arrow)" />

      <!-- Hit Path -->
      <line x1="370" y1="90" x2="650" y2="90" stroke="#34d399" stroke-width="2.5" marker-end="url(#tlb-green)" />
      <rect x="440" y="70" width="120" height="20" rx="4" fill="#065f46" />
      <text x="500" y="84" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">TLB HIT (~99%)</text>

      <!-- Miss Path -->
      <line x1="300" y1="160" x2="300" y2="210" stroke="#f43f5e" stroke-width="2" marker-end="url(#tlb-red)" />
      <rect x="245" y="175" width="110" height="20" rx="4" fill="#881337" />
      <text x="300" y="189" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">TLB MISS (~1%)</text>

      <!-- Page Table in RAM -->
      <rect x="230" y="215" width="170" height="55" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="315" y="238" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Page Table in RAM</text>
      <text x="315" y="255" fill="#94a3b8" font-size="9" text-anchor="middle">CR3 Register / Latency ~50ns</text>

      <line x1="400" y1="240" x2="670" y2="160" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3" marker-end="url(#tlb-arrow)" />

      <!-- Physical Address -->
      <rect x="660" y="80" width="160" height="75" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="740" y="105" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">Physical Address</text>
      <text x="700" y="130" fill="#34d399" font-size="11" font-family="monospace">PFN (f)</text>
      <text x="780" y="130" fill="#94a3b8" font-size="11" font-family="monospace">Offset (d)</text>
      <line x1="740" y1="115" x2="740" y2="145" stroke="#047857" />
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P0 Track A", "rose"), ("Core Systems", "indigo"), ("15-Min Sprint", "amber"), ("NIT Rourkela Core", "emerald")])
        + callout(
            "Operating Systems Interview Ground Rules",
            "Top tech interviewers at Google, Microsoft, Apple, Qualcomm, and Media.net ruthlessly test two facets of Operating Systems: (1) low-level concurrency & synchronization mechanisms (mutexes, semaphores, Peterson's, deadlocks), and (2) quantitative system calculations (CPU scheduling Gantt charts, Page replacement traces, Effective Access Time, and page table sizing).",
            "important"
        )
        + numbers_card("Operating System Latency Orders of Magnitude", [
            ("L1 Cache Access", "~0.5 - 1 ns", "Fastest hardware cache on chip"),
            ("TLB Lookup", "~0.5 - 1.5 ns", "Hardware MMU address translation hit"),
            ("DRAM Main Memory Access", "~50 - 100 ns", "Cache miss penalty requiring bus cycle"),
            ("Thread Context Switch (Same Process)", "~100 - 300 ns", "Save registers, switch SP/PC, keep same MMU CR3"),
            ("Process Context Switch (Cross-Process)", "~1 - 2 µs", "Full MMU CR3 change, flush TLB, cache pollution"),
            ("Hard Page Fault (Disk I/O)", "~5 - 10 ms", "100,000× slower than DRAM! Blocks process completely")
        ])
        + subsection(
            "process-vs-thread",
            "Process vs Thread: The Deep Comparison",
            table(
                ["Dimension", "Process", "Thread (Lightweight Process)", "Interview Defense / Trap"],
                [
                    ["Address Space", "Isolated virtual address space per process (private page tables)", "Shares parent process address space (Code, Data, Heap, FDs)", "Corruption in one thread can crash entire process"],
                    ["Resource Allocation", "Heavy: allocated by kernel via `fork()`/`exec()`. Separate PID, memory maps", "Lightweight: created via `pthread_create()` or `clone()`. Shares resources", "Threads have private Stack, Registers, Program Counter"],
                    ["Context Switch Overhead", "~1,000 - 2,000 ns (1-2 µs). Must flush/invalidate TLB (CR3 switch)", "~100 - 300 ns. Same page table; TLB remains warm!", "L1/L2 cache pollution is the hidden cost of process switches"],
                    ["Inter-Communication", "IPC required (Pipes, Sockets, Shared Memory, Message Queues)", "Direct memory read/write via shared Heap (needs synchronization)", "Shared memory is fastest IPC; threads need mutexes to prevent data races"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "classic-sync-problems",
            "Classic Synchronization Problems & Semaphore Allocations",
            table(
                ["Problem", "Shared Resources & Buffers", "Required Semaphores / Mutexes", "Key Invariants & Deadlock Pitfall"],
                [
                    ["Producer-Consumer (Bounded Buffer)", "Queue of size N", "`mutex = 1`, `empty = N`, `full = 0`", "Producer waits on `empty`, then locks `mutex`. Inverting wait order causes deadlock!"],
                    ["Readers-Writers (Reader-Preference)", "Shared file or database", "`rw_mutex = 1`, `mutex = 1`, `read_count = 0`", "First reader locks `rw_mutex`; last reader releases it. Trap: can starve writers indefinitely!"],
                    ["Readers-Writers (Writer-Preference)", "Shared file, read & write queues", "`rw_mutex = 1`, `r_mutex = 1`, `w_mutex = 1`, `read_try = 1`", "Writers queue up and block incoming readers once pending, preventing writer starvation."],
                    ["Dining Philosophers", "5 philosophers, 5 forks (shared array)", "5 semaphores `fork[5] = {1}`", "Deadlock occurs if all pick left fork simultaneously. Fix: resource ordering or asymmetric pickup."],
                    ["Sleeping Barber", "1 barber, N waiting chairs", "`customers = 0`, `barbers = 0`, `mutex = 1`", "Barber sleeps on `customers`; arriving customer checks waiting chairs count under `mutex`."]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "scheduling-matrix",
            "CPU Scheduling Algorithms Comparison",
            table(
                ["Algorithm", "Preemptive?", "Criteria / Formula", "Advantages", "Disadvantages / Traps"],
                [
                    ["FCFS", "No", "Arrival Time", "Simplest implementation; no starvation", "Convoy Effect: short jobs stuck behind long CPU burst"],
                    ["SJF (Shortest Job First)", "No", "Burst Time (predicted via exponential smoothing)", "Minimizes average waiting time theoretically", "Starvation of long jobs; impossible to know exact future burst length"],
                    ["SRTF (Shortest Remaining Time First)", "Yes", "Remaining Burst Time", "Optimal average turnaround time for preemptive systems", "High context-switch overhead; severe starvation for long processes"],
                    ["Round Robin (RR)", "Yes", "Time Quantum (q)", "Fair CPU allocation, responsive for interactive users", "If q is too small → thrashing context switches; if q too large → degrades to FCFS"],
                    ["Priority Scheduling", "Both", "Static or Dynamic Priority", "Important real-time tasks get CPU instantly", "Starvation of low-priority jobs. Fix: Aging (gradually increase priority)"]
                ]
            ),
            depth="sprint"
        )
    )

    # Section 2: Visual Memory Architecture
    visual_html = (
        subsection(
            "process-memory-svg",
            "Process Virtual Memory Layout (32-bit vs 64-bit)",
            svg_card("Process Address Space Segments (High to Low Memory)", svg_memory)
            + callout(
                "Why the Stack and Heap Grow Toward Each Other",
                "Stack grows downwards (from high address to low) because function frames are temporary and bounded by stack limits (default 8MB on Linux). Heap grows upwards (via `brk()` / `sbrk()` and `mmap()`). Placing them at opposite ends of the user space maximizes the contiguous unallocated dynamic growth zone without requiring rigid compile-time size partitions.",
                "tip"
            ),
            depth="deep"
        )
        + subsection(
            "tlb-paging-svg",
            "Paging & Hardware TLB Translation Flow",
            svg_card("MMU Hardware TLB Translation and Page Table Walk", svg_tlb)
            + formula_box(
                r"\text{EAT} = (1 - p) \cdot t_{\text{mem}} + p \cdot t_{\text{fault}}",
                "Effective Access Time equals probability of no fault times memory access plus fault rate times page fault penalty",
                [
                    ("p", "Page fault rate (probability between 0.0 and 1.0)."),
                    ("t_{mem}", "Normal physical memory access latency (~100 ns)."),
                    ("t_{fault}", "Full page fault service time including disk I/O seek, rotational latency, and OS context switch (~8 ms = 8,000,000 ns).")
                ],
                "Even a tiny page fault rate of p = 0.001 (0.1%) increases Effective Access Time by 80×! Memory thrashing degrades CPU utilization to near zero."
            ),
            depth="deep"
        )
    )

    # Section 3: Synchronization & Banker's Algorithm
    sync_html = (
        subsection(
            "petersons-algo",
            "Peterson's Algorithm: 3 Requirements of Critical Section",
            callout(
                "The 3 Non-Negotiable Critical Section Requirements",
                "1. **Mutual Exclusion**: If process Pi is executing in its critical section, no other process can be in its critical section.\n"
                "2. **Progress**: If no process is in its critical section and some wish to enter, only those not in their remainder section can participate in deciding who enters next, and this selection cannot be postponed indefinitely.\n"
                "3. **Bounded Waiting**: There must be a bound on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted (prevents starvation).",
                "important"
            )
            + code(r"""// Peterson's Algorithm for 2 processes P0 and P1
volatile bool flag[2] = {false, false};
volatile int turn = 0;

void process(int i) {
    int j = 1 - i; // Other process
    
    // Entry Section
    flag[i] = true;          // Declare intent to enter
    turn = j;                // Generously yield turn to other process
    
    // Busy wait while other process wants to enter and it's their turn
    while (flag[j] && turn == j) {
        // Wait (Spinlock)
    }
    
    // --- CRITICAL SECTION ---
    // Safe access to shared resources
    
    // Exit Section
    flag[i] = false;         // Release intent
    
    // Remainder Section
}""", "c", "petersons_algorithm.c")
            + callout(
                "Modern Hardware Warning: Why Peterson's Fails on x86/ARM Without Memory Barriers",
                "Modern CPUs feature Out-of-Order Execution and Store Buffers. Without memory fences, the CPU or compiler can reorder `flag[i] = true;` and `turn = j;`, or delay making the write visible to the other core. Both processes can read `flag = false` simultaneously and enter the critical section together! In modern C++, `std::atomic` with `std::memory_order_seq_cst` is mandatory.",
                "tip"
            ),
            depth="deep"
        )
        + subsection(
            "coffman-deadlock",
            "The 4 Coffman Conditions & Deadlock Strategies",
            table(
                ["Coffman Condition", "What It Means", "How to Prevent It (Break Condition)"],
                [
                    ["1. Mutual Exclusion", "Resources cannot be shared simultaneously", "Make resources shareable (e.g. read-only files). Usually impossible for printers/writers."],
                    ["2. Hold and Wait", "Process holds resources while requesting more", "Require process to request ALL resources upfront, or release held resources before requesting."],
                    ["3. No Preemption", "Resources cannot be forcibly taken from a process", "If request cannot be granted immediately, OS preempts all currently held resources."],
                    ["4. Circular Wait", "P0 waits for P1, P1 waits for P2... Pn waits for P0", "Impose a global total ordering on all resources (e.g., $F: R \\to \\mathbb{N}$). A process can only request resource $R_j$ if $F(R_j) > F(R_i)$."]
                ]
            )
            + decision_matrix(
                "Deadlock Handling Strategies",
                [
                    ("Deadlock Prevention", "Enforce strict compile/runtime protocols that break at least one of the 4 Coffman conditions.", "Low resource utilization and possible starvation."),
                    ("Deadlock Avoidance (Banker's)", "OS dynamically inspects resource allocation state before granting requests to ensure system stays in a Safe State.", "Requires processes to declare their MAXIMUM resource claim in advance, which is rarely known in general OS applications."),
                    ("Deadlock Detection & Recovery", "Allow deadlocks to occur; periodically run cycle detection on Resource Allocation Graph (Wait-For Graph) and abort processes.", "High recovery overhead; aborting processes can corrupt external state or waste CPU hours."),
                    ("Ostrich Algorithm (Ignore)", "Stick head in sand and pretend deadlock never happens (used by Linux, Windows, macOS).", "When deadlocks are exceedingly rare and cost of prevention exceeds reboot cost.")
                ]
            ),
            depth="deep"
        )
    )

    # Section 4: Worked Numericals
    worked_html = (
        subsection(
            "worked-gantt",
            "Worked Numerical 1: CPU Scheduling Gantt Charts Compared",
            worked_example(
                title="Scheduling Comparison on Identical Process Set: P1(0, 8), P2(1, 4), P3(2, 9), P4(3, 5)",
                steps=[
                    ("FCFS Execution", "Order: P1(0-8) → P2(8-12) → P3(12-21) → P4(21-26). Turnaround Times: P1=8, P2=11, P3=19, P4=23. Avg Turnaround = 15.25 ms. Waiting Times: P1=0, P2=7, P3=10, P4=18. Avg Waiting Time = 8.75 ms."),
                    ("SJF (Non-Preemptive)", "At t=0, only P1 arrives → executes P1(0-8). At t=8, P2, P3, P4 are ready. Shortest burst is P2(4) → executes P2(8-12). Next shortest is P4(5) → P4(12-17). Finally P3(9) → P3(17-26). Avg Waiting Time = (0 + 7 + 15 + 9)/4 = 7.75 ms."),
                    ("SRTF (Preemptive SJF)", "At t=0: P1 runs. At t=1: P2 arrives (burst 4 < remaining P1 7) → preempts P1! P2 runs (1-5). At t=5: remaining bursts are P4(5), P1(7), P3(9). P4 runs (5-10). P1 runs (10-17). P3 runs (17-26). Avg Waiting Time = (9 + 0 + 15 + 2)/4 = 6.5 ms (Optimal!)."),
                    ("Round Robin (q = 4 ms)", "Gantt timeline: P1(0-4) → P2(4-8, finishes!) → P3(8-12) → P4(12-16) → P1(16-20, finishes!) → P3(20-24) → P4(24-25, finishes!) → P3(25-26, finishes!). Avg Waiting Time = (12 + 3 + 15 + 17)/4 = 11.75 ms.")
                ],
                answer="SRTF achieves the minimal average waiting time (6.5 ms), while Round Robin provides the highest interactive responsiveness with fair time slicing."
            ),
            depth="deep"
        )
        + subsection(
            "worked-page-replacement",
            "Worked Numerical 2: Page Replacement Traces & Belady's Anomaly",
            worked_example(
                title="Page Reference String: [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] across 3 vs 4 Frames",
                steps=[
                    ("FIFO with 3 Frames", "Initial faults on 1, 2, 3 (3 frames filled). Fault on 4 replaces 1. Fault on 1 replaces 2. Fault on 2 replaces 3. Fault on 5 replaces 4. Hits on 1, 2. Fault on 3 replaces 1. Fault on 4 replaces 2. Fault on 5 replaces 5. Total Page Faults = 9 faults."),
                    ("FIFO with 4 Frames (Belady's Anomaly!)", "Frame capacity increased from 3 to 4. Tracing FIFO on the exact same string yields: Faults on 1, 2, 3, 4. Hits on 1, 2. Fault on 5 replaces 1. Fault on 1 replaces 2. Fault on 2 replaces 3. Fault on 3 replaces 4. Fault on 4 replaces 5. Fault on 5 replaces 1. Total Page Faults = 10 faults! (More memory caused MORE page faults!)."),
                    ("LRU with 3 Frames", "Evicts page not used for the longest period. Stack-based algorithm. Total Faults = 10 faults. Proven immune to Belady's Anomaly because it is a Stack Algorithm ($M(k) \\subseteq M(k+1)$)."),
                    ("Optimal (Bélády's Algorithm)", "Evicts page whose next reference is furthest in the future (theoretical lower bound). Total Page Faults = 7 faults.")
                ],
                answer="Belady's anomaly occurs under FIFO because FIFO is not a stack algorithm; increasing memory frames from 3 to 4 paradoxically increases page faults from 9 to 10."
            ),
            depth="deep"
        )
        + subsection(
            "worked-bankers",
            "Worked Numerical 3: Banker's Algorithm Safety Sequence Check",
            worked_example(
                title="5 Processes (P0-P4) with 3 Resource Types A(10), B(5), C(7)",
                steps=[
                    ("Allocation & Max State", "Allocation sum: A=7, B=2, C=5. Available vector = [10-7, 5-2, 7-5] = [3, 3, 2]. Need matrix = Max - Allocation: P0: [7,4,3], P1: [1,2,2], P2: [6,0,0], P3: [0,1,1], P4: [4,3,1]."),
                    ("Step 1: Check P1", "Need P1 [1,2,2] <= Available [3,3,2] → TRUE! P1 executes, releases resources. New Available = [3,3,2] + [2,0,0] = [5,3,2]."),
                    ("Step 2: Check P3", "Need P3 [0,1,1] <= Available [5,3,2] → TRUE! P3 executes. New Available = [5,3,2] + [2,1,1] = [7,4,3]."),
                    ("Step 3: Check P4, P0, P2", "Need P4 [4,3,1] <= [7,4,3] → TRUE! Available becomes [7,4,5]. Need P0 [7,4,3] <= [7,4,5] → TRUE! Available becomes [7,5,5]. Need P2 [6,0,0] <= [7,5,5] → TRUE! P2 finishes.")
                ],
                answer="System is in a SAFE STATE with safe execution sequence: <P1, P3, P4, P0, P2>. Deadlock is completely avoidable."
            ),
            depth="deep"
        )
    )

    # Section 5: Memory & Storage Internals
    internals_html = (
        subsection(
            "paging-math",
            "Virtual Memory & Multi-Level Page Table Size Arithmetic",
            callout(
                "Standard Interview Weeder Problem: 48-bit Virtual Address Space Size",
                "Question: 'In a 64-bit architecture with 48-bit virtual address space, 4KB page size, and 8-byte Page Table Entries (PTE), how much memory does a single-level page table require per process?'\n"
                "• Page Size = $4\\text{KB} = 2^{12}\\text{ bytes}$, so Offset = 12 bits.\n"
                "• Virtual Page Number (VPN) = $48 - 12 = 36\\text{ bits}$.\n"
                "• Number of Pages = $2^{36} \\approx 68.7\\text{ billion pages}$.\n"
                "• Size of Single-Level Page Table = $2^{36} \\times 8\\text{ bytes} = 2^{39}\\text{ bytes} = \\mathbf{512\\text{ GB}}$ per process!\n"
                "Conclusion: A single-level page table is completely impossible. Modern x86-64 uses a 4-Level Page Table (PML4 → PDPT → PD → PT) where levels are allocated dynamically on-demand, consuming only a few megabytes for typical processes.",
                "important"
            ),
            depth="deep"
        )
        + subsection(
            "file-systems-inodes",
            "File System Architecture: Inodes, Links & Disk Scheduling",
            table(
                ["File System Concept", "Internal Mechanism", "Engineering Implication / Trap"],
                [
                    ["Inode Structure", "Metadata record containing mode, owner, size, timestamps, and 12 direct block pointers, 1 single-indirect, 1 double-indirect, 1 triple-indirect.", "Filenames are NOT stored in the inode! Filenames are stored in directory data blocks mapping names to inode numbers."],
                    ["Hard Link", "Additional directory entry pointing directly to the exact same inode number. Increments inode `link_count`.", "Cannot span across different file systems/partitions. If original file is deleted, data remains accessible until `link_count == 0`."],
                    ["Symbolic (Soft) Link", "Independent file with its own unique inode, whose data block contains the pathname string of the target file.", "Can cross filesystem boundaries. If target file is deleted, symlink becomes a 'dangling / broken pointer'."],
                    ["Disk Scheduling (SCAN / Elevator)", "Disk arm moves in one direction servicing requests until it hits the end, then reverses direction.", "Prevents starvation; balances seek latency. C-SCAN only services in one direction, then immediately jumps back to start."]
                ]
            ),
            depth="deep"
        )
        + subsection(
            "linux-cfs",
            "Linux Completely Fair Scheduler (CFS) Internals",
            table(
                ["CFS Architecture Dimension", "Implementation Detail", "Why It Replaced the O(1) Scheduler"],
                [
                    ["Core Metric", "`vruntime` (Virtual Runtime)", "Tracks the normalized CPU time spent by a task: $vruntime += \\Delta exec\\_time \\times \\frac{NICE\\_0\\_LOAD}{weight}$."],
                    ["Data Structure", "Self-Balancing Red-Black Tree (`rb_node`)", "Tasks ordered by `vruntime`. The leftmost node `rb_leftmost` has the lowest `vruntime` and is picked next in $O(1)$ time."],
                    ["Fairness Principle", "Proportional CPU share based on task `nice` value", "A high-priority task (lower nice value) accumulates `vruntime` slower, receiving more physical CPU execution time."],
                    ["Handling Sleep / I/O", "`vruntime = \\max(vruntime, min\\_vruntime)`", "Prevents I/O-bound tasks that slept for a long time from monopolizing the CPU when they wake up!"]
                ]
            ),
            depth="deep"
        )
    )

    # Section 6: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield Operating Systems Interview Flashcards",
        flashcard(
            "Why is a system call (~100x) more expensive than a regular function call?",
            "A standard function call executes a `call` instruction, pushing the return address onto the stack and jumping within the same address space (takes ~1-2 ns). A system call requires an explicit CPU ring transition from User Mode (Ring 3) to Kernel Mode (Ring 0) via the `syscall` instruction. The CPU hardware switches to the kernel stack, saves user registers, verifies security boundaries, loads the kernel interrupt descriptor table (IDT), executes the privileged handler, and transitions back via `sysret`. This costs ~100-200 ns.",
            "P0 Core Systems"
        )
        + flashcard(
            "What causes Thrashing in virtual memory, and how does the OS detect and resolve it?",
            "Thrashing occurs when the sum of working set sizes of all active processes exceeds available physical RAM. The OS spends more time servicing page faults and swapping pages in/out of disk than executing actual CPU instructions, causing CPU utilization to plummet to near 0%. The OS detects this via Page Fault Frequency (PFF). Resolution: Suspend or terminate some processes (reduce degree of multiprogramming) to allow the remaining processes to fit their working sets into RAM.",
            "P0 Virtual Memory"
        )
        + flashcard(
            "What is the difference between a Zombie Process and an Orphan Process?",
            "A Zombie Process is a process that has completed execution via `exit()`, but its entry remains in the Process Table because its parent has not yet called `wait()` or `waitpid()` to read its exit status code. Consumes process IDs (PIDs). An Orphan Process is a process whose parent terminated while the child was still running. It is automatically adopted by `init` / `systemd` (PID 1), which periodically reaps its exit status when it finishes.",
            "P0 Process Management"
        )
        + flashcard(
            "Explain Priority Inversion and the Priority Inheritance solution (Mars Pathfinder bug).",
            "Priority Inversion occurs when a low-priority task (L) holds a shared mutex needed by a high-priority task (H), but a medium-priority task (M) preempts L (because M has higher priority than L). H is now indirectly starved by M! In the 1997 Mars Pathfinder mission, this caused system watchdog resets. Solution: Priority Inheritance Protocol — when high-priority task H blocks on a lock held by low-priority task L, L temporarily inherits the priority of H until it releases the lock.",
            "P0 Concurrency & Real-Time"
        )
        + flashcard(
            "Why can a spinlock cause deadlock on a uniprocessor system if interrupts are enabled?",
            "On a single CPU core, if a process running in user mode acquires a spinlock, and an interrupt handler triggers on the same CPU that attempts to acquire the exact same spinlock, the interrupt handler will busy-wait (spin) forever waiting for the lock to be released. But the lock holder can never run to release the lock because the interrupt handler has preempted it on the only CPU! Solution: Spinlocks in kernel space must always disable local interrupts before acquiring the lock.",
            "P0 Systems Internals"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: Process, Sync & Scheduling", sprint_html)
        + section("visual-memory-tlb", "📊 Memory Architecture: Layout & TLB Lookup", visual_html)
        + section("sync-problems-bankers", "🔒 Synchronization, Peterson & Banker's Algorithm", sync_html)
        + section("worked-numericals", "📐 Worked Numericals: Gantt Charts & Page Replacement", worked_html)
        + section("memory-storage-internals", "🧠 Multi-Level Page Tables, CFS & File Systems", internals_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
