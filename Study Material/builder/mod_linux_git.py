# mod_linux_git.py - Linux, Git & CLI Debugging Module Generator
# Conforms to instruction.md Part 7.8 Specification (P1 Track D)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Server Diagnosis & Git Mental Model"),
        ("cli-pipelines", "🛠️ Top 10 CLI Text-Processing One-Liners"),
        ("git-mechanics", "🐙 Git Internals, Merge vs Rebase & Surgery"),
        ("performance-strace", "🔍 Performance Profiling: strace & perf"),
        ("disk-inodes", "💾 Inode Exhaustion & Disk Space Anomalies"),
        ("interview-flashcards", "🎯 28 Top Tech Interview Q&As")
    ]

    # SVG 1: Git 4-Area Architecture
    svg_git_areas = """
    <svg viewBox="0 0 880 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="git-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <g transform="translate(20, 40)">
        <!-- Working Tree -->
        <rect x="0" y="0" width="160" height="90" rx="8" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
        <text x="80" y="35" fill="#f43f5e" font-size="12" font-weight="800" text-anchor="middle">WORKING DIRECTORY</text>
        <text x="80" y="60" fill="#94a3b8" font-size="10" text-anchor="middle">Unstaged edits on disk</text>

        <!-- Arrow to Staging -->
        <line x1="160" y1="45" x2="220" y2="45" stroke="#38bdf8" stroke-width="2" marker-end="url(#git-arr)" />
        <text x="190" y="35" fill="#38bdf8" font-size="10" text-anchor="middle">git add</text>

        <!-- Staging / Index -->
        <rect x="230" y="0" width="160" height="90" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
        <text x="310" y="35" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">STAGING (INDEX)</text>
        <text x="310" y="60" fill="#94a3b8" font-size="10" text-anchor="middle">Prepared snapshot</text>

        <!-- Arrow to Local Repo -->
        <line x1="390" y1="45" x2="450" y2="45" stroke="#38bdf8" stroke-width="2" marker-end="url(#git-arr)" />
        <text x="420" y="35" fill="#38bdf8" font-size="10" text-anchor="middle">git commit</text>

        <!-- Local Repository -->
        <rect x="460" y="0" width="160" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
        <text x="540" y="35" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">LOCAL REPOSITORY</text>
        <text x="540" y="60" fill="#94a3b8" font-size="10" text-anchor="middle">HEAD / Commit tree</text>

        <!-- Arrow to Remote -->
        <line x1="620" y1="45" x2="680" y2="45" stroke="#38bdf8" stroke-width="2" marker-end="url(#git-arr)" />
        <text x="650" y="35" fill="#38bdf8" font-size="10" text-anchor="middle">git push</text>

        <!-- Remote Repository -->
        <rect x="690" y="0" width="150" height="90" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
        <text x="765" y="35" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">REMOTE (ORIGIN)</text>
        <text x="765" y="60" fill="#bae6fd" font-size="10" text-anchor="middle">GitHub / GitLab</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("When an interviewer asks 'The production server is slow, what do you run?', memorize the strict diagnosis order: top (CPU/load) -> free -h (RAM/swap) -> df -h / iostat (Disk I/O) -> ss -tulpn (Socket/Network queues).")}

    <p>Every engineer uses Linux and Git daily, yet candidates freeze when asked about permissions, zombie process reaping, or unlinking open file descriptors.</p>

    {svg_card(svg_git_areas, "The 4 Areas of Git: Working Tree -> Staging Area -> Local HEAD -> Remote Origin")}

    {table(
        headers=["Diagnostic Command", "What Metric It Evaluates", "Normal Baseline", "Threshold Requiring Immediate Action"],
        rows=[
            ["<code>top</code> / <code>htop</code>", "CPU utilization, Load Average (1m, 5m, 15m), Per-process CPU.", "Load Avg &lt; Total CPU Cores.", "Load Avg &gt; 2x CPU Cores (CPU starvation or process convoy)."],
            ["<code>free -h</code>", "Total, Used, Free RAM and Swap space.", "Swap used = 0B or &lt; 5%.", "Swap actively growing & RAM full (Thrashing & imminent OOMKiller)."],
            ["<code>df -h</code> & <code>df -i</code>", "Disk capacity and Inode table utilization.", "Usage &lt; 80%.", "Disk 100% or Inodes 100% (file write failures)."],
            ["<code>iostat -xz 1</code>", "Disk I/O wait, throughput, and %util.", "%util &lt; 60%.", "%util = 100% with high await (Disk I/O bottleneck)."],
            ["<code>ss -tulpn</code>", "Active listening TCP/UDP ports and socket queue backlogs.", "Recv-Q = 0.", "Recv-Q &gt; 0 and full (Application unable to accept connections)."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Server Diagnosis & Git Mental Model", s1_body, pill="CLI & Server", pill_color="cyan"))

    # Section 2: CLI Pipelines
    s2_body = f"""
    {table(
        headers=["Task / Analysis", "Production CLI One-Liner", "Explanation of Mechanism"],
        rows=[
            ["Top 10 IP Addresses in Log", "<code>awk '{{print $1}}' access.log | sort | uniq -c | sort -nr | head -10</code>", "Extracts IP, sorts for grouping, counts frequency, reverse numeric sorts."],
            ["Kill All Zombie / Hung Processes", "<code>kill -9 $(ps aux | grep 'defunct' | awk '{{print $2}}')</code>", "Identifies PIDs of hung processes and sends SIGKILL."],
            ["Find Files &gt; 100MB", "<code>find / -type f -size +100M -exec ls -lh {{}} \\;</code>", "Scans disk for massive files causing disk space alerts."],
            ["Follow Log with Regex Filter", "<code>tail -f app.log | grep --line-buffered -E 'ERROR|FATAL'</code>", "Streams log file in real-time, buffering lines matching critical keywords."]
        ]
    )}
    """
    content.append(section("cli-pipelines", "🛠️ Top 10 CLI Text-Processing One-Liners", s2_body, pill="One-Liners", pill_color="emerald"))

    # Section 3: Git Mechanics
    s3_body = f"""
    {decision_matrix(
        title="Git Operations: Merge vs Rebase",
        options=[
            ("git merge", "Feature branch into main. Preserves complete historical context and exact timeline commits.", "Local unpushed feature branches where clean linear history is desired."),
            ("git rebase", "Updating a local unpushed feature branch against latest main to create a clean, linear PR history.", "Shared public branches! Never rebase commits that other engineers have pulled.")
        ]
    )}

    {table(
        headers=["Command", "What It Changes", "Safety & Recovery", "Canonical Use-Case"],
        rows=[
            ["<code>git reset --soft HEAD~1</code>", "Moves HEAD back by 1 commit. Working directory & Staging index UNTOUCHED.", "100% Safe.", "Rewording commit message or combining changes."],
            ["<code>git reset --hard HEAD~1</code>", "Discards commit, staging index, AND local working directory edits!", "⚠️ Dangerous (Can recover via <code>git reflog</code>).", "Completely throwing away broken experimental code."],
            ["<code>git revert &lt;commit&gt;</code>", "Appends a NEW commit that applies the inverse diff of target commit.", "100% Safe for shared branches.", "Undoing a broken commit pushed to shared main."]
        ]
    )}
    """
    content.append(section("git-mechanics", "🐙 Git Internals, Merge vs Rebase & Surgery", s3_body, pill="Git Depth", pill_color="purple", depth="deep"))

    # Section 4: Performance strace & perf
    s4_body = f"""
    {code(
        src=r"""# Trace system calls of a running process PID 1234
strace -p 1234 -c # Counts time, calls, and errors per system call

# Trace what file a hung process is attempting to open
strace -e trace=open,openat,read,write -p 1234""",
        lang="bash",
        title="Debugging Process System Calls with strace"
    )}
    """
    content.append(section("performance-strace", "🔍 Performance Profiling: strace & perf", s4_body, pill="Profiling", pill_color="amber", depth="deep"))

    # Section 5: Disk & Inodes
    s5_body = f"""
    {callout(
        title="The Classic Trap: 'df -h' says Disk Full, but 'du -sh' says files are small!",
        body="A process opened a massive log file (e.g. 50GB) and another developer ran <code>rm app.log</code>. The directory entry is deleted, so <code>du</code> cannot find it! However, because the running process still holds an open file descriptor, <strong>the Linux kernel does not reclaim the disk blocks</strong>! Run <code>lsof +L1</code> to locate the deleted file held open, and restart or kill the process to immediately free disk space.",
        kind="trap"
    )}
    """
    content.append(section("disk-inodes", "💾 Inode Exhaustion & Disk Space Anomalies", s5_body, pill="Linux Traps", pill_color="rose", depth="deep"))

    # Section 6: 28 Interview Flashcards
    qa_list = [
        ("What is the difference between kill and kill -9 (SIGTERM vs SIGKILL)?",
         "SIGTERM (kill PID / signal 15) politely asks the process to terminate, allowing it to execute cleanup handlers, flush files, and close network sockets. SIGKILL (kill -9 / signal 9) cannot be caught or ignored; the Linux kernel immediately terminates the process without cleanup.",
         ["Signals"], "Easy", ["Apple", "Qualcomm"]),
        ("Why should every shell script start with 'set -euo pipefail'?",
         "-e exits immediately on any command failure; -u treats unset variables as errors; -o pipefail ensures pipeline exit codes reflect the first failing command instead of only the last command. Prevents silent catastrophic failures in deployment scripts.",
         ["Bash"], "Medium", ["All Companies"]),
        ("You ran 'git reset --hard' and lost 3 days of work. How do you recover it?",
         "Run 'git reflog'. Git reflog maintains an append-only log of where HEAD has pointed locally over the last 30-90 days. Find the SHA before the reset and run 'git reset --hard <reflog_sha>' to restore your work.",
         ["Git Recovery"], "Medium", ["Google", "Meta"]),
        ("Why must PID 1 in a Linux container reap zombie child processes?",
         "In Unix, when a process terminates, it remains a 'zombie' until its parent calls wait(). If the parent terminates first, orphaned children get reparented to PID 1. If PID 1 does not implement a reaping loop, zombie processes accumulate and exhaust the kernel PID table.",
         ["Containers"], "Hard", ["Docker", "Kubernetes"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s6_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 28 Top Tech Interview Q&As", s6_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
