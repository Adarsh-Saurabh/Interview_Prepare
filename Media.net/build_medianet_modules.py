#!/usr/bin/env python3
"""
build_medianet_modules.py
Compiles all Markdown (.md) and HTML (.html) modules for Media.net
SDE Intern Interview Preparation Portal.
"""

import os
import markdown
from template import render_medianet_page
from modules_part1 import modules_part1
from modules_part2 import modules_part2
from modules_part3 import modules_part3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Combine all modules
modules_data = {}
modules_data.update(modules_part1)
modules_data.update(modules_part2)
modules_data.update(modules_part3)

index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(2, 132, 199, 0.15); border: 1px solid #0284c7; color: #0284c7; text-transform: uppercase;">
      Campus Drive • Batch 2027
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981;">
      1 LPM Stipend + 38 LPA CTC
    </span>
  </div>
  <h1 style="border-bottom: none; margin-bottom: 8px;">Media.net Interview Preparation Suite</h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 820px; margin-bottom: 1.5rem;">
    Comprehensive study system engineered for the Media.net SDE Intern recruitment drive at NIT Rourkela. Features verified company intelligence, 5 signature OA problem solutions, low-latency ad-tech architecture, deep CS core grilling, and candidate resume defenses.
  </p>

  <!-- Key Metrics Row -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 2rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Target Role</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">SDE Intern</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">PPO Conversion</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">18L + 4L + 16L</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Engineering SLA</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">Sub-50ms RTB</div>
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
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company &amp; Role Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Executive profile, ad-tech ecosystem, 500k+ publisher scale, and the 4 recruitment stages.</p>
    </div>
  </a>

  <a href="01_Online_Test.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Signature OA Problems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">5 complete CP solutions in Python &amp; C++: Top-K Vickrey auction, Wildcard Trie, Rate Limiter, and DAG cycle detection.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">OS, Networks &amp; DBMS</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Process vs Thread, TLB, Mutex vs Spinlock, TCP Keep-Alive, TIME_WAIT exhaustion, B+ Trees, and SQL window queries.</p>
    </div>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Ad-Tech &amp; RTB Systems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">OpenRTB 2.5 spec, Sub-50ms SLA breakdown, Header Bidding (Prebid.js), Redis Bitmaps, and HyperLogLog.</p>
    </div>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense &amp; Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending PathMapper (10k grid in &lt;0.5s), Uplan adversarial intelligence, Alt Data Radar, and M.Tech + B.Tech dual background.</p>
    </div>
  </a>

  <a href="05_System_Design_or_HIL.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">LLD &amp; Low-Latency HLD</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Thread-safe In-Memory Cache with TTL &amp; LRU (C++20), and Scalable Real-Time Contextual Ad Matching Engine architecture.</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Culture &amp; Ownership</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Navigating the JD's AI tools directive, Directi legacy meritocracy, and high-impact STAR behavioral responses.</p>
    </div>
  </a>

  <a href="07_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid Recall CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">C++ concurrency snippets, Little's Law, Amdahl's Law, SQL templates, Ad-Tech glossary, and candidate project metrics.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Study Guide</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Study Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Hour-by-hour preparation schedule across algorithms, CS fundamentals, ad-tech domain, and resume defense.</p>
    </div>
  </a>

</div>
"""

def main():
    print("Building Media.net Interview Preparation Suite...")
    for key, mod in modules_data.items():
        md_file = os.path.join(BASE_DIR, f"{key}.md")
        html_file = os.path.join(BASE_DIR, f"{key}.html")

        # 1. Write Markdown file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(mod["markdown"])
        print(f"  [MD] Created {key}.md")

        # 2. Render Markdown to HTML
        body_html = markdown.markdown(
            mod["markdown"],
            extensions=["fenced_code", "tables", "nl2br"]
        )

        # Wrap tables in responsive table-wrapper
        body_html = body_html.replace("<table>", '<div class="table-wrapper"><table>').replace("</table>", '</table></div>')

        full_html = render_medianet_page(
            title=mod["title"],
            active_page=f"{key}.html",
            content_html=body_html,
            prev_link=mod["prev_link"],
            prev_title=mod["prev_title"],
            next_link=mod["next_link"],
            next_title=mod["next_title"]
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  [HTML] Rendered {key}.html")

    # Render index.html hub page
    index_file = os.path.join(BASE_DIR, "index.html")
    index_full_html = render_medianet_page(
        title="Overview & Hub • Media.net Interview Preparation",
        active_page="index.html",
        content_html=index_html_content,
        prev_link="../index.html",
        prev_title="All Companies Hub",
        next_link="00_START_HERE.html",
        next_title="00: Company Deep Dive"
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_full_html)
    print("  [HUB] Rendered index.html")

    print("\nAll Media.net interview preparation modules generated successfully!")

if __name__ == "__main__":
    main()
