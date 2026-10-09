#!/usr/bin/env python3
"""
build_solumn_modules.py
Compiles all Markdown (.md) and HTML (.html) modules for Solumn AI
Foundations Programme Interview Preparation Portal.
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import markdown
from template import render_solumn_page
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
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(99, 102, 241, 0.18); border: 1px solid #6366f1; color: #818cf8; text-transform: uppercase;">
      Campus Drive • Batch 2027
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981;">
      ₹2,00,000 Stipend + Frontier AI PPO
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; color: #fcd34d;">
      Dubai / Remote (6 Weeks)
    </span>
  </div>
  <h1 style="border-bottom: none; margin-bottom: 8px;">Solumn AI Interview Preparation Suite</h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 820px; margin-bottom: 1.5rem;">
    Comprehensive evaluation and interview training system engineered for the Solumn AI Foundations Programme recruitment drive at NIT Rourkela. Features verified company &amp; founder intelligence, 21-hour practical assignment solutions, deterministic verification harness engineering, Anthropic RSP v3.2 alignment standards, and candidate resume defenses.
  </p>

  <!-- Key Metrics Row -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 2rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Target Role</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">AI Safety Fellow / Engineer</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">PPO Conversion</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">Frontier AI Benchmark</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Delivery Quota</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">250 RLEs (6 / Day)</div>
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
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company &amp; Role Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Executive profile, Dubai HQ, Anthropic RSP v3.2 client gates, 3 live workstreams, and the 21-hour selection sprint.</p>
    </div>
  </a>

  <a href="01_Practical_Assignment.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Practical Task &amp; Verifiers</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Complete RLE package anatomy, deterministic thread-safe LRU cache grading harness, and automated CVE exploit verifier.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Python, Docker &amp; Verifiers</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Process limits via setrlimit, Docker SDK python harness, cgroups quotas, zero-flakiness testing rules, and trajectory logs.</p>
    </div>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">AI Safety &amp; RSPs</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Anthropic RSP v3.2, ASL-3/4 gates, DeepMind Frontier Safety Framework, RLVR paradigm, and Model Context Protocol security.</p>
    </div>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense &amp; Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending Uplan multi-agent critic, Amazon ML 24.2M high-throughput pipeline, Warehouse PathMapper, and M.Tech + B.Tech background.</p>
    </div>
  </a>

  <a href="05_System_Design_or_HIL.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Eval Foundry Architecture</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Scalable agent evaluation platform (10k tasks/day), pre-warmed container sandboxes, async python dispatcher, and AST verification.</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Founder Mindset &amp; PPO</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">McKinsey/BCG top-line communication, 250 quota time management, debugging false positives, and the Week-5 research proposal pitch.</p>
    </div>
  </a>

  <a href="07_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid Recall CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Python sandbox snippets, Docker CLI &amp; SDK flags, pytest deterministic patterns, and frontier safety comparison table.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">Module 08</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Selection Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Hour-by-hour tactical roadmap for Friday Oct 9 through Sunday Oct 11 to dominate assignment submission and founder interviews.</p>
    </div>
  </a>

</div>
"""

def build_all():
    print("Building Solumn AI Interview Prep Modules...")
    
    # 1. Render Index Page
    index_page_html = render_solumn_page(
        title="Solumn AI Foundations Prep Hub · Adarsh Saurabh",
        active_page="index.html",
        content_html=index_html_content,
        prev_link="../index.html",
        prev_title="All Companies",
        next_link="00_START_HERE.html",
        next_title="00: Company & Role Intel"
    )
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_page_html)
    print("✓ index.html generated")

    # 2. Render Each Module
    for mod_key, data in modules_data.items():
        md_filename = f"{mod_key}.md"
        html_filename = f"{mod_key}.html"

        # Save Markdown source
        with open(os.path.join(BASE_DIR, md_filename), "w", encoding="utf-8") as f:
            f.write(data["content_md"])
        print(f"✓ {md_filename} generated")

        # Convert Markdown to HTML
        raw_html = markdown.markdown(
            data["content_md"],
            extensions=['fenced_code', 'tables', 'codehilite', 'nl2br']
        )

        # Wrap in Solumn Template
        full_html = render_solumn_page(
            title=data["title"],
            active_page=data["active_page"],
            content_html=raw_html,
            prev_link=data.get("prev_link"),
            prev_title=data.get("prev_title"),
            next_link=data.get("next_link"),
            next_title=data.get("next_title")
        )

        with open(os.path.join(BASE_DIR, html_filename), "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"✓ {html_filename} generated")

    print("\nAll Solumn AI prep modules built successfully!")

if __name__ == "__main__":
    build_all()
