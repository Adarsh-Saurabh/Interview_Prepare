# mod_coa.py - Computer Organization & Architecture Module Generator
# Conforms to instruction.md Part 6.5 Specification (P1 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: CPU Equations, Amdahl & AMAT"),
        ("pipeline-hazards-svg", "📊 5-Stage RISC Pipeline & Forwarding"),
        ("cache-hierarchy-mesi", "🧠 Cache Coherence MESI & False Sharing"),
        ("ooo-tomasulo", "🚀 Out-of-Order Execution & Tomasulo's Algorithm"),
        ("worked-coa-math", "📐 Worked Numericals: Amdahl, AMAT & Cache Bits"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: 5-Stage RISC Pipeline & Forwarding
    svg_pipeline = """
    <svg viewBox="0 0 860 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="coa-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="fwd-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Stage 1: IF -->
      <rect x="30" y="70" width="120" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="90" y="105" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">1. IF</text>
      <text x="90" y="125" fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">Instruction Fetch</text>
      <text x="90" y="142" fill="#94a3b8" font-size="9" text-anchor="middle">PC → I-Cache</text>

      <line x1="150" y1="115" x2="190" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#coa-arrow)" />

      <!-- Stage 2: ID -->
      <rect x="195" y="70" width="120" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="255" y="105" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">2. ID</text>
      <text x="255" y="125" fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">Decode / Reg Read</text>
      <text x="255" y="142" fill="#94a3b8" font-size="9" text-anchor="middle">Register File</text>

      <line x1="315" y1="115" x2="355" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#coa-arrow)" />

      <!-- Stage 3: EX -->
      <rect x="360" y="70" width="120" height="90" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="420" y="105" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle">3. EX</text>
      <text x="420" y="125" fill="#ffffff" font-size="11" font-weight="600" text-anchor="middle">Execute / ALU</text>
      <text x="420" y="142" fill="#bae6fd" font-size="9" text-anchor="middle">Arithmetic Ops</text>

      <line x1="480" y1="115" x2="520" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#coa-arrow)" />

      <!-- Stage 4: MEM -->
      <rect x="525" y="70" width="120" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="585" y="105" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">4. MEM</text>
      <text x="585" y="125" fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">Memory Access</text>
      <text x="585" y="142" fill="#94a3b8" font-size="9" text-anchor="middle">Load / Store D-Cache</text>

      <line x1="645" y1="115" x2="685" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#coa-arrow)" />

      <!-- Stage 5: WB -->
      <rect x="690" y="70" width="120" height="90" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="750" y="105" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">5. WB</text>
      <text x="750" y="125" fill="#f1f5f9" font-size="11" font-weight="600" text-anchor="middle">Write Back</text>
      <text x="750" y="142" fill="#94a3b8" font-size="9" text-anchor="middle">Result → Reg File</text>

      <!-- Forwarding Path 1: EX/MEM to EX -->
      <path d="M 480 140 C 480 200, 380 200, 380 165" fill="none" stroke="#34d399" stroke-width="2.5" stroke-dasharray="4" marker-end="url(#fwd-arrow)" />
      <text x="430" y="215" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">ALU Forwarding (EX/MEM → EX)</text>

      <!-- Forwarding Path 2: MEM/WB to EX -->
      <path d="M 690 140 C 690 250, 360 250, 360 165" fill="none" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4" marker-end="url(#fwd-arrow)" />
      <text x="525" y="265" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Load Forwarding (MEM/WB → EX)</text>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P1 Track A", "amber"), ("Hardware Architecture", "indigo"), ("15-Min Sprint", "teal"), ("Performance Equations", "rose")])
        + callout(
            "Computer Architecture & Hardware Performance Essentials",
            "Hardware engineering interviews at Nvidia, Qualcomm, Apple, Arm, and Texas Instruments focus on quantitative performance modeling: applying the CPU Performance Equation, calculating multi-level AMAT, deriving Amdahl's Law speedups, understanding pipeline hazards, and mitigating multicore cache coherence bottlenecks (MESI & False Sharing).",
            "important"
        )
        + numbers_card("Memory Hierarchy Latency Ladder (Reference Cycles)", [
            ("CPU Registers", "0 cycles (~0.25 ns)", "Fastest physical flip-flops on execution core"),
            ("L1 Cache Access", "~4 - 5 cycles (~1 ns)", "Dedicated per-core 32KB/64KB SRAM"),
            ("L2 Cache Access", "~14 cycles (~3 - 4 ns)", "Dedicated per-core 512KB/1MB SRAM"),
            ("L3 Shared Cache", "~40 - 60 cycles (~12 - 15 ns)", "Shared LLC across all cores on die (16MB - 64MB)"),
            ("Main Memory (DRAM)", "~150 - 200 cycles (~50 - 80 ns)", "Off-chip DDR5 memory bus roundtrip"),
            ("NVMe SSD / PCIe", "~10,000 - 50,000 cycles (~5 - 15 µs)", "Flash storage read over PCIe bus")
        ])
        + subsection(
            "core-equations",
            "The Three Foundational Performance Equations",
            formula_box(
                r"\text{CPU Time} = \text{Instruction Count (IC)} \times \text{CPI} \times \text{Clock Period } (T_c) = \frac{\text{IC} \times \text{CPI}}{\text{Clock Frequency } (f)}",
                "CPU execution time is the product of instructions executed, average cycles per instruction, and clock period",
                [
                    (r"\text{IC}", "Total dynamic instruction count executed by the binary (determined by compiler & ISA)."),
                    (r"\text{CPI}", "Average Cycles Per Instruction (determined by CPU microarchitecture, pipeline stalls, and cache misses)."),
                    (r"T_c = 1/f", "Clock cycle time in seconds (determined by semiconductor fabrication and longest pipeline stage delay).")
                ],
                "A compiler optimization that decreases IC might increase CPI (e.g. replacing simple ALU ops with slow unrolled loops). Real performance requires minimizing the full product!"
            )
            + formula_box(
                r"\text{Speedup} = \frac{1}{(1 - p) + \frac{p}{s}} \quad \xrightarrow{s \to \infty} \quad \text{Max Theoretical Speedup} = \frac{1}{1 - p}",
                "Amdahl's Law states overall speedup is strictly bounded by the serial fraction of the execution workload",
                [
                    ("p", "Parallelizable fraction of the execution runtime (between 0.0 and 1.0)."),
                    ("s", "Speedup factor achieved on the parallelizable fraction (number of CPU cores)."),
                    (r"1 - p", "Inherently serial portion that cannot be parallelized.")
                ],
                "If a program is 90% parallel (p = 0.90), the maximum possible speedup on INFINITE processors is 1 / (1 - 0.9) = 10×! The serial 10% dominates total execution time."
            )
            + formula_box(
                r"\text{AMAT} = t_{\text{L1\_hit}} + m_{\text{L1}} \left( t_{\text{L2\_hit}} + m_{\text{L2}} \left( t_{\text{L3\_hit}} + m_{\text{L2}} \cdot t_{\text{DRAM\_penalty}} \right) \right)",
                "Average Memory Access Time across a multi-level cache hierarchy",
                [
                    (r"t_{\text{hit}}", "Latency in cycles to access the cache level upon a hit."),
                    (r"m", "Local miss rate at the corresponding cache level."),
                    (r"t_{\text{penalty}}", "Miss penalty latency to retrieve the line from the next level down.")
                ],
                "Because DRAM latency is ~200 cycles, even a tiny 1% miss rate at L3 dramatically degrades effective CPI!"
            ),
            depth="sprint"
        )
        + subsection(
            "pipeline-hazards-table",
            "Pipeline Hazards Matrix & Hardware Mitigations",
            table(
                ["Hazard Type", "Underlying Cause", "Hardware Solution", "Compiler / Software Mitigation"],
                [
                    ["Structural Hazard", "Resource conflict: two instructions need same hardware unit simultaneously", "Separate Harvard Architecture (I-Cache vs D-Cache); multi-port register files", "Compiler instruction scheduling / bubble insertion"],
                    ["Data Hazard: RAW (True Dependency)", "Instruction reads a register before previous instruction writes it", "Hardware Forwarding / Bypassing (EX/MEM → EX, MEM/WB → EX)", "Reorder instructions to fill load delay slot"],
                    ["Data Hazard: Load-Use Hazard", "Instruction depends on result of immediate preceding LOAD", "Forwarding cannot travel backwards in time! Hardware inserts **1-cycle stall bubble**", "Schedule independent instruction between load and dependent use"],
                    ["Data Hazard: WAR & WAW (Name Dependencies)", "Anti-dependency (WAR) or Output dependency (WAW) sharing register name", "Register Renaming via Reorder Buffer / Tomasulo Reservation Stations", "Compiler register allocation with distinct registers"],
                    ["Control Hazard (Branch)", "Branch outcome / target unknown during Fetch stage", "Branch Prediction (Dynamic 2-bit branch predictor, BTB); Speculative execution", "Branchless programming (conditional moves `cmov`, bit hacks)"]
                ]
            ),
            depth="sprint"
        )
    )

    # Section 2: Pipeline & Forwarding Architecture
    pipeline_html = (
        subsection(
            "pipeline-arch",
            "5-Stage Classic RISC Pipeline Architecture",
            svg_card("5-Stage RISC Pipeline Execution and Hardware Forwarding Paths", svg_pipeline)
            + callout(
                "Why Forwarding Cannot Eliminate the Load-Use Hazard Stall",
                "Consider:\n"
                "`LW R1, 0(R2)` (Load Word into R1)\n"
                "`ADD R3, R1, R4` (Add depends on R1)\n"
                "In the pipeline: When `LW` is in the EX stage, memory has NOT yet been read (data is only fetched in the **MEM** stage). But `ADD` enters the EX stage in the very next cycle and needs the value of `R1` at the beginning of EX! Forwarding cannot send data backwards in time from the end of MEM to the start of EX in the same cycle. The hardware hazard detection unit must stall the pipeline by inserting **1 bubble cycle**, freezing PC and IF/ID registers.",
                "tip"
            ),
            depth="deep"
        )
    )

    # Section 3: Cache Coherence & False Sharing
    cache_html = (
        subsection(
            "mesi-protocol",
            "MESI Cache Coherence Protocol State Machine",
            table(
                ["MESI State", "Is Line in Memory Valid?", "Is Line in Other Caches?", "Can Core Read?", "Can Core Write Directly?"],
                [
                    ["M (Modified)", "❌ Stale (Cache line is dirty / updated)", "❌ No (Exclusive to this cache)", "✅ Yes", "✅ Yes (Zero bus traffic required)"],
                    ["E (Exclusive)", "✅ Clean (Identical to DRAM)", "❌ No (Exclusive to this cache)", "✅ Yes", "✅ Yes (Transitions silently to Modified)"],
                    ["S (Shared)", "✅ Clean (Identical to DRAM)", "✅ Yes (May exist in other caches)", "✅ Yes", "❌ No (Must broadcast Read-For-Ownership / Invalidate bus request!)"],
                    ["I (Invalid)", "N/A (Contains no valid data)", "N/A", "❌ Must fetch from bus", "❌ Must fetch from bus"]
                ]
            )
            + callout(
                "False Sharing: The Silent Multicore Performance Killer",
                "**Definition**: False sharing occurs when two threads on different CPU cores modify completely independent variables that happen to reside on the **exact same 64-byte cache line**.\n"
                "• Core 0 writes `struct.a` → MESI invalidates the entire 64-byte cache line on Core 1!\n"
                "• Core 1 writes `struct.b` → MESI invalidates the entire 64-byte cache line on Core 0!\n"
                "• The cache line bounces ping-pong across the interconnect bus, degrading throughput by 10× to 50×!\n"
                "**Production Fix**: Align independent concurrent variables to distinct cache lines using C++17 `alignas(64)` or padding:\n"
                "`struct alignas(64) ThreadData { uint64_t counter; };`",
                "important"
            ),
            depth="deep"
        )
    )

    # Section 4: Out-of-Order Execution
    ooo_html = (
        subsection(
            "tomasulo-algorithm",
            "Out-of-Order Execution (OoO) & Tomasulo's Algorithm",
            table(
                ["Component", "Role in Tomasulo's Microarchitecture", "Eliminates Bottleneck"],
                [
                    ["Reservation Stations (RS)", "Buffers holding decoded instructions and their operands at functional units until operands become ready", "Decouples Instruction Decode from Execution; enables out-of-order dispatch"],
                    ["Common Data Bus (CDB)", "High-speed internal broadcast bus transmitting computed results directly to waiting RS and Reorder Buffer", "Bypasses register file write-read latency; forwards results instantly to all consumers"],
                    ["Register Renaming", "Maps logical architectural registers (R0-R31) to physical tags in reservation stations / ROB", "Completely eliminates WAR (anti) and WAW (output) name dependencies!"],
                    ["Reorder Buffer (ROB)", "Maintains in-order instruction retirement queue at the end of the pipeline", "Guarantees **Precise Exceptions** and safe speculative execution rollback on branch mispredictions"]
                ]
            ),
            depth="deep"
        )
    )

    # Section 5: Worked Numericals
    worked_html = (
        subsection(
            "worked-cache-bits",
            "Worked Numerical 1: Cache Address Bit Breakdown (Tag, Index, Offset)",
            worked_example(
                title="System: 32-bit Address, 32 KB 4-Way Set Associative Cache, 64-Byte Cache Lines",
                steps=[
                    ("Calculate Block Offset Bits (b)", "Line size = $64\\text{ bytes} = 2^6\\text{ bytes} \\implies b = 6\\text{ bits}$."),
                    ("Calculate Total Sets in Cache", r"$$\text{Total Lines} = \frac{\text{Cache Size}}{\text{Line Size}} = \frac{32 \times 1024}{64} = 512\text{ lines}$$" + "\n" + r"$$\text{Number of Sets (S)} = \frac{\text{Total Lines}}{\text{Associativity}} = \frac{512}{4} = 128\text{ sets}$$"),
                    ("Calculate Set Index Bits (s)", "$128\\text{ sets} = 2^7\\text{ sets} \\implies s = 7\\text{ bits}$."),
                    ("Calculate Tag Bits (t)", "$$\\text{Tag Bits} = \\text{Total Address Bits} - s - b = 32 - 7 - 6 = \\mathbf{19\\text{ bits}}$$")
                ],
                answer="32-bit physical address is parsed by hardware into: Tag (19 bits) | Set Index (7 bits) | Byte Offset (6 bits)."
            ),
            depth="deep"
        )
        + subsection(
            "worked-amat",
            "Worked Numerical 2: 3-Level AMAT Calculation with Real Hardware Latencies",
            worked_example(
                title="L1 Hit = 1 ns (miss rate 5%), L2 Hit = 4 ns (miss rate 20%), L3 Hit = 15 ns (miss rate 10%), DRAM = 80 ns",
                steps=[
                    ("Compute L3 Effective Miss Penalty", r"$$\text{Penalty}_{\text{L3}} = t_{\text{L3\_hit}} + m_{\text{L3}} \times t_{\text{DRAM}} = 15 + (0.10 \times 80) = 15 + 8 = 23\text{ ns}$$"),
                    ("Compute L2 Effective Miss Penalty", r"$$\text{Penalty}_{\text{L2}} = t_{\text{L2\_hit}} + m_{\text{L2}} \times \text{Penalty}_{\text{L3}} = 4 + (0.20 \times 23) = 4 + 4.6 = 8.6\text{ ns}$$"),
                    ("Compute Overall AMAT", r"$$\text{AMAT} = t_{\text{L1\_hit}} + m_{\text{L1}} \times \text{Penalty}_{\text{L2}} = 1 + (0.05 \times 8.6) = 1 + 0.43 = \mathbf{1.43\text{ ns}}$$")
                ],
                answer="Effective AMAT is 1.43 ns. The 3-level cache hierarchy reduces average memory access time from 80 ns down to 1.43 ns (a 56× acceleration!)."
            ),
            depth="deep"
        )
        + subsection(
            "worked-ieee754",
            "Worked Numerical 3: IEEE-754 Single-Precision Floating Point Representation",
            worked_example(
                title="Encode -13.625 into IEEE-754 32-Bit Single Precision Format",
                steps=[
                    ("Determine Sign Bit (S)", "Number is negative $\\implies S = 1$ (1 bit)."),
                    ("Convert Integer & Fraction to Binary", "$13_{10} = 1101_2$. $0.625_{10} = 0.5 + 0.125 = 2^{-1} + 2^{-3} = 0.101_2$. Total binary: $1101.101_2$."),
                    ("Normalize into Scientific Notation", "$$1101.101_2 = 1.101101_2 \\times 2^3$$ Mantissa fraction bits = $101101000...$ (23 bits)."),
                    ("Compute Biased Exponent (E)", "Exponent = 3. Bias for single-precision is 127. $\\text{Biased Exponent} = 3 + 127 = 130_{10} = 10000010_2$ (8 bits)."),
                    ("Assemble 32-bit Hex Code", "Bits: `1 10000010 10110100000000000000000` → In Hex: `0xC15A0000`.")
                ],
                answer="-13.625 in IEEE-754 single precision is represented as hex `0xC15A0000`."
            ),
            depth="deep"
        )
    )

    # Section 6: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield Computer Architecture Interview Flashcards",
        flashcard(
            "What are the 3 C's of Cache Misses (and the 4th Coherence Miss)?",
            "1. **Compulsory (Cold) Misses**: First-ever access to a memory block. Unavoidable unless hardware prefetching is used.\n2. **Capacity Misses**: Cache is simply too small to contain all working set blocks accessed by the program. Solved by increasing cache capacity.\n3. **Conflict Misses**: Multiple active blocks map to the exact same cache set in direct-mapped or set-associative caches. Solved by increasing associativity (e.g. 4-way to 8-way).\n4. **Coherence Misses**: In multicore systems, a cache line is invalidated because another core modified a shared variable on that line (MESI invalidation).",
            "P1 Architecture Classic"
        )
        + flashcard(
            "Why is row-major matrix traversal ~10x faster than column-major in C/C++?",
            "In C and C++, 2D arrays are stored in **Row-Major Order** in memory (all elements of row 0 consecutively, followed by row 1). When you read `A[i][j]`, a 64-byte cache line is loaded into L1 containing 8 consecutive 64-bit doubles (`A[i][0]` through `A[i][7]`). Sequential row iteration hits L1 cache for the next 7 elements (100% spatial locality). Column-major iteration (`A[j][i]`) jumps by $N \\times 8$ bytes on every iteration, causing a compulsory cache miss on every single access!",
            "P1 Performance Engineering"
        )
        + flashcard(
            "How does Little-Endian differ from Big-Endian, and how do you test it in C?",
            "In Little-Endian systems (x86, ARM default), the Least Significant Byte (LSB) is stored at the lowest memory address. In Big-Endian (network byte order), the Most Significant Byte (MSB) is stored at the lowest address.\nC detection code: `uint16_t x = 0x0001; return *(char*)&x == 1;` (returns true for Little-Endian).",
            "P1 Hardware / Embedded"
        )
        + flashcard(
            "How does a 2-bit Saturating Counter Branch Predictor outperform a 1-bit predictor on loops?",
            "In a loop of 10 iterations, a 1-bit predictor mispredicts TWICE: once when exiting the loop (switches from Taken to Not Taken), and once when re-entering the loop in the next invocation (predicts Not Taken, but loop repeats). A 2-bit saturating counter has 4 states (Strongly Taken, Weakly Taken, Weakly Not Taken, Strongly Not Taken). A single exit condition only transitions Strongly Taken down to Weakly Taken! When the loop runs again, it still predicts Taken. A 2-bit predictor mispredicts only ONCE per loop.",
            "P1 Microarchitecture"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: CPU Equations, Amdahl & AMAT", sprint_html)
        + section("pipeline-hazards-svg", "📊 5-Stage RISC Pipeline & Forwarding", pipeline_html)
        + section("cache-hierarchy-mesi", "🧠 Cache Coherence MESI & False Sharing", cache_html)
        + section("ooo-tomasulo", "🚀 Out-of-Order Execution & Tomasulo's Algorithm", ooo_html)
        + section("worked-coa-math", "📐 Worked Numericals: Amdahl, AMAT & Cache Bits", worked_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
