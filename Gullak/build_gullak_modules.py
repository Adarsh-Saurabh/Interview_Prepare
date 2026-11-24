#!/usr/bin/env python3
"""
build_gullak_modules.py
Compiles all Markdown (.md) and HTML (.html) modules for Gullak Technologies
Backend Engineer Interview Preparation Portal.
"""

import os
import markdown
from template import render_gullak_page
from modules_part1 import modules_part1
from modules_part2 import modules_part2
from modules_part3 import modules_part3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Combine all modules
raw_modules = {}
raw_modules.update(modules_part1)
raw_modules.update(modules_part2)
raw_modules.update(modules_part3)

ordered_keys = [
    ("00_START_HERE", "00: Executive Intel"),
    ("01_Online_Test_and_Algorithms", "01: Signature DSA & Puzzles"),
    ("02_Technical_Rounds_CS_Core", "02: OS, Concurrency & Networks"),
    ("03_Database_Internals_and_Transactions", "03: DBMS, ACID & Redis"),
    ("04_System_Design_LLD_and_HLD", "04: Fintech LLD & HLD"),
    ("05_Candidate_Resume_Grilling", "05: Resume Defense & Traps"),
    ("06_Managerial_and_HR_Culture", "06: Startup Culture & HR"),
    ("07_Quick_Reference_CheatSheet", "07: Rapid CheatSheet"),
    ("README", "Emergency Study Roadmap"),
]

index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; color: #d97706; text-transform: uppercase;">
      Campus Recruitment • Batch 2027
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981;">
      ₹20.00 LPA CTC • ₹50,000/mo Stipend
    </span>
  </div>
  <h1 style="border-bottom: none; margin-bottom: 8px;">Gullak Backend Engineer Interview Suite</h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 820px; margin-bottom: 1.5rem;">
    High-impact preparation dossier engineered for the Gullak Technologies Backend Engineer recruitment drive at NIT Rourkela. Features deep architectural analysis of Gullak's ex-Juspay founding pedigree, signature live coding &amp; puzzle implementations, PostgreSQL MVCC &amp; transaction isolation, QR-code authentication system design, and candidate-specific project defenses.
  </p>

  <!-- Key Metrics Row -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 2rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Target Role</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">Backend Engineer</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Compensation</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">₹20.00 LPA (6M + FTE)</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Monthly Stipend</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">₹50,000 / month</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Study Modules</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">9 Modules</div>
    </div>
  </div>
</div>

<h2 style="margin-bottom: 1.2rem;">Preparation Modules</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

  <a href="00_START_HERE.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Executive Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Gullak origin, ex-Juspay founding pedigree (Dilip Jain), ₹2,000+ Cr gold savings scale, and the 3-stage interview rubric.</p>
    </div>
  </a>

  <a href="01_Online_Test_and_Algorithms.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Signature DSA &amp; Puzzles</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">5 complete solutions in C++ &amp; Python: Ledger Fenwick Tree, Two-Pointer Reconciler, Top-K Min-Heap, 100-Locker Puzzle, and Transfer Cycle Detection.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds_CS_Core.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">OS, Concurrency &amp; Networks</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Process vs Thread memory, Goroutine M:N scheduler, Mutex vs Spinlock vs Atomic CAS, Linux Epoll, and TCP TIME_WAIT socket exhaustion.</p>
    </div>
  </a>

  <a href="03_Database_Internals_and_Transactions.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">DBMS, ACID &amp; Redis</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">PostgreSQL MVCC (xmin/xmax), Transaction Isolation anomalies, SELECT FOR UPDATE, Redis Redlock with fencing tokens, and Payment Idempotency.</p>
    </div>
  </a>

  <a href="04_System_Design_LLD_and_HLD.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Fintech LLD &amp; HLD</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">QR-Code Web Login architecture with Redis Lua race condition handling, Automated Gold Round-Up Micro-Savings Engine, and Transactional Outbox Pattern.</p>
    </div>
  </a>

  <a href="05_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense &amp; Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending Apna Gold Solutions (multi-tenant RLS, DB conflict resolution), Warehouse PathMapper (10k grid in &lt;0.5s), and turning M.Tech Signal Processing into a superpower.</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR_Culture.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Startup Culture &amp; HR</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">The 0-to-1 startup mindset, high agency, 8 STAR behavioral answers, and high-caliber questions to ask the interviewer.</p>
    </div>
  </a>

  <a href="07_Quick_Reference_CheatSheet.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">25 rapid-recall flashcards, ACID &amp; SQL isolation table, fintech HTTP status codes, and 60-second elevator pitches.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #d97706; text-transform: uppercase;">Study Guide</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Emergency Study Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Night-before and morning-of T-90, T-45, T-20 minute battle plan to maximize performance and confidence.</p>
    </div>
  </a>

</div>
"""

def main():
    print("Building Gullak Backend Engineer Interview Preparation Suite...")
    num_mods = len(ordered_keys)
    master_markdown_content = "# Gullak Technologies — Backend Engineer Interview Preparation Master Dossier\n\n"

    for i, (key, label) in enumerate(ordered_keys):
        mod = raw_modules[key]
        md_file = os.path.join(BASE_DIR, f"{key}.md")
        html_file = os.path.join(BASE_DIR, f"{key}.html")

        # Determine prev / next links
        prev_link = None
        prev_title = None
        next_link = None
        next_title = None

        if i > 0:
            prev_key, prev_title = ordered_keys[i - 1]
            prev_link = f"{prev_key}.html"
        if i < num_mods - 1:
            next_key, next_title = ordered_keys[i + 1]
            next_link = f"{next_key}.html"

        # Write .md file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(mod)
        print(f"  [MD] Written: {key}.md")

        # Append to Master Guide
        master_markdown_content += f"\n\n---\n\n{mod}\n"

        # Convert markdown to html
        rendered_body = markdown.markdown(
            mod,
            extensions=["fenced_code", "tables", "codehilite", "toc"]
        )

        full_html = render_gullak_page(
            title=f"{label} · Gullak Prep",
            active_page=f"{key}.html",
            content_html=rendered_body,
            prev_link=prev_link,
            prev_title=prev_title,
            next_link=next_link,
            next_title=next_title
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  [HTML] Written: {key}.html")

    # Write Master Guide
    master_guide_path = os.path.join(BASE_DIR, "Gullak_Backend_Engineer_Complete_Interview_Guide.md")
    with open(master_guide_path, "w", encoding="utf-8") as f:
        f.write(master_markdown_content)
    print(f"  [MASTER] Written: Gullak_Backend_Engineer_Complete_Interview_Guide.md")

    # Write index.html
    index_file = os.path.join(BASE_DIR, "index.html")
    index_full_html = render_gullak_page(
        title="Gullak Backend Engineer Interview Portal · Adarsh Saurabh",
        active_page="index.html",
        content_html=index_html_content,
        prev_link=None,
        prev_title=None,
        next_link="00_START_HERE.html",
        next_title="00: Executive Intel"
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_full_html)
    print(f"  [INDEX] Written: index.html")

    print("\nAll Gullak modules successfully compiled and verified!")

if __name__ == "__main__":
    main()
