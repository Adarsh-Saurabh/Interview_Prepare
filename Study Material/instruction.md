# 📘 instruction.md — Master Rebuild Specification

**Target:** `C:\Users\adars\Desktop\Resume\Study Material\`
**Candidate:** Adarsh Saurabh — M.Tech Signal Processing, NIT Rourkela (Batch 2027) + B.Tech CSE
**Target roles:** AI/ML Engineer · SWE (Core CS) · Forward Deployed Engineer (FDE)
**Spec date:** 13 Oct 2026
**Status:** Authoritative. Rebuild modules one at a time against this document.

---

## 0. How To Use This Document

This file is the **single source of truth** for rebuilding the Study Material portal. It is written so you can open one module brief, rebuild that module, tick it off, and move on — without re-deriving decisions.

Read in this order:

| Part | What it gives you | Read when |
| :-- | :-- | :-- |
| **Part 1** | Blocking bugs in the current build | Before touching anything |
| **Part 2** | The Dual-Mode content model (15-min Sprint + 60-min Deep) | Before writing any content |
| **Part 3** | Website / UX redesign spec — navigation + learning system | Before editing `shared_theme.py` |
| **Part 4** | Component library you must build (Python helpers + new CSS) | While editing `shared_theme.py` |
| **Part 5** | Full module roster — 23 modules in 5 tracks, with priority order | To plan your sequence |
| **Part 6** | Per-module rewrite briefs for the 12 existing modules | One per sitting |
| **Part 7** | Specs for the 11 new modules | One per sitting |
| **Part 8** | Definition of Done + build workflow | Every time you finish a module |
| **Part 9** | Research appendix — verbatim interview questions + sources | While writing Q&A sections |

**Non-negotiable rule:** every claim you write must be *checkable*. No invented benchmarks, no fake latency numbers, no "studies show". If you state a number (cache latency, token overhead, parameter count), it must be a real, citable figure or explicitly marked as an order-of-magnitude estimate.

---

## 1. Blocking Bugs In The Current Build

Fix these **first**. They are factual defects, not style preferences.

### 1.1 Hardcoded module count is wrong

`builder/build_all.py` hardcodes `9` in two places while 12 modules exist:

- Line ~377: `<span class="pill pill-blue">9 Full Modules</span>`
- Line ~390: `Preparation Progress: 0 of 9 Modules Completed`

**Fix:** derive from `len(MODULES_META)`. The progress JS already computes `checks.length` correctly — only the static strings are stale.

### 1.2 KaTeX is advertised but never loaded

`README.md` line 17 claims *"KaTeX math rendering"*. `shared_theme.py` `render_page()` loads **only** PrismJS. There is no KaTeX CSS or JS anywhere. Every formula in the site is currently rendering as plain text or hand-built HTML.

**Fix:** add to `<head>` in `render_page()` **and** `build_index_html()`:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>
```

And in `JS_SCRIPTS` `DOMContentLoaded`:

```js
if (window.renderMathInElement) {
  renderMathInElement(document.body, {
    delimiters: [
      {left: '$$', right: '$$', display: true},
      {left: '$', right: '$', display: false},
      {left: '\\[', right: '\\]', display: true},
      {left: '\\(', right: '\\)', display: false}
    ],
    throwOnError: false
  });
}
```

This is a prerequisite for the Math Foundations, LLM Internals, ML Core, and Quant modules — do not start those until KaTeX works.

### 1.3 Four pill colour classes are used but never defined

`CSS_STYLES` defines only `.pill-blue`, `.pill-emerald`, `.pill-amber`, `.pill-rose`, `.pill-purple`.

Used in the wild but **undefined** (silently falling back to grey):

| Class | Used by |
| :-- | :-- |
| `.pill-cyan` | `mod_docker.py` |
| `.pill-indigo` | `mod_cpp_systems.py` |
| `.pill-teal` | `mod_dbms.py` |
| `.pill-orange` | `mod_ml_cv.py` |

Same problem for `badge_color` values `cyan` / `indigo` / `teal` / `orange` in `MODULES_META` → dashboard cards render grey badges.

**Fix:** define all nine, matching the existing pattern:

```css
.pill-cyan    { background: rgba(34, 211, 238, 0.12);  color: var(--accent-cyan);    border-color: rgba(34, 211, 238, 0.3); }
.pill-indigo  { background: rgba(129, 140, 248, 0.12); color: var(--accent-indigo);  border-color: rgba(129, 140, 248, 0.3); }
.pill-teal    { background: rgba(45, 212, 191, 0.12);  color: var(--accent-teal);    border-color: rgba(45, 212, 191, 0.3); }
.pill-orange  { background: rgba(251, 146, 60, 0.12);  color: var(--accent-orange);  border-color: rgba(251, 146, 60, 0.3); }
```

### 1.4 `MODULES_META` promises artifacts that do not exist

Every one of these is a broken promise shown on the dashboard card:

| Module | Promised in `highlights` / `desc` | Reality |
| :-- | :-- | :-- |
| `cpp_systems` | "Shared_ptr Control Block SVG" | **Missing** — only the vtable SVG exists |
| `cpp_systems` | "Lock-Free SPSC Ring Buffer" | **Missing** — no such code block |
| `cpp_systems` | "RAII & Rule of 5", "Forwarding" | Rule of 5 exists; **RAII never defined**, `std::forward` / perfect forwarding **never explained** |
| `dbms` | "WAL Recovery & Checkpoint SVG" | **Missing** — only the B+ tree SVG exists |
| `dbms` | "B+ Tree Indexing **vs LSM Trees**" | **LSM trees never mentioned** |
| `dbms` | "Query Execution Pipeline" | **Missing** |
| `lld` | "Factory vs Strategy Pattern Decision Flow" SVG | **Missing** — only the LRU UML exists |
| `lld` | "GoF **23** Design Patterns Matrix" | Table has **8 rows** |
| `lld` | "Rate Limiter LLD" | **Missing** |
| `lld` | "Thread-Safe Double-Checked Lock" | Only the **broken** version is shown; no working fix |
| `docker` | "Top 15 CLI Commands" | Table has **5 rows**, heading says "Top 12" |
| `ai_agents` | "IVF-PQ" indexing | **Missing** — only HNSW covered |
| `ml_cv` | "Embeddings & Metrics" | Embeddings/metric learning **never covered** |
| `README.md` | "120+ Flashcard Q&A" | Actual total: **75** |

**Rule going forward:** `MODULES_META` is a contract. If you remove an artifact, remove the claim. If you claim it, build it.

### 1.5 Zero authoring abstraction

`shared_theme.py` exports exactly one function — `render_page()`. There are **no** helpers: no `callout()`, no `flashcard()`, no `table()`, no `svg_card()`. Every module hand-writes raw HTML strings with literal class names.

Consequences already visible: the first 9 modules use `f"""` (requiring `{{`/`}}` brace escaping, a constant bug source), the last 3 switched to `r"""`. Class names are typo-prone (hence §1.3). Flashcard counts drifted 5 → 10.

**Fix:** build the component library in **Part 4** before rewriting content. This is the highest-leverage change in this entire document — it makes every subsequent module faster and consistent.

### 1.6 Mobile navigation is effectively broken

`.content-wrapper` collapses `280px 1fr` → `1fr` at `≤1024px`. The sticky sidebar TOC therefore becomes a **full-width block dumped above the content**, so on a phone you scroll past the entire table of contents before reaching the hero card. There is no drawer, no bottom nav, no back-to-top.

Your `0Interview Preparation/` portals already solve this (hamburger drawer + fixed bottom bar per `AGENTS.md` §5). Port that pattern here — spec in **Part 3.4**.

---

## 2. The Dual-Mode Content Model

### 2.1 The core decision

You asked for 1-hour depth **while keeping** the 15-minute version as a quick-review system. Do **not** create two separate files per subject — that doubles maintenance and the two copies will drift.

Instead: **one file per module, two depth tiers, toggled at runtime.**

```
┌─────────────────────────────────────────────────────────┐
│  ⚡ SPRINT (12-15 min)        🧠 DEEP DIVE (60 min)      │  ← header toggle
└─────────────────────────────────────────────────────────┘
         │                              │
         ▼                              ▼
  Everything marked              Everything, including
  data-depth="sprint"            data-depth="deep"
  (tables, SVGs, traps,          (derivations, worked
   10 core Q&A)                   numericals, code,
                                  30+ Q&A, follow-ups)
```

### 2.2 Mechanism

Every block gets a depth attribute. CSS hides what the current mode excludes.

```html
<!-- Shown in both modes -->
<section class="section-block" data-depth="sprint">...</section>

<!-- Shown only in Deep Dive -->
<section class="section-block" data-depth="deep">...</section>
```

```css
html[data-mode="sprint"] [data-depth="deep"] { display: none !important; }
```

Persist the choice in `localStorage` under `study_mode`, default `sprint`. Toggle lives in the sticky header next to the theme button.

**Critical detail:** depth filtering must also apply *inside* sections — individual table rows, flashcards, and paragraphs. So `data-depth` must be respected on `<tr>`, `<details>`, `<div>`, and `<p>` too, not just `<section>`. The CSS selector above already handles this.

### 2.3 What belongs in each tier

| | **Sprint tier** (`data-depth="sprint"`) | **Deep tier** (`data-depth="deep"`) |
| :-- | :-- | :-- |
| **Purpose** | Night-before recall. You already know it; you're reloading it. | Read-once comprehension. Builds the model from its reasons. |
| **Budget** | 12–15 min | +45 min (60 min total) |
| **Comparison tables** | 4–6 (the decision-making ones) | 10–18 total |
| **SVG diagrams** | 1–2 (the one mental model that matters) | 4–6 total |
| **Formulas** | Stated, boxed, no derivation | Derived or justified in 2–4 lines |
| **Code** | 0–2 snippets, ≤15 lines each | 10–15 snippets, full implementations |
| **Worked numericals** | 0 | 5–8 with step-by-step reveal |
| **Traps** | 3–5 one-liners | 10–15 with the *why* |
| **Q&A flashcards** | 10 (highest-frequency only) | 30–35 total |
| **Follow-up chains** | — | 1 per major topic (see §2.5) |
| **Cross-links** | — | "See also" to related modules |

### 2.4 Depth style: "Dense Reference, First-Principles Anchored"

You chose **dense reference expansion**, not a from-zero textbook. The resolution that makes "read it once and understand" actually work:

> Every concept gets **one** sentence establishing *why it exists / what problem it solves*, then goes straight to dense reference depth.

**Bad (too shallow — current site):**
> *MESI has 4 states: Modified, Exclusive, Shared, Invalid.*

**Bad (textbook bloat — do not do this):**
> *Before we discuss cache coherence, let us first consider what a cache is. A cache is a small, fast memory... [600 words]*

**Correct (dense + anchored):**
> *MESI exists because once each core has a private L1, two cores can hold the same line and silently disagree. The protocol makes every line's sharing status explicit so a write can invalidate the others before it lands.*
> *States: **M** — dirty, this core only, memory stale. **E** — clean, this core only, memory current (lets you upgrade M without a bus transaction). **S** — clean, ≥2 cores. **I** — stale.*
> *Transition that matters in interviews: a write to an `S` line issues RFO (Read-For-Ownership) → all other copies → `I` → this copy → `M`. Two cores alternately writing the same line therefore ping-pong RFOs at ~L3 latency per write. That is false sharing, and `alignas(64)` fixes it by guaranteeing the two variables never share a line.*

One anchor sentence, then full density, then the interview-relevant consequence. That's the target register for every Deep-tier paragraph.

### 2.5 Follow-up chains (new, Deep tier only)

Real interviews are not flat Q&A — they drill. The research is unambiguous that all three target tracks score *narrated reasoning under pressure* above correct one-shot answers. So model the drill explicitly.

Component: `followup_chain()`. Renders as a vertical sequence of progressively harder questions with collapsible answers.

```
Q:  What's the time complexity of your LRU get()?
└─ Q: O(1) — why does the hash map alone not give you that?
   └─ Q: Now make it thread-safe. What breaks first?
      └─ Q: Your single mutex is now the bottleneck. Shard it. How many shards?
         └─ Q: Sharding broke exact-LRU eviction. Is that acceptable? Defend it.
```

Put one chain on each module's 2–4 highest-value topics. This is the single most interview-realistic component on the site.

---

## 3. Website / UX Redesign Spec

Your ask: *"help me better navigate and understand the things better learn."* Three separate problems — navigation, comprehension, retention. Spec'd separately below.

### 3.1 Navigation fixes (priority order)

| # | Feature | Why | Where |
| :-: | :-- | :-- | :-- |
| 1 | **Scroll-spy TOC** — highlight the section you're currently in | Right now the 280px sidebar is a static link list; in a 60-min module you lose your place constantly | `JS_SCRIPTS` + `.toc-link.active` CSS |
| 2 | **Reading progress bar** — 3px fixed bar under the header | Tells you how much of a 60-min module is left. Essential once modules are 4× longer | `JS_SCRIPTS` scroll listener |
| 3 | **Nested TOC (h2 → h3)** | Deep tier has 8–14 sections with subsections. A flat 5-item TOC is useless at that length | `render_page()` — accept `toc_items` as `(anchor, label, children)` |
| 4 | **Mobile drawer + bottom nav** | §1.6 — mobile is currently broken | New CSS + JS, port from `0Interview Preparation/` |
| 5 | **Global cross-module search** | Current search is index-only and matches card metadata, not content. You cannot find "MESI" or "KV cache" from anywhere | Build `search_index.json` at compile time; add `Ctrl+K` palette |
| 6 | **Keyboard shortcuts** | `/` focus search · `Ctrl+K` palette · `j`/`k` next/prev section · `t` theme · `m` mode · `?` help | `JS_SCRIPTS` |
| 7 | **Back-to-top FAB** | Appears after 600px scroll | CSS + JS |
| 8 | **Prev/Next respecting track order** | Currently follows raw `MODULES_META` order. With 23 modules in 5 tracks, sequence should follow the track | `build_all.py` |
| 9 | **Anchor-link icons on headings** | So you can deep-link a specific concept into your own notes | `section_block()` helper |
| 10 | **Breadcrumb** `Hub › Track › Module` | Orientation across 23 modules | `render_page()` |

### 3.2 Comprehension aids (new components)

These are the "understand it better" half of the ask.

| Component | What it does | Used for |
| :-- | :-- | :-- |
| **`formula_box()`** | KaTeX formula + plain-English reading + every symbol defined in a mini-table + "what it means in practice" | Every formula on the site. The #1 reason people bounce off ML/COA/Quant content is undefined symbols |
| **`worked_example()`** | Numbered steps, each collapsible, with the answer hidden until clicked | Cache bits, subnetting, Banker's algorithm, Gantt charts, TF-IDF, attention shapes, capacity estimation |
| **`decision_matrix()`** | "Use X when… / Use Y when… / Never use either when…" 3-column table | Every A-vs-B topic. Interviews test *selection*, not recitation |
| **`anti_pattern()`** | Side-by-side ❌ broken code / ✅ fixed code with the failure mode named | SOLID, C++ UB, Python traps, SQL traps |
| **`mnemonic()`** | Compact memory hook | Coffman conditions, SOLID, OSI layers, ACID, CAP |
| **`numbers_card()`** | The reference magnitudes for a domain | Latency ladder, LLM token costs, QPS/storage estimates |
| **`compare_svg()`** | Two architectures side by side in one SVG | VM vs container, MHA vs GQA, B+ vs LSM |
| **`see_also()`** | Cross-module links | Connect false sharing (COA) ↔ atomics (C++) ↔ GIL (Python) |
| **`one_liner()`** | The 15-second spoken answer, visually distinct | Every major concept. You will be asked to be concise — practice the concise version |

### 3.3 Retention system (new)

Reading once is not retention. Add these.

**a) Per-section progress, not per-module.**
Current: one `module_done_<id>` boolean. With 60-min modules that's too coarse. Move to per-section checkboxes writing `sect_<module>_<anchor>`, and compute module % from them. Dashboard shows real partial progress.

**b) Self-test mode.**
A third header toggle: `🎓 Test Mode`. When on, all `<details class="faq-accordion">` are force-collapsed, answers unrevealable until clicked, and each card gets **Got it / Shaky / No idea** buttons writing to `localStorage`.

**c) Weak-topic review queue.**
Everything marked *Shaky* or *No idea* collects into `review.html` — a single page that pulls those flashcards from across all 23 modules. This is the highest-value feature on the site for actual exam outcomes.

**d) Spaced-repetition surfacing.**
Store a timestamp with each rating. On the dashboard, show a "Due for review" strip: *Shaky* resurfaces after 3 days, *Got it* after 14. No complex SM-2 algorithm needed — two intervals is enough.

**e) Last-visited resume.**
Store `last_module` + scroll offset. Dashboard shows *"Resume: C++ Internals — 40% through"*.

**f) Anki export.**
One button on `index.html`: dump all flashcards as TSV (`question<TAB>answer`) for Anki/Quizlet import. ~20 lines of JS, lets you use dead time on your phone.

### 3.4 Mobile spec (port from `0Interview Preparation/`)

Per `AGENTS.md` §5.4, your company portals already have the right pattern. Replicate exactly:

- Responsive viewport meta (already present ✓)
- **Slide-out drawer** with `☰ Sections` hamburger — the sidebar TOC becomes the drawer at `≤1024px`
- **Fixed bottom nav bar**: `🏠 Hub` · `📑 Sections` · `⚡ Sprint/Deep` · `🌙 Theme` · `↑ Top`
- Horizontal touch-scroll for tables (`.table-container` already does this ✓), code blocks, and KaTeX display math
- Minimum tap target 44×44px on all nav controls
- `svg` wrapper must allow pinch-zoom on diagrams — a 860px-wide SVG is unreadable on a 390px phone. Add a tap-to-fullscreen handler on `.svg-diagram-card`

### 3.5 Dashboard (`index.html`) redesign

Current: flat 12-card grid. At 23 modules a flat grid is unusable.

Required changes:

1. **Group cards by the 5 tracks** (Part 5) with collapsible track headers
2. **Role filter chips**: `All` · `AI/ML` · `SWE` · `FDE` — each module declares a `roles` list in `MODULES_META`; chips filter the grid. This directly serves the three-track ask
3. **Priority tier badges** — `P0 Must` / `P1 High` / `P2 Depth` from Part 5
4. **Two progress bars** per card — Sprint done / Deep done
5. **Search across content**, not just card metadata (needs `search_index.json` from §3.1.6)
6. **"Due for review" strip** at the top (§3.3d)
7. **"Resume where you left off"** card (§3.3e)
8. **Study plan presets** — buttons that highlight a subset in order:
   - `🔥 48-Hour Cram` → the P0 Sprint tiers only
   - `📅 2-Week Plan` → P0+P1 Deep
   - `🎯 FDE Loop` → decomposition, SQL/data, behavioral, DSA, API design
   - `🤖 AI Loop` → math, ML core, LLM internals, RAG/agents, evals
   - `💻 SWE Loop` → DSA, OS, DBMS, CN, LLD, HLD, concurrency
9. Fix the hardcoded `9` (§1.1)

---

## 4. Component Library To Build

Build this **before** rewriting content. Create `builder/components.py`, import into every module. This replaces hand-written HTML strings.

### 4.1 Required Python helpers

```python
# builder/components.py

def section(anchor, title, body, pill=None, pill_color="blue", depth="sprint"):
    """Top-level content section. Emits id= matching a TOC anchor."""

def subsection(anchor, title, body, depth="deep"):
    """h3-level block for nested TOC."""

def table(headers, rows, depth="sprint", caption=None, row_depths=None):
    """Dense comparison table. row_depths lets individual rows be deep-only."""

def callout(title, body, kind="info", depth="sprint"):
    """kind: info | trap | pro | hft | math | fde | ai | warn"""

def code(src, lang="python", title=None, depth="deep"):
    """Prism-highlighted block with copy button and optional filename header."""

def svg_card(svg_markup, caption, depth="sprint"):
    """Diagram container. Adds tap-to-fullscreen on mobile."""

def formula_box(katex, reading, symbols, meaning, depth="sprint"):
    """symbols: list[(symbol, definition)] -> rendered as a mini-table."""

def worked_example(title, steps, answer, depth="deep"):
    """steps: list[(step_label, step_html)]. Answer hidden until clicked."""

def flashcard(question, answer, tags=None, difficulty=None,
              companies=None, depth="sprint"):
    """<details class="faq-accordion"> + Got it/Shaky/No idea rating buttons."""

def followup_chain(root_question, chain, depth="deep"):
    """chain: list[(question, answer)] rendered as a nested drill ladder."""

def decision_matrix(title, options, depth="sprint"):
    """options: list[(name, use_when, avoid_when)]."""

def anti_pattern(title, bad_code, good_code, failure_mode,
                 lang="python", depth="deep"):
    """Side-by-side broken vs fixed."""

def mnemonic(label, hook, expansion, depth="sprint"):
    """Compact memory device."""

def numbers_card(title, rows, depth="sprint"):
    """Reference magnitudes. rows: list[(thing, number, note)]."""

def one_liner(text, depth="sprint"):
    """The 15-second spoken answer. Visually distinct from body prose."""

def see_also(links, depth="deep"):
    """links: list[(module_file, anchor, label)]."""

def pills(items):
    """items: list[(text, color)]."""
```

### 4.2 New CSS classes needed

Add to `CSS_STYLES`:

```
.pill-cyan .pill-indigo .pill-teal .pill-orange     /* §1.3 fix */
.callout-math .callout-fde .callout-ai .callout-warn /* new kinds */
.formula-box .formula-katex .formula-reading
  .formula-symbols .formula-meaning
.worked-example .we-step .we-step-label .we-answer
.decision-matrix
.anti-pattern .ap-bad .ap-good .ap-failure
.mnemonic .mnemonic-hook
.numbers-card
.one-liner
.see-also
.followup-chain .fc-level .fc-connector
.toc-link.active .toc-sublist .toc-sublink
.reading-progress
.mode-toggle .mode-toggle-btn.active
.mobile-drawer .drawer-overlay .hamburger-btn
.bottom-nav .bottom-nav-item
.back-to-top
.rating-buttons .rating-btn[data-rating]
.section-progress-check
.heading-anchor
.breadcrumb
.track-group .track-header
.role-chips .role-chip.active
.search-palette .sp-input .sp-results .sp-result-item
.svg-fullscreen-overlay
@media print { ... }   /* clean PDF export of any module */
```

### 4.3 New JS functions needed

Add to `JS_SCRIPTS`:

```js
initMode()            toggleMode()           // Sprint / Deep
initTestMode()        toggleTestMode()       // self-test
initScrollSpy()                              // active TOC
initReadingProgress()                        // top bar
initSectionProgress(moduleId)                // per-section checkboxes
initRatings(moduleId)                        // Got it / Shaky / No idea
initDrawer()                                 // mobile
initBackToTop()
initKeyboardShortcuts()
initSearchPalette()                          // Ctrl+K, reads search_index.json
initSvgFullscreen()
initKatex()                                  // §1.2
exportAnki()                                 // dashboard button
getReviewQueue()                             // powers review.html
```

### 4.4 Build-time additions to `build_all.py`

1. Emit `search_index.json` — `[{module, file, anchor, heading, text, depth}]` for every section. Powers §3.1.5.
2. Emit `review.html` — the weak-topic queue page (§3.3c). Static shell; JS populates from `localStorage` + `search_index.json`.
3. Validate `MODULES_META` contract — assert every `highlights` entry has a matching artifact marker in the generated HTML. Fail the build if a promise is unmet (prevents §1.4 recurring).
4. Validate TOC anchors — assert every `toc_items` anchor exists as an `id=` in the content. Fail loudly otherwise.
5. Count and report flashcards per module so `README.md` totals stay honest.

---

## 5. Full Module Roster — 23 Modules, 5 Tracks

12 existing (rewritten) + 11 new. Each module targets **15 min Sprint / 60 min Deep**.

### Priority tiers

- **P0 (Must)** — appears in essentially every loop for at least one target role. Build first.
- **P1 (High)** — role-specific but high frequency within that role.
- **P2 (Depth)** — differentiators and under-prepared edges.

### Track A — Core CS Fundamentals (6)

| # | ID | Module | Status | Tier | Roles |
| :-: | :-- | :-- | :-- | :-: | :-- |
| 1 | `dsa` | Data Structures & Algorithms | **Rewrite** | **P0** | SWE · FDE · AI |
| 2 | `os` | Operating Systems | **Rewrite** | **P0** | SWE · AI |
| 3 | `dbms` | DBMS & Storage Internals | **Rewrite** | **P0** | SWE · FDE |
| 4 | `cn` | Computer Networks | **Rewrite** | P1 | SWE |
| 5 | `coa` | Computer Organization & Architecture | **Rewrite** | P1 | SWE (hardware) |
| 6 | `concurrency` | **Concurrency & Parallelism** | **NEW** | **P0** | SWE · AI |

> **Why `concurrency` is new and P0:** currently split across `os` / `cpp_systems` / `python_internals` with no single coherent treatment. Research shows Anthropic threads concurrency through *multiple* rounds (not one isolated question), OpenAI lists coroutines as a named focus area, and LLD interviews increasingly carry a separate concurrency round (Print FooBar, Building H2O, thread-safe cache with TTL, concurrent hashmap). It needs one home.

### Track B — Software Engineering & Design (5)

| # | ID | Module | Status | Tier | Roles |
| :-: | :-- | :-- | :-- | :-- | :-- |
| 7 | `lld` | Low-Level Design & Design Patterns | **Rewrite** | **P0** | SWE · FDE |
| 8 | `system_design` | System Design / HLD | **Rewrite** | **P0** | SWE · AI · FDE |
| 9 | `api_security` | **API Design, Auth & Security** | **NEW** | P1 | SWE · FDE |
| 10 | `cpp_systems` | C++ Internals & Low-Latency | **Rewrite** | P1 | SWE (systems/HFT) |
| 11 | `python_internals` | Python Internals & Idioms | **Rewrite** | **P0** | AI · FDE |

### Track C — AI / ML (6) ← heaviest track per your weighting

| # | ID | Module | Status | Tier | Roles |
| :-: | :-- | :-- | :-- | :-- | :-- |
| 12 | `math_ml` | **Math Foundations for ML** | **NEW** | P1 | AI |
| 13 | `ml_core` | **Classical ML & Deep Learning Core** | **NEW** | **P0** | AI |
| 14 | `ml_cv` | Computer Vision & Signal Processing | **Refocus** | P1 | AI (CV/DSP) |
| 15 | `llm_internals` | **LLM & Transformer Internals** | **NEW** | **P0** | AI |
| 16 | `ai_agents` | RAG, Agents & GenAI System Design | **Rewrite** | **P0** | AI · FDE |
| 17 | `ai_evals` | **AI Evaluation, Observability & MLOps** | **NEW** | **P0** | AI · FDE |

> **Why `ml_core` is carved out:** the audit found `ml_cv` contains **zero classical ML** — no bias-variance, no regularization, no SVM/trees/ensembles, no PCA, no cross-validation, no backprop derivation, no optimizer progression, no activation/initialization comparison. That is the floor at every big-tech AI loop. It cannot be bolted onto a CV module without blowing the time budget. Split: `ml_core` = classical ML + DL fundamentals; `ml_cv` = vision + your signal-processing edge.

> **Why `ai_evals` is its own P0 module:** the research is emphatic and consistent — evaluation is named *the single biggest skill gap in AI candidates*, "eval is the new system design", and the #1 reason strong-looking take-homes get rejected. OpenAI's FDE loop uses *"how do you know your AI system is actually working well?"* as an explicit differentiator. One section buried inside `ai_agents` does not match that weight.

### Track D — Data & Infrastructure (3)

| # | ID | Module | Status | Tier | Roles |
| :-: | :-- | :-- | :-- | :-- | :-- |
| 18 | `sql_data` | **SQL Mastery & Data Engineering** | **NEW** | **P0** | FDE · AI · SWE |
| 19 | `linux_git` | **Linux, Git & CLI Debugging** | **NEW** | P1 | All |
| 20 | `docker` | Docker, Kubernetes & CI/CD | **Rewrite** | P1 | All |

> **Why `sql_data` is P0:** Palantir's FDSE loop puts SQL in both the HackerRank screen *and* the Learning round — including writing SQL against a schema you **cannot execute**. `dbms` covers database *theory*; this module covers SQL as a *tool* plus the data-engineering layer (pandas, ETL/ELT, pipeline debugging, data modeling) that is the literal job description of an FDE.

### Track E — Role-Specific & Human (3)

| # | ID | Module | Status | Tier | Roles |
| :-: | :-- | :-- | :-- | :-- | :-- |
| 21 | `fde_decomp` | **FDE Decomposition & Client-Facing Engineering** | **NEW** | **P0** (FDE) | FDE |
| 22 | `behavioral` | **Behavioral, STAR & Project Defense** | **NEW** | **P0** | All |
| 23 | `quant` | **Aptitude, Probability & Puzzles** | **NEW** | P1 | All (OA gate) |

> **Why `behavioral` is P0 for all roles:** three independent findings converge. Palantir embeds ~20 min of behavioral in *every* onsite round and its recruiter screen *"filters out more candidates than most companies do at this stage"*. Anthropic's Values round is *"where most candidates fail — per Anthropic recruiters themselves."* Indian campus panels spend *more* time on project defense than students expect, and *"a project you cannot defend in detail is worse than no project."* This is not soft filler.

### Recommended build order

```
Phase 0  — Infra:  §1 bug fixes → Part 4 component library → §3.1 nav → §3.3 retention
Phase 1  — P0 SWE core:       dsa · os · dbms · concurrency
Phase 2  — P0 AI core:        ml_core · llm_internals · ai_evals · ai_agents
Phase 3  — P0 design + human: lld · system_design · behavioral
Phase 4  — P0 FDE:            sql_data · fde_decomp · python_internals
Phase 5  — P1 breadth:        cn · coa · cpp_systems · api_security · math_ml
Phase 6  — P1 remainder:      ml_cv · docker · linux_git · quant
Phase 7  — README + dashboard + review.html + search index regeneration
```

Phase 0 is non-optional and must complete first — every later phase depends on the component library existing.

### `MODULES_META` schema additions

Each entry needs three new keys:

```python
{
    "id": "llm_internals",
    "file": "llm_internals.html",
    "title": "LLM & Transformer Internals",
    "short_title": "LLM Internals",
    "icon": "🧠",
    "badge": "Modern AI",
    "badge_color": "rose",
    "est_mins": "15 min",              # existing: Sprint estimate
    "est_mins_deep": "60 min",         # NEW
    "track": "C",                      # NEW: A|B|C|D|E
    "tier": "P0",                      # NEW: P0|P1|P2
    "roles": ["AI"],                   # NEW: AI|SWE|FDE
    "companies": [...],
    "desc": "...",
    "highlights": [...]                # CONTRACT — must match real artifacts
}
```

---

## 6. Per-Module Rewrite Briefs — The 12 Existing Modules

Each brief is self-contained. Open one, build it, tick it off.

Format per module: **Current state → Verdict → Must-add (Sprint) → Must-add (Deep) → Required artifacts → Q&A target → Canonical questions.**

---

### 6.1 `dsa` — Data Structures & Algorithms · **P0** · Track A

**Current state:** 3 tables (complexity matrix, sorting matrix, bit tricks), 1 SVG (pattern decision tree), 3 code templates (binary search on answer, monotonic stack, DSU), 5 flashcards. 2 traps with real proofs (build-heap O(N), Floyd's cycle algebra).

**Verdict:** the best-structured module on the site, and the most incomplete. The decision tree SVG advertises **9 patterns**; only **3 have templates**. There is **no dynamic programming section at all**.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Pattern → trigger phrase table** | The highest-yield artifact in the module. One row per pattern: *trigger sentence · template name · complexity*. Research: a topic is only "done" when you can name its trigger in one sentence |
| **Binary search on answer** promoted to its own row | Explicitly named *"appears far more often than students expect"* — cheapest high-yield gap in the whole DSA syllabus |
| **Grid = graph** callout | *"Graph problems wearing a matrix costume"* — islands, flood fill, rotting oranges, shortest-path-in-grid. Extremely common, routinely misclassified |
| **Constraint → complexity table** | `N ≤ 10⁵ → O(N log N)` · `N ≤ 10³ → O(N²)` · `N ≤ 20 → O(2^N)` · `N ≤ 12 → O(N!)`. Already in the SVG footer; promote to a real table |
| **DP: the 9 shapes that are actually asked** | Fibonacci-linear, climbing stairs, house robber, coin change, LIS, 0/1 knapsack, LCS, edit distance, grid paths. Memoization accepted almost universally |
| **DP priority correction callout** | Two independent sources rate DP **Low priority** for campus frequency while candidates over-invest in it. Say so explicitly — it reallocates your study time |

**Must-add — Deep tier:**

1. **Templates for all 9 patterns in the SVG** — currently missing: sliding window (fixed + variable), two pointers (opposite + same direction), BFS (level-order + multi-source), DFS (recursive + iterative), topological sort (Kahn + DFS), backtracking (subsets/permutations/combinations skeleton), heap (top-K + K-way merge).
2. **Full DP section** — memoization vs tabulation vs space-optimized, with 0/1 knapsack built all three ways so the transformation is visible. Plus: how to *write the recurrence first*, bitmask DP, tree DP (one example each).
3. **Recurrence analysis** — Master Theorem (all 3 cases + worked examples), recursion tree method, and amortized analysis (aggregate / accounting / potential) with `vector` push_back as the worked case.
4. **String algorithms** — KMP failure function (built by hand on a worked string), Rabin-Karp rolling hash, Z-algorithm. Research rates these Tier-4 "know it exists", so Deep tier only — but KMP's failure-function construction is asked often enough to need the hand-trace.
5. **Graph depth** — Dijkstra (with why it fails on negative edges), Bellman-Ford, Floyd-Warshall, MST (Kruskal via DSU + Prim), SCC (Kosaraju), bipartite check. Mark MST/max-flow explicitly as *"rare at campus level — add last"*, matching the research.
6. **Advanced structures** — Trie (with code), Fenwick/BIT (connects to the existing `n&(-n)` bit trick), segment tree with lazy propagation. Tier-4 framing.
7. **Greedy validity** — *"the difficulty is not implementation, it is knowing when greedy is valid at all."* Exchange argument + a counterexample where greedy fails (coin change with `{1,3,4}`, target 6).
8. **Intervals** — merge, insert, overlap count, meeting rooms II. Always starts with sort-by-start.

**Required artifacts:**
- SVG: **KMP failure function trace** on a concrete pattern
- SVG: **DP table fill animation** (static frames) for edit distance
- SVG: upgrade the decision tree so every leaf links to its template anchor
- Worked examples (5): Master Theorem all 3 cases · amortized `push_back` · KMP table by hand · 0/1 knapsack table fill · LIS patience-sorting trace
- Follow-up chain on **LRU complexity** and on **"now make your solution handle a stream"**

**Q&A target:** 5 → **32**. Keep all 5 existing.

**Canonical questions to include (sourced):**
- Why does `(low+high)/2` overflow and what's the fix?
- Prove build-heap is O(N), not O(N log N). *(exists — keep)*
- Floyd's cycle detection: prove the meeting point. *(exists — keep)*
- When is greedy provably optimal? Give a case where it fails.
- Dijkstra vs Bellman-Ford vs Floyd-Warshall — pick one for each of three scenarios.
- Why does `unordered_map` degrade to O(N), and what does Java 8 do about it? *(exists — keep)*
- QuickSelect vs size-K heap for streams. *(exists — keep)*
- LIS in O(N log N) — why does `lower_bound` on the tails array work?
- Memoization vs tabulation — when is tabulation strictly better?
- Given `N ≤ 20`, what complexity class should you be targeting and why?

---

### 6.2 `os` — Operating Systems · **P0** · Track A

**Current state:** 6 strong tables (process vs thread with real context-switch numbers, scheduling matrix with the exponential-smoothing formula, page replacement incl. Belady's anomaly, sync primitives incl. futex, Coffman conditions, zombie vs orphan), 2 good SVGs (process memory layout, TLB lookup), 5 flashcards.

**Verdict:** solid theory tables, **zero numerical practice**, and the classic synchronization problems are entirely absent.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Banker's algorithm + safe state** | Named in every GFG/campus OS list. Currently missing entirely |
| **Classic sync problems table** | Producer-Consumer (bounded buffer), Readers-Writers, Dining Philosophers, Sleeping Barber — one row each with the semaphore set required |
| **Peterson's algorithm + the 3 requirements** | Mutual exclusion, progress, bounded waiting. Standard campus question |
| **File system basics** | inodes, hard vs soft links, journaling. Completely absent today |
| **Disk scheduling** | FCFS / SSTF / SCAN / C-SCAN / LOOK — one row each |
| **IPC mechanisms table** | Pipes, FIFOs, message queues, shared memory, sockets, signals + the message-passing vs shared-memory tradeoff |
| **EAT formula** | `EAT = (1−p)·memory_access + p·page_fault_time` — boxed, with a worked number |

**Must-add — Deep tier:**

1. **Worked numericals (the biggest gap)** — Gantt charts + average waiting/turnaround for FCFS, SJF, SRTF, RR, Priority on the *same* process set so the comparison is direct. Plus page-replacement hit/miss traces for FIFO (showing Belady's anomaly concretely), LRU, Optimal on an identical reference string.
2. **Banker's algorithm fully worked** — Available/Max/Allocation/Need matrices, safety-sequence search, then a request that must be denied.
3. **Resource Allocation Graph → wait-for graph** cycle detection, and deadlock *detection* vs *avoidance* vs *prevention* as three distinct strategies (candidates routinely conflate them).
4. **All four classic sync problems with semaphore pseudocode** — and for Readers-Writers, both the reader-preference and writer-preference variants plus the starvation each causes.
5. **Lock-free primitives** — test-and-set, compare-and-swap, Peterson's, bakery algorithm. Bridges into the new `concurrency` module.
6. **Multi-level page tables** — 2-level and 3-level with page-table-size arithmetic (*"how much memory does a single-level page table need for a 48-bit address space with 4KB pages?"* is a standard weeder), inverted page tables, huge pages.
7. **File systems proper** — inode structure + the direct/single/double/triple-indirect block math, FAT vs ext4, journaling modes, directory implementation, hard vs symbolic links with the inode consequence.
8. **Linux CFS** — red-black tree, `vruntime`, and why it replaced O(1). Plus real-time scheduling (RMS, EDF) with the schedulability test.
9. **System call mechanism** — `syscall` instruction, trap, ring transition, and why a syscall costs ~100× a function call.
10. **Thread models** — 1:1 vs M:N vs user-level, thread pools, and why Linux chose 1:1.
11. **RAID 0–6** + the write-hole problem.
12. **Barrier-induced deadlock** and **semaphore FIFO fairness** — both newly added to the GFG 2026 set, specifically because candidates pass the standard questions by rote and fail these.

**Required artifacts:**
- SVG: **multi-level page table walk** (CR3 → PGD → PUD → PMD → PTE)
- SVG: **inode block pointer structure** with indirect levels
- SVG: **Dining Philosophers** deadlock state vs the resource-ordering fix
- SVG: **CFS red-black tree** keyed on `vruntime`
- Worked examples (8): 5 scheduling Gantt charts · 3 page-replacement traces · Banker's safety sequence · page-table size arithmetic · EAT calculation
- Anti-pattern blocks: naive Readers-Writers (writer starvation) → fixed · unordered philosopher forks (deadlock) → ordered

**Q&A target:** 5 → **34**. Keep all 5 existing.

**Canonical questions to include (sourced):**
- Process vs thread — address space, context-switch cost, IPC speed. *(exists)*
- The four Coffman conditions and how to break each. *(table exists — add as Q&A)*
- Banker's algorithm: is this state safe? Show the sequence.
- Why does FIFO exhibit Belady's anomaly but LRU cannot?
- Thrashing: what, how to detect, how to fix. *(exists)*
- Zombie vs orphan — who reaps each? *(table exists)*
- Priority inversion + priority inheritance (Mars Pathfinder). *(exists)*
- Internal vs external fragmentation. *(exists)*
- Why can a spinlock deadlock on a uniprocessor? *(exists)*
- Semaphore drawbacks — priority inversion, deadlock risk, debuggability.
- How does the OS guarantee bounded waiting on a semaphore? *(FIFO wait queue)*
- How can a barrier cause deadlock? *(one thread never arrives)*
- Monolithic kernel vs microkernel.
- User-level vs kernel-level threads.
- Hard link vs symbolic link — what happens when you delete the target?
- Why is a system call ~100× more expensive than a function call?

---

### 6.3 `dbms` — DBMS & Storage Internals · **P0** · Track A

**Current state:** 3 tables (ACID→mechanism, isolation×anomaly matrix with colour coding, index type comparison with fan-out math), 1 SVG (B+ tree with linked leaves), 1 SQL code block (window functions), 5 flashcards.

**Verdict:** the isolation matrix and B+ tree fan-out math are genuinely strong. But **three artifacts promised in `MODULES_META` do not exist** (LSM trees, WAL SVG, query execution pipeline), and SQL-as-a-skill is nearly absent.

> **Scope note:** pure SQL querying skill moves to the new `sql_data` module (§7.8). This module keeps *engine internals* — storage, indexing, transactions, recovery, optimization. Keep one bridging callout pointing at `sql_data`.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **LSM tree vs B+ tree** | Promised in `MODULES_META`, completely missing. Memtable → SSTable → compaction, write vs read amplification, RocksDB/Cassandra vs InnoDB/Postgres |
| **Join algorithms table** | Nested loop / block nested loop / hash join / sort-merge — with cost formula and when the optimizer picks each |
| **NULL three-valued logic** | `NULL != NULL`, `COUNT(*)` vs `COUNT(col)`, `NOT IN` with NULLs silently returning empty. A classic trap, currently absent |
| **Keys taxonomy** | super / candidate / primary / foreign / unique / alternate. Standard campus question |
| **DELETE vs TRUNCATE vs DROP** | Including the nuance most candidates get wrong: rollback-ability differs **by DBMS** (rollback-able in a transaction on SQL Server/Postgres; generally not MySQL) |
| **Composite index leftmost-prefix rule** | Why `INDEX(a,b,c)` serves `WHERE a=? AND b=?` but not `WHERE b=?` |

**Must-add — Deep tier:**

1. **WAL + ARIES recovery** — the promised SVG, plus analysis/redo/undo passes, checkpointing, steal/no-force policies, and why `fsync()` is the durability boundary.
2. **Query execution pipeline** — parse → bind → optimize → execute. Reading an `EXPLAIN`/`EXPLAIN ANALYZE` plan line by line. Cardinality estimation, histograms, selectivity, predicate pushdown, and why a bad row estimate produces a catastrophic plan.
3. **Concurrency control proper** — 2PL (basic / strict / rigorous), conflict serializability with **precedence-graph cycle testing** (worked), view serializability, timestamp ordering + Thomas write rule, recoverable vs cascadeless schedules, wait-die vs wound-wait.
4. **MVCC mechanics** — version chains, read views, snapshot isolation, write skew (the anomaly snapshot isolation *doesn't* prevent — Postgres `SERIALIZABLE` vs `REPEATABLE READ`), and vacuum/bloat.
5. **Lock granularity** — intention locks (IS/IX/SIX), gap locks, next-key locks, and the lock-escalation path.
6. **Normalization formally** — functional dependency closure, candidate-key derivation, canonical cover, lossless-join and dependency-preserving decomposition tests, 4NF/5NF with multivalued dependencies. Currently only a 1NF→BCNF flashcard exists.
7. **B+ tree mutation** — insert with node split, delete with merge/redistribute, drawn step by step.
8. **Replication & HA** — sync vs async, primary-replica, replication lag and the read-your-writes consequence, failover, split-brain.
9. **NoSQL taxonomy** — document / KV / wide-column / graph, when each wins, quorum `R + W > N`, ACID vs BASE.
10. **SQL injection + prepared statements** — the actual mechanism, not just "sanitize input".

**Required artifacts:**
- SVG: **WAL + checkpoint + recovery timeline** (the promised one)
- SVG: **LSM tree write path** — memtable → immutable → SSTable levels → compaction
- SVG: **B+ tree node split** during insert
- SVG: **MVCC version chain** with two concurrent read views
- Worked examples (6): precedence-graph serializability test · FD closure + candidate key · BCNF decomposition · join cost comparison · `EXPLAIN` plan read · composite-index prefix matching
- Decision matrix: B+ tree vs LSM vs hash vs bitmap index

**Q&A target:** 5 → **32**. Keep all 5 existing.

**Canonical questions to include (sourced):**
- ACID — and the *mechanism* implementing each. *(table exists)*
- Clustered vs non-clustered index; what is a covering index? *(exists)*
- MVCC: how do readers avoid blocking writers? *(exists)*
- 1NF → 2NF → 3NF → BCNF with an anomaly example at each step. *(exists, expand)*
- Sharding vs partitioning. *(exists)*
- Optimistic vs pessimistic concurrency. *(exists)*
- Why do databases use B+ trees instead of B-trees or BSTs?
- When would you choose an LSM tree over a B+ tree?
- `DELETE` vs `TRUNCATE` — and is `TRUNCATE` rollback-able?
- `UNION` vs `UNION ALL` — why is `UNION` slower?
- Why does `WHERE col != NULL` return nothing?
- Is this schedule conflict-serializable? Draw the precedence graph.
- What is write skew, and which isolation level permits it?
- `INDEX(a,b,c)` — which of these four queries use it?
- Three-schema architecture: external / conceptual / internal.
- Views vs materialized views — what's the refresh cost?
- Triggers vs stored procedures vs functions.

---

### 6.4 `cn` — Computer Networks · **P1** · Track A

**Current state:** 5 tables (OSI vs TCP/IP full 7 rows, TCP vs UDP, well-known ports, congestion phases, HTTP/1.1 vs 2 vs 3), 2 excellent SVGs (full handshake + teardown with all TCP states; DNS resolution chain), AIMD/Tahoe/Reno coverage, the TIME_WAIT 2×MSL trap with both reasons, an HFT Nagle + delayed-ACK callout with real `setsockopt` code, 5 flashcards.

**Verdict:** strongest existing module. The handshake SVG with full state labels is better than most paid resources. Gaps are the *computational* topics and the routing layer that the OSI table name-drops but never explains.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Sliding window protocols** | Stop-and-Wait / Go-Back-N / Selective Repeat with efficiency and window-size formulas. A GATE and campus staple, entirely absent |
| **Subnetting / VLSM** | Classful vs classless, CIDR, supernetting. Currently only one `/24` vs `/27` flashcard |
| **Routing: Link-State vs Distance-Vector** | Named in the OSI table, never explained. Plus count-to-infinity and split horizon |
| **Error detection** | Parity, checksum, CRC, Hamming code — one row each |
| **CSMA/CD + CSMA/CA** | Exponential backoff, Ethernet minimum frame size and *why* it exists |
| **NAT / PAT** | How the translation table works; why it breaks inbound connections |
| **IPv4 vs IPv6 header** | Field-by-field; what was removed and why |

**Must-add — Deep tier:**

1. **Worked numericals** — sliding-window efficiency and throughput, bandwidth-delay product, subnetting a block into unequal subnets (VLSM), CRC long division by hand, Hamming-code single-bit correction.
2. **TCP reliability mechanics** — window scaling, SACK, RTT estimation (Jacobson/Karels), Karn's algorithm, RTO backoff, fast retransmit/fast recovery, and modern congestion control (CUBIC, BBR) contrasted with Reno.
3. **"What happens when you type a URL"** — promote the existing flashcard to a **full section with an SVG**. Research names this the single highest-frequency CN integration question, and it is a *whole-stack* answer: cache → DNS (recursive + iterative) → ARP → TCP handshake → TLS 1.3 handshake → HTTP request → server → response → DOM/CSSOM → render.
4. **TLS properly** — handshake (1.3 vs 1.2 round trips), cipher suites, certificate chain and PKI, mTLS, HSTS, and what *exactly* `0-RTT` risks.
5. **Routing protocols** — RIP vs OSPF (areas, LSAs, Dijkstra) vs BGP (path attributes, AS-path, why the internet needs policy routing).
6. **Socket API state machine** — `socket/bind/listen/accept/connect`, blocking vs non-blocking, `select` vs `poll` vs `epoll` (and the O(N) vs O(1) difference), C10K. Bridges to `concurrency`.
7. **HTTP semantics** — idempotent vs safe methods, full status-code families, caching headers (`ETag`, `Cache-Control`, conditional requests), CORS preflight, cookies vs tokens. Bridges to `api_security`.
8. **ICMP + traceroute** — how TTL manipulation reveals the path.
9. **L2 topics** — VLANs, STP, switching vs routing, ARP cache poisoning.

**Required artifacts:**
- SVG: **"type a URL" full-stack sequence diagram** (highest-value addition to this module)
- SVG: **Go-Back-N vs Selective Repeat** timeline with a lost frame
- SVG: **TLS 1.3 handshake** vs 1.2 round-trip comparison
- SVG: **NAT translation table** rewriting a packet
- Worked examples (6): VLSM subnetting · sliding-window efficiency · bandwidth-delay product · CRC division · Hamming correction · `/27` host count
- Keep the HFT Nagle callout verbatim — it is excellent

**Q&A target:** 5 → **30**. Keep all 5 existing.

**Canonical questions to include (sourced):**
- What happens when you type `google.com` and hit Enter? *(exists — expand to full section)*
- TCP vs UDP, and name three protocols that chose UDP and why. *(table exists)*
- Why three-way, not two-way, handshake? *(exists)*
- Why does TIME_WAIT last 2×MSL? *(exists)*
- ARP vs RARP. *(exists)* · DHCP DORA. *(exists)* · Silly Window Syndrome. *(exists)*
- Go-Back-N vs Selective Repeat — window size constraint for each?
- How does TCP detect and recover from congestion? Walk through slow start → congestion avoidance → fast recovery.
- Distance-vector count-to-infinity — what is it and how is it mitigated?
- Why does Ethernet have a 64-byte minimum frame size?
- HTTP/2 multiplexing solved HoL blocking — so why did HTTP/3 move to QUIC?
- `select` vs `poll` vs `epoll`.
- Which HTTP methods are idempotent? Is `POST`? Is `PUT`?

---

### 6.5 `coa` — Computer Organization & Architecture · **P1** · Track A

**Current state:** 4 tables (memory hierarchy latency ladder with real cycle counts, cache address decoding, pipeline hazards, write policies), 1 SVG (5-stage pipeline with two forwarding paths), a fully worked cache-bits problem (32-bit/32KB/4-way/64B → 6/7/19), false sharing + `alignas(64)`, MESI, 5 flashcards.

**Verdict:** the latency ladder and the worked cache-bits problem are exactly right. The module is missing **every performance equation** — which is most of what COA interviews actually compute.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **CPU performance equation** | `CPU Time = IC × CPI × Clock Cycle Time`. The foundational formula, absent today |
| **Amdahl's Law** | `Speedup = 1 / ((1−p) + p/s)`. Universally asked; absent |
| **AMAT** | `AMAT = hit time + miss rate × miss penalty`, plus multi-level. The latency ladder is *right there* and never used in a formula |
| **Pipeline speedup / throughput / efficiency** | Ideal vs actual CPI with stall frequency |
| **IEEE-754** | Sign/exponent/mantissa layout, bias, denormals, why `0.1 + 0.2 != 0.3` |
| **Addressing modes + instruction formats** | Standard campus question |
| **WAR / WAW name dependencies** | Only RAW is covered today; register renaming is the fix |

**Must-add — Deep tier:**

1. **Worked numericals (the central gap)** — CPI with stall frequencies, Amdahl speedup given a parallel fraction, multi-level AMAT with L1/L2/L3 from the existing latency table, pipeline cycle count for N instructions, clock period from the slowest stage, speedup from forwarding vs stalling.
2. **Out-of-order execution** — scoreboarding, **Tomasulo's algorithm** (reservation stations, CDB, register renaming), reorder buffer, precise exceptions, speculative execution. This is the main COA depth topic for hardware roles and is entirely absent.
3. **Branch prediction depth** — 1-bit vs 2-bit saturating, global vs local history, gshare, tournament, BTB organization, return-address stack, and the misprediction penalty in cycles.
4. **Superscalar / VLIW / SIMD / SMT** — issue width, in-order vs out-of-order superscalar, vector registers, hyper-threading and when it hurts.
5. **Arithmetic circuits** — ripple-carry vs carry-lookahead, Booth multiplication, restoring vs non-restoring division. Worked traces.
6. **Cache depth** — VIPT vs PIPT and virtual-address aliasing, pseudo-LRU, non-blocking caches, victim cache, hardware prefetchers, and cache-inclusive vs exclusive hierarchies.
7. **Coherence + consistency** — MESI → MOESI/MESIF, snooping vs directory-based, then **memory consistency models** (sequential consistency, x86-TSO, ARM weak ordering) and store buffers. This is the piece that makes the C++ memory-order table in `cpp_systems` actually make sense — cross-link them.
8. **GPU / SIMT architecture** — warps, lane divergence, memory coalescing, occupancy. Nvidia and Qualcomm are named target companies and there is currently nothing.
9. **Control unit** — hardwired vs microprogrammed.
10. **DMA, interrupts, bus arbitration** — including interrupt vectoring and cycle stealing.

**Required artifacts:**
- SVG: **Tomasulo / OoO datapath** (reservation stations → CDB → ROB)
- SVG: **2-bit saturating predictor state machine** + BTB lookup
- SVG: **IEEE-754 bit layout** with a decoded concrete value
- SVG: **MESI state transition diagram** (states + bus transactions as edges)
- SVG: **GPU SIMT warp execution** with divergence
- Worked examples (8): CPI with stalls · Amdahl · multi-level AMAT · pipeline cycles for N instructions · cache bits *(exists — keep)* · IEEE-754 encode/decode · Booth multiply · carry-lookahead delay
- `see_also` → `cpp_systems` memory orders, `os` TLB, `concurrency` atomics

**Q&A target:** 5 → **30**. Keep all 5 existing.

**Canonical questions to include (sourced):**
- The 3 C's of cache misses — plus the 4th (coherence). *(exists)*
- MESI: define all four states and the RFO transition. *(exists, expand)*
- Why is row-major traversal ~10× faster than column-major? *(exists)*
- RISC vs CISC. *(exists)* · Little vs big endian + detection code. *(exists)*
- Compute AMAT for this 3-level hierarchy.
- A program is 80% parallelizable. Max speedup on infinite cores?
- What is false sharing, how do you detect it, how do you fix it? *(trap exists — promote to Q&A)*
- RAW vs WAR vs WAW — which are *real* dependencies and which can renaming eliminate?
- Load-use hazard — why can forwarding not fully eliminate the stall?
- How does a 2-bit predictor beat a 1-bit predictor on a loop?
- Superscalar vs VLIW — where does the scheduling complexity live?
- Why does x86 not need a fence for acquire-release, but ARM does?

---

### 6.6 `lld` — Low-Level Design & Design Patterns · **P0** · Track B

**Current state:** SOLID matrix with concrete violation→refactor pairs (genuinely good), an 8-row pattern table, 1 UML SVG (LRU with proper stereotypes and a composition diamond), 4 code blocks (full C++ LRUCache ~70 lines, Meyers' Singleton, LSP violation demo, broken DCLP), 10 flashcards.

**Verdict:** the SOLID matrix and the LRU implementation are the best content on the site. But the module claims **23 GoF patterns** and delivers **8 rows with code for exactly one**, and claims two LLD problems while implementing one.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Class relationship vocabulary** | Association vs aggregation vs composition vs dependency vs generalization, with UML notation and multiplicity. Research: *"asked constantly in LLD, answered vaguely almost always"* — and it is currently absent |
| **OOP fundamentals** | The four pillars, static vs dynamic binding, overloading vs overriding rules, abstract class vs interface. Campus panels ask for *"an example from your own code rather than a textbook"* |
| **Complete 23-pattern matrix** | Honour the `MODULES_META` claim. Group creational / structural / behavioural, one-line intent + stdlib example each |
| **Design principles beyond SOLID** | DRY, KISS, YAGNI, Law of Demeter, composition over inheritance, program-to-interface |
| **Working thread-safe singleton** | Currently only the *broken* DCLP is shown. Show the `std::atomic` acquire-release fix and the Meyers' preference |
| **LLD interview framework** | Clarify requirements → identify entities → relationships → class skeleton → core methods → concurrency → extensibility. Candidates jump straight to classes |

**Must-add — Deep tier:**

1. **Code for the 10 patterns that actually get asked** — Strategy, Factory Method, Abstract Factory, Builder, Observer, Decorator, Adapter, Command (with undo stack), State, Template Method. Currently only Singleton has code.
2. **Pattern disambiguation pairs** — these *are* the interview questions: Strategy vs State, Factory vs Abstract Factory, Adapter vs Facade vs Decorator vs Proxy, Template Method vs Strategy, Observer vs Pub-Sub. Four already exist as flashcards; promote to a `decision_matrix` each.
3. **Full LLD implementations (3 new)** — the audit shows Parking Lot is a 5-bullet flashcard with no code. Build out: **Parking Lot** (complete, with UML + fee strategy), **Elevator System** (state machine + scheduling), **Movie Ticket Booking** (the seat-locking concurrency problem — this is the one that separates candidates).
4. **Rate Limiter LLD** — promised in `MODULES_META`, missing. Token bucket class design, thread-safe, with the `system_design` cross-link.
5. **LFU cache** — the natural follow-up to LRU and far less practised. O(1) implementation with the frequency-bucket structure.
6. **Thread-safe LRU** — the follow-up chain: single mutex → lock contention → striped/sharded locks → the exact-LRU guarantee you lose. This is the single best `followup_chain()` on the site.
7. **Anti-patterns catalogue** — God object, anemic domain model, service locator, singleton abuse (and the *testability* critique, which is the real interview answer), spaghetti, primitive obsession.
8. **Immutability + `equals`/`hashCode` contract** — the four rules. One flashcard exists; expand with code.
9. **UML notation reference** — class, sequence, state-machine, activity, use-case diagrams. Research names all five as required supporting knowledge.
10. **Testability design** — DI for testability, mocks vs stubs vs fakes, why singletons resist testing.

**Required artifacts:**
- SVG: **Factory vs Strategy decision flow** (the promised, missing one)
- SVG: **Parking Lot class diagram** (full UML)
- SVG: **Elevator state machine**
- SVG: **Class relationships cheat sheet** — all five arrow types with notation
- SVG: **23 GoF patterns map** grouped by category
- Code: 10 patterns + LFU + thread-safe LRU + rate limiter + 3 full LLD problems
- `followup_chain()`: thread-safe LRU ladder · "now add TTL" · "now make it distributed"
- Anti-pattern blocks: God object → decomposed · singleton → injected · broken DCLP → atomic fix

**Q&A target:** 10 → **35**. Keep all 10.

**Canonical questions to include (sourced):**
- Association vs aggregation vs composition vs dependency — give a code example of each.
- Factory Method vs Abstract Factory. *(exists)* · Strategy vs State. *(exists)*
- Adapter vs Facade vs Decorator. *(exists)* · Template Method vs Strategy. *(exists)*
- Composition over inheritance — why? *(exists)* · DI vs IoC. *(exists)*
- Observer + the lapsed-listener leak. *(exists)* · Command + undo. *(exists)*
- Immutable class — the four rules. *(exists)* · Design a parking lot. *(exists — add code)*
- Design an LRU cache, then make it thread-safe, then shard it.
- Design an LFU cache in O(1).
- Why is Singleton considered an anti-pattern by some? *(answer: global state + untestable)*
- Identify the Liskov violation in this code. *(exists)*
- Why does double-checked locking fail in C++98/Java 1.4, and what fixes it? *(exists — add the fix)*
- Design a movie-booking system. How do you prevent two users booking the same seat?
- Abstract class vs interface — when do you choose which?
- Can you call a virtual function from a constructor? What happens?

---

### 6.7 `system_design` — System Design / HLD · **P0** · Track B

**Current state:** 3 tables (CAP + PACELC with real systems named, rate-limiting algorithms with the sliding-window formula, cache failure modes), 2 SVGs (consistent hashing ring with vnodes + a 3-rule panel; TinyURL architecture with KGS), capacity estimation worked for TinyURL (200 WPS / 20K QPS / 15 TB), Base62 reasoning, L4 vs L7, push vs pull fan-out + celebrity problem, a Redis Lua sliding-window limiter, 10 flashcards.

**Verdict:** good breadth on the *mechanisms*, but almost no **canonical designs** (one: TinyURL) and consensus is name-dropped without content. Research lists ~40 standard HLD problems; you have one.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Back-of-envelope reference card** | Latency numbers every programmer should know, plus the QPS/storage/bandwidth estimation *framework* (DAU → QPS → peak → storage → bandwidth). Currently only the TinyURL instance exists |
| **Cache patterns taxonomy** | Cache-aside / read-through / write-through / write-behind / refresh-ahead, plus the 7 eviction policies. Failure modes are covered; the *patterns* are not |
| **Delivery semantics** | At-most-once / at-least-once / exactly-once, and why exactly-once is really at-least-once + idempotency |
| **Resilience patterns** | Circuit breaker, bulkhead, retry with exponential backoff **+ jitter**, timeout, backpressure, dead-letter queue |
| **The 15 tradeoffs table** | Vertical vs horizontal · long-poll vs WebSocket · batch vs stream · stateful vs stateless · strong vs eventual · read-through vs write-through · push vs pull · REST vs RPC · sync vs async · SQL vs NoSQL · normalization vs denormalization · monolith vs microservices · CP vs AP · single-region vs multi-region · cache vs compute |
| **Availability math** | Nines → actual downtime; serial vs parallel composition |

**Must-add — Deep tier:**

1. **Consensus properly** — **Raft** (leader election, terms, log replication, commit index, safety) and why Paxos is harder to implement. Quorum math `R + W > N` with worked configurations. Currently both are only names.
2. **Canonical designs — build 8 fully** (each: requirements → estimation → API → data model → architecture SVG → deep dive → bottleneck):
   - **Chat / WhatsApp** (connection state, delivery receipts, fan-out)
   - **News feed** (the celebrity problem exists as a trap — make it a full design)
   - **YouTube / Netflix** (transcoding pipeline, HLS/DASH, CDN)
   - **Uber / geospatial** (geohash vs quadtree vs S2, matching)
   - **Rate limiter distributed** (exists partially — complete it)
   - **Notification system** (multi-channel, retries, preferences, DLQ)
   - **Distributed job scheduler / cron** (leader election, at-least-once, idempotency)
   - **Search autocomplete** (trie service, ranking, sharding by prefix)
   - Plus **Snowflake distributed ID generation** as a focused sub-design (timestamp + machine + sequence bits) — asked constantly, short to cover.
3. **Kafka architecture depth** — partitions, consumer groups, offsets, rebalancing, ISR, replication factor, log compaction, ordering guarantees. `MODULES_META` claims "Kafka partition vs consumer groups"; only the zero-copy throughput flashcard exists.
4. **Distributed transactions** — 2PC (exists) → **Saga** (choreography vs orchestration, compensating transactions), the **outbox pattern**, and idempotent consumers. Saga is mentioned once and never explained.
5. **Clocks and conflict resolution** — Lamport timestamps, vector clocks, hybrid logical clocks, last-write-wins and its data loss, CRDTs, read repair, anti-entropy with Merkle trees, hinted handoff, gossip.
6. **Microservices patterns** — API gateway, service discovery, sidecar/service mesh, BFF, strangler fig, CQRS, event sourcing.
7. **Distributed locking** — Redlock *and* the Kleppmann critique (why it is unsafe without fencing tokens). A favourite senior follow-up.
8. **Observability** — the three pillars, distributed tracing with spans/trace IDs, RED and USE methods, SLI/SLO/SLA and error budgets.
9. **Deployment & reliability** — blue-green, canary, feature flags, RTO/RPO, multi-AZ vs multi-region, chaos engineering.
10. **LLM-serving system design** — cross-link to `ai_agents`. Research shows Anthropic asks *"design a Claude chat service"* and *"request batching, queuing, GPU utilization under variable load"*. Keep the detail in `ai_agents`; put the pointer here.

**Required artifacts:**
- SVG per canonical design (8 new architecture diagrams)
- SVG: **Raft leader election + log replication** state flow
- SVG: **Saga orchestration vs choreography** side by side
- SVG: **Kafka partitions → consumer group assignment** with a rebalance
- SVG: **Vector clock divergence and merge**
- `numbers_card()`: latency ladder · storage/bandwidth reference · QPS tiers
- Worked examples (6): DAU→QPS→peak · storage for 5 years · bandwidth for video · quorum configurations · availability composition · Snowflake bit budget
- `followup_chain()`: "scale TinyURL to 10× reads" · "a shard is hot — now what" · "your cache just went down"

**Q&A target:** 10 → **35**. Keep all 10.

**Canonical questions to include (sourced):**
- Consistent hashing — why does only K/N move? *(exists)*
- Why is Kafka fast? *(exists — zero-copy, page cache, sequential I/O, batching)*
- Polling vs long-polling vs WebSocket vs SSE. *(exists)*
- Distributed rate limiter in Redis — why Lua? *(exists)*
- Strong vs eventual vs read-your-writes. *(exists)*
- Bloom filters against cache penetration. *(exists)*
- Design an idempotent payment API. *(exists)*
- How does a CDN route you to the nearest edge? *(exists — Anycast/BGP)*
- 2PC phases and the blocking-coordinator flaw. *(exists)*
- How do you pick a shard key? *(exists)*
- Explain Raft leader election. What happens on a split vote?
- Quorum: `N=5`. Pick `R` and `W` for read-heavy. For write-heavy.
- When would you use a Saga instead of 2PC?
- Is Redlock safe? *(the fencing-token critique)*
- Design a distributed ID generator. Why not UUIDv4?
- Exactly-once delivery — is it actually possible?
- Your p99 latency spiked but p50 is flat. Diagnose.

---

### 6.8 `cpp_systems` — C++ Internals & Low-Latency · **P1** · Track B

**Current state:** 3 tables (smart pointers with real byte sizes and the atomic-refcount-but-not-pointee note, value categories, memory orderings with the x86-TSO observation), 1 SVG (vtable layout with RTTI slot and `.rodata`), 2 code blocks (complete Rule of 5, vtable-less UB demo), the `std::move`-moves-nothing trap, 5 flashcards including the ABA problem and why HFT avoids `malloc`.

**Verdict:** the memory-orderings table and the HFT allocation flashcard are excellent and rare. But **four `MODULES_META` promises are unmet** (control-block SVG, SPSC ring buffer, RAII, forwarding), and templates/STL internals — the bulk of a C++ interview — are entirely absent.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **RAII defined** | Promised in `highlights`, never actually defined. Plus `lock_guard` / `unique_lock` / `scoped_lock` / `shared_lock` |
| **Perfect forwarding** | Promised, never explained. Universal references, reference collapsing rules, `std::forward` vs `std::move` |
| **STL container internals + complexity** | `vector` growth factor and amortized `push_back`, `deque` block structure, `map` vs `unordered_map`, `emplace_back` vs `push_back`, SSO. Absent today |
| **Iterator invalidation rules** | Per container. High-frequency, zero coverage |
| **`new` vs `malloc`, `delete` vs `delete[]`** | Research flags both as top-frequency GFG C++ questions |
| **Virtual function in a constructor** | Explicitly named a *"classic weed-out"* with a counter-intuitive answer (dispatch is disabled during construction) |
| **Diamond problem + virtual inheritance** | High frequency, absent |
| **`const` / `constexpr` / `mutable` / `volatile`** | Especially `volatile` **vs** atomic — the question that separates embedded candidates |

**Must-add — Deep tier:**

1. **Deliver the four broken promises** — `shared_ptr` control-block SVG, **lock-free SPSC ring buffer** (full implementation with the acquire-release reasoning and cache-line padding), RAII section, perfect-forwarding section.
2. **Templates & metaprogramming** — function/class templates, specialization (full + partial), variadic templates + fold expressions, SFINAE and `enable_if`, type traits, **CRTP**, C++20 concepts, `constexpr`/`consteval`, and template-induced code bloat.
3. **Concurrency API** — `std::thread`/`jthread`, `async`/`future`/`promise`/`packaged_task`, `condition_variable` + **spurious wakeups** + the `while` predicate, `mutex`/`recursive_mutex`/`shared_mutex`/`timed_mutex`, `std::atomic` CAS (`compare_exchange_weak` vs `strong` and why the loop), `atomic_flag`, fences. Cross-link heavily to `concurrency`.
4. **Object model depth** — multiple-inheritance vtable layout, virtual base offsets, `dynamic_cast` cost, RTTI, devirtualization, `override`/`final`, pure virtual with a body, vtable per class not per object.
5. **Copy elision / RVO / NRVO**, the most-vexing parse, static initialization order fiasco, initialization order within a class.
6. **Undefined behaviour catalogue** — strict aliasing (with the `reinterpret_cast` violation), signed overflow, use-after-move, dangling references, sequence points, `nullptr` deref, out-of-bounds. One table, one anti-pattern block each for the top three.
7. **Memory layout** — alignment, padding, struct-size computation worked by hand, `offsetof`, `alignas`, placement `new`, and a **custom arena/pool allocator** implementation (the natural companion to the existing "HFT avoids malloc" flashcard).
8. **Low-latency toolkit (the ₹41L-relevant section)** — `perf`, cachegrind, GDB essentials, sanitizers (ASan/TSan/UBSan), `-O2` vs `-O3` vs `-march=native`, inlining, LTO, PGO, `[[likely]]`/`[[unlikely]]`, `__builtin_prefetch`, SIMD intrinsics, CPU pinning/`isolcpus`/NUMA, huge pages, busy-polling, kernel bypass (DPDK/Solarflare), and `hardware_destructive_interference_size`. This is the whole reason the module exists for Pace-class targets and it is currently absent.
9. **Exception cost model** — zero-cost on the happy path, stack unwinding, why `noexcept` enables move optimizations, exception safety guarantees (basic/strong/nothrow).
10. **Move semantics completion** — when the compiler elides vs moves, why `return std::move(x)` is usually wrong, move-only types, `std::exchange` idiom.

**Required artifacts:**
- SVG: **`shared_ptr` control block** (the promised one) — object + control block + strong/weak counts + deleter
- SVG: **SPSC ring buffer** with head/tail, cache-line padding, acquire-release annotations
- SVG: **Diamond inheritance** layout with and without `virtual`
- SVG: **Struct padding** — same members, two orderings, two sizes
- Code (12+): SPSC ring buffer · arena allocator · CRTP · SFINAE/`enable_if` · variadic template · `condition_variable` + predicate · CAS loop · perfect-forwarding factory · RAII lock wrapper · custom comparator for `priority_queue` · strict-aliasing violation + fix · placement `new`
- `followup_chain()`: "make this queue lock-free" ladder · "this is 200ns too slow" ladder

**Q&A target:** 5 → **34**. Keep all 5.

**Canonical questions to include (sourced):**
- `make_shared` vs `shared_ptr(new T)`. *(exists)*
- Object slicing. *(exists)* · Exception in a destructor. *(exists)*
- ABA problem + tagged pointers. *(exists)* · Why HFT avoids `malloc` on the hot path. *(exists)*
- Why must a polymorphic base have a virtual destructor? *(trap exists — promote)*
- `std::move` — what does it actually compile to? *(trap exists — promote)*
- `new` vs `malloc`; `delete` vs `delete[]` — what is the UB?
- Can you call a virtual function from a constructor? What is dispatched?
- Diamond problem — what does `virtual public` change in the layout?
- `volatile` vs `std::atomic` — which gives you thread safety?
- Explain acquire-release. Why is it free on x86-64 but not ARM?
- `compare_exchange_weak` vs `strong` — why does weak need a loop?
- Shallow vs deep copy — what does the compiler generate?
- Reference vs pointer — three differences.
- What is the Rule of 0 / 3 / 5? When do you want Rule of 0?
- `vector` reallocation — what is the growth factor and why not 2× exactly everywhere?
- Which operations invalidate `vector` iterators? `unordered_map` iterators?
- `set::insert` returns what? How do you detect a duplicate key?
- What is SSO and when does `std::string` heap-allocate?
- Why is `inline` only a request? What happens with recursive inline?
- `friend` — is friendship inherited? Transitive?

---

### 6.9 `python_internals` — Python Internals & Idioms · **P0** · Track B

**Current state:** 2 tables (concurrency models with real memory figures, dunder methods), 2 SVGs (GIL two-thread timeline with the 5 ms switch interval; generational GC with thresholds), 5 code blocks (`PyObject` C struct, asyncio basics, mutable-default bug + fix, `is` vs `==`), 10 flashcards including the cyclic-GC trial-refcount algorithm, C3 linearization, and PEP 703.

**Verdict:** the internals coverage is genuinely strong — GIL, refcounting, generational GC, MRO. The gap is **the language itself**: decorators, descriptors, iterator protocol, context managers, and the data-model dunders have no code.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Decorator implementation** | Closure-based, parameterized, class-based. `functools.wraps` is described in a flashcard but there is no decorator code anywhere. Top-5 Python interview question |
| **Iterator protocol code** | `__iter__`/`__next__`/`StopIteration`, `yield from`, generator `send`/`throw`/`close`, and generator-vs-coroutine |
| **Context manager implementation** | `__enter__`/`__exit__`, `contextlib.contextmanager`, and the `__exit__` return-value suppression semantics |
| **`@property`, `@staticmethod` vs `@classmethod`** | Universal question, absent |
| **Built-in complexity table** | list / dict / set / deque / heapq operation costs. Needed for every coding round in Python |
| **`__eq__`/`__hash__` contract + hashability** | Why a mutable object cannot be a dict key |
| **Mutable class attribute trap** | Sibling of the mutable-default trap already covered |
| **Late-binding closure trap** | `[lambda: i for i in range(3)]` — all return 2. Classic |

**Must-add — Deep tier:**

1. **Descriptors** — `__get__`/`__set__`/`__delete__`, data vs non-data, how `@property` and methods themselves are descriptors, the full attribute-lookup order.
2. **Metaclasses** — `type` as a callable, `__new__` vs `__init__` at the metaclass level, `__init_subclass__`, `ABCMeta`, and *when not to use them*.
3. **Data model dunders with code** — `__repr__` vs `__str__`, `__eq__`/`__hash__`, ordering (`__lt__` + `total_ordering`), `__len__`/`__bool__`/`__contains__`, `__getitem__`, `__call__`, `__getattr__` vs `__getattribute__`, arithmetic dunders.
4. **Container internals** — dict open addressing + the compact layout (3.6+) + insertion-order guarantee (3.7+) + resize policy, set internals, list over-allocation growth, tuple vs list memory, string interning.
5. **Scoping** — LEGB, `global`/`nonlocal`, closures and cell objects, and class-body scoping surprises.
6. **Concurrency API depth** — `concurrent.futures` (ThreadPool vs ProcessPool), `multiprocessing` sharing (`Queue`/`Pipe`/`Value`/`Array`/`Manager`/`shared_memory`), pickling limits, `fork` vs `spawn` vs `forkserver` and the platform differences, daemon threads, all `threading` primitives, and the asyncio toolkit (`create_task`, `gather` vs `as_completed`, `wait_for`, `Semaphore`, `Queue`, `to_thread`, `run_in_executor`) plus **the blocking-call-in-event-loop pitfall**.
7. **Exceptions** — hierarchy, custom exceptions, `try/except/else/finally` evaluation order, EAFP vs LBYL, exception groups.
8. **Stdlib power tools** — `functools` (`lru_cache`, `cached_property`, `partial`, `reduce`), `itertools`, `collections` (`defaultdict`, `Counter`, `deque`, `OrderedDict` vs dict now), `dataclasses` vs `NamedTuple` vs `TypedDict` vs Pydantic, `enum`.
9. **Bytecode + the CPython pipeline** — `dis` output for a simple function, source → AST → bytecode → eval loop, `sys.modules` caching, circular imports, `__pycache__`.
10. **Performance** — `cProfile`/`timeit`/`memory_profiler`, NumPy vectorization, views vs copies, broadcasting rules, when to drop to Cython/ctypes. Cross-link to `ml_core`.

**Required artifacts:**
- SVG: **attribute lookup order** — instance `__dict__` → type MRO → descriptors → `__getattr__`
- SVG: **dict open addressing** with a collision and a probe sequence
- SVG: **asyncio event loop** — ready queue, selector, callbacks, task states
- SVG: **closure cell** diagram showing the late-binding trap
- Code (14+): three decorator forms · iterator class · generator with `send` · context manager both ways · descriptor · metaclass · `__eq__`/`__hash__` pair · `lru_cache` usage · `ProcessPoolExecutor` · asyncio `gather` with a semaphore · `to_thread` for blocking I/O · late-binding trap + fix · mutable class attribute trap + fix · `dis` output
- Anti-pattern blocks: mutable default *(exists)* · late-binding closure · blocking call in event loop · bare `except`

**Q&A target:** 10 → **33**. Keep all 10.

**Canonical questions to include (sourced):**
- Why does the GIL exist and what does PEP 703 change? *(exists)*
- `__slots__` — mechanism and savings. *(exists)*
- Shallow vs deep copy. *(exists)* · Generators and `PyFrameObject`. *(exists)*
- `*args` vs `**kwargs`. *(exists)* · `functools.wraps`. *(exists)*
- Cyclic GC trial-refcount algorithm. *(exists)* · MRO / C3 linearization. *(exists)*
- List comprehension vs generator expression. *(exists)* · True CPU parallelism. *(exists)*
- Write a decorator that retries a function 3 times with backoff.
- Write a decorator that takes an argument.
- Implement a context manager two different ways.
- `@staticmethod` vs `@classmethod` vs instance method — pick one for a factory.
- Why can a list not be a dict key?
- If you override `__eq__`, what else must you do?
- `is` vs `==` — and why does `256 is 256` differ from `257 is 257`? *(exists)*
- What is a descriptor? Name one you use every day. *(`@property`)*
- `threading` vs `multiprocessing` vs `asyncio` — pick one for each of three workloads. *(table exists)*
- What happens if you call `time.sleep()` inside a coroutine?
- `fork` vs `spawn` — why does macOS default to spawn?
- Is `dict` ordered? Since when, and is it guaranteed?

---

### 6.10 `ai_agents` — RAG, Agents & GenAI System Design · **P0** · Track C

**Current state:** 3 tables (vector DB matrix, agent frameworks, bi-encoder vs cross-encoder), 2 excellent SVGs (advanced RAG with hybrid retrieval + RRF + reranking; LangGraph cyclic state machine modelling the candidate's own Uplan project), HNSW explanation, RRF formula, naive-RAG failure modes incl. "Lost in the Middle", RAG Triad, 5 flashcards.

**Verdict:** conceptually the most modern module on the site and the LangGraph SVG tied to a real project is a genuine asset. Two structural problems: **zero code blocks in the entire module**, and transformer fundamentals are assumed rather than taught.

> **Scope note:** transformer internals move to the new `llm_internals` (§7.4). Evaluation moves to the new `ai_evals` (§7.6). This module keeps retrieval, agents, and GenAI system design. Cross-link all three.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Chunking strategy table** | Fixed / recursive / semantic / markdown-aware / parent-document, with real token sizes and overlap. Chunk-boundary failure is named as a top-3 naive-RAG failure mode and there is no table |
| **Distance metrics** | Cosine vs dot vs L2, and the normalization requirement that makes cosine and dot equivalent. Absent |
| **IVF-PQ / product quantization** | Promised in `MODULES_META`, missing. HNSW is covered; the memory-vs-recall tradeoff with PQ is the other half |
| **RAG vs fine-tune vs long-context vs agent** | A `decision_matrix`. Research lists this as a top-tier question in *every* AI loop |
| **Prompting taxonomy** | Zero/few-shot, CoT, self-consistency, ReAct, ToT — with when each is worth the tokens |
| **Decoding parameters** | Temperature, top-k, top-p, repetition penalty, and what each does to the distribution |
| **Context rot** | Performance degrades well *before* the hard window limit, so a bigger window is not a licence to stuff context. Research flags it as a term *"very few candidates know"* |

**Must-add — Deep tier:**

1. **Code — the module currently has none.** Add: a LangGraph `StateGraph` with `TypedDict` state + `add_conditional_edges` + recursion limit (making the existing SVG concrete), a hybrid retriever with RRF merge, a cross-encoder rerank step, a chunking function with token-boundary awareness, a tool-calling loop with a step budget and repeated-call detection, and structured-output enforcement with a JSON schema.
2. **Agent architecture depth** — ReAct vs plan-and-execute vs reflexion, memory (short-term buffer / summarization / long-term vector / entity), multi-agent topologies (supervisor, swarm, hierarchical, debate), handoffs, human-in-the-loop checkpoints, and **MCP** (Model Context Protocol) since it is now standard tooling.
3. **Agent failure modes + mitigations** — infinite loops (one flashcard exists; expand), hallucinated tool names, malformed arguments, cost runaway, partial failure mid-plan, and **retry with idempotency**.
4. **Enterprise RAG** — per-user access control enforced **in retrieval, before generation** (never rely on the model to withhold), permission sync with the source system, multi-tenancy, PII redaction, and freshness/incremental indexing.
5. **Advanced retrieval** — HyDE, query decomposition, step-back prompting, multi-query, ColBERT late interaction, GraphRAG, small-to-big / parent-document (flashcard exists — promote), metadata filtering pre vs post vs single-stage filtered HNSW (flashcard exists — promote).
6. **Serving & cost** — latency budget decomposition (TTFT vs inter-token), streaming, semantic caching, prompt caching, batching, and a worked token-cost model. Cross-link to `llm_internals` for vLLM/PagedAttention.
7. **Security** — prompt injection (direct and indirect), jailbreaks, tool-use privilege escalation, data exfiltration via retrieved content, output sanitization.
8. **GenAI system design walkthroughs (3 full)** — *"RAG over 10M internal docs with per-user access control"*, *"insurance-claims agent → approve/deny/needs-review with guardrails and cost control"*, *"code assistant over a large private codebase with a 2-second latency budget"*. All three are verbatim-sourced prompts.

**Required artifacts:**
- SVG: **HNSW vs IVF-PQ** side by side — graph traversal vs coarse-quantizer + PQ codes
- SVG: **agent memory architecture** — the four memory types and their read/write paths
- SVG: **multi-agent supervisor topology** with handoffs
- SVG: **enterprise RAG with ACL enforcement at retrieval**
- SVG: **latency budget waterfall** for one RAG request
- Code (8+, listed above)
- `decision_matrix()`: RAG vs fine-tune vs long-context vs agent · chunking strategies · vector DB selection
- `followup_chain()`: "your RAG returns irrelevant chunks — debug it" · "cut p95 latency in half without losing quality"

**Q&A target:** 5 → **33**. Keep all 5.

**Canonical questions to include (sourced verbatim where marked ★):**
- ★ When would you choose RAG vs fine-tuning vs long-context?
- ★ When is RAG the *wrong* tool? *(style change → fine-tune; small stable knowledge → prompt; needs an action → agent; cross-doc aggregation → structured query)*
- ★ Why might a model do *worse* with retrieved context than with none?
- ★ What is hybrid search, and when does pure vector retrieval fail? *(exact-match needs: product codes, error IDs, part numbers, rare acronyms)*
- ★ How do you handle permissions and access control in enterprise RAG?
- ★ What is context rot?
- Why can't you just add BM25 and cosine scores? *(exists — RRF)*
- HNSW vs IVFFlat — index build time, memory, recall. *(partially exists)*
- How do you stop a LangGraph agent from looping forever? *(exists)*
- ReAct vs native function calling. *(exists)*
- Pre-filtering vs post-filtering in vector search. *(exists)*
- Small-to-big / parent-document chunking. *(exists)*
- What is prompt injection and how do you defend a tool-using agent?
- Your agent calls the same tool 40 times. What are the three likely causes?
- Design a RAG system over 10M docs with per-user ACLs.

---

### 6.11 `ml_cv` — Computer Vision & Signal Processing · **P1** · Track C

**Current state:** 3 tables (metrics with formulas and a when-to-prioritize column, optimizers/losses incl. AdamW and Focal Loss, BatchNorm vs LayerNorm with normalization dimensions), 2 good SVGs (CNN pipeline with tensor shapes at every stage; HOG extraction tied to the candidate's K-HUKI project), conv output formula, VGG 3×3 parameter argument, ResNet identity-gradient proof, the ROC-AUC-on-imbalanced-data trap with real arithmetic, 5 flashcards (NMS, Canny 5 stages, data leakage, HOG invariance, transposed conv).

**Verdict:** the classical-CV content is strong and the HOG SVG is a genuine differentiator tied to real work. Two problems: **zero code blocks**, and the module is currently carrying ML fundamentals it cannot afford.

> **Scope change:** classical ML + DL fundamentals move out to the new `ml_core` (§7.3). This module becomes **Computer Vision & Signal Processing** — which also lets it carry your M.Tech signal-processing edge, currently nowhere on the site. Keep metrics/optimizers/norm tables here *only* as a Sprint-tier recap with a pointer to `ml_core`.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **IoU formula + the detection metric chain** | `mAP` is in the metrics table but **IoU itself is never defined**. IoU → NMS → AP → mAP@[.5:.95] as one chain |
| **Classical feature detectors** | SIFT / SURF / ORB / Harris corners — scale and rotation invariance properties. HOG is covered; the rest are absent |
| **Image filtering fundamentals** | Convolution vs correlation, kernel types (Gaussian, Sobel, Laplacian, box), separable kernels and the cost saving, padding/stride |
| **Morphological operations** | Erosion, dilation, opening, closing — and what each fixes |
| **Histogram equalization + CLAHE** | Standard preprocessing question |
| **Colour spaces** | RGB / HSV / YCbCr / Lab and why compression uses YCbCr |
| **Signal processing bridge** | Sampling + Nyquist, FFT and the convolution theorem, filter types (FIR/IIR, low/high/band), windowing, aliasing. **Your M.Tech specialization is currently invisible on this site** |

**Must-add — Deep tier:**

1. **Code — the module currently has none.** Add: IoU, NMS (full), conv2d from scratch in NumPy, Sobel/Canny with OpenCV, HOG with scikit-image, a `nn.Module` CNN, a training loop with validation, and a Dice/IoU loss.
2. **CNN architecture lineage** — AlexNet → VGG → Inception (1×1 bottleneck, multi-scale) → ResNet (bottleneck block) → MobileNet (depthwise separable, with the parameter arithmetic) → EfficientNet (compound scaling). Plus parameter/FLOP counting worked for one layer, receptive-field computation, and dilated/grouped/depthwise conv.
3. **Object detection families** — R-CNN → Fast → Faster (RPN, anchors) → YOLO (grid, anchor-free variants) → SSD → DETR (set prediction, Hungarian matching). With the two-stage vs one-stage accuracy/latency tradeoff.
4. **Segmentation** — FCN, U-Net (skip connections, and why they matter differently than in ResNet), Mask R-CNN, DeepLab/ASPP; semantic vs instance vs panoptic; Dice vs IoU loss and class imbalance.
5. **Vision transformers** — patch embedding, `[CLS]` token, why ViT needs more data than a CNN, and the CNN-vs-ViT inductive-bias argument. Cross-link to `llm_internals`.
6. **Multimodal** — CLIP/SigLIP contrastive training, LLaVA-style projection into an LLM, and VLA models (discrete action tokens vs flow-matching heads). Research newly promoted these from specialty to expected *breadth*.
7. **Generative vision** — DDPM forward/reverse process, latent diffusion, DiT, classifier-free guidance, flow matching / rectified flow, and diffusion vs autoregressive. **Your SDE/denoising background is a direct advantage here** — write it to exploit that.
8. **Geometric vision** — camera intrinsics/extrinsics, calibration, homography, epipolar geometry, stereo disparity, and the pinhole model.
9. **Tracking** — optical flow (Lucas-Kanade, Farnebäck), Kalman filter (and its signal-processing roots), SORT/DeepSORT.
10. **Edge deployment** — quantization (PTQ vs QAT), pruning (structured vs unstructured), distillation, ONNX/TensorRT, and DSP/NPU targeting. Qualcomm CV/DSP is a named target company and this is absent.

**Required artifacts:**
- SVG: **IoU + NMS** visual with overlapping boxes and suppression order
- SVG: **U-Net** encoder-decoder with skip connections
- SVG: **Depthwise-separable conv** vs standard conv with the parameter counts
- SVG: **ViT patch embedding** pipeline
- SVG: **Diffusion forward/reverse** process
- SVG: **FFT / convolution theorem** — spatial conv ≡ frequency multiply
- Code (10+, listed above)
- Worked examples (5): conv output shape chain · parameter count for one conv layer · receptive field · IoU by hand · FLOP count
- Keep the HOG SVG and the ROC-AUC trap verbatim — both are excellent

**Q&A target:** 5 → **30**. Keep all 5.

**Canonical questions to include (sourced):**
- NMS — walk through the algorithm. *(exists)* · Canny's 5 stages. *(exists)*
- Data leakage in K-fold. *(exists — may move to `ml_core`)*
- Why is HOG illumination-invariant? *(exists)*
- Transposed conv vs bilinear upsampling, and checkerboard artifacts. *(exists)*
- Define IoU. Why report mAP@[.5:.95] instead of mAP@0.5?
- Why are two 3×3 convs preferred over one 5×5? *(deep dive exists — promote)*
- Compute the receptive field after three 3×3 convs with stride 2 in between.
- Why does BatchNorm hurt at batch size 2, and what do you use instead? *(table exists)*
- Two-stage vs one-stage detectors — what are you trading?
- Why do U-Net skip connections matter *differently* than ResNet's?
- Why does ViT need more data than a ResNet?
- How does CLIP learn without labels?
- Diffusion vs autoregressive generation — when is each used?
- What is classifier-free guidance?
- How do you deploy a 25M-parameter model on a DSP with 2MB of SRAM?
- What is aliasing, and how does Nyquist decide your sampling rate?

---

### 6.12 `docker` — Docker, Kubernetes & CI/CD · **P1** · Track D

**Current state:** 3 tables (containers vs VMs, a 5-row CLI table, Linux primitives), 2 good SVGs (VM vs Docker stack; OverlayFS union mount), 3 code blocks (a genuinely good multi-stage Dockerfile with non-root user, ENTRYPOINT/CMD override demo, layer-cache ordering), 5 flashcards including the OverlayFS whiteout-file answer.

**Verdict:** the container-internals content (namespaces, cgroups, OverlayFS, whiteouts) is accurate and better than most tutorials. But the module is titled "Docker, Containers & **DevOps**" and contains **zero Kubernetes, zero compose, and zero CI/CD** — and the CLI table delivers 5 of the promised 15 rows.

**Must-add — Sprint tier:**

| Topic | Why |
| :-- | :-- |
| **Complete the CLI table to 15+ rows** | Honour the claim. Add `ps`, `images`, `pull/push`, `stop/rm/rmi`, `inspect`, `stats`, `cp`, `tag`, `network`, `volume` |
| **docker-compose** | Services, `depends_on`, `healthcheck`, networks, volumes, env files. Completely absent |
| **Kubernetes core objects** | Pod / ReplicaSet / Deployment / Service (ClusterIP/NodePort/LoadBalancer) / Ingress / ConfigMap / Secret / StatefulSet / DaemonSet / Job / CronJob — one row each. **The single biggest gap in the module** |
| **K8s control plane** | API server, etcd, scheduler, controller manager, kubelet, kube-proxy — and the reconciliation loop as the core mental model |
| **Probes** | Liveness vs readiness vs startup, and what each failure does |
| **Remaining namespaces** | UTS, IPC, USER, cgroup, time — only PID/NET/MNT are covered. Plus rootless Docker and user-namespace remapping |
| **`ARG` vs `ENV`, `.dockerignore`, `HEALTHCHECK`, shell vs exec form** | High-frequency Dockerfile semantics |

**Must-add — Deep tier:**

1. **Kubernetes depth** — rolling update strategy (`maxSurge`/`maxUnavailable`), HPA (and what metric), resource requests vs limits and the QoS classes (Guaranteed/Burstable/BestEffort), **why a memory limit means OOMKill but a CPU limit means throttling**, taints/tolerations, affinity/anti-affinity, PV/PVC/StorageClass, RBAC, namespaces, and real manifest YAML for a Deployment + Service + Ingress.
2. **CI/CD** — GitHub Actions workflow syntax (the one you will actually use), the build→test→scan→push→deploy pipeline, caching layers in CI, matrix builds, secrets handling, and blue-green vs canary vs rolling deploys.
3. **Image security** — distroless vs Alpine vs slim (and the musl/glibc gotcha), Trivy/Snyk scanning, image signing, SBOM, and **the trap that build-args leak into layer history** — so a secret passed via `--build-arg` is recoverable from the image.
4. **cgroups v1 vs v2**, `--memory`/`--cpus`/`--pids-limit`, and how the OOM killer picks a victim.
5. **BuildKit** — cache mounts, secret mounts, multi-arch `buildx`, and parallel stage execution.
6. **Registry internals** — manifests, digests vs tags, layer deduplication, content-addressable storage, and why `:latest` is unsafe.
7. **OCI + runtimes** — the spec, `runc` vs `crun` vs `gVisor` vs Kata, and the isolation/performance tradeoff.
8. **Networking** — bridge/host/none *(exists)* plus overlay, macvlan, ipvlan; the CNI model; K8s Service → Endpoint → iptables/IPVS path; DNS inside a cluster.
9. **Observability** — Prometheus metrics + scrape model, Grafana, structured logging, the ELK/Loki path, and container logging drivers.
10. **IaC** — Terraform state and plan/apply, and where Ansible fits. Keep this short; it is breadth, not depth.

**Required artifacts:**
- SVG: **Kubernetes architecture** — control plane vs node components with the reconciliation loop
- SVG: **Pod → Service → Ingress** request path
- SVG: **Rolling update timeline** with `maxSurge`/`maxUnavailable`
- SVG: **CI/CD pipeline** stages with the gates
- Code: `docker-compose.yml` · Deployment + Service + Ingress manifests · HPA manifest · GitHub Actions workflow · multi-stage Dockerfile *(exists — keep)* · BuildKit secret mount
- `decision_matrix()`: Docker vs Compose vs Swarm vs K8s · volume types *(flashcard exists — promote)*
- Anti-pattern blocks: secret via `--build-arg` → BuildKit secret mount · `:latest` → pinned digest · root user → non-root *(flashcard exists)*

**Q&A target:** 5 → **30**. Keep all 5.

**Canonical questions to include (sourced):**
- Volumes vs bind mounts vs tmpfs. *(exists)*
- Bridge vs host vs none networking. *(exists)*
- Why never run a container as root? *(exists)*
- How does layer caching work, and what invalidates it? *(exists)*
- Why does deleting a file not shrink the image? *(exists — whiteout)*
- `CMD` vs `ENTRYPOINT` — what does each do on override? *(trap exists — promote)*
- Container exits with code 0 immediately. Diagnose. *(trap exists — promote)*
- What is a Pod, and why is it the unit rather than a container?
- Liveness vs readiness probe — which one takes you out of the load balancer?
- Your pod is `CrashLoopBackOff`. Walk me through debugging it.
- What happens when a container exceeds its memory limit? Its CPU limit?
- How does a Service find its Pods?
- Deployment vs StatefulSet — when do you need the latter?
- How do you get a secret into a build without baking it into the image?
- Docker Swarm vs Kubernetes.
- What does `kubectl apply` actually do differently from `create`?

---

## 7. New Module Specs — The 11 Additions

Same depth contract: 15 min Sprint / 60 min Deep. Format: **Why it exists → Sprint → Deep → Artifacts → Q&A → Canonical questions.**

---

### 7.1 `concurrency` — Concurrency & Parallelism · **P0** · Track A

`🧵` · badge `Cross-Language` · colour `indigo` · roles `SWE, AI`

**Why it exists:** concurrency is currently fragmented across `os` (primitives), `cpp_systems` (atomics/memory orders), and `python_internals` (GIL) with no unified treatment. Research shows Anthropic threads concurrency through **multiple rounds rather than one isolated question**, OpenAI names coroutines as a focus area, and LLD loops increasingly carry a dedicated concurrency round. The classic multithreading problems (Print FooBar, Building H2O, thread-safe cache with TTL, concurrent hashmap) appear nowhere on the site.

**Sprint tier:**
- Concurrency vs parallelism vs asynchrony — the three-way distinction, stated precisely
- Race condition / data race / deadlock / livelock / starvation / priority inversion — one row each with a minimal repro
- Primitive selection matrix: mutex · recursive mutex · reader-writer lock · semaphore · condition variable · barrier · latch · spinlock · atomic — *use when / avoid when*
- Memory model crash course: atomicity vs visibility vs ordering; why `volatile` ≠ thread-safe in C++/Java; happens-before
- CAS and the ABA problem (cross-link `cpp_systems`)
- Amdahl's Law applied to threading, and the contention point where more threads make things slower
- Thread pool sizing: `N_cpu` for CPU-bound vs `N_cpu × (1 + wait/compute)` for I/O-bound
- Language comparison table: C++ `std::thread` · Python GIL/asyncio · Java/JVM · Go goroutines+channels — what each gives you and what it costs

**Deep tier:**
1. **The classic coordination problems, implemented** — Print FooBar alternately, Print Zero-Even-Odd, FizzBuzz multithreaded, Building H2O, Dining Philosophers. These are *literal* interview questions at Anthropic-class companies. C++ and Python versions.
2. **Thread-safe data structures, implemented** — blocking bounded queue (condition variables, both-ends), thread-safe cache with TTL, concurrent hash map with striped locks, thread pool from scratch, and a concurrent counter three ways (mutex / atomic / per-thread sharded) with the contention comparison.
3. **Lock-free programming** — SPSC ring buffer (shared with `cpp_systems`), MPMC considerations, the ABA problem + tagged pointers, hazard pointers and epoch-based reclamation at a conceptual level, and **when lock-free is the wrong answer** (it usually is).
4. **Lock granularity and contention** — coarse → fine → striped → lock-free as a progression with the cost of each step; reentrancy; try-lock and timed-lock; lock ordering as the practical deadlock defence; convoy effect.
5. **Async models** — event loop, callbacks → futures → async/await, coroutines (stackful vs stackless), `epoll`/`io_uring`, and the C10K problem. Cross-link `cn` and `python_internals`.
6. **Parallel patterns** — fork-join, map-reduce, pipeline, work stealing, producer-consumer, scatter-gather, and parallel merge sort implemented.
7. **False sharing in practice** — the measurement, not just the theory. Cross-link `coa`.
8. **Debugging concurrency** — TSan, race detectors, why `printf` debugging changes the bug, stress testing, deterministic replay, and the fact that a passing test proves nothing.
9. **Distributed concurrency bridge** — optimistic vs pessimistic locking, distributed locks and fencing tokens. Cross-link `system_design` and `dbms`.

**Artifacts:** SVG — happens-before / reordering visualization · SVG — striped locking vs single mutex · SVG — thread pool with work queue and stealing · SVG — producer-consumer with a bounded buffer and both wait conditions · Code 14+ (all problems above) · `followup_chain()`: "make this counter thread-safe" → "it's now slower than single-threaded, why" → "fix it without a lock" · `decision_matrix()`: primitive selection · Anti-patterns: double-checked locking · `if (!ready) wait()` without a loop (spurious wakeup) · lock held across I/O

**Q&A target: 32.**

**Canonical questions:**
- Concurrency vs parallelism — one sentence each.
- Race condition vs data race — are they the same thing?
- Mutex vs semaphore vs condition variable — pick one for each of three scenarios.
- Why must `wait()` always be in a `while` loop? *(spurious wakeups)*
- What is a livelock? Give an example that is not a deadlock.
- Print FooBar alternately with two threads. *(implement)*
- Implement a bounded blocking queue.
- Implement a thread-safe LRU cache with TTL.
- How many threads for a CPU-bound task? For an I/O-bound task? Derive it.
- Your 8-thread version is slower than 1 thread. Give four possible causes.
- What is false sharing and how do you prove it is happening?
- Is `volatile` enough for thread safety in C++? In Java?
- What does `memory_order_relaxed` *not* guarantee?
- When is lock-free actually worse than a mutex?
- How do you test concurrent code? Why does a green test suite not help?

---

### 7.2 `api_security` — API Design, Auth & Security · **P1** · Track B

`🔐` · badge `Interfaces & Trust` · colour `amber` · roles `SWE, FDE`

**Why it exists:** completely absent from the site. `system_design` touches rate limiting and idempotency; nothing covers API contract design, auth, or the OWASP surface. FDE roles are explicitly API-and-integration jobs, and the Palantir HackerRank screen includes a REST API task.

**Sprint tier:**
- REST resource modelling: nouns not verbs, correct status-code families, and the full idempotency/safety matrix for GET/POST/PUT/PATCH/DELETE
- REST vs gRPC vs GraphQL vs WebSocket vs SSE vs webhooks — `decision_matrix`
- Pagination: offset vs cursor vs keyset — and why offset breaks on a mutating dataset
- Versioning: URL path vs header vs content negotiation, and deprecation policy
- Idempotency keys — the design, the storage, the expiry (cross-link `system_design`)
- AuthN vs AuthZ. Session vs JWT: the stateless/revocation tradeoff, access + refresh token pattern, where to store a token in a browser and why `localStorage` is the wrong answer
- OAuth 2.0 authorization-code + PKCE flow, and OIDC vs OAuth
- RBAC vs ABAC vs ReBAC
- OWASP Top 10 — one row each with the concrete defence
- TLS essentials: what it guarantees, cert chain, mTLS (cross-link `cn`)

**Deep tier:**
1. **API contract design** — OpenAPI schema, request validation, error-response shape (RFC 7807 problem details), partial failure, bulk endpoints, long-running operations (202 + polling vs callback), and backwards-compatibility rules.
2. **gRPC depth** — protobuf schema evolution rules, the four streaming modes, deadlines vs timeouts, interceptors, and when gRPC beats REST.
3. **JWT internals** — header/payload/signature, `HS256` vs `RS256`, the **`alg: none` attack**, signature-stripping, key rotation via `kid`/JWKS, and why you cannot revoke a JWT without reintroducing state.
4. **OAuth flows in full** — authorization code + PKCE, client credentials, device code, and the deprecated implicit/password flows with *why* they were deprecated. Plus token introspection and scopes vs claims.
5. **Injection classes** — SQL injection with the prepared-statement mechanism (cross-link `dbms`), command injection, SSRF (and why it is the cloud-metadata killer), XXE, path traversal, deserialization. One anti-pattern block each for the top four.
6. **Browser-side** — XSS (stored/reflected/DOM) + CSP, CSRF + SameSite cookies + double-submit, CORS preflight explained properly (it is not a security feature *for your server*), clickjacking.
7. **Secrets management** — env vars vs secret managers, rotation, the build-arg leak (cross-link `docker`), and what to do when a key is committed.
8. **Crypto hygiene** — hashing vs encryption vs encoding, password hashing (bcrypt/scrypt/Argon2 and *why not* SHA-256), salting, HMAC, symmetric vs asymmetric, encryption at rest vs in transit. Plus timing attacks and constant-time comparison.
9. **Abuse controls** — rate limiting by tier, quotas, WAF, bot detection, DDoS layers, and request signing for webhooks.
10. **Multi-tenancy & data isolation** — row-level security, tenant-scoped keys, and the noisy-neighbour problem. **This is the FDE-relevant section** — Palantir's design round centres on *integration across systems plus isolation/governance of multi-party data*.

**Artifacts:** SVG — OAuth 2.0 auth-code + PKCE sequence · SVG — JWT structure with the signature-verification path · SVG — CORS preflight sequence · SVG — multi-tenant isolation models (silo / bridge / pool) · Code — JWT verify done right · prepared statement vs concatenation · CSP header · idempotency-key handler · HMAC webhook verification · Worked example — design the API for a given feature end to end · `decision_matrix()`: protocol choice · token strategy · pagination strategy

**Q&A target: 30.**

**Canonical questions:**
- Is `PUT` idempotent? Is `POST`? Is `DELETE`?
- Design a REST API for a movie-booking service. Now version it.
- Offset vs cursor pagination — why does offset break?
- Session vs JWT — which one can you revoke, and what does that cost you?
- Walk through the OAuth authorization-code flow. What does PKCE add?
- Where do you store an access token in a browser?
- What is the `alg: none` JWT attack?
- Why is bcrypt better than SHA-256 for passwords?
- Explain CSRF. Does `SameSite=Lax` fully fix it?
- Is CORS protecting my server?
- What is SSRF and why is it catastrophic in a cloud environment?
- How do you make a payment endpoint safe to retry?
- gRPC vs REST — pick one for service-to-service, and justify it.
- How do you isolate two customers' data in one deployment?
- You find an API key in git history. What are your next five actions?

---

### 7.3 `ml_core` — Classical ML & Deep Learning Core · **P0** · Track C

`📊` · badge `ML Foundations` · colour `orange` · roles `AI`

**Why it exists:** the audit found `ml_cv` contains **zero classical ML** — no bias-variance, no regularization, no trees/ensembles, no PCA, no cross-validation, no backprop derivation, no optimizer progression, no activations, no initialization, no dropout. That set is the floor at every big-tech AI loop and the first thing an Applied Scientist round tests. It cannot be appended to a CV module without destroying the time budget.

**Sprint tier:**
- The supervised/unsupervised/self-supervised/RL map, and where LLMs sit
- **Bias-variance decomposition** — stated, decomposed, and connected to model capacity
- Overfitting/underfitting diagnosis from learning curves — the single most practically useful table
- Regularization: L1 vs L2 (the sparsity geometry argument), dropout, early stopping, data augmentation, weight decay vs L2 (they differ under Adam — this is the AdamW point already in `ml_cv`)
- Metrics under imbalance: precision/recall/F1/ROC-AUC/PR-AUC, threshold tuning, calibration. Keep the existing ROC-AUC trap, cross-linked
- Cross-validation: k-fold, stratified, group, time-series split — and the leakage each prevents
- Algorithm selection matrix: linear/logistic · SVM · trees · Random Forest · GBDT/XGBoost · KNN · Naive Bayes · k-means · PCA — *use when / avoid when / key hyperparameter*
- Bagging vs boosting vs stacking — the variance-vs-bias framing
- Activation comparison: sigmoid · tanh · ReLU · LeakyReLU · GELU · SwiGLU — with dying ReLU and the saturation problem
- Optimizer progression: SGD → momentum → Nesterov → Adagrad → RMSProp → Adam → AdamW, each fixing the previous one's named flaw

**Deep tier:**
1. **Derivations that get asked** — linear regression normal equation + the MLE view, logistic regression gradient (full), the cross-entropy gradient simplifying to `ŷ − y` (and *why* that is elegant), SVM margin maximization + the kernel trick, and the bias-variance decomposition algebra.
2. **Backpropagation from scratch** — chain rule through a 2-layer net, written in NumPy forward *and* backward. Research lists this verbatim: *"Write in plain NumPy the forward and backward pass for a two-layer feed-forward neural network with a ReLU layer in between."*
3. **Tree methods properly** — Gini vs entropy vs information gain (computed), CART splitting, pruning, feature importance and its bias, Random Forest (bootstrap + feature subsampling, OOB error), AdaBoost reweighting, gradient boosting as residual fitting, and XGBoost's specific additions (second-order, regularized objective, sparsity-aware splits).
4. **Unsupervised** — k-means (+ k-means++, elbow, silhouette, and the failure cases), hierarchical clustering, DBSCAN, GMM/EM, PCA from the eigendecomposition *and* SVD view (cross-link `math_ml`), t-SNE vs UMAP and why neither preserves global distance.
5. **Training dynamics** — vanishing/exploding gradients, gradient clipping, weight initialization (Xavier vs He, with the variance argument), BatchNorm vs LayerNorm vs RMSNorm (table exists in `ml_cv` — own it here), learning-rate schedules (step/cosine/warmup, and *why* warmup), and batch-size/LR scaling.
6. **Imbalance remedies** — class weights, resampling, SMOTE, focal loss (formula exists in `ml_cv`), threshold moving — and when each is the wrong choice.
7. **Feature engineering** — scaling (fit on train only — the leakage point), encoding (one-hot vs target vs ordinal), binning, interactions, missing-value strategies, and leakage taxonomy.
8. **Embeddings & metric learning** — promised in `ml_cv`'s `MODULES_META` and never delivered. Triplet loss, contrastive/InfoNCE, siamese networks, negative sampling and hard-negative mining, cosine vs dot vs L2 for embeddings.
9. **Recommenders** — collaborative vs content-based, matrix factorization, implicit feedback, and the cold-start problem.
10. **The 9-step ML system design framework**, verbatim-sourced, to recite out loud: problem formulation → metrics (offline + online) → architecture/MVP → data collection → feature engineering → model dev + offline eval → prediction service → online testing/deployment → scaling, monitoring, updates. Then apply it to two full designs (e.g. a feed ranker and a fraud detector).

**Artifacts:** SVG — bias-variance tradeoff curve with the capacity axis · SVG — L1 vs L2 constraint geometry (why L1 hits the axes) · SVG — backprop computation graph with gradients labelled on the edges · SVG — bagging vs boosting data flow · SVG — k-means iteration steps · SVG — the 9-step ML system design pipeline · Code 14+: NumPy 2-layer net forward+backward · NumPy dropout forward+backward · stable softmax + cross-entropy · logistic regression with GD · k-means · PCA via SVD · k-NN · decision-tree Gini split · gradient-boosting residual step · ROC-AUC from scratch · train/val/test split without leakage · standardization using train statistics only · triplet loss · InfoNCE · Worked examples (6): bias-variance on a concrete model · information gain for one split · ROC-AUC by hand on 6 points · PCA on a 2×2 covariance matrix · gradient descent two steps by hand · confusion-matrix metric chain

**Q&A target: 35.**

**Canonical questions (★ = sourced verbatim):**
- Explain the bias-variance tradeoff. Where does regularization sit?
- L1 vs L2 — why does L1 produce sparsity?
- ★ *"Why shouldn't we have two consecutive linear layers in a neural network?"*
- ★ *"Can a network with only ReLU act as a linear classifier?"*
- ★ *"Design the smallest neural network that can function as an XOR gate."*
- ★ *"When building a neural network, should you overfit or underfit it first?"*
- ★ *"Your validation loss is often lower than your train loss. What might be happening?"* *(dropout/augmentation active at train time; loss averaged differently)*
- ★ *"How should we adjust the learning rate as we increase or decrease the batch size?"*
- ★ *"What's learning rate warmup? Why do we need it?"*
- ★ *"Compare batch norm and layer norm."*
- ★ *"Why is squared L2 norm sometimes preferred to L2 norm for regularizing?"*
- ★ *"Why is Adagrad favored with sparse gradients?"*
- ★ *"Adam vs SGD — convergence and generalization?"*
- ★ *"Why distill a big model instead of just training a small one from the beginning?"*
- ★ Dead neurons — what are they, how do you detect them, how do you prevent them?
- ★ *"It's common practice to train using epochs (sampling without replacement). Why not just sample with replacement?"*
- Bagging vs boosting — which reduces variance and which reduces bias?
- Why does Random Forest subsample features and not just rows?
- Your model has 99% accuracy on a 1%-positive dataset. What do you report instead?
- Walk me through backprop for a 2-layer net. *(implement)*
- Why Xavier vs He initialization?
- How do you detect data leakage in a pipeline? *(cross-link)*
- k-means vs DBSCAN vs GMM — pick one for three dataset shapes.
- Explain PCA two ways: eigendecomposition and SVD.

---

### 7.4 `llm_internals` — LLM & Transformer Internals · **P0** · Track C

`🧠` · badge `Frontier AI` · colour `rose` · roles `AI`

**Why it exists:** the single most important new module. Research: *"The biggest shift in 2026 ML interviews: LLMs / foundation models are now expected **breadth**, not a specialty."* The site has `ai_agents` (applications) but **nothing** on attention math, KV cache, positional encodings, tokenization, post-training, or quantization. These are now baseline questions.

**Sprint tier:**
- Transformer block anatomy — attention → residual → norm → FFN → residual → norm, with pre-norm vs post-norm
- **Scaled dot-product attention** in a `formula_box`: `Attention(Q,K,V) = softmax(QKᵀ/√d_k)V`, every symbol defined, **and why `√d_k`** (keeps softmax out of saturation → stable gradients)
- Multi-head attention, and the shape walkthrough `[B, T, d] → [B, h, T, d_h]`
- **MHA vs MQA vs GQA** — KV head count, memory saved, quality cost, and why Llama chose GQA
- **KV cache** — what it stores, why inference is O(n) per token instead of O(n²), and the memory formula `2 × layers × heads × d_head × seq × batch × bytes`
- Positional encoding: sinusoidal vs learned vs **RoPE** vs ALiBi, and why rotary won
- Tokenization: BPE vs WordPiece vs SentencePiece/Unigram; vocabulary size tradeoff; **non-English text costing 2–3× more tokens**; truncate on token boundaries not character boundaries
- Decoder-only vs encoder-only vs encoder-decoder — and which task shape each fits
- Decoding: greedy · beam · temperature · top-k · top-p · min-p · repetition penalty, with what each does to the distribution
- Training stages: pretrain → SFT → preference optimization → (optional) RLVR
- **Post-training selection matrix:** SFT · RLHF-PPO · DPO · SimPO · KTO · ORPO · GRPO · RLVR — data required, extra models required, when to use
- PEFT: LoRA (and the rank/alpha meaning), QLoRA, adapters, prefix tuning — vs full fine-tuning
- Quantization: INT8/INT4/FP8, PTQ vs QAT, GPTQ/AWQ/GGUF, **KV-cache quantization**
- Scaling laws + Chinchilla-optimal, and compute `≈ 6ND`

**Deep tier:**
1. **Attention implemented** — scaled dot-product with masking applied *before* a numerically stable softmax, multi-head with reshape/transpose, causal mask construction, and an append-only KV cache. All four are in the sourced drill list with company tags (Anthropic, OpenAI, Meta, Perplexity).
2. **FlashAttention** — the tiling/recomputation idea, why it is IO-bound not FLOP-bound, and the memory complexity change from O(n²) to O(n).
3. **Efficiency variants** — sliding-window/local attention, sparse attention, linear attention, **MoE** (routing, top-k gating, load-balancing loss, and **active vs total parameters** — a specifically named question), and Mamba/SSM at a conceptual level.
4. **Modern architecture details** — RMSNorm vs LayerNorm, SwiGLU vs GELU, weight tying (sourced: *"some NLP models use the same weights for the embedding layer and the layer before softmax — what's the purpose?"*), and why bias terms got dropped.
5. **Post-training depth** — RLHF pipeline (reward model → PPO), DPO's derivation intuition (implicit reward, no reward model), **GRPO: why the critic is dropped and how the advantage is group-normalized** (named a central 2026 theme), RLVR for verifiable domains, and the scale-dependence nuance (online RL can win at ~1.5B while SimPO wins at ~7B — citing that nuance reads as real understanding).
6. **LoRA mathematics** — `W + BA` with rank `r`, the parameter-count arithmetic, why it merges at inference with zero latency cost, and QLoRA's NF4 + double quantization + paged optimizers.
7. **Inference serving** — vLLM and **PagedAttention** (KV cache as virtual memory with blocks), continuous batching vs static batching, speculative decoding (draft + verify), prefill vs decode phases, **TTFT vs inter-token latency**, and the throughput-vs-latency tradeoff. Then a worked latency/cost budget.
8. **Long context** — position interpolation, YaRN, the needle-in-haystack test, **"Lost in the Middle"** (cross-link `ai_agents`), and **context rot** — degradation well before the hard limit.
9. **Multimodal** — vision encoder + projector + LLM (LLaVA pattern), CLIP/SigLIP contrastive pretraining, and VLA models: discrete action tokens (RT-2, OpenVLA) vs flow-matching action heads (π0). Cross-link `ml_cv`.
10. **Information-theory corner — your edge.** Entropy, cross-entropy, KL divergence, perplexity (and the relation `perplexity = exp(cross-entropy)`), and label smoothing. OpenAI's coding round reportedly asks you to **implement KL divergence for continuous distributions**, expected iterations of a probabilistic function, and minimum error via cross-entropy. The research explicitly names this a blind spot for general candidates — and it is your M.Tech coursework. **Write this section to be exploited.**
11. **Diffusion vs autoregressive** — DDPM, latent diffusion, DiT, classifier-free guidance, flow matching / rectified flow. Cross-link `ml_cv`; keep the math here.

**Artifacts:** SVG — full transformer block with tensor shapes annotated at every arrow · SVG — attention matrix with a causal mask applied · SVG — MHA vs MQA vs GQA KV-head layout side by side · SVG — KV cache growth across decode steps · SVG — RoPE rotation in 2D · SVG — MoE top-2 routing · SVG — PagedAttention block table · SVG — speculative decoding draft/verify timeline · Code 12+: scaled dot-product attention · causal mask · multi-head reshape · KV cache append · sinusoidal PE · RoPE application · BPE learn + apply · temperature/top-k/top-p sampling · LoRA linear layer update · DPO loss · InfoNCE/symmetric contrastive loss · KL divergence (discrete + continuous) · perplexity · Worked examples (7): KV cache memory for a concrete config · attention FLOPs · LoRA parameter count vs full fine-tune · Chinchilla-optimal tokens for a given N · token cost for a given workload · perplexity from a loss value · GQA memory saving

**Q&A target: 35.** All sourced.

**Canonical questions (all ★ sourced verbatim):**
- *"Walk through a transformer block. Why divide attention scores by √dₖ?"*
- *"What is the KV cache and why does it matter for inference? How does its memory scale?"*
- *"Compare MHA, MQA, and GQA. Why did Llama adopt GQA?"*
- *"What is RoPE and why are rotary embeddings preferred over learned positional embeddings?"*
- *"When would you choose RAG vs fine-tuning vs long-context?"*
- *"Compare SFT, DPO, GRPO, and RLVR — data requirements, what extra models each needs, and when to use each."*
- *"Why does GRPO drop the critic network, and how does it estimate advantage?"*
- *"What is LoRA / QLoRA and when would you use PEFT over full fine-tuning?"*
- *"Explain quantization (INT8/INT4, FP8) and KV-cache quantization. What's the accuracy/latency tradeoff?"*
- *"How does speculative decoding speed up generation?"*
- *"What is a Mixture-of-Experts model? Distinguish active vs total parameters."*
- *"How does a VLM combine a vision encoder with an LLM?"*
- *"What is a VLA model? Contrast discrete action tokens vs flow-matching action heads."*
- *"Diffusion vs autoregressive generation — how do they differ and when is each used?"*
- *"What is classifier-free guidance?"* · *"What is flow matching / rectified flow?"*
- *"Why do many models use relative position embedding instead of absolute?"*
- *"Some NLP models use the same weights for both the embedding layer and the layer just before softmax. What's the purpose?"*
- *"What problems might we encounter when using softmax as the last layer for word-level LMs? How do we fix it?"*
- *"On the same test set, LM A has character-level entropy 2 while LM B has word-level entropy 6. Which would you deploy?"*
- *"Your client's dataset has only ~10,000 tokens. Would you use an n-gram or a neural LM?"*
- *"Under what conditions would it be possible to recover training data from the weight checkpoints?"*
- Implement KL divergence for continuous distributions and interpret the result.
- Compute the KV cache size for 70B / 80 layers / 64 heads / 128 head-dim / 8K context / batch 16 in FP16.
- What is context rot, and what does it imply about a 1M-token window?

---

### 7.5 `ai_evals` — AI Evaluation, Observability & MLOps · **P0** · Track C

`📈` · badge `The Differentiator` · colour `emerald` · roles `AI, FDE`

**Why it exists:** the research is blunt and repeated — evaluation is *"the single biggest skill gap in candidates"*, *"eval is the new system design"*, and *"shipping a demo with zero evaluation is the most common reason strong-looking take-homes get rejected."* OpenAI's FDE deep dive uses **"how do you know your AI system is actually working well?"** as an explicit differentiator. One subsection inside `ai_agents` does not match that weight. This is the highest marginal-return module on the entire site for AI and FDE loops.

**Sprint tier:**
- The eval hierarchy: unit → component → end-to-end → online. What each catches and what it cannot
- **Code-based graders before model-based graders** — *"push as much of the evaluation as possible into deterministic code before falling back to a judge."* Almost no candidate says this; say it first
- Building a golden set: 15–30 hand-labelled examples split **answerable / partially answerable / unanswerable**
- **LLM-as-judge** — and the mandatory step everyone skips: **measure judge-vs-human agreement before you trust the judge.** Plus position bias, verbosity bias, self-preference bias, and pairwise vs pointwise scoring
- **RAG triad**: context relevance · groundedness/faithfulness · answer relevance (exists in `ai_agents` — own it here, cross-link back)
- Retrieval metrics: Recall@k · Precision@k · MRR · nDCG · hit rate — with what each is blind to
- **pass@k vs pass^k** — `pass@k` = ≥1 of k succeeds; **`pass^k` = all k independent attempts succeed**. For autonomous production tasks `pass^k` is the honest number. A named, rarely-known distinction
- **Agent trajectory evaluation** — final-output-only scoring *flatters* agents; a right answer via a broken path fails next time. Score tool selection, argument accuracy, step count, cost
- Classification/generation metric reference: accuracy family · BLEU/ROUGE/METEOR and their limits · BERTScore · exact match vs F1
- Offline gate + online monitor as a loop, not two separate things

**Deep tier:**
1. **Eval harness implemented** — a dataset schema, a runner, deterministic graders, a judge grader with an agreement check against human labels, per-slice reporting, and regression-vs-baseline diffing. Code, not prose.
2. **Reward hacking / eval gaming** — how metrics get gamed, and the defences: held-out sets, adversarial evals, multiple diverse judges, and the heuristic *"be suspicious of a score that jumps without a plausible mechanism."*
3. **The "the model is getting worse" drill** — separate real regression from perception by replaying a fixed, versioned eval set against a stored baseline. The usual answer: the model is unchanged and the **inputs drifted**. This is a sourced, high-frequency scenario question.
4. **Online evaluation** — A/B testing, sample size and power, guardrail metrics, sequential testing and peeking, interleaving for ranking, shadow deployment, canary, and multi-armed bandits.
5. **Drift** — covariate vs label vs concept drift, detection (PSI, KL, KS test), embedding drift, and what to actually do when each fires.
6. **Observability for LLM systems** — tracing a request across retrieval/tool/generation spans, token and cost accounting per request, prompt versioning, and capturing production failures back into the eval set as a closed loop.
7. **Safety evaluation** — hallucination rate measurement, toxicity, PII leakage, jailbreak resistance, refusal calibration (over- *and* under-refusal), and red-teaming.
8. **MLOps lifecycle** — experiment tracking, model registry, data and model versioning, feature stores, **training/serving skew**, reproducibility, CI for models, and the rollback path. Cross-link `docker`.
9. **Human evaluation** — annotation guidelines, inter-annotator agreement (Cohen's/Fleiss' kappa), adjudication, and cost per label.
10. **Statistical rigour** — confidence intervals on an eval score, bootstrap resampling, multiple-comparison correction, and why a 2-point gain on 50 examples is noise. Cross-link `math_ml` and `quant`.

**Artifacts:** SVG — eval pyramid (unit → component → e2e → online) · SVG — offline gate ↔ online monitor closed loop · SVG — agent trajectory scored at each step · SVG — RAG triad mapped onto the pipeline stages · SVG — A/B test decision flow with guardrails · SVG — drift types with distribution shifts drawn · Code 10+: golden-set schema · deterministic grader · judge grader + agreement check · Recall@k / MRR / nDCG · pass@k and pass^k · groundedness check · bootstrap CI on an eval score · PSI drift detector · trajectory scorer · cost-per-request tracker · Worked examples (5): nDCG by hand on 5 ranked items · sample size for a 2% lift · bootstrap CI on 40 examples · judge-human kappa · pass@k vs pass^k on the same data

**Q&A target: 32.**

**Canonical questions (★ = sourced verbatim):**
- ★ *"How do you know your AI system is actually working well?"*
- ★ What is the difference between `pass@k` and `pass^k`, and which do you report to a customer?
- ★ Why might a model do worse with retrieved context than with none?
- How do you evaluate a RAG system end to end? What is the RAG triad?
- Before you trust an LLM judge, what must you measure?
- Name three biases in LLM-as-judge scoring and the mitigation for each.
- Your agent gets the right answer 90% of the time. Why is that not enough?
- A stakeholder says "the model has gotten worse." You have no eval set. What do you do first?
- Recall@10 is 0.95 but answer quality is poor. Where is the problem?
- nDCG vs MRR — when does the difference matter?
- You improved your eval score 2 points on 50 examples. Ship it?
- How do you detect concept drift without labels?
- What is training/serving skew and how have you prevented it?
- Design the evaluation system for an LLM feature already in production with hallucination complaints.
- How do you turn a production failure into a permanent regression test?

---

### 7.6 `math_ml` — Math Foundations for ML · **P1** · Track C

`∑` · badge `Foundations` · colour `purple` · roles `AI`

**Why it exists:** no math module exists. Applied-Scientist loops test it directly, and OpenAI's reported coding round is **math-heavy** (information theory, probability). Your M.Tech Signal Processing makes this your strongest comparative advantage — but only if the material is organized for interview recall rather than coursework.

**Sprint tier:**
- Linear algebra core: vector/matrix ops, rank, trace, determinant, inverse vs pseudo-inverse, norms (L0/L1/L2/L∞/Frobenius), orthogonality, projections
- Eigenvalues/eigenvectors — the geometric meaning, and what positive-definite buys you
- **SVD** — statement, geometric reading, the low-rank approximation property, and its relation to PCA
- Matrix calculus: gradient, Jacobian, Hessian, the chain rule in matrix form, and the identities you actually reuse (`∂(xᵀAx)/∂x`, `∂‖Ax−b‖²/∂x`)
- Probability core: conditional probability, **Bayes' theorem**, independence, LOTP, expectation/variance/covariance, and the law of total expectation
- Distribution reference card: Bernoulli · Binomial · Poisson · Geometric · Uniform · Normal · Exponential · Beta · Gamma · Multinomial — with mean/variance/when-it-appears
- CLT and the Law of Large Numbers — stated precisely, including what CLT does *not* say
- MLE vs MAP vs Bayesian — the one-line distinction and the prior's role
- Hypothesis testing: null/alternative, p-value (and the standard misinterpretation), Type I/II error, power, confidence intervals
- **Information theory**: entropy · cross-entropy · KL divergence · JS divergence · mutual information · perplexity. **Your edge — put it in Sprint tier, not buried in Deep**
- Convexity, gradient descent convergence intuition, and why convexity matters for guarantees

**Deep tier:**
1. **Linear algebra applied** — least squares three ways (normal equations, QR, SVD) and the conditioning difference; eigendecomposition vs SVD; the spectral theorem; matrix factorizations (LU, Cholesky, QR) and what each is for; the covariance matrix as the bridge to PCA.
2. **PCA derived** — maximize variance ⇒ eigenvector of covariance; the SVD route; explained-variance ratio; whitening. Cross-link `ml_core`.
3. **Probability depth** — joint/marginal/conditional manipulation, Bayes with worked medical-test numbers (the base-rate fallacy — a perennial interview question), conditional expectation, variance decomposition, moment generating functions, and concentration inequalities (Markov, Chebyshev, Hoeffding) at a usable level.
4. **Estimation** — bias/variance of an estimator, consistency, efficiency, Cramér-Rao at a conceptual level, MLE derivations for Bernoulli/Gaussian/Poisson, and the MAP-as-regularized-MLE equivalence (this is *why* L2 ≡ Gaussian prior and L1 ≡ Laplace prior — a question that separates candidates).
5. **Optimization** — convex sets/functions, first- and second-order conditions, gradient descent convergence rate, Newton's method and why we rarely use it at scale, Lagrange multipliers + KKT (needed to actually explain SVMs), SGD convergence, momentum as a heavy-ball analogy, and why Adam is not convergence-guaranteed.
6. **Information theory derived** — entropy from first principles, cross-entropy as the coding-length interpretation, KL asymmetry and what each direction optimizes (forward vs reverse KL, mode-seeking vs mass-covering — directly relevant to VI and RLHF), mutual information, and the data-processing inequality.
7. **Statistics for experiments** — t-test, chi-square, ANOVA, bootstrap, permutation tests, multiple comparisons, and sample-size/power computation. Cross-link `ai_evals`.
8. **Signal-processing bridge (your differentiator)** — Fourier transform and the convolution theorem, sampling/Nyquist/aliasing, filter design, windowing, STFT/spectrogram, wavelets, and the Kalman filter as recursive Bayesian estimation. Then connect each to an ML counterpart: convolution ↔ CNN · spectrogram ↔ audio models · SDEs ↔ diffusion · Kalman ↔ state-space/Mamba. **This section is the reason an interviewer remembers you.**
9. **Numerical stability** — catastrophic cancellation, log-sum-exp (and why every softmax implementation uses it), condition number, floating-point pitfalls. Cross-link `coa` IEEE-754.

**Artifacts:** SVG — SVD geometric decomposition (rotate → scale → rotate) · SVG — eigenvector as an invariant direction under a transform · SVG — gradient descent paths on a convex vs non-convex surface, and with/without momentum · SVG — Bayes' theorem as areas on a 2×2 population grid · SVG — forward vs reverse KL fitting a bimodal target · SVG — convolution theorem (spatial ↔ frequency) · Code: log-sum-exp · PCA via SVD · MLE for a Gaussian · bootstrap CI · KL for discrete and continuous · gradient check · Worked examples (10): base-rate Bayes · MLE for Bernoulli · PCA on a 2×2 covariance · gradient of `‖Ax−b‖²` · two steps of GD by hand · entropy of a biased coin · KL between two Gaussians · sample size for a given power · Chebyshev bound · Nyquist rate for a given signal

**Q&A target: 30.**

**Canonical questions:**
- State Bayes' theorem. A test is 99% accurate for a disease with 0.1% prevalence — you test positive. What is `P(disease)`?
- What does SVD do geometrically? How does it relate to PCA?
- What does a positive-definite Hessian tell you?
- Why is cross-entropy the natural loss for classification?
- KL divergence is not symmetric — what does each direction optimize for?
- Derive the MLE for the mean of a Gaussian.
- Show that MAP with a Gaussian prior is L2-regularized MLE.
- What does the Central Limit Theorem actually claim? What does it not claim?
- Explain a p-value to a non-statistician. What is the common misinterpretation?
- Why do all softmax implementations subtract the max?
- Why don't we use Newton's method for deep learning?
- What are the KKT conditions and where have you used them? *(SVM dual)*
- Entropy of a fair coin? A biased coin at p=0.9? Which is more compressible?
- What is the relationship between perplexity and cross-entropy?
- What is aliasing and what sampling rate avoids it?
- Compute the expected number of coin flips to get two heads in a row.

---

### 7.7 `sql_data` — SQL Mastery & Data Engineering · **P0** · Track D

`🔎` · badge `FDE Core` · colour `teal` · roles `FDE, AI, SWE`

**Why it exists:** `dbms` covers engine *theory*; nothing covers SQL as a *tool* or the data layer. Palantir's FDSE loop puts SQL in the 90-minute HackerRank screen **and** in the Learning round — including the specific scenario of **writing SQL against a schema you cannot execute**. The FDE job *is* data integration. This is P0 for that track and high-value for AI (feature pipelines) and SWE (every backend touches SQL).

**Sprint tier:**
- Join taxonomy: INNER / LEFT / RIGHT / FULL / CROSS / **SELF** — with the row-count consequence of each, and the self-join employee-manager query as the canonical example
- Set operations: UNION vs UNION ALL · INTERSECT · EXCEPT
- `WHERE` vs `HAVING` vs `QUALIFY`, and the **logical execution order** `FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT` — this single table resolves most SQL confusion
- Aggregates + `GROUP BY` semantics; `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`
- **NULL three-valued logic** — `NULL != NULL`, `NOT IN` with NULLs returning empty, `COALESCE`/`NULLIF`, and aggregates skipping NULLs
- **Window functions** — the full set: `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` (the distinction is asked constantly), `LAG`/`LEAD`, `NTILE`, `FIRST_VALUE`/`LAST_VALUE`, running aggregates, and the **frame clause** (`ROWS` vs `RANGE`, `UNBOUNDED PRECEDING`)
- CTEs and **recursive CTEs** (hierarchy traversal, date spines)
- The 12 query patterns that cover ~90% of SQL interviews: Nth highest · top-N per group · running total · month-over-month growth · gaps and islands · duplicate detection · pivot · self-join hierarchy · cumulative distinct · first/last event per entity · sessionization · funnel conversion
- Pandas ↔ SQL translation table — the same operation side by side (`merge`/`groupby`/`pivot_table`/`melt`/`shift`/`rank`)

**Deep tier:**
1. **All 12 query patterns written out**, each with the schema, the query, and the common wrong answer.
2. **Query performance** — reading `EXPLAIN ANALYZE`, index usage vs sequential scan, why `WHERE func(col) = x` kills an index (and the expression-index fix), `LIKE 'x%'` vs `LIKE '%x'`, implicit type-cast index loss, `OR` vs `UNION ALL`, and `EXISTS` vs `IN` vs `JOIN` for semi-joins. Cross-link `dbms`.
3. **Correlated subqueries** — the per-row cost, and rewriting them as joins or windows.
4. **Data modeling** — OLTP normalized vs OLAP dimensional; star vs snowflake schema; fact vs dimension tables; grain (and *"what is the grain of this table"* as the question that exposes whether you actually understand a schema); slowly changing dimensions type 1/2/3; surrogate vs natural keys.
5. **OLTP vs OLAP vs columnar storage** — row vs column layout, compression, vectorized execution, and why analytics moved to Parquet/ORC. Plus partitioning and clustering.
6. **ETL vs ELT** — the modern ELT argument, staging layers, medallion (bronze/silver/gold), idempotent reloads, and backfills.
7. **Pipeline engineering** — orchestration DAGs (Airflow concepts: operators, sensors, backfill, idempotency), incremental vs full refresh, watermarks, late-arriving data, and **exactly-once vs at-least-once in a data pipeline**. Cross-link `system_design`.
8. **Data quality** — schema validation, null/range/uniqueness/referential checks, freshness SLAs, reconciliation against the source, and what you do when the source is wrong.
9. **Pandas for real work** — `merge` semantics and the indicator column, `groupby.agg`/`transform`/`apply` (and the performance difference), `pivot_table`, `melt`, `MultiIndex`, memory reduction via dtypes/categoricals, vectorization vs `apply`, chunked reads, and `SettingWithCopyWarning` explained properly.
10. **Spark concepts** — RDD vs DataFrame, lazy evaluation, narrow vs wide transformations, shuffle cost, partitioning, broadcast joins, **skew and the salting fix**, and `cache`/`persist`. Breadth-level only; the interview question is usually *"why is this job slow"* and the answer is usually *shuffle or skew*.
11. **Messy-data wrangling** — the FDE core skill. Dirty joins (fuzzy keys, inconsistent casing/whitespace, date-format chaos), deduplication strategy, entity resolution, dealing with multiple source systems disagreeing, and documenting the assumptions you had to make. **This section is what the Palantir Learning round actually tests.**
12. **Writing SQL you cannot run** — a named, sourced scenario. The discipline: restate the schema, state your assumptions explicitly, name the join keys and their cardinality, handle NULLs defensively, and say what you would check first if you could execute it. Drill this with 5 unexecutable exercises.

**Artifacts:** SVG — join types as Venn + row-count table · SVG — logical query execution order pipeline · SVG — window frame visualization (`ROWS BETWEEN` on real rows) · SVG — star vs snowflake schema · SVG — medallion ETL architecture · SVG — Spark shuffle with skew and after salting · Code 18+: all 12 query patterns · recursive CTE hierarchy · pandas equivalents for 6 of them · Airflow DAG skeleton · data-quality check suite · chunked pandas read · broadcast join hint · Worked examples (6): trace `GROUP BY` + `HAVING` evaluation order on real rows · `RANK` vs `DENSE_RANK` vs `ROW_NUMBER` on tied data · gaps-and-islands step by step · `EXPLAIN` plan read · a dirty join with 4 data-quality problems · an unexecutable-SQL exercise with assumptions written out

**Q&A target: 33.**

**Canonical questions:**
- `WHERE` vs `HAVING` — and what is the execution order of a `SELECT`?
- `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` on tied values.
- Find the Nth highest salary. Now do it per department.
- Running total per customer, ordered by date.
- Find all duplicate rows. Now delete all but one.
- Month-over-month growth as a percentage.
- Gaps and islands: find consecutive-day streaks per user.
- `UNION` vs `UNION ALL` — why is one slower?
- Why does `WHERE col NOT IN (subquery)` return nothing?
- `EXISTS` vs `IN` vs `JOIN` — which would you use and why?
- Why does `WHERE YEAR(created_at) = 2026` not use the index on `created_at`?
- Write a recursive CTE to get the full reporting chain for an employee.
- What is the grain of this table? *(given a schema)*
- Star vs snowflake — which would you build and why?
- ETL vs ELT — why has the industry moved?
- This Spark job takes 4 hours. Name the three most likely causes.
- You are joining two systems' customer tables and 12% of rows don't match. Walk me through what you do.
- Write a query against this schema. You cannot run it — tell me your assumptions.

---

### 7.8 `linux_git` — Linux, Git & CLI Debugging · **P1** · Track D

`🐧` · badge `Daily Tools` · colour `cyan` · roles `All`

**Why it exists:** entirely absent. Every role assumes it; nobody studies it; it shows up as "debug this live" in re-engineering rounds and as "walk me through your workflow" in behavioural rounds. Cheap to learn, embarrassing to fail.

**Sprint tier:**
- Filesystem navigation + the FHS essentials (`/proc`, `/etc`, `/var/log`, `/tmp`, `/dev`)
- Permissions: `rwx`, octal, `chmod`/`chown`, umask, **setuid/setgid/sticky bit**
- Text processing pipeline: `grep` (+ `-r -i -v -E -A -B`), `sed`, `awk`, `cut`, `sort`, `uniq -c`, `tr`, `wc`, `xargs`, `tee` — with the 10 one-liners you actually need (count by field, top-N from a log, extract a column, dedupe, find large files)
- Process management: `ps aux`, `top`/`htop`, `kill` vs `kill -9` (SIGTERM vs SIGKILL and why the difference matters), `nohup`, `&`, `jobs`, `nice`
- **Resource diagnosis order**: `top` → `free -h` → `df -h` → `iostat` → `netstat`/`ss` → `lsof`. Memorize the sequence; it is the answer to "the server is slow"
- Networking CLI: `curl` (with `-v -H -d -X`), `dig`, `ss -tulpn`, `traceroute`, `tcpdump` basics
- `journalctl` / `systemctl` essentials
- Git mental model: working tree → index → HEAD → remote. Every Git confusion is a confusion about which of the four you are touching
- Daily Git: `add -p`, `commit --amend`, `stash`, `restore` vs `reset` vs `revert` (the three are constantly confused — one table settles it)
- **`merge` vs `rebase`** — history shape, when each is correct, and the golden rule (never rebase shared history)
- Conflict resolution walkthrough

**Deep tier:**
1. **Git internals** — objects (blob/tree/commit/tag), content-addressable storage via SHA-1/SHA-256, refs and `HEAD`, what a branch actually is (a 41-byte file), the index as a staging snapshot, packfiles. Understanding this makes every Git question trivial.
2. **Git recovery and surgery** — `reflog` (the "I lost my commits" answer), `cherry-pick`, interactive rebase (squash/reword/drop/edit), `bisect` (the single most impressive Git skill in a debugging round), `blame`, `worktree`, `rerere`, and `filter-repo` for removing a committed secret.
3. **Branching strategies** — trunk-based vs Git Flow vs GitHub Flow; PR hygiene; conventional commits; semantic versioning; tags and releases.
4. **Shell scripting** — variables and quoting (the `"$@"` vs `$*` distinction), `set -euo pipefail` and why every script should start with it, exit codes, traps, here-docs, conditionals, loops, functions, parameter expansion, and process substitution.
5. **Signals and job control** — the full common set (`SIGTERM`, `SIGKILL`, `SIGINT`, `SIGHUP`, `SIGCHLD`, `SIGSEGV`, `SIGPIPE`), handler semantics, why PID 1 must reap (cross-link `docker`), and graceful shutdown.
6. **Performance tooling** — `strace` (what syscalls is it actually making), `ltrace`, `perf top`/`perf record`, `/proc/<pid>/` inspection, `vmstat`, `pidstat`, flame graphs, and the "where did the time go" decision tree.
7. **Debugging a running process** — `gdb` attach, backtrace, breakpoints, watchpoints, core dumps, and `coredumpctl`. Cross-link `cpp_systems`.
8. **Disk and I/O** — inodes in practice ("disk full but `df` says there's space" → inode exhaustion, a classic), mounts, `du` vs `df` disagreement and why, log rotation, and filling `/var/log`.
9. **SSH and keys** — keygen, agent, config, port forwarding (local/remote/dynamic), and `known_hosts`.
10. **The "it works on my machine" checklist** — environment, path, version, permissions, locale, timezone, DNS. A structured answer to a question you will definitely be asked.
11. **Vim survival** — enough to not freeze when a remote editor opens: modes, `:wq`, `dd`, `/`, `u`, `:%s/a/b/g`. Thirty lines; saves a real moment of embarrassment.

**Artifacts:** SVG — Git four areas with the command that moves between each · SVG — merge vs rebase resulting history graphs · SVG — Linux process states and the signal transitions · SVG — "server is slow" diagnosis decision tree · SVG — Git object graph for two commits · Code 14+: 12 shell one-liners · a `set -euo pipefail` script with a trap · `git bisect run` with a test script · `strace` and `perf` invocations with annotated output · an interactive-rebase sequence · secret removal with `filter-repo` · Worked examples (5): find the top 10 IPs in a 1GB access log · "disk full" but `df` shows space · `git bisect` a regression across 200 commits · recover a deleted branch via reflog · trace a hung process to a blocking syscall

**Q&A target: 28.**

**Canonical questions:**
- `kill` vs `kill -9` — what is the difference and when does `-9` lose you data?
- The server is slow. What do you run, in what order?
- Disk is full but `df` shows free space. What is wrong?
- `du` and `df` disagree. Why?
- What do the three bits in `755` mean? What does the setuid bit do?
- Count the top 10 most frequent IPs in an access log. *(one-liner)*
- `reset --soft` vs `--mixed` vs `--hard` vs `revert` vs `restore`.
- `merge` vs `rebase` — which do you use on a shared branch, and why?
- You committed to the wrong branch. Fix it without losing work.
- You committed an API key and pushed. What do you do? *(rotate first, then rewrite)*
- You lost commits after a bad `reset --hard`. Recover them.
- A regression appeared in the last 200 commits. Find it in ~8 steps.
- What is a Git branch, physically?
- Why should every shell script start with `set -euo pipefail`?
- A process is hung and using 0% CPU. How do you find out what it is waiting on?
- Why must PID 1 in a container reap children?

---

### 7.9 `fde_decomp` — FDE Decomposition & Client-Facing Engineering · **P0 (FDE)** · Track E

`🧭` · badge `FDE Loop` · colour `blue` · roles `FDE`

**Why it exists:** this is the **highest-leverage module for the FDE track and it has no equivalent anywhere on the site.** Research is unambiguous: the decomposition round is *"probably the most important technical round you will face"* and *"one of the options that you will almost definitely get."* It is a trainable skill with a known structure, and the most common failure — jumping to implementation — is entirely preventable.

**Sprint tier:**
- **What the round actually is** — Palantir's own definition: *"technical challenges that are open-ended in nature, with multiple possible solutions that will incur different trade-offs."*
- **The invariant prompt structure** (sourced): *a named institution + a loosely-bounded measurable problem + 2–3 data sources messier than they sound + no technical spec.* Once you can see the template, every prompt looks the same.
- **The two-phase structure** — **(1) Ideation**: break it into pieces, propose a solution to each, and **agree on the solution with your interviewer before moving on**. **(2) Execution**: high-level design. That explicit *handshake* step is the thing nobody practises and it is the sourced structure of the round.
- **Palantir's own tactic, verbatim:** *"Deliver a functioning idea first, then expand it afterwards."*
- **The scoping question bank** — the questions to ask before designing anything. OpenAI reportedly *stopped* a candidate for jumping to design and asked *"what questions would you ask the customer before designing anything?"* Have 15 ready, grouped: who is the user · what decision does this change · what data exists and who owns it · what does success look like numerically · what is the constraint (legal/political/technical) · what happens if we do nothing
- **The workflow spine** — users and their decisions → data sources and ownership → the minimum viable pipeline → the model/ontology → the interface → the measurable outcome → the failure modes
- **Scoring rubric** — what they are actually grading: user focus, decomposition quality, explicit tradeoffs, adaptability when a constraint changes, and whether you translate a technical choice into operational value or risk unprompted
- **Failure modes to avoid** — jumping to implementation · designing for the data instead of the user · proposing ML where a join and a dashboard would do · silence · over-cleverness. Sourced: *"Silence and cleverness both cost you."*

**Deep tier:**
1. **The decomposition framework, written as a repeatable script** — 8 phases with the exact sentences to say at each transition. This is the deliverable; everything else supports it.
2. **10 full worked decompositions** using the sourced prompts. Each one: clarifying questions asked → stated assumptions → decomposition tree → proposed solution per branch → the agreement checkpoint → data model sketch → the pipeline → the interface → metrics → failure modes → the tradeoff summary.
   - Elderly people with poor vision who want to cook for themselves *(the one verbatim-confirmed prompt)*
   - Route a city's emergency calls to the right responder
   - A city wants to cut 911 response times — call data, traffic sensors, ambulance GPS
   - A hospital has never inventoried its equipment
   - A logistics company's shipments get stuck somewhere
   - A hospital network wants to reduce post-surgery medication errors
   - A retailer wants to reduce out-of-stock on its top 500 SKUs
   - A transit authority wants to improve on-time performance on 120 routes
   - A government client's data is fragmented across ten systems → one operational view
   - Model a parking garage system: inputs, business logic, outputs
3. **The mid-round constraint break — drill this specifically.** Sourced: interviewers *"almost always introduce a new constraint mid-session"* (e.g. *"the city can't share ambulance GPS due to a union contract"*). **Defending your original plan is a hard fail; narrating what changes is the pass.** Give 10 constraint-injections across the 10 prompts and the correct re-plan for each.
4. **Data integration patterns** — the actual FDE craft: source inventory and ownership, schema mapping across disagreeing systems, entity resolution, reconciliation, incremental sync, the "source of truth" negotiation, and **multi-party data governance and isolation** (sourced as the focus when a design round does appear). Cross-link `sql_data` and `api_security`.
5. **Ontology / semantic-layer thinking** — objects, properties, links, actions; why a shared vocabulary beats per-team schemas; and modeling a domain from a verbal description. **Explicitly note that Foundry product knowledge is NOT required** (sourced: *"the loop tests general engineering, decomposition, learning, and customer judgment, not product-specific knowledge"*) — this saves you from wasting prep time.
6. **The re-engineering round** — you get 100–500 lines of unfamiliar code, told how it *should* behave and that the output is wrong. The sourced discipline: **read it all before touching anything**, because *"it's really important not to get lost in the first issue you see… they will probably put in red herrings."* Include two full practice exercises with deliberately planted red herrings.
7. **The learning round** — staged tasks in an unfamiliar system, pacing is scored (one candidate reached task 3 of 5). Drill: time-boxed sprints over an unknown API with deliberately incomplete docs.
8. **Writing SQL you cannot execute** — sourced as a real scenario. Cross-link `sql_data` §12.
9. **Translating technical → operational** — the sourced FDSE-vs-SWE differentiator. A phrase bank: *"this choice means the client can… / risks… / costs…"*. Practise converting 15 technical decisions into operational statements.
10. **The build-vs-custom judgment call** — a real FDSE named this as a live decision: *"whether to invest time building a feature your customer needs into the core platform, or to create something custom that we can deliver faster."* Have a framework and an opinion.
11. **Dev vs Delta** — Palantir's own framing: *"one capability, many customers"* vs *"one customer, many capabilities."* Know which you are applying for and why.

**Artifacts:** SVG — the 8-phase decomposition framework as a flow · SVG — the decomposition tree for one worked prompt, fully expanded · SVG — the FDE workflow spine (users → decisions → data → pipeline → model → interface → outcome) · SVG — multi-source data integration with ownership boundaries · SVG — the Palantir FDSE loop structure (recruiter → phone screen → 3-of-4 onsite → HM) with the behavioural overlay on every round · `worked_example()` × 10 (the decompositions) · `followup_chain()` × 10 (the constraint injections) · 2 re-engineering exercises with red herrings · `one_liner()` for every framework phase

**Q&A target: 30** (mostly scenario-style rather than factual).

**Canonical prompts (★ = verbatim-sourced):**
- ★ *"How would you design a technology to help elderly people with poor vision who want to cook for themselves?"*
- ★ *"Walk through how you would model a parking garage system: your inputs, the business logic, and the outputs."*
- ★ *"What strategies do you consider for enhancing performance beyond just the code you're currently working on? Consider aspects such as caching and pre-computation."*
- ★ *"What questions would you ask the customer before designing anything?"*
- A city wants to reduce 911 response times with call data, traffic sensors, and ambulance GPS. What would you build?
- A government client's data is fragmented across ten systems. Give them one operational view.
- Allocate limited emergency-response resources after a natural disaster.
- A logistics client is losing money on deliveries. Find the root cause using only the data they already have.
- Track disease spread through a contact network given people and interactions.
- Given a company's chat logs, how would you model how a rumor spreads through the org?
- *(mid-round)* The client just told you they legally cannot share that dataset. Now what?
- How do you isolate two customers' data in a shared deployment?
- The client's "source of truth" disagrees with another system by 8%. What do you do?
- Here are 300 lines of code; the output is wrong. Find the bug. *(with red herrings)*
- Dev vs Delta — which do you want, and why?

---

### 7.10 `behavioral` — Behavioral, STAR & Project Defense · **P0** · Track E

`🎤` · badge `Every Loop` · colour `emerald` · roles `All`

**Why it exists:** three independent sourced findings make this P0, not soft filler. **(1)** Palantir embeds ~20 minutes of behavioural in *every* onsite round and its recruiter screen *"filters out more candidates than most companies do at this stage"* — *"they will reject strong technical candidates if they don't seem like a good cultural fit."* **(2)** Anthropic's Values round is *"where most candidates fail — per Anthropic recruiters themselves."* **(3)** Indian campus panels spend *more* time on project defense than students expect, and *"a project you cannot defend in detail is worse than no project, because it invites exactly the questions you cannot answer."*

**Sprint tier:**
- **STAR, but weighted correctly** — Situation 10% / Task 10% / **Action 60%** / Result 20%. Most candidates invert this and narrate context for two minutes
- **The 12-story bank** — build once, reuse everywhere: hardest technical problem · a real failure · conflict with a teammate · led without authority · learned something fast · shipped under a deadline · changed your mind given data · pushed back on a decision · made a tradeoff you regret · debugged something brutal · simplified something overcomplicated · worked on something unglamorous
- ★ **The failure story — the sourced trap.** Palantir hiring manager, verbatim: *"we're going to ask you about your failures, your mistakes, your struggles. **We're not fishing for a success story.**"* A disguised success is a detected failure. Spec: real cost, your specific contribution to the cause, what you changed afterwards, and no redemption bow
- ★ **"Which project did you NOT enjoy?"** — sourced as a genuine trap. The real test: *"they want to know you're OK working on all sorts of projects, not just glamorous ones."* Answer honestly, then show you did it well anyway
- **Project defense checklist** — for each of your three resume projects: why this database · why this framework · what broke · what you measured · what you would change · what you would do with 10× the data · what you would do with 1/10th the time · what the alternative was and why you rejected it
- **Your three mandated projects** (per `AGENTS.md`): **Warehouse PathMapper (IBYD)** · **Uplan** · **K-HUKI** — plus Alternative Data Radar and Apna Gold. Build the defense sheet for each
- **"Why this company"** per target — and have a real reason, not a recited mission statement
- **Questions to ask them** — sourced as *scored positively*: a Palantirian's own example was asking *"some really tough questions about the culture."* Interrogating them reads as conviction, not insubordination

**Deep tier:**
1. **The 12 stories written out in full**, each tagged with every competency it can answer (ownership, ambiguity, conflict, failure, influence, speed, rigour, judgment) so one story covers four questions.
2. **Project defense dossiers** — one per project, with the full depth ladder: what it does → architecture → the key technical decision → the alternative you rejected and why → what you measured → the hardest bug → the limitation you know about → what you would change → the scaling question → the "what if the constraint flipped" question.
3. **The 40-question bank with answer scaffolds** — grouped by competency, each with the trap and the structure, not a script.
4. **Anthropic Values round — a dedicated section.** Sourced: it is *"closer to a therapy session than a job interview"*, follow-ups target **how you felt** rather than what you did, and **they actively look for skepticism and pushback** — *"thoughtful disagreement lands better than agreement."* Required reading named by the source: *Machines of Loving Grace* (Amodei, 2024), *The Adolescence of Technology* (Amodei, Jan 2026), *Core Views on AI Safety* (2023), plus a long-form Amodei interview. You must be able to say **why safety-first framing specifically**, not just "frontier AI is exciting." Note also that references are probed on **conflict and ethical friction.**
5. **Palantir mission conviction** — the comfort question is asked directly, and so is defense-industry comfort at Anduril (*"they seem to tailor the process to what you say you're interested in during the early rounds, so be careful about what you say you want"*). Decide your actual position in advance and state it honestly, including the discomfort.
6. **The communication failure mode that cuts across all three tracks** — sourced convergence: Palantir *"silence and cleverness both cost you"*; OpenAI candidates coached toward *"technical overcommunication"*; campus panels failing candidates on project defense. **This is a rehearsal problem, not a knowledge problem, and it cannot be fixed by reading.** Include a drill protocol: record yourself answering 5 questions, time them, cut the setup in half.
7. **The OpenAI recorded-video walkthrough** — a real deliverable in that loop and re-opened live at the start of the next round. Sourced lesson, first-person: *"I nearly over-explained the code line by line in the video. Instead, I focused on decisions and tradeoffs."* Include a video-walkthrough template.
8. **Salary, timeline, and offer conversations** — brief but practical.
9. **Red flags you should be screening for** — this is a two-way interview; have your own rubric.

**Artifacts:** SVG — STAR with the correct time weighting drawn to scale · SVG — the 12-story bank mapped to competencies as a matrix (shows one story covering many questions) · SVG — project defense depth ladder · `one_liner()` for each story's 20-second version (you will sometimes be asked to be brief) · Full dossier per project · 40-question bank with scaffolds · Drill protocol with timings

**Q&A target: 40** (the bank *is* the content here).

**Canonical questions (★ = verbatim-sourced):**
- ★ *"Tell me about a real failure, not a disguised success."*
- ★ *"What projects have you enjoyed, and which have you NOT enjoyed?"*
- ★ *"Tell me about a time you got up to speed on something unfamiliar fast."*
- ★ *"Why Palantir, and why forward-deployed specifically?"*
- Walk me through Warehouse PathMapper. Why that routing approach and not A*?
- Walk me through Uplan. What does the critic node actually catch, and how do you know?
- Walk me through K-HUKI. Where does the 11× come from, and what did you measure it against?
- What would you change about your main project today?
- What would break first if your project got 100× the data?
- Tell me about a time you disagreed with someone senior.
- Tell me about a time you were wrong and changed your mind because of data.
- Describe the hardest bug you have debugged. How did you find it?
- Tell me about something you shipped that you later regretted.
- Tell me about a time you had to deliver with incomplete requirements.
- What do you do when you disagree with the company's direction? *(Anthropic Values)*
- How do you feel about working on something with no immediate impact?
- What questions do you have for me? *(scored — have three real ones)*

---

### 7.11 `quant` — Aptitude, Probability & Puzzles · **P1** · Track E

`🎲` · badge `OA Gate` · colour `amber` · roles `All`

**Why it exists:** absent from the site, but it is a **gate** — Indian campus OAs (and HFT/quant screens like Pace) routinely eliminate candidates here before any human sees the resume. Also directly feeds `math_ml` and `ai_evals`, and OpenAI's reported coding round includes *expected number of iterations of a probabilistic function*.

**Sprint tier:**
- Counting: permutations vs combinations, with/without repetition, circular arrangements, identical objects, **stars and bars**, inclusion-exclusion
- Pigeonhole principle and its non-obvious applications
- Probability basics: sample space, conditional, independence, Bayes (cross-link `math_ml`)
- **Expected value** — linearity of expectation as the single most useful trick in the entire module, with 5 problems it trivializes
- Indicator-variable technique
- **Expected number of trials** — geometric distribution, and the recursive-equation method for "expected flips until pattern X"
- Classic problem families with the standard trick for each: birthday problem · coupon collector · gambler's ruin · Monty Hall · two-envelope · Bertrand's box · balls in bins · random walk
- Combinatorial identities worth knowing cold: `C(n,k)` symmetry, hockey stick, binomial theorem
- Quantitative aptitude speed set: percentages, ratios, profit/loss, time-speed-distance, time-work, mixtures, averages, simple vs compound interest, number systems (divisibility, HCF/LCM, remainders, modular arithmetic), clocks, calendars — one worked template each
- Logical reasoning: syllogisms, blood relations, seating arrangements, series completion, coding-decoding
- **Time management strategy for an OA** — which question types to skip, and when

**Deep tier:**
1. **Expected value mastery** — 15 problems solved by linearity of expectation, including ones where the direct computation is intractable. This is the highest-yield skill in the module.
2. **Conditional expectation and recursion** — the `E[X] = 1 + p·E[A] + q·E[B]` pattern for absorbing-state problems, worked on 8 problems (expected flips for HH vs HT — famously different, and a favourite).
3. **Markov chains at an interview level** — states, transitions, absorbing states, expected hitting time, stationary distribution. Needed for random-walk and gambler's-ruin families.
4. **Probability paradoxes and why they fool people** — Monty Hall (with the explicit statement of the host's knowledge, which is where most explanations fail), Simpson's paradox, base-rate fallacy, the boy-girl/Tuesday problem, Bertrand's paradox. Each with the precise reason the intuition breaks.
5. **Classic brainteasers with the generalizable technique** — 100 prisoners and light bulbs, 25 horses / 5 races, egg drop, weighing puzzles (12 coins / 3 weighings, and the information-theoretic lower bound), bridge crossing, poisoned wine, 100 doors, two ropes, river crossing, hat-colour / prisoners-and-hats. For each: the *transferable* idea, not just the answer.
6. **Information-theoretic lower bounds for puzzles** — `⌈log₃(N)⌉` weighings, `⌈log₂(N)⌉` comparisons. This is the move that turns "lucky guess" into "I derived the bound first." **Your edge again** — cross-link `math_ml`.
7. **Game theory basics** — Nim and the XOR rule, combinatorial game states, minimax, and simple optimal-strategy problems.
8. **Estimation / Fermi problems** — *"how many petrol pumps in India"*, *"how much does a cloud weigh"*. Structure, stated assumptions, and sanity-check magnitude. These also appear in FDE and consulting-flavoured rounds — cross-link `fde_decomp`.
9. **Number theory for OAs** — modular arithmetic, Fermat's little theorem, CRT at a basic level, last-digit and remainder tricks, counting divisors, trailing zeros in `n!`.
10. **Probability coding problems** — the sourced OpenAI shape: expected iterations of a probabilistic function, reservoir sampling (also in the ML drill list), random shuffle correctness (Fisher-Yates vs the naive wrong version), generating a fair coin from a biased one, and rejection sampling.

**Artifacts:** SVG — Monty Hall probability tree with the host's knowledge made explicit · SVG — stars and bars visual · SVG — Markov chain with an absorbing state and hitting times · SVG — 25 horses tournament bracket showing the 7 races · SVG — 12-coin weighing decision tree · 60+ `worked_example()` blocks (this module *is* worked examples — answers hidden until clicked) · Code: reservoir sampling · Fisher-Yates · fair-from-biased coin · expected-iterations simulation to verify your analytic answer · `numbers_card()`: Fermi reference magnitudes (population, areas, rates)

**Q&A target: 45** (highest on the site — it is a problem bank).

**Canonical questions:**
- Expected number of coin flips to get `HH`? To get `HT`? Why are they different?
- Expected number of rolls to see all six faces? *(coupon collector)*
- 23 people — probability two share a birthday?
- Monty Hall — and state precisely what assumption makes switching correct.
- 25 horses, 5 at a time, no timer. Minimum races to find the top 3?
- 12 coins, one fake, 3 weighings. Find it — and prove 3 is sufficient and necessary.
- 2 eggs, 100 floors. Minimum worst-case drops?
- 100 prisoners, one light bulb. Devise the protocol.
- Generate a fair coin from a coin with unknown bias.
- Shuffle an array uniformly. Why is the naive `swap(i, random(0,n))` wrong?
- Pick a random element from a stream of unknown length. *(reservoir)*
- Expected number of iterations of this probabilistic function. *(sourced shape)*
- A test is 99% accurate, disease prevalence 0.1%. You test positive — now what?
- Three ants on a triangle move randomly. Probability of no collision?
- Stick broken at two random points — probability the pieces form a triangle?
- How many petrol pumps are there in India? *(Fermi)*
- Nim with piles 3, 4, 5 — who wins and what is the first move?
- Last two digits of `7^2026`.
- Trailing zeros in `100!`.

---

## 8. Definition of Done & Build Workflow

### 8.1 Per-module Definition of Done

A module is **not** finished until every box is true. Run this checklist before ticking it off.

**Content**
- [ ] Sprint tier reads in **12–15 min** (time yourself; cut if over)
- [ ] Deep tier reads in **~45 additional min** (60 total)
- [ ] Every section has a matching `id=` and a TOC entry (and vice versa — no orphans either way)
- [ ] Every Deep-tier concept has its **one anchor sentence** establishing why it exists (§2.4)
- [ ] Every formula uses `formula_box()` with **all symbols defined**
- [ ] Every A-vs-B topic has a `decision_matrix()`, not just a comparison table
- [ ] Every major topic has a `one_liner()` — the 15-second spoken version
- [ ] 2–4 `followup_chain()` blocks on the highest-value topics
- [ ] `see_also()` links to at least 2 other modules
- [ ] Q&A count hits the module's target; each card has tags + difficulty
- [ ] Worked examples hit the module's target, with answers hidden until clicked
- [ ] Code blocks are **complete and runnable** — no `# ...` elisions in a block you'd be asked to write live

**Accuracy**
- [ ] Every number is real and checkable, or explicitly marked as an order-of-magnitude estimate
- [ ] Every verbatim-sourced question is marked (★ or equivalent) so you know it is real, not invented
- [ ] No fabricated benchmarks, no "studies show", no invented company-specific claims
- [ ] Claims about your own projects match what you actually built (`Master Resume.tex` is the authority)

**Contract**
- [ ] `MODULES_META` `highlights` ↔ artifacts that actually exist (§1.4)
- [ ] `est_mins` and `est_mins_deep` are accurate
- [ ] `track`, `tier`, `roles` are set
- [ ] Build validation passes (§4.4 items 3 and 4)

**Rendering**
- [ ] `python builder/build_all.py` runs clean
- [ ] Opens correctly in dark **and** light mode
- [ ] Sprint/Deep toggle hides and shows the right blocks
- [ ] Test Mode collapses all answers
- [ ] All KaTeX renders (no raw `$...$` visible)
- [ ] All Prism blocks highlight with the correct language
- [ ] **Checked at 390px width** — tables scroll, SVGs are readable or tappable-to-fullscreen, drawer opens, bottom nav works
- [ ] All SVGs legible in both themes (no hardcoded `#000` or `#fff` — use `currentColor` or CSS variables)
- [ ] No console errors

### 8.2 SVG authoring rules

19 SVGs exist today and the good ones (handshake, vtable, HNSW, LRU UML, HOG) share a pattern. Codify it:

1. **Width ≤ 880px**, `height="auto"` via `viewBox`. Always set `viewBox` so it scales.
2. **Theme-safe colours only** — `currentColor`, `var(--accent-*)`, or `var(--text-*)`. A hardcoded `#000` becomes invisible in dark mode. Audit the existing 19 for this.
3. **Label everything** — the best existing SVGs annotate state names, byte offsets, latencies, and tensor shapes. An unlabelled box is decoration, not a diagram.
4. **One idea per diagram.** If you need two, make two.
5. **Always add `diagram-caption`** stating what the reader should take away.
6. **Font size ≥ 11px** — anything smaller is unreadable on a phone.
7. Prefer **sequence/timeline** diagrams for protocols and **layout/memory** diagrams for structures. Those two forms cover most needs.

### 8.3 Working rhythm

Per module, in one sitting:

```
1. Read the module brief in Part 6 or 7.
2. Draft the Sprint tier first. Time it. Cut to 15 min.
3. Draft the Deep tier sections in the brief's order.
4. Write the code blocks. Actually run them.
5. Draw the SVGs last (they're the slowest; don't let them block content).
6. Write the Q&A bank. Use Part 9 for verbatim questions.
7. Update MODULES_META. Run build_all.py.
8. Walk the §8.1 checklist.
9. Update README.md (table row + totals).
10. Commit: "study: rebuild <module> (sprint+deep)".
```

### 8.4 README.md updates required

The current `README.md` has two factual errors to fix as you go:

- Claims **"120+ flashcards"** — the real current total is **75**. Make the number computed, not asserted (§4.4 item 5).
- Claims **"KaTeX math rendering"** — not actually loaded (§1.2). True once you fix it.

New structure for the table: group by the 5 tracks, and add columns for **Tier**, **Roles**, **Sprint min**, **Deep min**, **Q&A count**. Add a "Study Plans" section documenting the 5 presets from §3.5.8.

### 8.5 What not to do

- **Don't** split Sprint and Deep into separate files. They will drift.
- **Don't** write content before the component library (Part 4) exists. You will rewrite it.
- **Don't** pad the Deep tier to hit a time target. 45 minutes of dense content beats 60 minutes of filler, and padding destroys the thing that makes the module useful.
- **Don't** invent interview questions. Part 9 has enough real ones; mark anything you add yourself as unsourced.
- **Don't** add a 24th module without removing something. 23 × 60 min is already 23 hours of deep reading.

---

## 9. Research Appendix

Live research conducted 13 Oct 2026. Use this section when writing Q&A banks — these are real questions, not invented ones.

### 9.1 Source reliability tiers

| Tier | Sources | Trust |
| :-- | :-- | :-- |
| **P0 — Official** | `blog.palantir.com` · `palantir.com/careers/getting-hired/` · `openai.com/interview-guide` · `anthropic.com/candidate-ai-guidance` | Company's own words |
| **P1 — Engineer-sourced** | `interviewing.io` company guides (built from current/former engineers, cross-referenced against Glassdoor + their own 100K+ mock-interview dataset) | Highest-confidence third party |
| **P1 — Canonical repos** | `alirezadir/AIMLInterviews` (9.8k★, 2026) · `aishwaryanr/awesome-generative-ai-guide` (29.8k★) · `ashishps1/awesome-low-level-design` (27.4k★) · `ashishps1/awesome-system-design-resources` (42.2k★) · `techinterviewhandbook.org` (Blind 75 author) · `huyenchip.com/ml-interviews-book` | Community-validated |
| **P2 — First-person (n=1)** | `gaijineer.co` OpenAI FDE writeup | One data point — treat as such |
| **P2 — Practitioner** | `theforwarddeployed.io` (self-labels "evidence level: reported") · `hackingthecaseinterview.com` (ex-Bain) · `blcompiler.com` (Indian campus training, orders DSA by *campus* frequency) · `prepare.sh` | Useful shapes; verify format |
| **P3 — Content farms** | Excluded as evidence | AI-generated, circular citation |

### 9.2 Interview loop structures (sourced)

**Palantir FDSE:**
```
Recruiter 30m → Technical phone screen 1h (CodePair)
  → Onsite 3h: you get 3 of 4
     [Problem Decomposition | System Design | Re-engineering | Coding]
  → Hiring Manager 1h
```
Mechanics: **every onsite round carries ~20 min of behavioural** (there is no standalone behavioural round). The HM round **repeats whichever onsite round the panel was least sure about**. Team matching happens *after* the onsite. Final decision rests with the last HM. **AI use is strictly prohibited.** Timeline 3–4 weeks.
Coding topic list (Glassdoor-cross-referenced): **Hash Maps, Search, Sets, Arrays, Strings, Graphs, Queues.**

**Anthropic:**
```
Recruiter 30m → CodeSignal 60–90m (4 progressive levels, black-box evaluator, 2h)
  → Onsite 4–5h: HM · Coding · System Design · 2nd role-specific coding · Company Values
```
The circulated challenge: **"implement a bank with multiple transaction types."** Candidate quote: *"The spec interpretation could only be obtained by repeatedly running your code to see what test cases failed… the folks who go to the next level are probably good at reading ambiguous specs and trying out theories against black-box graders."*
Style: **first-principles / build-from-scratch** — expect to reimplement a data structure *after* solving it with the standard library. **Concurrency recurs across multiple rounds.** Python is the working language. SD prompts: *design a Claude chat service*, *design a system enabling a GPT to handle multiple questions in one thread*, *LLM-serving API with request batching / queuing / GPU utilization under variable load*.

**OpenAI SWE:** math-heavy coding from **information theory and probability** (formula provided): implement **KL divergence for continuous distributions**; **expected iterations of a probabilistic function**; **minimum error of a distribution via cross entropy**. Niche focus: time-based data structures, versioned data stores, coroutines/concurrency, OOP (abstract classes, iterators, inheritance). Questions are **multi-part (~4 parts)**, time-tight. *"You're not going to get questions on string manipulation."* Onsite includes a **slide presentation round** on a recent hard technical problem and an **agentic coding round (beta)** where you drive an AI agent over a codebase too large to hand-edit. Pre-onsite SD: Yelp / Foursquare / Twitter / notifications.

**OpenAI FDE:** ~7 touchpoints over 3–4 weeks. **~5-hour take-home on OpenAI's APIs + a recorded video walkthrough**, re-opened at the start of the live deep dive. The deep dive pushes hardest on **evaluation**.

**Anduril:** LeetCode-medium with domain dressing (*"a collection of robots with tasks, track the highest priority tasks"*, drone management, graph manipulation). *"The question is not difficult algorithmically, but the follow-up questions in terms of how to speed and scale it up were trickier."* SD: **TinyURL, Tetris**, or drone fleet management. They ask how comfortable you are with defense work. Warning: *"they seem to tailor the process to what you say you're interested in during the early rounds, so be careful about what you say you want."*

### 9.3 Palantir's own grading language (P0 verbatim)

- Decomposition = *"technical challenges that are open-ended in nature, with multiple possible solutions that will incur different trade-offs."*
- Tactic: **"Deliver a functioning idea first, then expand it afterwards."**
- Re-engineering = *"The ability to work within the constraints and complexity of existing systems, codebases, and infrastructure."*
- *"We will not ask you about tricky or obscure features of some specific programming language."*
- Languages: most are fine *"as long as they're imperative."*
- Dev vs Delta = **"one capability, many customers"** vs **"one customer, many capabilities."**
- Failure stories: *"we're going to ask you about your failures, your mistakes, your struggles. **We're not fishing for a success story.**"*
- **Read directly** (JS-rendered, my fetcher couldn't read it; both P0 and P2 sources call it the single highest-value prep artifact):
  `palantir.com/careers/getting-hired/navigating-open-ended-questions/`

### 9.4 The 2026 AI interview shift (sourced)

> *"The biggest shift in 2026 ML interviews: LLMs / foundation models are now expected **breadth**, not a specialty."* — `alirezadir/AIMLInterviews`

> *"Roughly 75% of a modern AI Engineer technical loop is RAG, agents, evals, and LLM-powered system design; classic ML (trees, CNNs, gradient descent) is maybe 25% and often skipped entirely at product-focused startups."* — `awesome-generative-ai-guide`

**Caveat:** this applies to **AI Engineer** roles. **Applied Scientist** loops retain far more classical ML and math — which is why `ml_core` and `math_ml` stay P0/P1 rather than being dropped.

**Ranked AI topics by yield:** 1 Evaluation · 2 RAG end-to-end (**40%+ of take-homes are RAG systems**) · 3 Transformer/LLM internals · 4 GenAI system design (now a separate round) · 5 Agents/tools/MCP · 6 Post-training selection · 7 Inference optimization · 8 Classical ML breadth · 9 ML coding from scratch · 10 Math/stats · 11 Multimodal/VLM/VLA · 12 Diffusion.

**The 9-step ML system design script** (recite this out loud in the round): problem formulation → metrics (offline + online) → architectural components/MVP → data collection & prep → feature engineering → model dev & offline eval → prediction service → online testing & deployment → scaling, monitoring, updates.

### 9.5 Campus DSA frequency (two independent sources agreeing)

`blcompiler.com` (ordered *"by return per hour, based on what campus panels actually put in front of students"*) and `techinterviewhandbook.org` (High/Mid/Low priority) converge:

**Tier 1 — every round touches these:** arrays & strings (*"by a wide margin, usually combined with hashing or two pointers… they appear in almost every coding round regardless of company tier, and they are also the cheapest topics to learn well"*) · hashing · two pointers & sliding window (*"the highest yield shapes relative to how little there is to learn"*) · sorting · **binary search on the answer space** (*"this one shape appears far more often than students expect"*).

**Tier 2:** recursion & backtracking · trees · linked lists · stacks/queues (incl. **monotonic stack**) · graphs BFS/DFS — and note *"grid problems, which are graph problems wearing a matrix costume, are extremely common."*

**Tier 3:** **DP — flagged as the single most over-invested topic relative to campus frequency.** TIH independently rates it **Low**. What is actually asked clusters tightly into ~9 shapes. *"Interviewers accept memoisation almost universally."* Also: heaps (trigger = the word "k") · greedy (*"the difficulty is not implementation, it is knowing when greedy is valid at all"*) · intervals.

**Tier 4 — know it exists:** tries · segment trees · DSU · advanced bits · advanced graphs. *"DSU and basic bit manipulation are the two most likely to surface; the rest are rare at campus level."* And: *"Dijkstra is worth knowing conceptually. Minimum spanning trees, max flow and advanced shortest path variants are rarely asked at campus level and should be the last thing you add."*

**Topic completion rubric** (the best one I found — use it): a topic is done when you can (1) name the trigger in one sentence, (2) write the standard implementation from memory, (3) trace it by hand and predict state at each step, (4) state *and justify* both complexities, (5) **solve a fresh unseen problem in that shape.** Only (5) is a real test.

**Core-subject timing:** start theory subjects **in parallel from ~week 4**, not at the end. Named as the specific scheduling mistake that catches students.

### 9.6 Campus theory question set (sourced)

> *"DBMS: normalisation, indexing, joins, transactions, ACID, and writing a query with a join and a group by. Operating systems: processes against threads, deadlock and its four conditions, scheduling, paging, virtual memory. Networks: the OSI layers, TCP against UDP, the three way handshake, what happens when you type a URL into a browser. Object oriented programming: the four principles, **with an example from your own code rather than a textbook**."* — `blcompiler.com`

That last clause is the whole reason `behavioral` project-defense dossiers matter.

### 9.7 Under-prepared, high-impact gaps (the differentiators)

**FDE:**
1. The first 3 minutes of decomposition — the most common rejection is jumping to implementation. The **agree-with-your-interviewer handshake** after ideation is almost never practised.
2. **Adapting when the interviewer breaks your constraint mid-round.** Interviewers *"almost always introduce a new constraint mid-session."* Defending the original plan is a hard fail.
3. Writing SQL you cannot execute.
4. Reading 200–500 lines of hostile code **top to bottom before touching anything** — red herrings are deliberate.
5. *"Which project did you NOT enjoy?"* — tests whether you'll take unglamorous work.
6. Mission conviction stated honestly, **including discomfort**. Interrogating them is scored *positively*.
7. Pacing under staged tasks (one candidate reached task 3 of 5).
8. Translating a technical choice into operational value or risk, **unprompted** — the explicit FDSE-vs-SWE differentiator.

**AI:**
1. **Evaluation as a buildable artifact**, not a sentence. *"Shipping a demo with zero evaluation is the most common reason strong-looking take-homes get rejected."*
2. **Code-based graders before model-based graders.** Almost nobody says this.
3. **Trajectory evaluation for agents** — final-output-only scoring *flatters* agents.
4. Reward hacking and the defences. *"Be suspicious of a score that jumps without a plausible mechanism."*
5. **Tokenization as a production hazard** — non-English costs 2–3× more tokens; truncate on token boundaries.
6. The "model is getting worse" drill — usually the model is unchanged and **the inputs drifted**.
7. **Information theory in a coding round** — *"these questions aren't hard if you're fresh on the material, but they can catch you off guard."* **Your direct M.Tech advantage.**
8. **Concurrency** — Anthropic threads it through multiple rounds; rarely prepped by ML candidates.
9. **GRPO/RLVR and *why* the critic is dropped.** Most candidates stop at "DPO is simpler than PPO." Also know that algorithm ranking is **scale-dependent** (online RL can win at ~1.5B while SimPO wins at ~7B) — citing that nuance reads as real understanding.
10. **Taste: name the cheapest thing that clears the bar first.** Prompt → RAG → fine-tune → agent, with a reason. *"Over-engineering (a 4-agent framework for a task a single retrieval call would solve)"* is an explicitly listed failure mode.

**SWE:**
1. **Binary search on the answer space** — cheapest high-yield gap in the syllabus.
2. **Monotonic stack** — *"a recognisable family that looks impossible until you have seen two of them."*
3. **Stop over-investing in DP** — reallocate to Tier-1 + core subjects.
4. **Grid problems recognized as graph problems.**
5. **Defending your own projects** — *"a project you cannot defend in detail is worse than no project."* Specifically: why this database, why this framework, what broke, what you'd change.
6. **Virtual function called from a constructor** — high-frequency C++ weed-out, counter-intuitive answer.
7. **Barrier-induced deadlock** and **semaphore FIFO fairness** — added to the GFG 2026 set *because* candidates pass the standard questions by rote.
8. **`DELETE` vs `TRUNCATE` rollback semantics differ by DBMS** — most candidates state the MySQL answer as universal.
9. **Class relationship vocabulary** (association vs aggregation vs composition vs dependency) — *"asked constantly in LLD, answered vaguely almost always."*
10. **"What happens when you type a URL"** — a whole-stack answer, not a networking trivia item.

### 9.8 Calibration for this candidate

- **Your M.Tech Signal Processing is a documented edge in exactly one named blind spot:** OpenAI's information-theory coding questions (KL divergence, cross-entropy, expected iterations). Entropy, integration, and distributions are your coursework. The same advantage extends to diffusion/flow-matching (SDEs, denoising), attention numerical stability, and the information-theoretic lower bounds in `quant`. **Three modules are specced to exploit this: `math_ml` §8, `llm_internals` §10, `quant` §6.**
- **Your B.Tech CSE makes the SWE track defensible** — which matters because the FDE coding floor is real (Palantir's topic list is entirely Tier-1/Tier-2 DSA) and AI loops at big tech still gate on one DSA round.
- **The highest-leverage single artifact across all three tracks** is one project you can defend at full depth *and* whose evaluation you can show. That satisfies FDE's decomposition/ownership bar, AI's "can you prove it works" throughline, and the campus project-defense round simultaneously. **Warehouse PathMapper is your mandated always-present project — make it the one with a defensible evaluation story.**
- **Highest-risk shared gap:** all three tracks now score **narrated reasoning under ambiguity** above correct answers delivered silently. Palantir: *"silence and cleverness both cost you."* OpenAI: *"technical overcommunication."* Campus: *"a project you cannot defend."* **That is a rehearsal problem, not a knowledge problem, and it cannot be fixed by reading this site.** Hence `behavioral` §6 and `fde_decomp` §3 being drill protocols rather than reading material.

### 9.9 Honest negative results

Recorded so you don't waste time chasing them:

- **No credible public writeups exist** for FDE / Deployment-Strategist loops at **Scale AI, Databricks, Sigma, Applied Intuition, Harvey, Glean, Cohere, or Mistral.** Only content farms with no underlying evidence. Anything specific about those loops would be invention.
- **No NIT/IIT-specific Palantir FDSE drive data found.** *[Inference, not sourced]* Palantir's Indian campus footprint appears thin; the realistic channel for FDE-shaped roles on-campus is adjacent (enterprise-deployment and consulting-tech hybrid roles at Indian offices of global firms), with Palantir/OpenAI/Anthropic FDE pursued off-campus. **Verify against your placement cell's actual company list — do not plan around a Palantir campus slot existing.**
- **Foundry/Ontology product knowledge is explicitly NOT tested:** *"No. The loop tests general engineering, decomposition, learning, and customer judgment, not product-specific knowledge."* Don't study the product.
- `huyenchip.com/ml-interviews-book` is **2021, pre-LLM**. It remains the canonical bank for training-internals and NumPy questions, but do not treat its coverage as current on LLMs.

### 9.10 Full source list

**P0 (official):**
- `blog.palantir.com/interviewing-at-palantir-advice-from-palantirians-88444a90e7c4`
- `blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87`
- `palantir.com/careers/getting-hired/` and `.../navigating-open-ended-questions/` ← **read this one directly**
- `openai.com/interview-guide`
- `anthropic.com/candidate-ai-guidance`

**P1 (engineer-sourced / canonical):**
- `interviewing.io` — Palantir, OpenAI, Anthropic, Anduril company guides
- `github.com/alirezadir/AIMLInterviews` (9.8k★, updated 2026)
- `github.com/aishwaryanr/awesome-generative-ai-guide` (29.8k★)
- `github.com/ashishps1/awesome-low-level-design` (27.4k★)
- `github.com/ashishps1/awesome-system-design-resources` (42.2k★)
- `techinterviewhandbook.org`
- `huyenchip.com/ml-interviews-book` *(2021 — see §9.9)*
- GeeksforGeeks interview hubs: OS (70+ Q, Aug 2026) · DBMS (58 Q, Aug 2026) · CN · C++ (54+ Q, Aug 2026)

**P2 (treat as reported):**
- `gaijineer.co/openai-forward-deployed-engineer-interview-process` *(n=1 first-person)*
- `theforwarddeployed.io` *(self-labelled "evidence level: reported")*
- `hackingthecaseinterview.com` *(ex-Bain author)*
- `blcompiler.com` *(Indian campus training; DSA ordered by campus frequency)*
- `prepare.sh`
- LeetCode Discuss — 2022 Palantir new-grad loop report

**Named Anthropic Values-round reading (sourced as expected):**
- *Machines of Loving Grace* — Amodei, 2024
- *The Adolescence of Technology* — Amodei, Jan 2026
- *Core Views on AI Safety* — Anthropic, 2023
- A long-form Amodei interview (Dwarkesh or Lex)

---

## 10. Quick Reference — The Whole Spec On One Screen

```
BLOCKERS (do first)
  hardcoded "9" → len(MODULES_META)
  KaTeX not loaded → add CDN + auto-render
  4 undefined pill classes → define them
  14 unmet MODULES_META promises → build or remove
  zero authoring helpers → build components.py
  mobile nav broken → drawer + bottom bar

MODEL
  One file per module. Two tiers: data-depth="sprint" | "deep".
  Sprint = 15 min night-before recall.
  Deep   = 60 min read-once comprehension.
  Style  = dense reference + ONE anchor sentence per concept.

UX
  Navigate: scroll-spy · progress bar · nested TOC · drawer ·
            Ctrl+K global search · shortcuts · breadcrumb
  Understand: formula_box · worked_example · decision_matrix ·
            anti_pattern · one_liner · see_also · followup_chain
  Retain:   per-section progress · Test Mode · weak-topic queue
            (review.html) · spaced resurfacing · Anki export

ROSTER — 23 modules, 5 tracks (12 rewrite + 11 new)
  A Core CS      dsa* os* dbms* cn coa concurrency†*
  B SWE/Design   lld* system_design* api_security† cpp_systems python_internals*
  C AI/ML        math_ml† ml_core†* ml_cv llm_internals†* ai_agents* ai_evals†*
  D Data/Infra   sql_data†* linux_git† docker
  E Role/Human   fde_decomp†* behavioral†* quant†
                 († = new, * = P0)

ORDER
  Phase 0 infra → 1 SWE core → 2 AI core → 3 design+human
  → 4 FDE → 5 P1 breadth → 6 P1 remainder → 7 README/dashboard

DON'T
  split sprint/deep into separate files · write content before
  components.py · pad to hit 60 min · invent interview questions ·
  add a 24th module
```

---

*End of specification. Rebuild one module per sitting against its brief in Part 6 or 7, walk the §8.1 checklist, then tick it off.*





