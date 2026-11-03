# mod_dbms.py - DBMS, Storage Internals & Transactions Module Generator
# Conforms to instruction.md Part 6.3 Specification (P0 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: ACID, Isolation & Indexes"),
        ("bplus-lsm-storage", "🌲 Storage Engines: B+ Trees vs LSM Trees"),
        ("wal-aries-recovery", "💾 WAL & ARIES Recovery Protocol (Durability)"),
        ("concurrency-mvcc", "🔒 Concurrency Control, 2PL & Conflict Serializability"),
        ("worked-dbms-math", "📐 Worked Derivations: Precedence Graphs & Normalization"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: B+ Tree Architecture
    svg_bplus = """
    <svg viewBox="0 0 860 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="b-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="leaf-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>
      <!-- Root -->
      <rect x="340" y="20" width="180" height="40" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="430" y="45" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Root: [ Key: 50 ]</text>

      <line x1="380" y1="60" x2="200" y2="100" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#b-arrow)" />
      <line x1="480" y1="60" x2="660" y2="100" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#b-arrow)" />

      <!-- Internal Nodes -->
      <rect x="110" y="100" width="200" height="40" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="210" y="125" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Internal: [ 20 | 35 ]</text>

      <rect x="550" y="100" width="200" height="40" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="650" y="125" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle">Internal: [ 65 | 80 ]</text>

      <!-- Branches to Leaves -->
      <line x1="150" y1="140" x2="70" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />
      <line x1="210" y1="140" x2="210" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />
      <line x1="270" y1="140" x2="350" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />

      <line x1="590" y1="140" x2="490" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />
      <line x1="650" y1="140" x2="630" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />
      <line x1="710" y1="140" x2="770" y2="180" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#b-arrow)" />

      <!-- Leaves -->
      <rect x="20" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="77" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 10, 15 ]</text>
      <text x="77" y="218" fill="#a7f3d0" font-size="8" text-anchor="middle">Record Pointers →</text>

      <rect x="160" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="217" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 20, 28 ]</text>

      <rect x="300" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="357" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 35, 45 ]</text>

      <rect x="440" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="497" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 50, 60 ]</text>

      <rect x="580" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="637" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 65, 75 ]</text>

      <rect x="720" y="180" width="115" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="777" y="205" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">[ 80, 95 ]</text>

      <!-- Linked Leaves -->
      <line x1="135" y1="202" x2="155" y2="202" stroke="#34d399" stroke-width="2" marker-end="url(#leaf-arrow)" />
      <line x1="275" y1="202" x2="295" y2="202" stroke="#34d399" stroke-width="2" marker-end="url(#leaf-arrow)" />
      <line x1="415" y1="202" x2="435" y2="202" stroke="#34d399" stroke-width="2" marker-end="url(#leaf-arrow)" />
      <line x1="555" y1="202" x2="575" y2="202" stroke="#34d399" stroke-width="2" marker-end="url(#leaf-arrow)" />
      <line x1="695" y1="202" x2="715" y2="202" stroke="#34d399" stroke-width="2" marker-end="url(#leaf-arrow)" />

      <text x="430" y="255" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">↔ Doubly Linked Leaves enable O(log N + K) range scans without tree re-traversals</text>
    </svg>
    """

    # SVG 2: WAL & ARIES Recovery Protocol
    svg_wal = """
    <svg viewBox="0 0 880 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="860" height="240" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
      <!-- Timeline axis -->
      <line x1="50" y1="120" x2="820" y2="120" stroke="#64748b" stroke-width="2" />
      <text x="820" y="145" fill="#94a3b8" font-size="11" text-anchor="end">Log Sequence Number (LSN) Timeline →</text>

      <!-- Checkpoint -->
      <line x1="160" y1="40" x2="160" y2="200" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4" />
      <rect x="100" y="25" width="120" height="25" rx="4" fill="#0369a1" />
      <text x="160" y="42" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">Fuzzy Checkpoint</text>
      <text x="160" y="220" fill="#38bdf8" font-size="10" text-anchor="middle">Flushes Dirty Page Table</text>

      <!-- Crash Event -->
      <line x1="600" y1="40" x2="600" y2="200" stroke="#f43f5e" stroke-width="2.5" />
      <rect x="540" y="25" width="120" height="25" rx="4" fill="#881337" />
      <text x="600" y="42" fill="#ffffff" font-size="10" font-weight="800" text-anchor="middle">💥 SYSTEM CRASH</text>

      <!-- Phase 1: Analysis -->
      <path d="M 160 80 L 600 80" stroke="#fbbf24" stroke-width="3" />
      <rect x="330" y="65" width="120" height="22" rx="3" fill="#1e293b" stroke="#fbbf24" />
      <text x="390" y="80" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">1. Analysis Pass →</text>
      <text x="390" y="100" fill="#cbd5e1" font-size="9" text-anchor="middle">Finds active TXs and Dirty Pages at crash</text>

      <!-- Phase 2: Redo -->
      <path d="M 160 145 L 600 145" stroke="#34d399" stroke-width="3" />
      <rect x="330" y="135" width="120" height="22" rx="3" fill="#1e293b" stroke="#34d399" />
      <text x="390" y="150" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">2. Redo Pass (Repeating History) →</text>
      <text x="390" y="170" fill="#cbd5e1" font-size="9" text-anchor="middle">Replays all logged changes up to crash point</text>

      <!-- Phase 3: Undo -->
      <path d="M 600 195 L 300 195" stroke="#c084fc" stroke-width="3" />
      <rect x="400" y="185" width="120" height="22" rx="3" fill="#1e293b" stroke="#c084fc" />
      <text x="460" y="200" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">← 3. Undo Pass</text>
      <text x="460" y="220" fill="#cbd5e1" font-size="9" text-anchor="middle">Rolls back uncommitted loser transactions</text>
    </svg>
    """

    # SVG 3: LSM Tree Architecture
    svg_lsm = """
    <svg viewBox="0 0 880 240" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="860" height="220" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
      
      <!-- Write Entry -->
      <rect x="30" y="40" width="130" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <text x="95" y="65" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Write Request</text>
      <text x="95" y="85" fill="#94a3b8" font-size="9" text-anchor="middle">Append-only speed</text>

      <line x1="160" y1="70" x2="200" y2="70" stroke="#38bdf8" stroke-width="2" />

      <!-- In-Memory Component -->
      <rect x="200" y="25" width="220" height="90" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="310" y="48" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">RAM: MemTable (SkipList)</text>
      <text x="310" y="68" fill="#bae6fd" font-size="9" text-anchor="middle">+ Append to WAL on Disk (Crash safety)</text>
      <text x="310" y="88" fill="#fbbf24" font-size="9" text-anchor="middle">Memory Size Cap: ~64MB</text>

      <line x1="420" y1="70" x2="470" y2="70" stroke="#34d399" stroke-width="2" stroke-dasharray="3,3" />

      <!-- Immutable MemTable -->
      <rect x="470" y="30" width="160" height="80" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="550" y="55" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Immutable MemTable</text>
      <text x="550" y="75" fill="#a7f3d0" font-size="9" text-anchor="middle">Flushing to Disk as SSTable</text>

      <line x1="550" y1="110" x2="550" y2="140" stroke="#34d399" stroke-width="2" />

      <!-- Disk SSTables -->
      <rect x="200" y="140" width="620" height="75" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="280" y="165" fill="#fbbf24" font-size="11" font-weight="700">Disk: SSTables (Sorted String Tables) with Bloom Filters</text>
      <text x="280" y="185" fill="#94a3b8" font-size="9">Level 0 (Overlapping keys) → Level 1 (Sorted partitions) → Compaction merges duplicates</text>
      <text x="280" y="200" fill="#38bdf8" font-size="9">Read Amplification reduced via Bloom Filters (fast check if key exists in SSTable file)</text>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P0 Track A", "rose"), ("Engine Internals", "teal"), ("15-Min Sprint", "amber"), ("Databases", "blue")])
        + callout(
            "Database Engine Internals: The Foundation",
            "Top tech database interviews at Media.net, Oracle, Microsoft, Swiggy, and Cred probe engine internals rather than basic SQL syntax. You must master the physical mechanics: how B+ trees provide O(log N) point and range lookups, how LSM trees achieve 10× write throughput, how Write-Ahead Logging (WAL) guarantees durability before writing to dirty pages, and how Snapshot Isolation permits Write Skew.",
            "important"
        )
        + numbers_card("Database Storage & Latency Benchmarks", [
            ("L1 Cache Access", "~1 ns", "CPU cache lookup for buffer pool pointer"),
            ("RAM Page Access", "~100 ns", "Buffer pool hit for a 16KB InnoDB page"),
            ("NVMe SSD Random Read", "~20 - 50 µs", "Buffer pool miss requiring SSD read IOPS"),
            ("fsync() Latency", "~1 - 5 ms", "The true durability boundary for WAL flushes"),
            ("B+ Tree Fanout", "~100 - 1200 keys", "A 3-level B+ tree indexes >1 billion records in 3 I/Os!"),
            ("InnoDB Default Page", "16 KB", "Standard block transfer unit between disk and RAM")
        ])
        + subsection(
            "acid-internals",
            "ACID Properties & Concrete Engine Mechanisms",
            table(
                ["ACID Property", "Formal Guarantee", "Implementation Mechanism in Engine", "Failure / Recovery Edge Case"],
                [
                    ["Atomicity", "All-or-nothing execution of transaction statements", "Undo Log (Rollback Segments in InnoDB)", "Crash during active transaction rolled back via Undo Log during recovery"],
                    ["Consistency", "Database moves from one valid state to another satisfying schema constraints", "Application validation, Foreign Keys, CHECK constraints, Unique Indexes", "Violations trigger automatic transaction abort"],
                    ["Isolation", "Concurrent transactions execute without interfering with one another", "2PL (Pessimistic locking) or MVCC (Multi-Version Concurrency Control)", "Anomalies: Dirty Read, Non-Repeatable Read, Phantom Read, Write Skew"],
                    ["Durability", "Committed transactions survive crashes, power outages, and OS faults", "Write-Ahead Logging (WAL / Redo Log) + `fsync()` to persistent disk", "Steal/No-Force buffer pool policy ensures dirty pages flushed later"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "isolation-anomalies",
            "Transaction Isolation Levels × Anomalies Matrix",
            table(
                ["Isolation Level", "Dirty Read", "Non-Repeatable Read", "Phantom Read", "Write Skew", "Mechanism"],
                [
                    ["Read Uncommitted", "❌ Permitted", "❌ Permitted", "❌ Permitted", "❌ Permitted", "Reads raw uncommitted dirty buffers. Never used in production."],
                    ["Read Committed", "✅ Prevented", "❌ Permitted", "❌ Permitted", "❌ Permitted", "MVCC: fresh Read View taken at EVERY individual statement. Default in Postgres."],
                    ["Repeatable Read", "✅ Prevented", "✅ Prevented", "⚠️ Prevented in InnoDB (Next-Key)", "❌ Permitted!", "MVCC: single Read View taken at transaction start. Permits Write Skew anomaly!"],
                    ["Serializable", "✅ Prevented", "✅ Prevented", "✅ Prevented", "✅ Prevented", "Strict 2PL, Predicate Locking, or Serializable Snapshot Isolation (SSI)."]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "bplus-vs-lsm",
            "B+ Tree vs LSM Tree: Storage Engine Selection",
            table(
                ["Dimension", "B+ Tree (InnoDB, Postgres, SQLite)", "LSM Tree (RocksDB, Cassandra, LevelDB)", "Architectural Tradeoff"],
                [
                    ["Target Workload", "Read-heavy (80% reads / 20% writes), Point + Range scans", "Write-heavy (Time-series, Event logs, High-velocity ingest)", "Random write vs sequential append"],
                    ["Write Path", "In-place updates in 16KB dirty pages. Random disk writes!", "Append to WAL + in-memory MemTable. 100% sequential writes!", "LSM writes up to 10× faster than B+ trees"],
                    ["Read Path", "O(log_B N) deterministic disk page reads (~2-3 I/Os)", "Check MemTable → Bloom Filters → Level 0 to Level K SSTables", "LSM suffers from Read Amplification"],
                    ["Write Amplification", "High: updating 1 byte requires writing entire 16KB dirty page", "Moderate: compaction repeatedly rewrites SSTable layers", "Compaction requires background disk I/O bandwidth"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "null-logic-traps",
            "NULL Three-Valued Logic & Production Gotchas",
            callout(
                "Why 'WHERE col != NULL' Silently Returns Zero Rows",
                "In ANSI SQL, NULL represents an *unknown* value, not zero or empty string. Comparison operators with NULL evaluate to **UNKNOWN** (Three-Valued Logic: TRUE, FALSE, UNKNOWN).\n"
                "• `WHERE col = NULL` or `WHERE col != NULL` both evaluate to UNKNOWN, which the WHERE clause filters out as falsy! Always use `IS NULL` or `IS NOT NULL`.\n"
                "• `COUNT(*)` counts total rows including NULLs. `COUNT(col)` counts only rows where `col IS NOT NULL`!\n"
                "• `WHERE id NOT IN (SELECT parent_id FROM t)`: If the subquery contains even a SINGLE row with `parent_id IS NULL`, the entire `NOT IN` condition collapses to UNKNOWN and returns 0 rows! Fix: Use `NOT EXISTS` instead.",
                "important"
            ),
            depth="sprint"
        )
    )

    # Section 2: Storage Engines Deep Dive
    storage_html = (
        subsection(
            "bplus-architecture",
            "B+ Tree Storage Architecture: Fanout & Inode Mapping",
            svg_card("B+ Tree Internal Nodes and Doubly Linked Leaf Nodes", svg_bplus)
            + callout(
                "Why Databases Use B+ Trees Instead of Binary Search Trees or B-Trees",
                "1. **Massive Fanout Minimizes Disk I/O**: A binary tree has fanout 2, requiring 30 disk seeks for 1 billion items. A B+ tree with 16KB page size and 8-byte keys has fanout ~1000, requiring only 3 disk reads!\n"
                "2. **Internal Nodes Hold Only Keys**: Unlike standard B-trees which store record payloads in internal nodes, B+ trees store payloads exclusively in leaf pages. This maximizes internal node key capacity and keeps the tree shallow.\n"
                "3. **Doubly Linked Leaf Level**: Leaves are connected via sequential pointers. Range scans (`BETWEEN 20 AND 80`) perform ONE root-to-leaf lookup, then scan horizontally in O(1) page traversals without ascending the tree.",
                "tip"
            )
            + svg_card("LSM Tree (Log-Structured Merge-Tree) Architecture", svg_lsm),
            depth="deep"
        )
        + subsection(
            "composite-index-rule",
            "The Leftmost Prefix Rule for Composite Indexes",
            callout(
                "Interview Query Analysis: INDEX(a, b, c)",
                "A composite index creates a single B+ tree ordered lexicographically by `(a, then b, then c)`:\n"
                "• `WHERE a = 1 AND b = 2 AND c = 3` → ✅ Full Index Lookup on all 3 columns.\n"
                "• `WHERE a = 1 AND b = 2` → ✅ Index Lookup using prefix `(a, b)`.\n"
                "• `WHERE a = 1` → ✅ Index Lookup using prefix `(a)`.\n"
                "• `WHERE b = 2 AND c = 3` → ❌ Cannot use index lookup! The tree is sorted by `a` first; without filtering on `a`, it degrades to a Full Index Scan or Table Scan.\n"
                "• `WHERE a = 1 AND c = 3` → ⚠️ Uses index for `a = 1`, but cannot use index for `c` directly (Index Condition Pushdown evaluates `c`).",
                "tip"
            ),
            depth="deep"
        )
    )

    # Section 3: WAL & Recovery
    recovery_html = (
        subsection(
            "wal-aries",
            "Write-Ahead Logging (WAL) & ARIES Crash Recovery",
            svg_card("ARIES Recovery Pipeline: Analysis, Redo, and Undo Passes", svg_wal)
            + callout(
                "The Write-Ahead Logging Invariant",
                "**Invariant**: Any dirty data page modified in the buffer pool must NEVER be flushed to disk until the corresponding log record in the WAL has been persisted to disk via `fsync()`.\n"
                "• **Steal Policy**: Buffer manager can flush dirty pages to disk before transaction commit to free RAM. (Requires Undo Log to rollback if aborted).\n"
                "• **No-Force Policy**: Buffer manager does NOT force dirty pages to disk at transaction commit; only the WAL is forced. (Requires Redo Log to replay changes on restart).\n"
                "• ARIES crash recovery executes in 3 sequential passes: (1) **Analysis** scans forward from checkpoint to identify active loser transactions and dirty pages, (2) **Redo** repeats history from earliest unwritten LSN to restore exact crash state, (3) **Undo** scans backward rolling back active uncommitted transactions.",
                "important"
            ),
            depth="deep"
        )
    )

    # Section 4: Concurrency & MVCC
    concurrency_html = (
        subsection(
            "two-phase-locking",
            "Two-Phase Locking (2PL) vs Multi-Version Concurrency (MVCC)",
            table(
                ["Protocol Variant", "Growing Phase", "Shrinking Phase", "Deadlock Risk", "Cascading Aborts?"],
                [
                    ["Basic 2PL", "Acquires locks; cannot release any lock until all required locks acquired", "Releases locks; cannot acquire any new lock", "Yes", "Yes: uncommitted changes read by others"],
                    ["Strict 2PL", "Acquires shared and exclusive locks", "Holds **Exclusive Locks** until transaction Commit/Abort", "Yes", "✅ No: prevents dirty reads completely"],
                    ["Rigorous 2PL", "Acquires shared and exclusive locks", "Holds **ALL Locks** (Shared and Exclusive) until Commit/Abort", "Yes", "✅ No: guarantees strict conflict serializability"]
                ]
            )
            + callout(
                "Write Skew Anomaly: Why Repeatable Read Fails Under MVCC",
                "Write Skew occurs when two concurrent transactions read overlapping data sets, make decisions based on what they read, and write non-overlapping updates that together violate a global consistency constraint!\n"
                "**Classic Example (Hospital On-Call Doctors)**: Constraint: At least 1 doctor must be on call. Both Dr. Alice and Dr. Bob are currently on call (count = 2).\n"
                "• Transaction 1 (Dr. Alice): Checks `SELECT COUNT(*) WHERE on_call = true` (reads 2). Decides she can take leave: `UPDATE doctor SET on_call = false WHERE name = 'Alice'`; Commits.\n"
                "• Transaction 2 (Dr. Bob): Simultaneously checks `SELECT COUNT(*)` (reads 2 in his snapshot). Decides he can take leave: `UPDATE doctor SET on_call = false WHERE name = 'Bob'`; Commits.\n"
                "Both updates succeed because they updated different rows without write lock conflict! Result: ZERO doctors on call, violating the invariant! Snapshot Isolation / Repeatable Read permits this; only **Serializable** prevents it.",
                "tip"
            ),
            depth="deep"
        )
    )

    # Section 5: Worked Derivations
    worked_html = (
        subsection(
            "worked-serializability",
            "Worked Numerical 1: Conflict Serializability & Precedence Graphs",
            worked_example(
                title="Conflict Serializability Test on Schedule S: R1(A), W2(A), R1(B), W3(B), R2(A), W1(B)",
                steps=[
                    ("Identify Conflicting Operations", "Two operations conflict if they belong to different transactions, access the exact same data item, and at least one is a write operation."),
                    ("Conflict 1 (Item A)", "R1(A) precedes W2(A) → Directed edge: T1 → T2."),
                    ("Conflict 2 (Item A)", "W2(A) precedes R2(A) → Same transaction T2 (no edge)."),
                    ("Conflict 3 (Item B)", "W3(B) precedes W1(B) → Directed edge: T3 → T1."),
                    ("Conflict 4 (Item B)", "R1(B) precedes W3(B) → Directed edge: T1 → T3."),
                    ("Cycle Detection", "We have edge T3 → T1 and edge T1 → T3! There is a directed cycle between T1 and T3 (T1 ⇄ T3).")
                ],
                answer="Schedule S is NOT conflict-serializable because its precedence graph contains a directed cycle (T1 ⇄ T3). It cannot be transformed into any equivalent serial schedule."
            ),
            depth="deep"
        )
        + subsection(
            "worked-normalization",
            "Worked Numerical 2: Functional Dependencies & BCNF Decomposition",
            worked_example(
                title="Relation R(A, B, C, D, E) with FDs: { A → BC, CD → E, B → D, E → A }",
                steps=[
                    ("Find Candidate Keys", "Attribute A closure: A+ = {A, B, C, D, E} → A is a Candidate Key! Attribute E closure: E+ = {E, A, B, C, D} → E is a Candidate Key! Attribute (B, C) closure: BC+ = {B, C, D, E, A} → BC is a Candidate Key!"),
                    ("Check 3NF Condition", "For every FD X → Y: either X is a superkey, or Y is a prime attribute (part of a candidate key). In B → D: B is not a superkey, but D is prime? Candidate keys are A, E, BC. Prime attributes: {A, B, C, E}. D is NOT prime! Violates 3NF."),
                    ("Check BCNF Condition", "In B → D: B is not a superkey. Therefore R is NOT in BCNF."),
                    ("BCNF Decomposition", "Decompose R on violating FD B → D into R1(B, D) with key B (in BCNF) and R2(A, B, C, E) with key A or E (in BCNF).")
                ],
                answer="Relation R is decomposed into R1(B, D) and R2(A, B, C, E), both satisfying BCNF with a lossless join decomposition."
            ),
            depth="deep"
        )
    )

    # Section 6: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield DBMS Engine Interview Flashcards",
        flashcard(
            "What is the difference between Clustered and Non-Clustered Indexes?",
            "A Clustered Index dictates the physical on-disk storage order of table data rows. The leaf nodes of a clustered index contain the actual data rows themselves (e.g. primary key in InnoDB). A table can have only ONE clustered index. A Non-Clustered (Secondary) Index maintains a separate B+ tree where leaf nodes store the indexed key along with a pointer to the clustered index key (Primary Key in InnoDB) or disk RID. Looking up via non-clustered index requires a second lookup ('bookmark lookup') to fetch unindexed columns, unless it is a Covering Index.",
            "P0 Storage Systems"
        )
        + flashcard(
            "How does MVCC (Multi-Version Concurrency Control) allow readers to not block writers?",
            "Instead of placing shared locks on data rows, MVCC creates a new timestamped version of a row whenever an UPDATE occurs. In InnoDB, each row contains hidden system columns: `DB_TRX_ID` (transaction ID that created the row) and `DB_ROLL_PTR` (pointer to the undo log record containing prior version). When a transaction reads under Repeatable Read, the engine establishes a Read View. If a row was modified after the Read View, the engine traverses the Undo Log version chain backwards to read the historical snapshot. Readers never acquire locks and writers never block readers!",
            "P0 Transaction Internals"
        )
        + flashcard(
            "What is the difference between DELETE, TRUNCATE, and DROP?",
            "1. `DELETE`: DML operation. Scans and removes rows one by one, firing triggers and logging each row in the Undo/Redo log. Very slow on large tables; does NOT reset auto-increment or release disk space. Rollback-able.\n2. `TRUNCATE`: DDL operation. Deallocates entire data pages directly and resets the high-water mark and auto-increment counter. Extremely fast. Rollback-ability varies: MySQL cannot rollback TRUNCATE; PostgreSQL and SQL Server CAN rollback TRUNCATE within a transaction!\n3. `DROP`: DDL operation. Completely destroys table schema, indexes, constraints, and data pages from the database catalog.",
            "P0 Campus Classic"
        )
        + flashcard(
            "Why is SELECT COUNT(*) slow in MySQL InnoDB but instant in MyISAM?",
            "MyISAM stores an exact row count counter in the table header metadata file (`.MYI`), returning `COUNT(*)` in O(1) time without reading data. However, InnoDB uses MVCC: different concurrent transactions can see different numbers of active rows simultaneously depending on their active Read Views and uncommitted transactions! Therefore, InnoDB must perform an actual index scan over the smallest available secondary index to count visible rows, which takes O(N) time.",
            "P0 Database Engines"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: ACID, Isolation & Indexes", sprint_html)
        + section("bplus-lsm-storage", "🌲 Storage Engines: B+ Trees vs LSM Trees", storage_html)
        + section("wal-aries-recovery", "💾 WAL & ARIES Recovery Protocol (Durability)", recovery_html)
        + section("concurrency-mvcc", "🔒 Concurrency Control, 2PL & Conflict Serializability", concurrency_html)
        + section("worked-dbms-math", "📐 Worked Derivations: Precedence Graphs & Normalization", worked_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
