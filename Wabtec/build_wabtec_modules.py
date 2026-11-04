#!/usr/bin/env python3
"""
build_wabtec_modules.py
Compiles all Markdown (.md) and HTML (.html) modules for Wabtec Corporation
LEAD Program Interview Preparation Portal.
"""

import os
import markdown
from template import render_wabtec_page
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
    ("00_START_HERE", "00: Company & LEAD Intel"),
    ("01_Online_Test", "01: Signature OA Problems"),
    ("02_Technical_Rounds", "02: OS, RTOS & C++"),
    ("03_Domain_Deep_Dive", "03: Rail Tech & Systems"),
    ("04_Candidate_Resume_Grilling", "04: Resume Defense"),
    ("05_System_Design_or_HIL", "05: LLD & HLD Architecture"),
    ("06_Managerial_and_HR", "06: Leadership & HR"),
    ("07_Quick_Reference", "07: Rapid CheatSheet"),
    ("README", "3-Day Study Roadmap"),
]

index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(0, 51, 102, 0.15); border: 1px solid #003366; color: #0284c7; text-transform: uppercase;">
      Campus Recruitment • Batch 2027
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981;">
      ₹15.50 LPA Fixed + 7.5% Variable
    </span>
  </div>
  <h1 style="border-bottom: none; margin-bottom: 8px;">Wabtec LEAD Program Interview Suite</h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 820px; margin-bottom: 1.5rem;">
    Comprehensive preparation dossier engineered for the Wabtec Corporation Leadership Expertise &amp; Accelerated Development (LEAD) recruitment drive at NIT Rourkela. Features deep rail-tech systems intelligence, 5 signature OA problem implementations, real-time operating systems (RTOS), and candidate-specific project defenses.
  </p>

  <!-- Key Metrics Row -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 2rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Target Role</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">LEAD Program</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Fixed Compensation</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">₹15.50 LPA (CS/EC)</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Rotational Structure</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">4 × 6 Months (2 Yrs)</div>
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
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company &amp; LEAD Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Executive profile, GE Transportation merger, WITEC Bengaluru hub, 2-year rotational roadmap, and selection stages.</p>
    </div>
  </a>

  <a href="01_Online_Test.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Signature OA Problems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">5 complete solutions in C++ &amp; Python: Grid pathfinding with momentum, train velocity DP, CAN hex byte swap, and lock-free SPSC buffer.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">OS, RTOS &amp; C++ Internals</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Process vs Thread memory, RMS vs EDF real-time scheduling, Priority Inversion (PIP), vtable/vptr mechanics, and RAII smart pointers.</p>
    </div>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rail Tech &amp; Digital Systems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Positive Train Control (PTC) fail-safe braking, Trip Optimizer autonomous physics cruise control, and Distributed Power wireless synchronization.</p>
    </div>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense &amp; Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending Warehouse PathMapper (10k grid in &lt;0.5s), K-HUKI edge vision (11× faster), Uplan deterministic rule engines, and dual M.Tech+B.Tech profile.</p>
    </div>
  </a>

  <a href="05_System_Design_or_HIL.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">LLD &amp; HLD Architecture</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">C++20 State Pattern PTC signal controller (LLD) and 10,000-locomotive EdgeLINC streaming telemetry &amp; predictive maintenance platform (HLD).</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Leadership &amp; HR Fit</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">The LEAD rotational mindset, 8 STAR behavioral scenario answers, domain ramp-up strategy, and high-impact questions to ask interviewers.</p>
    </div>
  </a>

  <a href="07_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid Recall CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">C++ memory cheatsheet, RMS/EDF formulas, CAN bus electrical specs, and candidate project metrics flashcards for last-minute review.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Study Guide</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Study Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Structured day-by-day revision checklist covering algorithms, systems fundamentals, rail domain, and executive behavioral rounds.</p>
    </div>
  </a>

</div>
"""

def main():
    print("Building Wabtec LEAD Interview Preparation Suite...")
    num_mods = len(ordered_keys)
    master_markdown_content = "# Wabtec Corporation — LEAD Program Interview Preparation Master Dossier\n\n"

    for i, (key, label) in enumerate(ordered_keys):
        mod = raw_modules[key]
        md_file = os.path.join(BASE_DIR, f"{key}.md")
        html_file = os.path.join(BASE_DIR, f"{key}.html")

        # Determine prev / next links
        prev_link = None
        prev_title = None
        if i == 0:
            prev_link = "index.html"
            prev_title = "Overview & Hub"
        else:
            prev_key, prev_label = ordered_keys[i - 1]
            prev_link = f"{prev_key}.html"
            prev_title = prev_label

        next_link = None
        next_title = None
        if i < num_mods - 1:
            next_key, next_label = ordered_keys[i + 1]
            next_link = f"{next_key}.html"
            next_title = next_label

        # 1. Write Markdown file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(mod["content"])
        print(f"  [MD] Created {key}.md")

        master_markdown_content += f"\n\n---\n\n{mod['content']}\n"

        # 2. Render Markdown to HTML
        body_html = markdown.markdown(
            mod["content"],
            extensions=["fenced_code", "tables", "nl2br"]
        )

        # Wrap tables in responsive table-wrapper
        body_html = body_html.replace("<table>", '<div class="table-wrapper"><table>').replace("</table>", '</table></div>')

        full_html = render_wabtec_page(
            title=mod["title"],
            active_page=f"{key}.html",
            content_html=body_html,
            prev_link=prev_link,
            prev_title=prev_title,
            next_link=next_link,
            next_title=next_title
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  [HTML] Rendered {key}.html")

    # Write Master Consolidated Markdown Guide
    master_md_file = os.path.join(BASE_DIR, "Wabtec_LEAD_Complete_Interview_Guide.md")
    with open(master_md_file, "w", encoding="utf-8") as f:
        f.write(master_markdown_content)
    print(f"  [MASTER MD] Created Wabtec_LEAD_Complete_Interview_Guide.md")

    # Render index.html hub page
    index_file = os.path.join(BASE_DIR, "index.html")
    index_full_html = render_wabtec_page(
        title="Overview & Hub • Wabtec LEAD Interview Preparation",
        active_page="index.html",
        content_html=index_html_content,
        prev_link="../index.html",
        prev_title="All Companies Hub",
        next_link="00_START_HERE.html",
        next_title="00: Company & LEAD Intel"
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_full_html)
    print("  [HUB] Rendered index.html")

    print("\nAll Wabtec Corporation LEAD interview preparation modules generated successfully!")

if __name__ == "__main__":
    main()
