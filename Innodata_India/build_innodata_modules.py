#!/usr/bin/env python3
"""
build_innodata_modules.py
Compiles all Markdown (.md) and HTML (.html) modules for Innodata India
Industrial Technical Visual Reasoning Specialist Interview Preparation Portal.
"""

import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import markdown
from template import render_innodata_page
from modules_data_part1 import modules_data_part1
from modules_data_part2 import modules_data_part2
from modules_data_part3 import modules_data_part3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Combine all modules
modules_data = {}
modules_data.update(modules_data_part1)
modules_data.update(modules_data_part2)
modules_data.update(modules_data_part3)

index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(2, 132, 199, 0.18); border: 1px solid #0284c7; color: #0284c7; text-transform: uppercase;">
      Campus Drive • NIT Rourkela 2027
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; color: #10b981;">
      ₹60,000 – ₹70,000 / mo Stipend • 3M + PPO
    </span>
    <span style="font-size: 0.82rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: rgba(245, 158, 11, 0.15); border: 1px solid #f59e0b; color: #d97706;">
      PPO CTC: ₹10.00 – ₹14.00 LPA
    </span>
  </div>
  <h1 style="border-bottom: none; margin-bottom: 8px;">Innodata India Interview Preparation Suite</h1>
  <p style="font-size: 1.05rem; color: var(--text-secondary); max-width: 820px; margin-bottom: 1.5rem;">
    Comprehensive evaluation, benchmarking, and technical training system tailored for the <strong>Industrial Technical Visual Reasoning Specialist (Subject Matter Expert)</strong> recruitment drive at NIT Rourkela. Features authentic engineering artifact analysis, non-Googleable multimodal benchmark authoring protocols, Vision-Language Model failure mode catalogs, and candidate resume defenses.
  </p>

  <!-- Key Metrics Row -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 2rem;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Target Role</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">Visual Reasoning SME</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">PPO Conversion</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">₹10.00 – ₹14.00 LPA</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Quality Threshold</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">≥ 95% Accuracy</div>
    </div>
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 10px; padding: 14px 16px;">
      <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Study Modules</div>
      <div style="font-size: 1.15rem; font-weight: 800; color: var(--accent-primary); margin-top: 2px;">10 Modules</div>
    </div>
  </div>
</div>

<h2 style="margin-bottom: 1.2rem;">Preparation Modules</h2>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

  <a href="00_START_HERE.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company &amp; Role Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Executive business model, hyperscaler client partnerships, role mandate, and 4-stage hiring funnel.</p>
    </div>
  </a>

  <a href="01_Benchmark_Creation_Protocol.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Benchmark &amp; Gold-Sets</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">The 4-part benchmark schema, visual essentiality rules, non-Googleable problem formulation, and proof derivations.</p>
    </div>
  </a>

  <a href="02_Technical_Engineering_Artifacts.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Schematics, P&amp;ID &amp; Layouts</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">IEEE circuit standards, ISA-5.1 P&amp;ID instrument tagging conventions, and CAD spatial floorplan constraints.</p>
    </div>
  </a>

  <a href="03_Multimodal_AI_and_VLM_Foundations.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">VLMs &amp; Visual Reasoning</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Vision Transformer patch embedding, coordinate grounding, and the 5 signature failure modes of frontier models.</p>
    </div>
  </a>

  <a href="04_Coding_and_Automated_Verifiers.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Python &amp; C++ Verifiers</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Production JSON schema validator, NetworkX topological hydraulic verifier, and C++ bounding box IoU engine.</p>
    </div>
  </a>

  <a href="05_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Candidate Resume Defense</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Strategic defenses for Adarsh Saurabh: M.Tech Signal Processing synergy, Uplan semantic graphs, PathMapper, and K-HUKI.</p>
    </div>
  </a>

  <a href="06_System_Design_Benchmark_Pipeline.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Eval Pipeline Architecture</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">DPI-preserving rasterization, dual-blind SME annotation, Cohen's Kappa consensus scoring, and leakage filters.</p>
    </div>
  </a>

  <a href="07_Managerial_HR_and_Evaluation_Ethics.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">SOP Compliance &amp; HR</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Handling ambiguous client guidelines, fatigue mitigation, behavioral questions, and the 90-day PPO roadmap.</p>
    </div>
  </a>

  <a href="08_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Module 08</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid Recall CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">ISA-5.1 quick tables, circuit formulas, coordinate normalizations, KaTeX math, and the 10-point audit checklist.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s; height: 100%;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0284c7; text-transform: uppercase;">Study Roadmap</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Selection Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Day-by-day structured execution sprint from foundational symbology to mock interview defense.</p>
    </div>
  </a>

</div>
"""

# Render index.html
hub_html = render_innodata_page(
    title="Innodata India Prep Portal · Overview & Hub",
    active_page="index.html",
    content_html=index_html_content,
    prev_link=None,
    prev_title=None,
    next_link="00_START_HERE.html",
    next_title="00: Company & Role Intel"
)

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)
print("[+] Generated index.html")

md_compiler = markdown.Markdown(extensions=['tables', 'fenced_code', 'codehilite', 'toc'])

full_guide_parts = ["# Innodata India — Complete Interview Preparation Guide\n\n*Target Role: Industrial Technical Visual Reasoning Specialist (Subject Matter Expert)*\n*Batch 2027 • NIT Rourkela On-Campus Drive*\n\n---\n"]

# Render each module
for mod_key, mod_info in modules_data.items():
    md_filename = f"{mod_key}.md"
    html_filename = f"{mod_key}.html"
    
    # Save .md
    with open(os.path.join(BASE_DIR, md_filename), "w", encoding="utf-8") as f:
        f.write(mod_info["markdown"])
    print(f"[+] Generated {md_filename}")
    
    full_guide_parts.append(f"\n\n---\n\n{mod_info['markdown']}\n")
    
    # Convert md to html
    md_compiler.reset()
    body_html = md_compiler.convert(mod_info["markdown"])
    
    page_html = render_innodata_page(
        title=mod_info["title"],
        active_page=html_filename,
        content_html=body_html,
        prev_link=mod_info["prev_link"],
        prev_title=mod_info["prev_title"],
        next_link=mod_info["next_link"],
        next_title=mod_info["next_title"]
    )
    
    with open(os.path.join(BASE_DIR, html_filename), "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"[+] Generated {html_filename}")

# Generate consolidated guide
with open(os.path.join(BASE_DIR, "Innodata_India_Complete_Interview_Guide.md"), "w", encoding="utf-8") as f:
    f.write("".join(full_guide_parts))
print("[+] Generated Innodata_India_Complete_Interview_Guide.md")

print("\n[SUCCESS] All Innodata India Interview Preparation modules built successfully!")
