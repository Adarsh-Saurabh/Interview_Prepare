# components.py - Component Library for Fast Interview Study Material
# Conforms to instruction.md Part 4 specification

import html

def pills(items):
    """Render a list of (text, color) pills. Color: blue, emerald, amber, rose, purple, cyan, indigo, teal, orange."""
    if not items:
        return ""
    res = []
    for item in items:
        if isinstance(item, tuple) or isinstance(item, list):
            text, col = item[0], item[1]
        else:
            text, col = str(item), "blue"
        res.append(f'<span class="pill pill-{col}">{html.escape(str(text))}</span>')
    return "".join(res)

def section(anchor, title, body, pill=None, pill_color="blue", depth="sprint"):
    """
    Top-level content section. Emits id= matching a TOC anchor.
    depth: 'sprint' (shown in both modes) or 'deep' (shown only in Deep Dive).
    """
    pill_html = f'<span class="pill pill-{pill_color}">{html.escape(pill)}</span>' if pill else ''
    return f"""
<section class="section-block" id="{anchor}" data-depth="{depth}">
  <div class="section-header">
    <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
      <h2 class="section-title">
        <a href="#{anchor}" class="heading-anchor" title="Direct link to this section">#</a>
        {title}
      </h2>
      {pill_html}
    </div>
    <label class="section-progress-label">
      <input type="checkbox" class="section-check" data-anchor="{anchor}" onchange="toggleSectionDone('{anchor}', this.checked)">
      <span>Reviewed</span>
    </label>
  </div>
  <div class="section-body">
    {body}
  </div>
</section>
"""

def subsection(anchor, title, body="", depth="deep"):
    """h3-level block for nested TOC and deep-dive drills."""
    body_html = f'<div class="subsection-body">{body}</div>' if body else ''
    return f"""
<div class="subsection-block" id="{anchor}" data-depth="{depth}">
  <h3 class="subsection-title">
    <a href="#{anchor}" class="heading-anchor" title="Direct link">#</a>
    {title}
  </h3>
  {body_html}
</div>
"""

def table(headers, rows, depth="sprint", caption=None, row_depths=None):
    """
    Dense comparison table with optional caption and per-row depth support.
    headers: list of strings
    rows: list of lists of strings/HTML
    row_depths: optional list of strings ('sprint' or 'deep') matching len(rows)
    """
    th_html = "".join([f"<th>{h}</th>" for h in headers])
    tr_html = []
    for i, row in enumerate(rows):
        r_depth = f' data-depth="{row_depths[i]}"' if (row_depths and i < len(row_depths)) else ''
        tds = "".join([f"<td>{cell}</td>" for cell in row])
        tr_html.append(f"<tr{r_depth}>{tds}</tr>")
    
    caption_html = f'<div class="table-caption">{caption}</div>' if caption else ''
    return f"""
<div class="table-container" data-depth="{depth}">
  {caption_html}
  <table class="data-table">
    <thead>
      <tr>{th_html}</tr>
    </thead>
    <tbody>
      {"".join(tr_html)}
    </tbody>
  </table>
</div>
"""

def callout(title, body, kind="info", depth="sprint"):
    """
    Callout box.
    kind: info | trap | pro | hft | math | fde | ai | warn
    """
    icon_map = {
        "info": "💡",
        "trap": "⚠️ INTERVIEW TRAP",
        "pro": "⚡ PRO TIP",
        "hft": "🏎️ LOW-LATENCY / HFT",
        "math": "∑ MATHEMATICAL GROUNDING",
        "fde": "🧭 FDE CLIENT / OPERATIONAL",
        "ai": "🤖 MODERN AI NUANCE",
        "warn": "🚨 CRITICAL WARNING"
    }
    badge_label = icon_map.get(kind, kind.upper())
    return f"""
<div class="callout callout-{kind}" data-depth="{depth}">
  <div class="callout-title">
    <span class="callout-badge">{badge_label}</span>
    <span>{title}</span>
  </div>
  <div class="callout-body">
    {body}
  </div>
</div>
"""

def code(src, lang="python", title=None, depth="deep"):
    """Prism-highlighted code block with copy button and optional filename header."""
    header_html = f'<div class="code-title-bar"><span>📄 {html.escape(title)}</span><span class="code-lang-tag">{lang}</span></div>' if title else ''
    escaped_src = html.escape(src.strip())
    return f"""
<div class="code-block-wrapper" data-depth="{depth}">
  {header_html}
  <pre class="line-numbers"><code class="language-{lang}">{escaped_src}</code></pre>
</div>
"""

def svg_card(svg_markup, caption, depth="sprint"):
    """Diagram container with mobile pinch/fullscreen support."""
    return f"""
<div class="svg-diagram-card" data-depth="{depth}">
  <div class="svg-container" onclick="openSvgFullscreen(this)" title="Click to view full screen">
    {svg_markup}
  </div>
  <div class="diagram-caption">🔍 {caption}</div>
</div>
"""

def formula_box(katex_display, reading, symbols, meaning, depth="sprint"):
    """
    Renders KaTeX formula with plain-English reading, symbol dictionary mini-table, and practical takeaway.
    symbols: list of (symbol_str, definition_str)
    """
    sym_rows = "".join([f"<tr><td class='formula-sym'><code>{html.escape(s)}</code></td><td class='formula-def'>{d}</td></tr>" for s, d in symbols])
    return f"""
<div class="formula-box" data-depth="{depth}">
  <div class="formula-katex">{katex_display}</div>
  <div class="formula-reading"><strong>🗣️ Spoken Reading:</strong> <em>{reading}</em></div>
  <div class="formula-symbols-wrapper">
    <table class="formula-symbols-table">
      <thead>
        <tr><th>Symbol</th><th>Meaning & Units</th></tr>
      </thead>
      <tbody>
        {sym_rows}
      </tbody>
    </table>
  </div>
  <div class="formula-meaning"><strong>🎯 Practical System Takeaway:</strong> {meaning}</div>
</div>
"""

def worked_example(title, steps, answer, depth="deep"):
    """
    Numbered step-by-step worked numerical or architectural derivation.
    steps: list of (step_label, step_html)
    answer: final takeaway (revealed upon click)
    """
    steps_html = []
    for idx, (label, content) in enumerate(steps, 1):
        steps_html.append(f"""
        <div class="we-step">
          <div class="we-step-header">
            <span class="we-step-num">Step {idx}</span>
            <span class="we-step-label">{label}</span>
          </div>
          <div class="we-step-body">{content}</div>
        </div>
        """)
    return f"""
<div class="worked-example" data-depth="{depth}">
  <div class="we-header">
    <span class="we-badge">📐 WORKED PROBLEM</span>
    <h4 class="we-title">{title}</h4>
  </div>
  <div class="we-steps-list">
    {"".join(steps_html)}
  </div>
  <details class="we-answer-details">
    <summary class="we-answer-summary">👁️ Click to Reveal Final Verification & Answer</summary>
    <div class="we-answer-body">
      {answer}
    </div>
  </details>
</div>
"""

def flashcard(question, answer, tags=None, difficulty=None, companies=None, depth="sprint"):
    """
    Self-assessment flashcard with Got it / Shaky / No idea rating buttons for Spaced Repetition.
    """
    pills_html = []
    if difficulty:
        diff_color = {"Easy": "emerald", "Medium": "amber", "Hard": "rose", "Expert": "purple"}.get(difficulty, "blue")
        pills_html.append(f'<span class="pill pill-{diff_color}">{difficulty}</span>')
    if tags:
        for t in tags:
            pills_html.append(f'<span class="pill pill-cyan">{html.escape(t)}</span>')
    if companies:
        for c in companies:
            pills_html.append(f'<span class="pill pill-indigo">{html.escape(c)}</span>')
            
    header_pills = f'<div class="faq-pills">{"".join(pills_html)}</div>' if pills_html else ''
    q_hash = abs(hash(question)) % 1000000
    
    return f"""
<details class="faq-accordion" data-depth="{depth}" data-qid="{q_hash}">
  <summary class="faq-summary">
    <div class="faq-question-text">{question}</div>
    {header_pills}
  </summary>
  <div class="faq-answer">
    <div class="faq-answer-content">
      {answer}
    </div>
    <div class="rating-strip">
      <span class="rating-prompt">Rate Recall:</span>
      <button class="rating-btn btn-got-it" onclick="rateFlashcard('{q_hash}', 'got_it', this)" title="Solid comprehension - review in 14 days">✅ Got it</button>
      <button class="rating-btn btn-shaky" onclick="rateFlashcard('{q_hash}', 'shaky', this)" title="Fumbled or hesitant - review in 3 days">⚠️ Shaky</button>
      <button class="rating-btn btn-no-idea" onclick="rateFlashcard('{q_hash}', 'no_idea', this)" title="Blanked out - add to urgent review">❌ No idea</button>
    </div>
  </div>
</details>
"""

def followup_chain(root_question, chain, depth="deep"):
    """
    Follow-up chain drill ladder: models high-pressure interview drills.
    chain: list of (question, answer)
    """
    levels_html = []
    for idx, (q, a) in enumerate(chain, 1):
        levels_html.append(f"""
        <div class="fc-level">
          <div class="fc-connector">↳ Follow-Up Drill {idx}</div>
          <details class="fc-accordion">
            <summary class="fc-summary"><strong>Q:</strong> {q}</summary>
            <div class="fc-answer">{a}</div>
          </details>
        </div>
        """)
        
    return f"""
<div class="followup-chain" data-depth="{depth}">
  <div class="fc-header">
    <span class="fc-badge">🎯 INTERVIEW DRILL LADDER</span>
    <div class="fc-root-q"><strong>Root Question:</strong> {root_question}</div>
  </div>
  <div class="fc-levels-container">
    {"".join(levels_html)}
  </div>
</div>
"""

def decision_matrix(title, options, depth="sprint"):
    """
    Decision matrix for A vs B choices: options is list of (name, use_when, avoid_when).
    """
    rows = []
    for name, use_when, avoid_when in options:
        rows.append(f"""
        <tr>
          <td class="dm-name"><strong>{name}</strong></td>
          <td class="dm-use"><span class="badge-use">USE WHEN:</span> {use_when}</td>
          <td class="dm-avoid"><span class="badge-avoid">AVOID WHEN:</span> {avoid_when}</td>
        </tr>
        """)
    return f"""
<div class="decision-matrix-card" data-depth="{depth}">
  <div class="dm-title">⚖️ Decision Matrix: {title}</div>
  <div class="table-container">
    <table class="data-table dm-table">
      <thead>
        <tr><th>Option / Pattern</th><th>Prime Use-Cases (Best Choice)</th><th>Anti-Patterns / Failure Points</th></tr>
      </thead>
      <tbody>
        {"".join(rows)}
      </tbody>
    </table>
  </div>
</div>
"""

def anti_pattern(title, bad_code, good_code, failure_mode, lang="python", depth="deep"):
    """Side-by-side anti-pattern vs clean refactor."""
    return f"""
<div class="anti-pattern-card" data-depth="{depth}">
  <div class="ap-header">
    <span class="ap-badge">❌ ANTI-PATTERN vs ✅ PRODUCTION FIX</span>
    <h4 class="ap-title">{title}</h4>
  </div>
  <div class="ap-grid">
    <div class="ap-col ap-bad">
      <div class="ap-col-header">❌ Broken / Buggy / Anti-Pattern</div>
      <pre class="line-numbers"><code class="language-{lang}">{html.escape(bad_code.strip())}</code></pre>
    </div>
    <div class="ap-col ap-good">
      <div class="ap-col-header">✅ Safe / Correct / Idiomatic Fix</div>
      <pre class="line-numbers"><code class="language-{lang}">{html.escape(good_code.strip())}</code></pre>
    </div>
  </div>
  <div class="ap-failure-mode">
    <strong>⚠️ Failure Mode & Root Cause:</strong> {failure_mode}
  </div>
</div>
"""

def mnemonic(label, hook, expansion, depth="sprint"):
    """Compact memory hook."""
    return f"""
<div class="mnemonic-box" data-depth="{depth}">
  <div class="mnemonic-badge">🧠 MNEMONIC</div>
  <div class="mnemonic-hook"><strong>{label}:</strong> <span class="hook-text">{hook}</span></div>
  <div class="mnemonic-expansion">{expansion}</div>
</div>
"""

def numbers_card(title, rows, depth="sprint"):
    """Reference magnitudes: rows is list of (thing, number, note)."""
    tr_html = []
    for thing, num, note in rows:
        tr_html.append(f"""
        <tr>
          <td><strong>{thing}</strong></td>
          <td><span class="num-highlight">{num}</span></td>
          <td style="color: var(--text-secondary); font-size: 0.85rem;">{note}</td>
        </tr>
        """)
    return f"""
<div class="numbers-card" data-depth="{depth}">
  <div class="numbers-title">📊 Key Numbers to Know Cold: {title}</div>
  <div class="table-container">
    <table class="data-table">
      <thead>
        <tr><th>Operation / Quantity</th><th>Order of Magnitude</th><th>Engineering Implication</th></tr>
      </thead>
      <tbody>
        {"".join(tr_html)}
      </tbody>
    </table>
  </div>
</div>
"""

def one_liner(text, depth="sprint"):
    """Visually distinct 15-second spoken answer."""
    return f"""
<div class="one-liner-box" data-depth="{depth}">
  <div class="ol-badge">🗣️ 15-SECOND INTERVIEW ANSWER</div>
  <p class="ol-text">"{text}"</p>
</div>
"""

def see_also(links, depth="deep"):
    """Cross-module links: links is list of (module_file, anchor, label)."""
    pills = []
    for f, anc, lbl in links:
        href = f"{f}#{anc}" if anc else f
        pills.append(f'<a href="{href}" class="see-also-link">🔗 {lbl}</a>')
    return f"""
<div class="see-also-box" data-depth="{depth}">
  <span class="see-also-label">Connected Concepts (See Also):</span>
  <div class="see-also-links">{" ".join(pills)}</div>
</div>
"""
