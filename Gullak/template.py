# template.py - Gullak Technologies Backend Engineer Interview Preparation Portal HTML Renderer

def render_gullak_page(title, active_page, content_html, prev_link=None, prev_title=None, next_link=None, next_title=None):
    nav_items = [
        ("index.html", "Overview & Hub", "Portal"),
        ("00_START_HERE.html", "00: Executive Intel", "Strategy"),
        ("01_Online_Test_and_Algorithms.html", "01: Signature DSA & Puzzles", "Algorithms"),
        ("02_Technical_Rounds_CS_Core.html", "02: OS, Concurrency & Networks", "CS Core"),
        ("03_Database_Internals_and_Transactions.html", "03: DBMS, ACID & Redis", "Databases"),
        ("04_System_Design_LLD_and_HLD.html", "04: Fintech LLD & HLD", "Architecture"),
        ("05_Candidate_Resume_Grilling.html", "05: Resume Defense & Traps", "Defense"),
        ("06_Managerial_and_HR_Culture.html", "06: Startup Culture & HR", "Behavioral"),
        ("07_Quick_Reference_CheatSheet.html", "07: Rapid CheatSheet", "CheatSheet"),
        ("README.html", "Emergency Study Roadmap", "Roadmap"),
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
  <meta name="theme-color" content="#b45309">
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
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-go.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-json.min.js"></script>

  <style>
:root {{
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
  
  /* Light Theme */
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-card: #ffffff;
  --bg-sidebar: #fefce8;
  --bg-code-header: #f1f5f9;
  --bg-inline-code: #fef3c7;
  
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  
  --border-color: #e2e8f0;
  --border-subtle: #fde68a;
  --border-focus: #d97706;
  
  --accent-primary: #d97706;
  --accent-primary-hover: #b45309;
  --accent-light: rgba(217, 119, 6, 0.08);
  
  --tag-bg: #fef3c7;
  --tag-border: #f59e0b;
  --tag-text: #b45309;
  
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.08);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.12);
}}

[data-theme="dark"] {{
  --bg-primary: #0b0f19;
  --bg-surface: #111827;
  --bg-card: #151e2e;
  --bg-sidebar: #0d1322;
  --bg-code-header: #1e293b;
  --bg-inline-code: #2e2616;
  
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --border-color: #1e293b;
  --border-subtle: #2d2616;
  --border-focus: #f59e0b;
  
  --accent-primary: #f59e0b;
  --accent-primary-hover: #fbbf24;
  --accent-light: rgba(245, 158, 11, 0.12);
  
  --tag-bg: rgba(245, 158, 11, 0.15);
  --tag-border: #f59e0b;
  --tag-text: #fbbf24;
  
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
  background: linear-gradient(90deg, #b45309, #f59e0b, #fbbf24);
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
  background: linear-gradient(135deg, #b45309, #f59e0b);
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

.sidebar-nav {{
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 3px;
  flex-grow: 1;
}}

.nav-link {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 12px;
  border-radius: 8px;
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 500;
  transition: all 0.15s ease;
}}

.nav-link:hover {{
  background-color: var(--accent-light);
  color: var(--accent-primary);
}}

.nav-link.active {{
  background-color: var(--accent-primary);
  color: #ffffff !important;
  font-weight: 600;
}}

.nav-badge {{
  font-size: 10px;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
  background-color: var(--border-color);
  color: var(--text-muted);
  text-transform: uppercase;
}}

.nav-link.active .nav-badge {{
  background-color: rgba(255, 255, 255, 0.25);
  color: #ffffff;
}}

.sidebar-footer {{
  padding-top: 14px;
  border-top: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 10px;
}}

.theme-toggle-btn {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s;
}}

.theme-toggle-btn:hover {{
  border-color: var(--border-focus);
  color: var(--accent-primary);
}}

/* Main Content Area */
.main-wrapper {{
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}}

.top-bar {{
  height: 56px;
  background-color: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  position: sticky;
  top: 0;
  z-index: 1020;
}}

.top-bar-left {{
  display: flex;
  align-items: center;
  gap: 12px;
}}

.mobile-menu-btn {{
  display: none;
  background: none;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  padding: 6px 10px;
  color: var(--text-primary);
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
}}

.top-breadcrumb {{
  font-size: 13px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}}

.top-breadcrumb a {{
  color: var(--accent-primary);
  text-decoration: none;
  font-weight: 600;
}}

.content-container {{
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  padding: 40px 32px 100px 32px;
}}

/* Typography inside content */
.content-container h1 {{
  font-size: 2.1rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  margin-bottom: 16px;
  color: var(--text-primary);
  border-bottom: 2px solid var(--border-color);
  padding-bottom: 12px;
}}

.content-container h2 {{
  font-size: 1.5rem;
  font-weight: 700;
  margin-top: 36px;
  margin-bottom: 14px;
  color: var(--text-primary);
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 8px;
}}

.content-container h3 {{
  font-size: 1.2rem;
  font-weight: 700;
  margin-top: 24px;
  margin-bottom: 10px;
  color: var(--text-primary);
}}

.content-container p {{
  margin-bottom: 16px;
  color: var(--text-secondary);
  font-size: 15px;
}}

.content-container ul, .content-container ol {{
  margin-bottom: 18px;
  padding-left: 24px;
  color: var(--text-secondary);
}}

.content-container li {{
  margin-bottom: 6px;
  font-size: 15px;
}}

.content-container hr {{
  border: none;
  border-top: 1px solid var(--border-color);
  margin: 32px 0;
}}

.content-container blockquote {{
  border-left: 4px solid var(--accent-primary);
  background-color: var(--accent-light);
  padding: 12px 18px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 20px;
  color: var(--text-secondary);
  font-style: italic;
}}

/* Tables */
.content-container table {{
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 14px;
  background: var(--bg-surface);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  display: block;
  overflow-x: auto;
}}

.content-container th, .content-container td {{
  padding: 11px 14px;
  text-align: left;
  border-bottom: 1px solid var(--border-color);
}}

.content-container th {{
  background-color: var(--bg-card);
  font-weight: 700;
  color: var(--text-primary);
  border-bottom: 2px solid var(--border-color);
}}

.content-container tr:last-child td {{
  border-bottom: none;
}}

/* Code Blocks & Inline Code */
.content-container code:not([class*="language-"]) {{
  font-family: var(--font-mono);
  font-size: 0.88em;
  padding: 2px 6px;
  border-radius: 4px;
  background-color: var(--bg-inline-code);
  color: var(--accent-primary);
  border: 1px solid var(--border-subtle);
}}

.content-container pre {{
  position: relative;
  margin: 20px 0;
  border-radius: 10px;
  overflow-x: auto;
  box-shadow: var(--shadow-md);
  border: 1px solid var(--border-color);
}}

.content-container pre code {{
  font-family: var(--font-mono);
  font-size: 13.5px;
  line-height: 1.5;
}}

.copy-btn {{
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.25);
  color: #ffffff;
  font-size: 11px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.15s;
}}

.copy-btn:hover {{
  background: rgba(255, 255, 255, 0.3);
}}

/* Callouts / Alerts */
.callout {{
  padding: 16px;
  border-radius: 8px;
  margin: 20px 0;
  border-left: 4px solid;
}}

.callout-info {{
  background-color: var(--accent-light);
  border-color: var(--accent-primary);
}}

.callout-warning {{
  background-color: rgba(245, 158, 11, 0.1);
  border-color: #f59e0b;
}}

.callout-success {{
  background-color: rgba(16, 185, 129, 0.1);
  border-color: #10b981;
}}

.module-footer-nav {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--border-color);
  gap: 12px;
  flex-wrap: wrap;
}}

.footer-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 9px 16px;
  border-radius: 8px;
  background-color: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  text-decoration: none;
  font-weight: 600;
  font-size: 13.5px;
  transition: all 0.15s;
}}

.footer-btn:hover {{
  border-color: var(--accent-primary);
  color: var(--accent-primary);
  box-shadow: var(--shadow-sm);
}}

/* Bottom Nav Bar for Mobile */
.bottom-nav {{
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-color: var(--bg-surface);
  border-top: 1px solid var(--border-color);
  z-index: 1030;
  justify-content: space-around;
  align-items: center;
  padding: 0 8px;
}}

.bottom-nav-item {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 10px;
  font-weight: 600;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 6px;
}}

.bottom-nav-item.active, .bottom-nav-item:hover {{
  color: var(--accent-primary);
}}

.bottom-nav-icon {{
  font-size: 18px;
}}

/* Responsive Breakpoints */
@media (max-width: 900px) {{
  .sidebar {{
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    transform: translateX(-100%);
    box-shadow: var(--shadow-lg);
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
    padding: 24px 18px 80px 18px;
  }}
}}
  </style>
</head>
<body>
  <div id="reading-progress"></div>

  <div class="sidebar-backdrop" id="sidebar-backdrop"></div>

  <div class="app-container">
    <!-- Sidebar -->
    <aside class="sidebar" id="sidebar">
      <div class="sidebar-brand">
        <a href="index.html" class="brand-left">
          <div class="brand-icon">G</div>
          <div class="brand-text">
            <h2>Gullak Prep Hub</h2>
            <span>Backend Engineer • ₹20 LPA</span>
          </div>
        </a>
        <button class="drawer-close-btn" id="drawer-close-btn">✕</button>
      </div>

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

    <!-- Main Wrapper -->
    <div class="main-wrapper">
      <header class="top-bar">
        <div class="top-bar-left">
          <button class="mobile-menu-btn" id="mobile-menu-btn">☰ Modules</button>
          <div class="top-breadcrumb">
            <a href="../index.html">← All Companies</a>
            <span>/</span>
            <a href="index.html">Gullak</a>
            <span>/</span>
            <span>{title}</span>
          </div>
        </div>
        
        <div class="top-bar-right">
          <a href="index.html" class="footer-btn" style="padding: 5px 10px; font-size: 12px;">
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
    <a href="07_Quick_Reference_CheatSheet.html" class="bottom-nav-item{' active' if active_page == '07_Quick_Reference_CheatSheet.html' else ''}">
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
