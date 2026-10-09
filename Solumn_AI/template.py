# template.py - Solumn AI Foundations Programme Interview Preparation Portal HTML Renderer

def render_solumn_page(title, active_page, content_html, prev_link=None, prev_title=None, next_link=None, next_title=None):
    nav_items = [
        ("index.html", "Overview & Hub", "Portal"),
        ("00_START_HERE.html", "00: Company & Role Intel", "Strategy"),
        ("01_Practical_Assignment.html", "01: Practical Task & Verifiers", "Harnesses"),
        ("02_Technical_Rounds.html", "02: Python, Docker & Verifiers", "Systems"),
        ("03_Domain_Deep_Dive.html", "03: AI Safety & RSPs", "Alignment"),
        ("04_Candidate_Resume_Grilling.html", "04: Resume Defense & Traps", "Defense"),
        ("05_System_Design_or_HIL.html", "05: Eval Foundry Architecture", "Architecture"),
        ("06_Managerial_and_HR.html", "06: Founder Mindset & PPO", "Behavioral"),
        ("07_Quick_Reference.html", "07: Rapid Recall CheatSheet", "CheatSheet"),
        ("README.html", "3-Day Selection Roadmap", "Roadmap"),
    ]

    sidebar_links = ""
    for url, label, badge in nav_items:
        is_active = " active" if url == active_page else ""
        sidebar_links += f"""
        <li>
          <a href="{url}" class="nav-link{is_active}">
            <span>{label}</span>
            <span class="nav-badge">{badge}</span>
          </a>
        </li>"""

    footer_buttons = ""
    if prev_link:
        footer_buttons += f'<a href="{prev_link}" class="footer-btn">← {prev_title}</a>'
    if next_link:
        style = ' style="margin-left: auto;"' if not prev_link else ''
        footer_buttons += f'<a href="{next_link}" class="footer-btn"{style}>{next_title} →</a>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#090d16">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <title>{title}</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}, {{left: '\\\\(', right: '\\\\)', display: false}}, {{left: '\\\\[', right: '\\\\]', display: true}}]}});"></script>

  <!-- PrismJS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-yaml.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-docker.min.js"></script>

  <style>
:root {{
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
  
  /* Light Theme */
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-card: #ffffff;
  --bg-sidebar: #f1f5f9;
  --bg-code-header: #e2e8f0;
  --bg-inline-code: #e2e8f0;
  
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  
  --border-color: #cbd5e1;
  --border-subtle: #e2e8f0;
  --border-focus: #6366f1;
  
  --accent-primary: #6366f1;
  --accent-primary-hover: #4f46e5;
  --accent-light: rgba(99, 102, 241, 0.08);
  
  --tag-bg: #e0e7ff;
  --tag-border: #6366f1;
  --tag-text: #4f46e5;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.08);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.12);
}}

[data-theme="dark"] {{
  --bg-primary: #090d16;
  --bg-surface: #0f172a;
  --bg-card: #131d31;
  --bg-sidebar: #0b1324;
  --bg-code-header: #1e293b;
  --bg-inline-code: #1e293b;
  
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --border-color: #1e293b;
  --border-subtle: #334155;
  --border-focus: #818cf8;
  
  --accent-primary: #818cf8;
  --accent-primary-hover: #a5b4fc;
  --accent-light: rgba(129, 140, 248, 0.12);
  
  --tag-bg: rgba(99, 102, 241, 0.18);
  --tag-border: #818cf8;
  --tag-text: #a5b4fc;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.6);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.5);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.6);
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}}

html {{
  scroll-behavior: smooth;
  font-size: 16px;
}}

body {{
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.7;
  transition: background-color 0.2s ease, color 0.2s ease;
  overflow-x: hidden;
  min-height: 100vh;
}}

#reading-progress {{
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #6366f1, #818cf8, #a855f7);
  width: 0%;
  z-index: 2000;
  transition: width 0.08s ease;
}}

.app-container {{
  display: flex;
  min-height: 100vh;
}}

/* Sidebar Backdrop for Mobile */
.sidebar-backdrop {{
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  z-index: 1040;
}}

.sidebar-backdrop.active {{
  display: block;
}}

/* Sidebar */
.sidebar {{
  width: 310px;
  background-color: var(--bg-sidebar);
  border-right: 1px solid var(--border-color);
  padding: 20px 16px;
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  z-index: 1050;
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}}

.sidebar-brand {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-color);
}}

.brand-left {{
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--text-primary);
}}

.brand-icon {{
  width: 38px;
  height: 38px;
  background: linear-gradient(135deg, #6366f1, #4f46e5);
  border: 1px solid var(--border-subtle);
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  font-weight: 900;
  font-size: 19px;
  box-shadow: var(--shadow-sm);
}}

.brand-text h2 {{
  font-size: 15px;
  font-weight: 800;
  letter-spacing: -0.02em;
}}

.brand-text span {{
  font-size: 11px;
  color: var(--text-muted);
  display: block;
}}

.drawer-close-btn {{
  display: none;
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 20px;
  cursor: pointer;
  padding: 4px;
}}

.nav-section-title {{
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin: 14px 10px 8px;
}}

.sidebar-nav {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 3px;
}}

.nav-link {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px 12px;
  border-radius: 8px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.15s ease;
}}

.nav-link:hover {{
  background-color: var(--accent-light);
  color: var(--accent-primary);
}}

.nav-link.active {{
  background-color: var(--accent-primary);
  color: #ffffff;
  font-weight: 600;
  box-shadow: var(--shadow-sm);
}}

.nav-badge {{
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  background-color: rgba(255, 255, 255, 0.15);
  font-weight: 600;
  text-transform: uppercase;
}}

.nav-link:not(.active) .nav-badge {{
  background-color: var(--border-color);
  color: var(--text-muted);
}}

.sidebar-footer {{
  margin-top: auto;
  padding-top: 16px;
  border-top: 1px solid var(--border-color);
}}

.theme-toggle-btn {{
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-secondary);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}}

.theme-toggle-btn:hover {{
  background: var(--accent-light);
  color: var(--accent-primary);
  border-color: var(--accent-primary);
}}

/* Main Layout */
.main-wrapper {{
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}}

.top-bar {{
  height: 58px;
  background-color: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  position: sticky;
  top: 0;
  z-index: 1000;
  backdrop-filter: blur(8px);
}}

.top-bar-left {{
  display: flex;
  align-items: center;
  gap: 12px;
}}

.mobile-menu-btn {{
  display: none;
  align-items: center;
  gap: 6px;
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-primary);
  color: var(--text-primary);
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}}

.breadcrumb {{
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  color: var(--text-muted);
}}

.breadcrumb a {{
  color: var(--accent-primary);
  text-decoration: none;
  font-weight: 500;
}}

.breadcrumb a:hover {{
  text-decoration: underline;
}}

.hub-return-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: 6px;
  border: 1px solid var(--border-color);
  background: var(--bg-primary);
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.15s ease;
}}

.hub-return-btn:hover {{
  background: var(--accent-light);
  color: var(--accent-primary);
  border-color: var(--accent-primary);
}}

/* Content Container */
.content-container {{
  flex: 1;
  max-width: 980px;
  width: 100%;
  margin: 0 auto;
  padding: 36px 24px 80px;
}}

/* Typography */
h1, h2, h3, h4, h5, h6 {{
  color: var(--text-primary);
  font-weight: 700;
  line-height: 1.3;
  margin-top: 1.8rem;
  margin-bottom: 0.8rem;
}}

h1 {{
  font-size: 2.1rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-top: 0;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.6rem;
}}

h2 {{
  font-size: 1.45rem;
  letter-spacing: -0.02em;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 0.4rem;
}}

h3 {{ font-size: 1.18rem; }}
h4 {{ font-size: 1.02rem; }}

p {{
  margin-bottom: 1.1rem;
  color: var(--text-secondary);
}}

ul, ol {{
  margin-bottom: 1.2rem;
  padding-left: 1.5rem;
  color: var(--text-secondary);
}}

li {{
  margin-bottom: 0.45rem;
}}

strong {{
  color: var(--text-primary);
  font-weight: 600;
}}

a {{
  color: var(--accent-primary);
  text-decoration: underline;
  text-underline-offset: 3px;
}}

a:hover {{
  color: var(--accent-primary-hover);
}}

/* Tables */
table {{
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
  font-size: 14px;
  display: block;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}}

th, td {{
  padding: 10px 14px;
  border: 1px solid var(--border-color);
  text-align: left;
}}

th {{
  background-color: var(--bg-surface);
  font-weight: 700;
  color: var(--text-primary);
}}

tr:nth-child(even) {{
  background-color: rgba(255, 255, 255, 0.02);
}}

/* Code Blocks */
pre {{
  position: relative;
  border-radius: 10px;
  margin: 1.2rem 0;
  padding: 18px 20px !important;
  background: #111827 !important;
  border: 1px solid var(--border-color);
  overflow-x: auto;
}}

code {{
  font-family: var(--font-mono) !important;
  font-size: 13.5px;
}}

:not(pre) > code {{
  background-color: var(--bg-inline-code);
  color: var(--accent-primary);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 12.5px;
}}

.copy-btn {{
  position: absolute;
  top: 8px;
  right: 8px;
  padding: 4px 8px;
  border-radius: 5px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  background: rgba(0, 0, 0, 0.5);
  color: #e2e8f0;
  font-size: 11px;
  font-family: var(--font-sans);
  cursor: pointer;
  transition: all 0.15s;
}}

.copy-btn:hover {{
  background: rgba(255, 255, 255, 0.2);
}}

/* Callout Boxes */
.callout {{
  padding: 16px 18px;
  border-radius: 10px;
  margin: 1.4rem 0;
  border-left: 4px solid var(--accent-primary);
  background-color: var(--accent-light);
}}

.callout-title {{
  font-weight: 700;
  color: var(--accent-primary);
  margin-bottom: 6px;
  font-size: 14px;
}}

.callout p {{
  margin: 0;
  font-size: 14px;
}}

/* Module Footer Nav */
.module-footer-nav {{
  display: flex;
  justify-content: space-between;
  margin-top: 3.5rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
  gap: 12px;
  flex-wrap: wrap;
}}

.footer-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-primary);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 600;
  transition: all 0.15s ease;
  box-shadow: var(--shadow-sm);
}}

.footer-btn:hover {{
  border-color: var(--accent-primary);
  background: var(--accent-light);
  color: var(--accent-primary);
  transform: translateY(-1px);
}}

/* Mobile Bottom Nav */
.bottom-nav {{
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  background-color: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  z-index: 1020;
  justify-content: space-around;
  align-items: center;
  box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.15);
}}

.bottom-nav-item {{
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 10px;
  font-weight: 600;
  background: none;
  border: none;
  cursor: pointer;
  gap: 2px;
}}

.bottom-nav-item.active {{
  color: var(--accent-primary);
}}

.bottom-nav-icon {{
  font-size: 17px;
}}

/* Responsive Breakpoints */
@media (max-width: 900px) {{
  .sidebar {{
    position: fixed;
    transform: translateX(-100%);
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.5);
  }}

  .sidebar.open {{
    transform: translateX(0);
  }}

  .drawer-close-btn {{
    display: block;
  }}

  .mobile-menu-btn {{
    display: inline-flex;
  }}

  .bottom-nav {{
    display: flex;
  }}

  .content-container {{
    padding: 24px 16px 90px;
  }}
}}
  </style>
</head>
<body>

  <div id="reading-progress"></div>

  <div class="sidebar-backdrop" id="sidebar-backdrop"></div>

  <div class="app-container">
    
    <!-- Sidebar Drawer -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-brand">
        <a href="index.html" class="brand-left">
          <div class="brand-icon">S</div>
          <div class="brand-text">
            <h2>Solumn AI Prep</h2>
            <span>Foundations &bull; ₹2L + PPO</span>
          </div>
        </a>
        <button class="drawer-close-btn" id="drawer-close-btn" aria-label="Close menu">✕</button>
      </div>

      <div class="nav-section-title">Navigation Modules</div>
      <ul class="sidebar-nav">
        {sidebar_links}
      </ul>

      <div class="sidebar-footer">
        <button class="theme-toggle-btn" id="theme-toggle">
          <span id="theme-icon">🌙</span>
          <span id="theme-text">Dark Mode</span>
        </button>
      </div>
    </aside>

    <!-- Main Content Area -->
    <div class="main-wrapper">
      
      <header class="top-bar">
        <div class="top-bar-left">
          <button class="mobile-menu-btn" id="mobile-menu-btn">
            <span>☰</span>
            <span>Modules</span>
          </button>
          <div class="breadcrumb">
            <a href="../index.html">← All Companies</a>
            <span>/</span>
            <a href="index.html">Solumn AI</a>
          </div>
        </div>
        
        <div class="top-bar-right">
          <a href="index.html" class="hub-return-btn">
            <span>🏠 Hub</span>
          </a>
        </div>
      </header>

      <main class="content-container">
        {content_html}

        <nav class="module-footer-nav">
          {footer_buttons}
        </nav>
      </main>

    </div>
  </div>

  <!-- Mobile Bottom Navigation Bar -->
  <nav class="bottom-nav">
    <a href="index.html" class="bottom-nav-item{' active' if active_page == 'index.html' else ''}">
      <span class="bottom-nav-icon">🏠</span>
      <span>Hub</span>
    </a>
    <button class="bottom-nav-item" id="b-nav-modules">
      <span class="bottom-nav-icon">📑</span>
      <span>Modules</span>
    </button>
    <a href="07_Quick_Reference.html" class="bottom-nav-item{' active' if active_page == '07_Quick_Reference.html' else ''}">
      <span class="bottom-nav-icon">⚡</span>
      <span>CheatSheet</span>
    </a>
    <button class="bottom-nav-item" id="b-nav-theme">
      <span class="bottom-nav-icon">🌙</span>
      <span>Theme</span>
    </button>
    <button class="bottom-nav-item" id="b-nav-top">
      <span class="bottom-nav-icon">↑</span>
      <span>Top</span>
    </button>
  </nav>

  <script>
    // Theme Management
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');
    const bNavTheme = document.getElementById('b-nav-theme');

    function setTheme(mode) {{
      if (mode === 'dark') {{
        document.documentElement.setAttribute('data-theme', 'dark');
        if (themeIcon) themeIcon.textContent = '☀️';
        if (themeText) themeText.textContent = 'Light Mode';
        localStorage.setItem('theme', 'dark');
      }} else {{
        document.documentElement.removeAttribute('data-theme');
        if (themeIcon) themeIcon.textContent = '🌙';
        if (themeText) themeText.textContent = 'Dark Mode';
        localStorage.setItem('theme', 'light');
      }}
    }}

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
      setTheme('dark');
    }} else {{
      setTheme('light');
    }}

    if (themeToggle) {{
      themeToggle.addEventListener('click', () => {{
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        setTheme(isDark ? 'light' : 'dark');
      }});
    }}
    if (bNavTheme) {{
      bNavTheme.addEventListener('click', () => {{
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        setTheme(isDark ? 'light' : 'dark');
      }});
    }}

    // Mobile Drawer Management
    const sidebar = document.getElementById('sidebar');
    const sidebarBackdrop = document.getElementById('sidebar-backdrop');
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const drawerCloseBtn = document.getElementById('drawer-close-btn');
    const bNavModules = document.getElementById('b-nav-modules');

    function openDrawer() {{
      sidebar.classList.add('open');
      sidebarBackdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeDrawer() {{
      sidebar.classList.remove('open');
      sidebarBackdrop.classList.remove('active');
      document.body.style.overflow = '';
    }}

    if (mobileMenuBtn) mobileMenuBtn.addEventListener('click', openDrawer);
    if (bNavModules) bNavModules.addEventListener('click', openDrawer);
    if (drawerCloseBtn) drawerCloseBtn.addEventListener('click', closeDrawer);
    if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeDrawer);

    // Scroll to Top
    const bNavTop = document.getElementById('b-nav-top');
    if (bNavTop) {{
      bNavTop.addEventListener('click', () => {{
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});
    }}

    // Reading Progress Indicator
    const progressBar = document.getElementById('reading-progress');
    window.addEventListener('scroll', () => {{
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (totalHeight > 0) {{
        const progress = (window.pageYOffset / totalHeight) * 100;
        progressBar.style.width = progress + '%';
      }}
    }});

    // Code Copy Buttons
    document.querySelectorAll('pre').forEach(block => {{
      const btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.addEventListener('click', () => {{
        const code = block.querySelector('code');
        if (code) {{
          navigator.clipboard.writeText(code.innerText).then(() => {{
            btn.textContent = 'Copied!';
            btn.style.background = '#10b981';
            setTimeout(() => {{
              btn.textContent = 'Copy';
              btn.style.background = '';
            }}, 2000);
          }});
        }}
      }});
      block.appendChild(btn);
    }});
  </script>
</body>
</html>"""
