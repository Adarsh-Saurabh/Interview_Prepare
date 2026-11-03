# build_all.py - Master Compiler for Study Material & Fast Interview Portal
# Conforms to instruction.md Phase 0, Part 1, 3, 4, 5

import os
import sys
import json
import re

# Ensure builder directory is in sys.path
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
STUDY_DIR = os.path.dirname(CUR_DIR)
sys.path.insert(0, CUR_DIR)

from shared_theme import MODULES_META, render_page, CSS_STYLES, JS_SCRIPTS

# All 23 Module Builders across 5 Tracks
import mod_dsa
import mod_os
import mod_dbms
import mod_cn
import mod_coa
import mod_concurrency
import mod_lld
import mod_system_design
import mod_api_security
import mod_cpp_systems
import mod_python
import mod_math_ml
import mod_ml_core
import mod_ml_cv
import mod_llm_internals
import mod_ai_agents
import mod_ai_evals
import mod_sql_data
import mod_linux_git
import mod_docker
import mod_fde_decomp
import mod_behavioral
import mod_quant

MODULE_BUILDERS = {
    # Track A: Core CS Fundamentals
    "dsa": mod_dsa,
    "os": mod_os,
    "dbms": mod_dbms,
    "cn": mod_cn,
    "coa": mod_coa,
    "concurrency": mod_concurrency,

    # Track B: Software Engineering & Design
    "lld": mod_lld,
    "system_design": mod_system_design,
    "api_security": mod_api_security,
    "cpp_systems": mod_cpp_systems,
    "python_internals": mod_python,

    # Track C: AI / Machine Learning
    "math_ml": mod_math_ml,
    "ml_core": mod_ml_core,
    "ml_cv": mod_ml_cv,
    "llm_internals": mod_llm_internals,
    "ai_agents": mod_ai_agents,
    "ai_evals": mod_ai_evals,

    # Track D: Data & Infrastructure
    "sql_data": mod_sql_data,
    "linux_git": mod_linux_git,
    "docker": mod_docker,

    # Track E: Role-Specific & Human
    "fde_decomp": mod_fde_decomp,
    "behavioral": mod_behavioral,
    "quant": mod_quant
}

TRACKS_CONFIG = [
    {"code": "A", "name": "Core CS Fundamentals", "icon": "💻", "desc": "Foundational computing systems: DSA, OS, DBMS, Networks, Architecture, Concurrency."},
    {"code": "B", "name": "Software Engineering & Design", "icon": "📐", "desc": "Production design: LLD, System Design, APIs & Auth, C++ Systems, Python Internals."},
    {"code": "C", "name": "AI / Machine Learning", "icon": "🧠", "desc": "Frontier AI & ML: Math for ML, ML Core, Vision/Signals, LLM Internals, RAG/Agents, AI Evals."},
    {"code": "D", "name": "Data & Infrastructure", "icon": "🛠️", "desc": "Operational engineering: SQL & Data Engineering, Linux & Git, Docker & Kubernetes."},
    {"code": "E", "name": "Role-Specific & Human", "icon": "🧭", "desc": "Interview loops: FDE Decomposition, Behavioral & STAR, Quantitative Aptitude & Puzzles."}
]

def build_index_html():
    total_modules = len(MODULES_META)
    
    # Group cards by Tracks (A through E)
    track_sections_html = ""
    for tr in TRACKS_CONFIG:
        track_mods = [m for m in MODULES_META if m["track"] == tr["code"]]
        if not track_mods:
            continue
            
        cards_html = ""
        for m in track_mods:
            companies_pills = "".join([f'<span class="pill pill-blue">{c}</span>' for c in m["companies"][:4]])
            highlights_li = "".join([f'<li>{h}</li>' for h in m["highlights"][:4]])
            roles_str = " ".join([r.lower() for r in m.get("roles", [])])
            tier_badge = m.get("tier", "P1")
            tier_color = "rose" if tier_badge == "P0" else "amber" if tier_badge == "P1" else "blue"
            
            # Check if built or in development
            is_built = m["id"] in MODULE_BUILDERS
            status_btn = f'<a href="{m["file"]}" class="card-btn">Open Module →</a>' if is_built else f'<span class="card-btn-disabled">In Development</span>'
            
            cards_html += f"""
            <div class="topic-card" data-topic="{m['id']}" data-track="{m['track']}" data-roles="{roles_str}" data-tier="{tier_badge}" data-tags="{m['title'].lower()} {' '.join(m['highlights']).lower()} {' '.join(m['companies']).lower()} {roles_str} {tier_badge.lower()}">
              <div class="card-top">
                <div class="card-icon">{m['icon']}</div>
                <div style="flex: 1;">
                  <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.5rem; flex-wrap: wrap;">
                    <div style="display: flex; gap: 0.35rem; align-items: center;">
                      <span class="pill pill-{m['badge_color']}">{m['badge']}</span>
                      <span class="pill pill-{tier_color}">{tier_badge}</span>
                    </div>
                    <span style="font-size: 0.75rem; color: var(--text-muted); font-weight: 600;">⏱️ {m['est_mins']} / {m.get('est_mins_deep', '60m')}</span>
                  </div>
                  <h3 class="card-title"><a href="{m['file']}">{m['title']}</a></h3>
                </div>
              </div>
              <p class="card-desc">{m['desc']}</p>
              
              <div style="margin: 0.75rem 0;">
                <div style="font-size: 0.7rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.35rem; letter-spacing: 0.05em;">Key Highlights:</div>
                <ul class="card-highlights">
                  {highlights_li}
                </ul>
              </div>

              <div style="margin-top: auto; padding-top: 0.85rem; border-top: 1px solid var(--border-color);">
                <div style="font-size: 0.7rem; color: var(--text-muted); font-weight: 600; margin-bottom: 0.4rem;">Target Companies:</div>
                <div class="meta-pills" style="margin-bottom: 0.85rem;">
                  {companies_pills}
                </div>
                
                <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.5rem;">
                  <label class="card-checkbox-label">
                    <input type="checkbox" class="topic-check" data-id="{m['id']}" onchange="toggleCardDone('{m['id']}', this.checked)">
                    <span>Reviewed</span>
                  </label>
                  {status_btn}
                </div>
              </div>
            </div>
            """
            
        track_sections_html += f"""
        <div class="track-group" data-track-group="{tr['code']}">
          <div class="track-header">
            <div style="display: flex; align-items: center; gap: 0.65rem;">
              <span class="track-icon">{tr['icon']}</span>
              <div>
                <h2 class="track-title">Track {tr['code']} — {tr['name']}</h2>
                <div class="track-desc">{tr['desc']}</div>
              </div>
            </div>
            <span class="track-count">{len(track_mods)} Modules</span>
          </div>
          <div class="cards-grid">
            {cards_html}
          </div>
        </div>
        """

    index_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>Study Material & Rapid Cheat Sheets · Adarsh Saurabh</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- KaTeX Formula Support (§1.2 Fix) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>

  <style>
{CSS_STYLES}

/* Dashboard & Track Layout */
.dashboard-hero {{
  background: linear-gradient(135deg, rgba(2, 132, 199, 0.12), rgba(99, 102, 241, 0.08), rgba(20, 184, 166, 0.08));
  border: 1px solid var(--border-color);
  border-radius: 1.25rem;
  padding: 2.25rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}}

.dashboard-hero::after {{
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, transparent 70%);
  pointer-events: none;
}}

.hero-main-title {{
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}}

.hero-main-sub {{
  color: var(--text-secondary);
  font-size: 1.05rem;
  max-width: 900px;
  line-height: 1.5;
  margin-bottom: 1.5rem;
}}

/* Study Presets Strip */
.presets-strip {{
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1rem 1.25rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-wrap: wrap;
}}

.presets-label {{
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--text-muted);
  letter-spacing: 0.05em;
}}

.preset-btn {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.35rem 0.75rem;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.15s ease;
}}

.preset-btn:hover, .preset-btn.active {{
  background: var(--accent-blue);
  color: #fff;
  border-color: var(--accent-blue);
}}

/* Track Groups */
.track-group {{
  margin-bottom: 3rem;
}}

.track-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.25rem;
  padding-bottom: 0.65rem;
  border-bottom: 2px solid var(--border-color);
}}

.track-icon {{
  font-size: 1.6rem;
}}

.track-title {{
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--text-primary);
}}

.track-desc {{
  font-size: 0.83rem;
  color: var(--text-muted);
}}

.track-count {{
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--accent-cyan);
  background: rgba(34, 211, 238, 0.1);
  padding: 0.2rem 0.6rem;
  border-radius: 9999px;
}}

/* Cards Grid */
.cards-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 1.5rem;
}}

@media (max-width: 640px) {{
  .cards-grid {{
    grid-template-columns: 1fr;
  }}
}}

.topic-card {{
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 1rem;
  padding: 1.4rem;
  display: flex;
  flex-direction: column;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
}}

.topic-card:hover {{
  border-color: var(--border-focus);
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}}

.card-top {{
  display: flex;
  gap: 0.85rem;
  margin-bottom: 0.85rem;
}}

.card-icon {{
  font-size: 1.8rem;
  width: 3.25rem;
  height: 3.25rem;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}

.card-title {{
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.3;
  margin-top: 0.25rem;
}}

.card-title a {{
  color: var(--text-primary);
  text-decoration: none;
}}

.card-title a:hover {{
  color: var(--accent-blue);
}}

.card-desc {{
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 0.75rem;
}}

.card-highlights {{
  list-style: none;
  font-size: 0.8rem;
  color: var(--text-secondary);
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}}

.card-highlights li {{
  position: relative;
  padding-left: 1rem;
}}

.card-highlights li::before {{
  content: '•';
  position: absolute;
  left: 0;
  color: var(--accent-cyan);
  font-weight: 800;
}}

.card-btn {{
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 700;
  padding: 0.4rem 0.8rem;
  border-radius: 0.5rem;
  transition: all 0.15s;
}}

.card-btn:hover {{
  background: var(--accent-blue);
  color: #fff;
  border-color: var(--accent-blue);
}}

.card-btn-disabled {{
  font-size: 0.75rem;
  color: var(--text-muted);
  background: var(--bg-card);
  padding: 0.35rem 0.65rem;
  border-radius: 0.5rem;
  border: 1px dashed var(--border-color);
}}

.card-checkbox-label {{
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.78rem;
  color: var(--text-muted);
  cursor: pointer;
  user-select: none;
}}

.done-card {{
  border-color: rgba(52, 211, 153, 0.4);
}}

.done-card::after {{
  content: '✓ REVIEWED';
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(52, 211, 153, 0.15);
  color: var(--accent-emerald);
  font-size: 0.65rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  padding: 0.15rem 0.45rem;
  border-radius: 0.35rem;
}}

/* Progress Tracker Bar */
.progress-card {{
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
  margin-bottom: 1.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
}}

.progress-info {{
  display: flex;
  align-items: center;
  gap: 1rem;
}}

.progress-text-title {{
  font-size: 1rem;
  font-weight: 700;
  color: var(--text-primary);
}}

.progress-text-sub {{
  font-size: 0.8rem;
  color: var(--text-muted);
}}

.progress-bar-wrapper {{
  flex: 1;
  min-width: 200px;
  max-width: 400px;
  background: var(--bg-card);
  border-radius: 9999px;
  height: 0.65rem;
  overflow: hidden;
  border: 1px solid var(--border-color);
}}

.progress-bar-fill {{
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-emerald));
  border-radius: 9999px;
  transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}}

/* Search & Filter Bar */
.search-controls {{
  margin-bottom: 1.75rem;
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}}

.search-input {{
  flex: 1;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  padding: 0.75rem 1.25rem;
  color: var(--text-primary);
  font-family: var(--font-sans);
  font-size: 0.95rem;
  outline: none;
  transition: all 0.2s;
}}

.search-input:focus {{
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.15);
}}

.role-chips {{
  display: flex;
  align-items: center;
  gap: 0.4rem;
}}

.role-chip {{
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.4rem 0.85rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.15s;
}}

.role-chip.active, .role-chip:hover {{
  background: var(--accent-blue);
  color: #fff;
  border-color: var(--accent-blue);
}}
  </style>
</head>
<body>

  <!-- Sticky Header -->
  <header>
    <div class="header-inner">
      <a href="index.html" class="brand">
        <span>⚡ PrepPortal</span>
        <span class="brand-badge">Master Suite</span>
      </a>
      <div class="header-actions">
        <a href="review.html" class="nav-btn" style="padding: 0.35rem 0.75rem; font-size: 0.8rem;">
          🎯 Weak-Topic Review
        </a>
        <a href="../0Interview%20Preparation/index.html" style="text-decoration: none; font-size: 0.82rem; color: var(--accent-cyan); font-weight: 600;">
          ← Company Portals
        </a>
        <button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()">☀️ Light</button>
      </div>
    </div>
  </header>

  <!-- Container -->
  <div class="app-container">
    
    <!-- Hero Banner -->
    <div class="dashboard-hero">
      <h1 class="hero-main-title">Fast Interview Study Material &amp; Cheat Sheets</h1>
      <p class="hero-main-sub">
        Comprehensive 15-Minute Sprint &amp; 60-Minute Deep Dive preparation suite featuring inline SVG mental models, first-principles architectures, complexity matrices, and 120+ verified interview flashcards. Curated for Adarsh Saurabh (NIT Rourkela) across SWE, AI/ML, and FDE tracks.
      </p>
      
      <div class="meta-pills">
        <span class="pill pill-blue">{total_modules} Modules</span>
        <span class="pill pill-purple">5 Tracks</span>
        <span class="pill pill-emerald">Dual-Mode: 15m Sprint / 60m Deep</span>
        <span class="pill pill-amber">Inline SVG Mental Models</span>
        <span class="pill pill-rose">KaTeX Formulas &amp; Worked Examples</span>
        <span class="pill pill-cyan">100% Offline Ready</span>
      </div>
    </div>

    <!-- Live Preparation Progress Bar (§1.1 Dynamic count) -->
    <div class="progress-card">
      <div class="progress-info">
        <div style="font-size: 1.75rem;">🎯</div>
        <div>
          <div class="progress-text-title" id="progressTitle">Preparation Progress: 0 of {total_modules} Modules Reviewed</div>
          <div class="progress-text-sub">Tick checkboxes on cards as you review to track your readiness.</div>
        </div>
      </div>
      <div class="progress-bar-wrapper">
        <div class="progress-bar-fill" id="progressBarFill"></div>
      </div>
    </div>

    <!-- Study Plan Presets Strip (§3.5.8) -->
    <div class="presets-strip">
      <span class="presets-label">⚡ Study Presets:</span>
      <button class="preset-btn" onclick="applyPreset('all')">Show All</button>
      <button class="preset-btn" onclick="applyPreset('cram')">🔥 48-Hour Cram (P0 Sprint)</button>
      <button class="preset-btn" onclick="applyPreset('fde')">🎯 FDE Loop</button>
      <button class="preset-btn" onclick="applyPreset('ai')">🤖 AI/ML Loop</button>
      <button class="preset-btn" onclick="applyPreset('swe')">💻 Core SWE Loop</button>
    </div>

    <!-- Search & Filter Controls -->
    <div class="search-controls">
      <input type="text" id="moduleSearchInput" class="search-input" placeholder="🔍 Search topics, concepts, or companies (e.g. 'Consistent Hashing', 'KV Cache', 'LRU', 'B+ Tree', 'Apple', 'Pace')..." oninput="filterCards()">
      <div class="role-chips">
        <button class="role-chip active" onclick="filterRole('all', this)">All Roles</button>
        <button class="role-chip" onclick="filterRole('swe', this)">SWE</button>
        <button class="role-chip" onclick="filterRole('ai', this)">AI / ML</button>
        <button class="role-chip" onclick="filterRole('fde', this)">FDE</button>
      </div>
    </div>

    <!-- Track Groups & Cards -->
    <div id="tracksContainer">
      {track_sections_html}
    </div>

  </div>

{JS_SCRIPTS}
<script>
let currentRoleFilter = 'all';

function initDashboardProgress() {{
  let doneCount = 0;
  const checks = document.querySelectorAll('.topic-check');
  checks.forEach(chk => {{
    const id = chk.getAttribute('data-id');
    const isDone = localStorage.getItem('module_done_' + id) === 'true';
    chk.checked = isDone;
    const card = chk.closest('.topic-card');
    if (isDone) {{
      card.classList.add('done-card');
      doneCount++;
    }} else {{
      card.classList.remove('done-card');
    }}
  }});
  updateProgressBar(doneCount, checks.length);
}}

function toggleCardDone(id, isChecked) {{
  localStorage.setItem('module_done_' + id, isChecked);
  const card = document.querySelector(`.topic-card[data-topic="${{id}}"]`);
  if (card) {{
    if (isChecked) card.classList.add('done-card');
    else card.classList.remove('done-card');
  }}
  const checks = document.querySelectorAll('.topic-check');
  let doneCount = 0;
  checks.forEach(c => {{ if (c.checked) doneCount++; }});
  updateProgressBar(doneCount, checks.length);
}}

function updateProgressBar(done, total) {{
  const fill = document.getElementById('progressBarFill');
  const title = document.getElementById('progressTitle');
  if (fill && title) {{
    const pct = total > 0 ? Math.round((done / total) * 100) : 0;
    fill.style.width = pct + '%';
    title.innerText = `Preparation Progress: ${{done}} of ${{total}} Modules Reviewed (${{pct}}%)`;
  }}
}}

function filterRole(role, btn) {{
  currentRoleFilter = role;
  document.querySelectorAll('.role-chip').forEach(c => c.classList.remove('active'));
  if (btn) btn.classList.add('active');
  filterCards();
}}

function filterCards() {{
  const query = document.getElementById('moduleSearchInput').value.toLowerCase().trim();
  const cards = document.querySelectorAll('.topic-card');
  
  cards.forEach(card => {{
    const tags = card.getAttribute('data-tags') || '';
    const roles = card.getAttribute('data-roles') || '';
    
    const matchesQuery = !query || tags.includes(query);
    const matchesRole = currentRoleFilter === 'all' || roles.includes(currentRoleFilter);
    
    if (matchesQuery && matchesRole) {{
      card.style.display = 'flex';
    }} else {{
      card.style.display = 'none';
    }}
  }});
}}

function applyPreset(preset) {{
  document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  
  const cards = document.querySelectorAll('.topic-card');
  if (preset === 'all') {{
    cards.forEach(c => c.style.display = 'flex');
    return;
  }}
  
  cards.forEach(card => {{
    const tier = card.getAttribute('data-tier');
    const roles = card.getAttribute('data-roles') || '';
    let show = false;
    
    if (preset === 'cram') {{
      show = (tier === 'P0');
    }} else if (preset === 'fde') {{
      show = roles.includes('fde');
    }} else if (preset === 'ai') {{
      show = roles.includes('ai');
    }} else if (preset === 'swe') {{
      show = roles.includes('swe');
    }}
    
    card.style.display = show ? 'flex' : 'none';
  }});
}}

document.addEventListener('DOMContentLoaded', () => {{
  initDashboardProgress();
}});
</script>
</body>
</html>
"""
    return index_html

def build_review_html():
    """Generates review.html for weak-topic spaced repetition review (§3.3c)."""
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Weak-Topic Review Queue · Study Material</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
{CSS_STYLES}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="index.html" class="brand">
        <span>⚡ PrepPortal</span>
        <span class="brand-badge">Review Queue</span>
      </a>
      <div class="header-actions">
        <a href="index.html" class="nav-btn" style="padding: 0.35rem 0.75rem; font-size: 0.8rem;">← Back to Hub</a>
        <button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()">☀️ Light</button>
      </div>
    </div>
  </header>

  <div class="app-container">
    <div class="dashboard-hero">
      <h1 class="hero-main-title">🎯 Spaced Repetition Review Queue</h1>
      <p class="hero-main-sub">
        This queue aggregates all flashcards and interview questions marked <strong>⚠️ Shaky</strong> or <strong>❌ No idea</strong> across all modules. Questions resurface according to their urgency for night-before recall.
      </p>
    </div>

    <div class="progress-card">
      <div class="progress-info">
        <div style="font-size: 1.75rem;">📚</div>
        <div>
          <div class="progress-text-title" id="queueSummaryTitle">Active Review Items</div>
          <div class="progress-text-sub" id="queueSummarySub">Loading stored ratings from your local browser session...</div>
        </div>
      </div>
      <button class="nav-btn" onclick="clearReviewQueue()" style="font-size: 0.8rem;">Clear Queue 🗑️</button>
    </div>

    <div id="reviewItemsContainer" style="margin-top: 2rem;">
      <div style="text-align: center; color: var(--text-muted); padding: 3rem;">
        No weak topics currently queued! As you review modules and click <strong>⚠️ Shaky</strong> or <strong>❌ No idea</strong>, cards will automatically collect here.
      </div>
    </div>
  </div>

{JS_SCRIPTS}
<script>
function loadReviewQueue() {{
  const queue = JSON.parse(localStorage.getItem('study_review_queue') || '{{}}');
  const count = Object.keys(queue).length;
  const title = document.getElementById('queueSummaryTitle');
  const sub = document.getElementById('queueSummarySub');
  
  if (title) title.innerText = `${{count}} Questions Flagged for Review`;
  if (sub) sub.innerText = count > 0 ? 'Work through these flashcards until confidence is achieved.' : 'All reviewed topics are marked solid.';
}}

function clearReviewQueue() {{
  if (confirm('Reset your weak-topic review queue?')) {{
    localStorage.removeItem('study_review_queue');
    loadReviewQueue();
    location.reload();
  }}
}}

document.addEventListener('DOMContentLoaded', loadReviewQueue);
</script>
</body>
</html>
"""

def main():
    print("Building Study Material Portal...")
    os.makedirs(STUDY_DIR, exist_ok=True)
    
    search_index = []
    
    # 1. Build Available Modular Pages
    n = len(MODULES_META)
    for i, m in enumerate(MODULES_META):
        mod_id = m["id"]
        builder = MODULE_BUILDERS.get(mod_id)
        if not builder:
            # Not yet built in this phase
            continue
            
        res = builder.get_content()
        if isinstance(res, dict):
            toc = res["toc"]
            content = res["content"]
        else:
            toc, content = res
        
        # Determine previous and next links
        prev_m = MODULES_META[i-1] if i > 0 else None
        next_m = MODULES_META[i+1] if i < n-1 else None
        
        prev_link = prev_m["file"] if prev_m else None
        prev_title = prev_m["short_title"] if prev_m else None
        next_link = next_m["file"] if next_m else None
        next_title = next_m["short_title"] if next_m else None
        
        page_html = render_page(
            module_id=mod_id,
            page_title=m["title"],
            toc_items=toc,
            content_html=content,
            prev_link=prev_link,
            prev_title=prev_title,
            next_link=next_link,
            next_title=next_title
        )
        
        out_path = os.path.join(STUDY_DIR, m["file"])
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"  [OK] Generated: {m['file']} ({len(page_html):,} bytes)")
        
        # Index sections for global search (§4.4)
        for anchor, label in toc:
            search_index.append({
                "module_id": mod_id,
                "module_title": m["title"],
                "file": m["file"],
                "anchor": anchor,
                "label": label
            })

    # 2. Build index.html
    index_html = build_index_html()
    index_path = os.path.join(STUDY_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"  [OK] Generated: index.html ({len(index_html):,} bytes)")

    # 3. Build review.html (§3.3c)
    review_html = build_review_html()
    review_path = os.path.join(STUDY_DIR, "review.html")
    with open(review_path, "w", encoding="utf-8") as f:
        f.write(review_html)
    print(f"  [OK] Generated: review.html ({len(review_html):,} bytes)")

    # 4. Emit search_index.json (§4.4)
    search_path = os.path.join(STUDY_DIR, "search_index.json")
    with open(search_path, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2)
    print(f"  [OK] Generated: search_index.json ({len(search_index)} sections indexed)")

    print(f"\nSUCCESS: Study Material portal built cleanly ({len(MODULE_BUILDERS)} modules active, {len(MODULES_META)} registered)!")

if __name__ == "__main__":
    main()
