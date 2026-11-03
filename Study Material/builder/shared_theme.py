# shared_theme.py - Shared layout, CSS styling, components, and navigation for Study Material Portal
# Conforms to instruction.md Part 1, 2, 3, 4, 5

import html

# Master Registry of All 23 Modules across 5 Tracks (Part 5 Specification)
MODULES_META = [
    # Track A - Core CS Fundamentals (6 Modules)
    {
        "id": "dsa",
        "file": "dsa.html",
        "title": "Data Structures & Algorithms (DSA)",
        "short_title": "DSA & Patterns",
        "icon": "🧩",
        "badge": "Coding Master",
        "badge_color": "purple",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P0",
        "roles": ["SWE", "FDE", "AI"],
        "companies": ["Media.net", "Apple", "Swiggy", "Juspay", "Cred"],
        "desc": "Master Complexity Matrix, 9 Decision Patterns, Monotonic Stacks, DP Shapes, DSU, and Binary Search on Answer.",
        "highlights": ["Pattern Decision Tree SVG", "Master Complexity Matrix", "Monotonic Stack / Window Maximum", "Binary Search on Answer Pattern"]
    },
    {
        "id": "os",
        "file": "os.html",
        "title": "Operating Systems (OS)",
        "short_title": "Operating Systems",
        "icon": "⚡",
        "badge": "Core Systems",
        "badge_color": "emerald",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P0",
        "roles": ["SWE", "AI"],
        "companies": ["Qualcomm", "Nvidia", "Texas Instruments", "Apple", "Pace"],
        "desc": "Process Virtual Memory, TLB Paging Walk, Banker's Algorithm, Semaphore Classic Problems, and CFS Scheduling.",
        "highlights": ["Process Memory Layout SVG", "Paging & TLB Lookup SVG", "Deadlock 4 Conditions", "Copy-on-Write & fork() Internals"]
    },
    {
        "id": "dbms",
        "file": "dbms.html",
        "title": "DBMS & Storage Internals",
        "short_title": "DBMS & Storage",
        "icon": "🗄️",
        "badge": "Databases",
        "badge_color": "teal",
        "est_mins": "12 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P0",
        "roles": ["SWE", "FDE"],
        "companies": ["Swiggy", "Cred", "Media.net", "Apple", "NextWave"],
        "desc": "Storage Engines, B+ Tree vs LSM Trees, WAL Logging, MVCC Mechanics, Isolation Levels, and Precedence Serializability.",
        "highlights": ["B+ Tree Index Architecture SVG", "WAL Recovery & Checkpoint SVG", "Transaction Isolation Matrix", "Window Functions & Top SQL Queries"]
    },
    {
        "id": "cn",
        "file": "cn.html",
        "title": "Computer Networks (CN)",
        "short_title": "Networks",
        "icon": "🌐",
        "badge": "Core CS",
        "badge_color": "blue",
        "est_mins": "12 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P1",
        "roles": ["SWE"],
        "companies": ["Cisco", "Apple", "Nokia", "Media.net", "Swiggy"],
        "desc": "OSI/TCP-IP, 3-Way Handshake & Teardown, TCP Congestion AIMD/BBR, Sliding Windows, Full-Stack URL Navigation, and TLS 1.3.",
        "highlights": ["3-Way Handshake SVG", "TCP Congestion Control (AIMD)", "HTTP/1.1 vs HTTP/2 vs HTTP/3", "TIME_WAIT 2*MSL Trap"]
    },
    {
        "id": "coa",
        "file": "coa.html",
        "title": "Computer Organization & Architecture (COA)",
        "short_title": "Architecture",
        "icon": "💻",
        "badge": "Hardware / Systems",
        "badge_color": "amber",
        "est_mins": "12 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P1",
        "roles": ["SWE"],
        "companies": ["Texas Instruments", "Nvidia", "Qualcomm", "Arm", "Apple"],
        "desc": "CPU Performance Equation, Amdahl's Law, AMAT Latencies, 5-Stage RISC Pipeline, Out-of-Order Tomasulo, and Cache Coherence MESI.",
        "highlights": ["5-Stage Pipeline Hazards SVG", "Memory Hierarchy Latency SVG", "Cache Read/Write Policy Flow", "False Sharing & alignas(64)"]
    },
    {
        "id": "concurrency",
        "file": "concurrency.html",
        "title": "Concurrency & Parallelism",
        "short_title": "Concurrency",
        "icon": "🧵",
        "badge": "Cross-Language",
        "badge_color": "indigo",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "A",
        "track_name": "Core CS Fundamentals",
        "tier": "P0",
        "roles": ["SWE", "AI"],
        "companies": ["Anthropic", "OpenAI", "Pace (₹41L)", "Apple", "Qualcomm"],
        "desc": "Race Conditions, Memory Models & Happens-Before, Print FooBar/H2O, Thread-Safe Bounded Queues, Striped Locks, and CAS ABA.",
        "highlights": ["Happens-Before Memory Order SVG", "Thread-Safe Bounded Queue", "Print FooBar Alternately", "Striped Lock Concurrent HashMap"]
    },

    # Track B - Software Engineering & Design (5 Modules)
    {
        "id": "lld",
        "file": "lld_design_patterns.html",
        "title": "Low-Level Design & Design Patterns (LLD / OOD)",
        "short_title": "LLD & Patterns",
        "icon": "📐",
        "badge": "OOD & LLD",
        "badge_color": "purple",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "B",
        "track_name": "Software Engineering & Design",
        "tier": "P0",
        "roles": ["SWE", "FDE"],
        "companies": ["Swiggy", "Media.net", "Cred", "Juspay", "Apple"],
        "desc": "SOLID Principles, 23 GoF Patterns Matrix, Thread-Safe Singleton, O(1) LRU & LFU Caches, Parking Lot, and Elevator LLD.",
        "highlights": ["LRU Cache Class Diagram SVG", "Factory vs Strategy Flowchart SVG", "Thread-Safe Double-Checked Lock", "Parking Lot LLD Schema"]
    },
    {
        "id": "system_design",
        "file": "system_design.html",
        "title": "System Design & Distributed Systems (HLD)",
        "short_title": "System Design (HLD)",
        "icon": "🏗️",
        "badge": "Architecture",
        "badge_color": "blue",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "B",
        "track_name": "Software Engineering & Design",
        "tier": "P0",
        "roles": ["SWE", "AI", "FDE"],
        "companies": ["Media.net", "Apple", "Swiggy", "Cred", "Warner Bros"],
        "desc": "CAP/PACELC, Consistent Hashing Ring, TinyURL Architecture, Raft Consensus, Kafka Internals, Distributed Sagas, and Rate Limiters.",
        "highlights": ["Consistent Hashing Ring SVG", "TinyURL Architecture SVG", "Rate Limiting Algorithms Matrix", "Cache Stampede & Thundering Herd"]
    },
    {
        "id": "api_security",
        "file": "api_security.html",
        "title": "API Design, Auth & Security",
        "short_title": "API & Security",
        "icon": "🔐",
        "badge": "Interfaces & Trust",
        "badge_color": "amber",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "B",
        "track_name": "Software Engineering & Design",
        "tier": "P1",
        "roles": ["SWE", "FDE"],
        "companies": ["Palantir", "Cred", "Swiggy", "Apple", "AiPrise"],
        "desc": "REST vs gRPC vs GraphQL, OAuth 2.0 PKCE, JWT alg:none Attack, OWASP Top 10, Multi-Tenant Data Isolation, and Idempotency Keys.",
        "highlights": ["OAuth 2.0 PKCE Flow SVG", "JWT Header & Signature SVG", "Idempotency Key Protocol", "OWASP Top 10 Defenses"]
    },
    {
        "id": "cpp_systems",
        "file": "cpp_systems.html",
        "title": "C++ Internals & Low-Latency Systems",
        "short_title": "C++ Low-Latency",
        "icon": "🚀",
        "badge": "Systems & HFT",
        "badge_color": "indigo",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "B",
        "track_name": "Software Engineering & Design",
        "tier": "P1",
        "roles": ["SWE"],
        "companies": ["Pace Stock Broking (₹41L)", "Texas Instruments", "Qualcomm", "Nvidia", "Apple"],
        "desc": "Vtables, Smart Pointer Overhead, Move Semantics & Forwarding, Lock-Free SPSC Ring Buffer, Atomics, and Linux Kernel Bypass.",
        "highlights": ["Vtable Memory Layout SVG", "Shared_ptr Control Block SVG", "Lock-Free SPSC Ring Buffer", "std::move & Universal References Trap"]
    },
    {
        "id": "python_internals",
        "file": "python_internals.html",
        "title": "Python Internals, GIL & Concurrency",
        "short_title": "Python Internals",
        "icon": "🐍",
        "badge": "Language Deep Dive",
        "badge_color": "emerald",
        "est_mins": "14 min",
        "est_mins_deep": "60 min",
        "track": "B",
        "track_name": "Software Engineering & Design",
        "tier": "P0",
        "roles": ["AI", "FDE"],
        "companies": ["Anthropic", "OpenAI", "Solumn AI", "AiPrise", "Apple"],
        "desc": "CPython PyObject, GIL Mechanics, Generational Cyclic GC, Decorators & Descriptors, AsyncIO Event Loop, and __slots__ Memory.",
        "highlights": ["CPython GIL Execution Flow SVG", "Generational GC Pipeline SVG", "Mutable Default Arguments Trap", "__slots__ 40% Memory Savings"]
    },

    # Track C - AI / ML (6 Modules)
    {
        "id": "math_ml",
        "file": "math_ml.html",
        "title": "Math Foundations for Machine Learning",
        "short_title": "Math for ML",
        "icon": "∑",
        "badge": "Foundations",
        "badge_color": "purple",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P1",
        "roles": ["AI"],
        "companies": ["OpenAI", "Anthropic", "Apple AI", "Qualcomm", "DeepMind"],
        "desc": "Linear Algebra & SVD, Matrix Calculus, Bayes' Theorem, Information Theory (Entropy/KL/Cross-Entropy), and Signal Processing Bridge.",
        "highlights": ["SVD Geometric Transformation SVG", "Forward vs Reverse KL Divergence SVG", "Bayes Theorem Population Grid SVG", "Information Theory Coding Challenges"]
    },
    {
        "id": "ml_core",
        "file": "ml_core.html",
        "title": "Classical ML & Deep Learning Core",
        "short_title": "ML Core",
        "icon": "📊",
        "badge": "ML Foundations",
        "badge_color": "orange",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P0",
        "roles": ["AI"],
        "companies": ["Apple AI", "Google", "Meta", "Amazon", "Assurant"],
        "desc": "Bias-Variance Decomposition, NumPy Backprop from Scratch, Trees & XGBoost, Optimizer Progression, Normalization, and 9-Step ML System Design.",
        "highlights": ["Bias-Variance Capacity Curve SVG", "Backprop Computation Graph SVG", "L1 vs L2 Geometry SVG", "NumPy 2-Layer Net Forward & Backward"]
    },
    {
        "id": "ml_cv",
        "file": "ml_cv.html",
        "title": "Computer Vision & Signal Processing",
        "short_title": "CV & Signals",
        "icon": "👁️",
        "badge": "Vision & Signals",
        "badge_color": "orange",
        "est_mins": "14 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P1",
        "roles": ["AI"],
        "companies": ["Qualcomm CV/DSP", "Apple Vision", "Autobot Robotics", "Lumilens", "Texas Instruments"],
        "desc": "Classical Vision & HOG Keyframes, CNN Lineage (ResNet/MobileNet), IoU & NMS, Vision Transformers (ViT), Diffusion Models, and Nyquist Sampling.",
        "highlights": ["CNN Feature Map Pipeline SVG", "HOG Feature Extraction SVG", "IoU & NMS Suppression SVG", "U-Net Architecture & Skip Connections"]
    },
    {
        "id": "llm_internals",
        "file": "llm_internals.html",
        "title": "LLM & Transformer Internals",
        "short_title": "LLM Internals",
        "icon": "🧠",
        "badge": "Frontier AI",
        "badge_color": "rose",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P0",
        "roles": ["AI"],
        "companies": ["Anthropic", "OpenAI", "Meta AI", "Perplexity", "Apple AI"],
        "desc": "Scaled Dot-Product Attention, MHA vs GQA, KV Cache Scaling, RoPE, Post-Training (SFT/DPO/GRPO), LoRA/PEFT, and PagedAttention Serving.",
        "highlights": ["Transformer Block Tensor Shapes SVG", "MHA vs MQA vs GQA Layout SVG", "KV Cache Memory Scaling Formula", "GRPO vs DPO vs RLHF Mechanics"]
    },
    {
        "id": "ai_agents",
        "file": "ai_agents.html",
        "title": "RAG, Agents & GenAI System Design",
        "short_title": "RAG & Agents",
        "icon": "🤖",
        "badge": "GenAI Systems",
        "badge_color": "rose",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P0",
        "roles": ["AI", "FDE"],
        "companies": ["Anthropic", "OpenAI", "Palantir", "Solumn AI", "AiPrise"],
        "desc": "Hybrid Search & RRF, Vector DBs (HNSW/IVF-PQ), LangGraph Multi-Agent Workflows, Context Rot, Enterprise ACLs, and Model Context Protocol (MCP).",
        "highlights": ["Advanced RAG Flowchart SVG", "LangGraph Cyclic State Machine SVG", "HNSW vs IVF Indexing", "Hallucination Triad & Evaluation"]
    },
    {
        "id": "ai_evals",
        "file": "ai_evals.html",
        "title": "AI Evaluation, Observability & MLOps",
        "short_title": "AI Evals & MLOps",
        "icon": "📈",
        "badge": "The Differentiator",
        "badge_color": "emerald",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "C",
        "track_name": "AI / Machine Learning",
        "tier": "P0",
        "roles": ["AI", "FDE"],
        "companies": ["OpenAI", "Anthropic", "Palantir", "Scale AI", "Apple"],
        "desc": "Deterministic vs LLM-as-Judge Graders, RAG Triad, pass@k vs pass^k, Agent Trajectory Evals, A/B Testing, and Drift Detection.",
        "highlights": ["Evaluation Pyramid SVG", "pass@k vs pass^k Reliability Formula", "LLM-as-Judge Agreement Grader", "Covariate & Concept Drift Mitigations"]
    },

    # Track D - Data & Infrastructure (3 Modules)
    {
        "id": "sql_data",
        "file": "sql_data.html",
        "title": "SQL Mastery & Data Engineering",
        "short_title": "SQL & Data Eng",
        "icon": "🔎",
        "badge": "FDE Core",
        "badge_color": "teal",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "D",
        "track_name": "Data & Infrastructure",
        "tier": "P0",
        "roles": ["FDE", "AI", "SWE"],
        "companies": ["Palantir FDSE", "Swiggy", "Cred", "Apple", "Media.net"],
        "desc": "12 Standard SQL Query Patterns, Window Frames, Gaps & Islands, Data Modeling (Star/Snowflake), Messy-Data Wrangling, and Unexecutable SQL Execution.",
        "highlights": ["Logical Query Execution Order SVG", "Window Frame ROWS vs RANGE SVG", "12 Production SQL Query Templates", "Spark Skew Salting Technique"]
    },
    {
        "id": "linux_git",
        "file": "linux_git.html",
        "title": "Linux, Git & CLI Debugging",
        "short_title": "Linux & Git",
        "icon": "🐧",
        "badge": "Daily Tools",
        "badge_color": "cyan",
        "est_mins": "12 min",
        "est_mins_deep": "60 min",
        "track": "D",
        "track_name": "Data & Infrastructure",
        "tier": "P1",
        "roles": ["SWE", "AI", "FDE"],
        "companies": ["All Companies", "Palantir", "Qualcomm", "Apple", "Nvidia"],
        "desc": "Server Diagnosis Order, Text Pipelines (grep/awk/sed), Git Internals & Surgery (reflog/bisect), Process Signals, and strace/perf Profiling.",
        "highlights": ["Git 4 Areas Lifecycle SVG", "Merge vs Rebase History Graph SVG", "Server Diagnosis Flowchart SVG", "git bisect Binary Search Debugging"]
    },
    {
        "id": "docker",
        "file": "docker.html",
        "title": "Docker, Kubernetes & CI/CD",
        "short_title": "Docker & K8s",
        "icon": "🐳",
        "badge": "Containers & K8s",
        "badge_color": "cyan",
        "est_mins": "12 min",
        "est_mins_deep": "60 min",
        "track": "D",
        "track_name": "Data & Infrastructure",
        "tier": "P1",
        "roles": ["SWE", "AI", "FDE"],
        "companies": ["Warner Bros", "Celonis", "IBM", "AiPrise", "Cred"],
        "desc": "Namespaces & Cgroups, Multi-Stage Dockerfiles, Kubernetes Core Objects (Pods/Deployments/Services), Probes, and CI/CD GitHub Actions.",
        "highlights": ["Docker vs VM Architecture SVG", "OverlayFS Union Mount SVG", "Kubernetes Control Plane Architecture SVG", "Multi-Stage Build Pipeline"]
    },

    # Track E - Role-Specific & Human (3 Modules)
    {
        "id": "fde_decomp",
        "file": "fde_decomp.html",
        "title": "FDE Decomposition & Client-Facing Engineering",
        "short_title": "FDE Decomposition",
        "icon": "🧭",
        "badge": "FDE Loop",
        "badge_color": "blue",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "E",
        "track_name": "Role-Specific & Human",
        "tier": "P0",
        "roles": ["FDE"],
        "companies": ["Palantir FDSE", "OpenAI FDE", "Enterprise Tech", "Consulting Tech"],
        "desc": "Palantir Open-Ended Decomposition Framework, 10 Verbatim Client Prompts, Scoping Question Bank, Mid-Round Constraint Breaks, and Re-Engineering Red Herrings.",
        "highlights": ["8-Phase Decomposition Framework SVG", "FDE Workflow Spine SVG", "10 Verbatim Client Prompts Decomposed", "Re-Engineering Code Red Herrings"]
    },
    {
        "id": "behavioral",
        "file": "behavioral.html",
        "title": "Behavioral, STAR & Project Defense",
        "short_title": "Behavioral & STAR",
        "icon": "🎤",
        "badge": "Every Loop",
        "badge_color": "emerald",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "E",
        "track_name": "Role-Specific & Human",
        "tier": "P0",
        "roles": ["SWE", "AI", "FDE"],
        "companies": ["Palantir", "Anthropic", "Apple", "Qualcomm", "All Companies"],
        "desc": "Action-Weighted STAR (60% Action), Real Failure Defense, Anthropic Values Round Preparation, Project Defense Dossiers, and Spoken Rehearsal Drills.",
        "highlights": ["STAR 60% Action Breakdown SVG", "12-Story Competency Matrix SVG", "Warehouse PathMapper Defense Dossier", "Anthropic Values Disagreement Strategy"]
    },
    {
        "id": "quant",
        "file": "quant.html",
        "title": "Aptitude, Probability & Puzzles",
        "short_title": "Quant & Puzzles",
        "icon": "🎲",
        "badge": "OA Gate",
        "badge_color": "amber",
        "est_mins": "15 min",
        "est_mins_deep": "60 min",
        "track": "E",
        "track_name": "Role-Specific & Human",
        "tier": "P1",
        "roles": ["SWE", "AI", "FDE"],
        "companies": ["Pace Stock Broking (₹41L)", "Campus OAs", "HFT/Quant", "OpenAI"],
        "desc": "Linearity of Expectation, Markov Absorbing States, Classic Brainteasers (12 Coins, 25 Horses, Monty Hall), Fermi Estimation, and Reservoir Sampling.",
        "highlights": ["Monty Hall Host Knowledge Tree SVG", "Stars and Bars Combinatorics SVG", "12 Coins 3 Weighings Decision Tree SVG", "Linearity of Expectation 15 Problem Bank"]
    }
]

CSS_STYLES = """
:root {
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
  
  /* Dark Theme (Default) */
  --bg-primary: #090d16;
  --bg-surface: #111827;
  --bg-card: #151e2e;
  --bg-card-hover: #1c283c;
  --bg-header: rgba(9, 13, 22, 0.94);
  --bg-subtle: #1e293b;
  --bg-code: #0b111e;
  
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --border-color: #1e293b;
  --border-focus: #38bdf8;
  
  --accent-blue: #38bdf8;
  --accent-cyan: #22d3ee;
  --accent-emerald: #34d399;
  --accent-amber: #fbbf24;
  --accent-rose: #f43f5e;
  --accent-purple: #c084fc;
  --accent-indigo: #818cf8;
  --accent-teal: #2dd4bf;
  --accent-orange: #fb923c;

  --header-height: 4rem;

  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.5);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
}

[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-surface: #ffffff;
  --bg-card: #ffffff;
  --bg-card-hover: #f1f5f9;
  --bg-header: rgba(255, 255, 255, 0.94);
  --bg-subtle: #f1f5f9;
  --bg-code: #f8fafc;
  
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  
  --border-color: #e2e8f0;
  --border-focus: #0284c7;
  
  --accent-blue: #0284c7;
  --accent-cyan: #0891b2;
  --accent-emerald: #059669;
  --accent-amber: #d97706;
  --accent-rose: #e11d48;
  --accent-purple: #9333ea;
  --accent-indigo: #4f46e5;
  --accent-teal: #0d9488;
  --accent-orange: #ea580c;

  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.08);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}

/* Dual-Mode Runtime Filtering (Sprint vs Deep Dive) */
html[data-mode="sprint"] [data-depth="deep"] {
  display: none !important;
}

/* Test Mode Styling */
html[data-test-mode="active"] details.faq-accordion:not([open]) summary {
  border-left: 4px solid var(--accent-amber);
  background-color: var(--bg-subtle);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

body {
  font-family: var(--font-sans);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  transition: background-color 0.2s ease, color 0.2s ease;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 3px Reading Progress Bar */
.reading-progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-emerald), var(--accent-purple));
  width: 0%;
  z-index: 1001;
  transition: width 0.1s linear;
}

/* Header */
header {
  background-color: var(--bg-header);
  border-bottom: 1px solid var(--border-color);
  padding: 0.65rem 1.25rem;
  position: sticky;
  top: 0;
  z-index: 1000;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  height: var(--header-height);
  display: flex;
  align-items: center;
}

.header-inner {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  width: 100%;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 800;
  font-size: 1.05rem;
  letter-spacing: -0.01em;
}

.brand-badge {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
  color: #fff;
  padding: 0.15rem 0.5rem;
  border-radius: 9999px;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  flex-wrap: wrap;
}

/* Dual-Mode Toggle */
.mode-toggle-group {
  display: flex;
  align-items: center;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 2px;
  gap: 2px;
}

.mode-btn {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.3rem 0.65rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.mode-btn.active {
  background: var(--accent-blue);
  color: #fff;
}

.test-mode-btn {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.35rem 0.7rem;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.test-mode-btn.active {
  background: rgba(245, 158, 11, 0.15);
  color: var(--accent-amber);
  border-color: var(--accent-amber);
}

.nav-select {
  background: var(--bg-surface);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  padding: 0.4rem 0.75rem;
  border-radius: 0.5rem;
  font-family: var(--font-sans);
  font-size: 0.8rem;
  cursor: pointer;
  outline: none;
  max-width: 220px;
}

.theme-toggle-btn {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 0.4rem 0.65rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 0.82rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.hamburger-btn {
  display: none;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 0.4rem 0.65rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1.1rem;
}

/* Breadcrumbs */
.breadcrumb-nav {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 1.25rem;
}

.breadcrumb-nav a {
  color: var(--accent-blue);
  text-decoration: none;
  font-weight: 600;
}

.breadcrumb-sep {
  color: var(--text-muted);
}

/* Layout */
.app-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 1.5rem 1.25rem 5rem;
  width: 100%;
  flex: 1;
}

.content-wrapper {
  display: grid;
  grid-template-columns: 290px 1fr;
  gap: 2.25rem;
  align-items: start;
}

@media (max-width: 1024px) {
  .content-wrapper {
    grid-template-columns: 1fr;
  }
  .sidebar-toc {
    display: none !important;
  }
  .hamburger-btn {
    display: block !important;
  }
  .nav-select {
    display: none !important;
  }
}

/* Sticky Sidebar TOC */
.sidebar-toc {
  position: sticky;
  top: calc(var(--header-height) + 1.25rem);
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
  max-height: calc(100vh - 6.5rem);
  overflow-y: auto;
}

.toc-title {
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  font-weight: 700;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.toc-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.toc-link {
  display: block;
  padding: 0.35rem 0.6rem;
  border-radius: 0.375rem;
  text-decoration: none;
  color: var(--text-secondary);
  font-size: 0.83rem;
  line-height: 1.4;
  transition: all 0.15s;
}

.toc-link:hover {
  color: var(--accent-blue);
  background: var(--bg-subtle);
  transform: translateX(2px);
}

.toc-link.active {
  color: var(--accent-blue);
  background: rgba(56, 189, 248, 0.12);
  font-weight: 700;
  border-left: 3px solid var(--accent-blue);
  padding-left: 0.5rem;
}

/* Mobile Slide-out Drawer */
.mobile-drawer-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  z-index: 2000;
  backdrop-filter: blur(4px);
}

.mobile-drawer-overlay.active {
  display: block;
}

.mobile-drawer {
  position: fixed;
  top: 0;
  left: -320px;
  width: 300px;
  height: 100vh;
  background: var(--bg-surface);
  border-right: 1px solid var(--border-color);
  z-index: 2001;
  overflow-y: auto;
  padding: 1.5rem;
  transition: transform 0.25s ease-out;
}

.mobile-drawer.active {
  transform: translateX(320px);
}

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--border-color);
}

.drawer-close-btn {
  background: transparent;
  border: none;
  font-size: 1.5rem;
  color: var(--text-muted);
  cursor: pointer;
}

/* Fixed Mobile Bottom Nav */
.bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3.5rem;
  background: var(--bg-header);
  border-top: 1px solid var(--border-color);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  z-index: 1000;
  align-items: center;
  justify-content: space-around;
  padding: 0 0.5rem;
}

@media (max-width: 1024px) {
  .bottom-nav {
    display: flex;
  }
}

.bottom-nav-item {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.7rem;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.2rem;
  text-decoration: none;
  cursor: pointer;
  padding: 0.3rem 0.5rem;
  min-width: 48px;
}

.bottom-nav-item span:first-child {
  font-size: 1.1rem;
}

.bottom-nav-item:hover, .bottom-nav-item.active {
  color: var(--accent-blue);
}

/* Floating Back-to-Top Button */
.back-to-top-btn {
  position: fixed;
  bottom: 4.5rem;
  right: 1.5rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  width: 2.75rem;
  height: 2.75rem;
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: var(--shadow-md);
  opacity: 0;
  pointer-events: none;
  transition: all 0.2s;
  z-index: 900;
  font-size: 1.1rem;
}

.back-to-top-btn.visible {
  opacity: 1;
  pointer-events: auto;
}

/* Main Content Area */
.main-body {
  min-width: 0;
}

/* Hero Banner */
.hero-card {
  background: linear-gradient(135deg, rgba(56, 189, 248, 0.08), rgba(99, 102, 241, 0.05));
  border: 1px solid var(--border-color);
  border-radius: 1rem;
  padding: 1.75rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}

.hero-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.hero-title-group {
  display: flex;
  align-items: center;
  gap: 0.85rem;
}

.hero-icon {
  font-size: 2.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 3.5rem;
  height: 3.5rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
}

.hero-title {
  font-size: 1.75rem;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
}

.hero-subtitle {
  color: var(--text-secondary);
  font-size: 0.95rem;
  margin-top: 0.25rem;
  max-width: 800px;
}

/* Pill Badges - Complete 9 Colors (§1.3 Fix) */
.meta-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  padding: 0.25rem 0.65rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  border: 1px solid transparent;
}

.pill-blue    { background: rgba(56, 189, 248, 0.12); color: var(--accent-blue);   border-color: rgba(56, 189, 248, 0.3); }
.pill-emerald { background: rgba(52, 211, 153, 0.12); color: var(--accent-emerald);border-color: rgba(52, 211, 153, 0.3); }
.pill-amber   { background: rgba(251, 191, 36, 0.12); color: var(--accent-amber);  border-color: rgba(251, 191, 36, 0.3); }
.pill-rose    { background: rgba(244, 63, 94, 0.12);  color: var(--accent-rose);   border-color: rgba(244, 63, 94, 0.3); }
.pill-purple  { background: rgba(192, 132, 252, 0.12);color: var(--accent-purple); border-color: rgba(192, 132, 252, 0.3); }
.pill-cyan    { background: rgba(34, 211, 238, 0.12); color: var(--accent-cyan);   border-color: rgba(34, 211, 238, 0.3); }
.pill-indigo  { background: rgba(129, 140, 248, 0.12);color: var(--accent-indigo); border-color: rgba(129, 140, 248, 0.3); }
.pill-teal    { background: rgba(45, 212, 191, 0.12); color: var(--accent-teal);   border-color: rgba(45, 212, 191, 0.3); }
.pill-orange  { background: rgba(251, 146, 60, 0.12); color: var(--accent-orange); border-color: rgba(251, 146, 60, 0.3); }

/* Section Blocks */
.section-block {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 1rem;
  padding: 1.75rem;
  margin-bottom: 2rem;
  scroll-margin-top: calc(var(--header-height) + 1rem);
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  flex-wrap: wrap;
}

.section-title {
  font-size: 1.35rem;
  font-weight: 800;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.heading-anchor {
  color: var(--text-muted);
  text-decoration: none;
  opacity: 0.4;
  font-size: 1rem;
}

.heading-anchor:hover {
  opacity: 1;
  color: var(--accent-blue);
}

.section-progress-label {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-secondary);
  cursor: pointer;
  background: var(--bg-card);
  padding: 0.3rem 0.65rem;
  border-radius: 0.5rem;
  border: 1px solid var(--border-color);
}

.section-body {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.65;
}

.section-body p {
  margin-bottom: 1rem;
}

/* Subsections */
.subsection-block {
  margin-top: 1.75rem;
  padding-top: 1.25rem;
  border-top: 1px dashed var(--border-color);
  scroll-margin-top: calc(var(--header-height) + 1rem);
}

.subsection-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Dense Data Tables */
.table-container {
  overflow-x: auto;
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  margin: 1.25rem 0;
  background: var(--bg-card);
}

.table-caption {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-muted);
  padding: 0.6rem 1rem 0.2rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  text-align: left;
}

.data-table th, .data-table td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--border-color);
  vertical-align: top;
}

.data-table th {
  background: var(--bg-subtle);
  color: var(--text-primary);
  font-weight: 700;
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.data-table tr:last-child td {
  border-bottom: none;
}

.data-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}

/* SVGs & Diagram Containers */
.svg-diagram-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
  margin: 1.5rem 0;
  text-align: center;
}

.svg-container {
  overflow-x: auto;
  display: flex;
  justify-content: center;
  cursor: zoom-in;
}

.svg-container svg {
  max-width: 100%;
  height: auto;
  border-radius: 0.5rem;
}

.diagram-caption {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 0.75rem;
  font-weight: 500;
}

/* Formula Box (KaTeX + Spoken Reading + Meaning) */
.formula-box {
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.08), rgba(56, 189, 248, 0.04));
  border: 1px solid var(--accent-indigo);
  border-radius: 0.85rem;
  padding: 1.25rem;
  margin: 1.5rem 0;
}

.formula-katex {
  font-size: 1.2rem;
  text-align: center;
  padding: 0.75rem 0;
  overflow-x: auto;
}

.formula-reading {
  font-size: 0.9rem;
  color: var(--text-secondary);
  margin-bottom: 0.75rem;
  padding: 0.4rem 0.6rem;
  background: var(--bg-surface);
  border-radius: 0.5rem;
  border-left: 3px solid var(--accent-blue);
}

.formula-symbols-wrapper {
  margin: 0.75rem 0;
}

.formula-symbols-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.83rem;
}

.formula-symbols-table th, .formula-symbols-table td {
  padding: 0.4rem 0.6rem;
  border-bottom: 1px solid var(--border-color);
}

.formula-symbols-table th {
  color: var(--text-muted);
  font-size: 0.75rem;
  text-transform: uppercase;
}

.formula-sym {
  width: 25%;
  font-family: var(--font-mono);
  color: var(--accent-cyan);
}

.formula-meaning {
  font-size: 0.88rem;
  color: var(--text-primary);
  margin-top: 0.75rem;
  background: rgba(16, 185, 129, 0.1);
  padding: 0.6rem 0.75rem;
  border-radius: 0.5rem;
  border-left: 3px solid var(--accent-emerald);
}

/* Worked Example Card */
.worked-example {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
  margin: 1.5rem 0;
}

.we-header {
  margin-bottom: 1rem;
}

.we-badge {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: var(--accent-purple);
  text-transform: uppercase;
}

.we-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-top: 0.25rem;
}

.we-step {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  padding: 0.85rem;
  margin-bottom: 0.75rem;
}

.we-step-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.4rem;
}

.we-step-num {
  background: var(--accent-purple);
  color: #fff;
  padding: 0.15rem 0.45rem;
  border-radius: 0.35rem;
  font-size: 0.7rem;
}

.we-step-body {
  font-size: 0.88rem;
  color: var(--text-secondary);
}

.we-answer-details {
  margin-top: 1rem;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid var(--accent-blue);
  border-radius: 0.5rem;
  overflow: hidden;
}

.we-answer-summary {
  padding: 0.75rem 1rem;
  cursor: pointer;
  font-weight: 700;
  color: var(--accent-blue);
  font-size: 0.88rem;
}

.we-answer-body {
  padding: 1rem;
  border-top: 1px solid var(--border-color);
  font-size: 0.9rem;
  color: var(--text-primary);
}

/* Callouts */
.callout {
  border-radius: 0.75rem;
  padding: 1.25rem;
  margin: 1.25rem 0;
  border: 1px solid transparent;
}

.callout-title {
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.callout-badge {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  padding: 0.15rem 0.45rem;
  border-radius: 0.35rem;
  text-transform: uppercase;
}

.callout-info   { background: rgba(56, 189, 248, 0.08); border-color: rgba(56, 189, 248, 0.3); color: var(--text-primary); }
.callout-info .callout-badge { background: var(--accent-blue); color: #000; }

.callout-trap   { background: rgba(244, 63, 94, 0.08); border-color: rgba(244, 63, 94, 0.3); color: var(--text-primary); }
.callout-trap .callout-badge { background: var(--accent-rose); color: #fff; }

.callout-pro    { background: rgba(52, 211, 153, 0.08); border-color: rgba(52, 211, 153, 0.3); color: var(--text-primary); }
.callout-pro .callout-badge { background: var(--accent-emerald); color: #000; }

.callout-hft    { background: rgba(129, 140, 248, 0.08); border-color: rgba(129, 140, 248, 0.3); color: var(--text-primary); }
.callout-hft .callout-badge { background: var(--accent-indigo); color: #fff; }

.callout-math   { background: rgba(192, 132, 252, 0.08); border-color: rgba(192, 132, 252, 0.3); color: var(--text-primary); }
.callout-math .callout-badge { background: var(--accent-purple); color: #000; }

.callout-fde    { background: rgba(45, 212, 191, 0.08); border-color: rgba(45, 212, 191, 0.3); color: var(--text-primary); }
.callout-fde .callout-badge { background: var(--accent-teal); color: #000; }

.callout-ai     { background: rgba(251, 146, 60, 0.08); border-color: rgba(251, 146, 60, 0.3); color: var(--text-primary); }
.callout-ai .callout-badge { background: var(--accent-orange); color: #000; }

.callout-warn   { background: rgba(251, 191, 36, 0.08); border-color: rgba(251, 191, 36, 0.3); color: var(--text-primary); }
.callout-warn .callout-badge { background: var(--accent-amber); color: #000; }

.callout-body {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Decision Matrix */
.decision-matrix-card {
  margin: 1.5rem 0;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
}

.dm-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
}

.dm-table td {
  font-size: 0.85rem;
}

.badge-use {
  color: var(--accent-emerald);
  font-weight: 700;
  font-size: 0.75rem;
}

.badge-avoid {
  color: var(--accent-rose);
  font-weight: 700;
  font-size: 0.75rem;
}

/* Anti-Pattern Side-by-Side */
.anti-pattern-card {
  margin: 1.5rem 0;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
}

.ap-header {
  margin-bottom: 0.85rem;
}

.ap-badge {
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  color: var(--accent-rose);
}

.ap-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-top: 0.2rem;
}

.ap-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

@media (max-width: 768px) {
  .ap-grid {
    grid-template-columns: 1fr;
  }
}

.ap-col {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  overflow: hidden;
}

.ap-col-header {
  padding: 0.4rem 0.75rem;
  font-size: 0.75rem;
  font-weight: 700;
}

.ap-bad .ap-col-header { background: rgba(244, 63, 94, 0.15); color: var(--accent-rose); }
.ap-good .ap-col-header { background: rgba(52, 211, 153, 0.15); color: var(--accent-emerald); }

.ap-failure-mode {
  margin-top: 0.75rem;
  padding: 0.65rem 0.85rem;
  background: rgba(251, 191, 36, 0.08);
  border-left: 3px solid var(--accent-amber);
  border-radius: 0.35rem;
  font-size: 0.85rem;
  color: var(--text-secondary);
}

/* Follow-up Chains (Drill Ladder) */
.followup-chain {
  margin: 1.5rem 0;
  background: var(--bg-card);
  border: 1px solid var(--accent-indigo);
  border-radius: 0.85rem;
  padding: 1.25rem;
}

.fc-header {
  margin-bottom: 1rem;
}

.fc-badge {
  font-size: 0.7rem;
  font-weight: 800;
  color: var(--accent-indigo);
  letter-spacing: 0.05em;
}

.fc-root-q {
  font-size: 1.05rem;
  color: var(--text-primary);
  margin-top: 0.25rem;
}

.fc-levels-container {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.fc-level {
  margin-left: 1rem;
  border-left: 2px dashed var(--accent-indigo);
  padding-left: 1rem;
}

.fc-connector {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--accent-indigo);
  margin-bottom: 0.25rem;
}

.fc-accordion {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  overflow: hidden;
}

.fc-summary {
  padding: 0.65rem 0.85rem;
  cursor: pointer;
  font-size: 0.88rem;
  color: var(--text-primary);
}

.fc-answer {
  padding: 0.85rem;
  border-top: 1px solid var(--border-color);
  font-size: 0.88rem;
  color: var(--text-secondary);
  line-height: 1.55;
}

/* Numbers Card */
.numbers-card {
  margin: 1.5rem 0;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.85rem;
  padding: 1.25rem;
}

.numbers-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.num-highlight {
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--accent-amber);
}

/* One-Liner Spoken Answer */
.one-liner-box {
  margin: 1.25rem 0;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid var(--accent-blue);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
}

.ol-badge {
  font-size: 0.7rem;
  font-weight: 800;
  color: var(--accent-blue);
  letter-spacing: 0.05em;
  margin-bottom: 0.35rem;
}

.ol-text {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  font-style: italic;
  line-height: 1.45;
}

/* Mnemonic Card */
.mnemonic-box {
  margin: 1.25rem 0;
  background: rgba(192, 132, 252, 0.08);
  border: 1px solid var(--accent-purple);
  border-radius: 0.75rem;
  padding: 1rem 1.25rem;
}

.mnemonic-badge {
  font-size: 0.7rem;
  font-weight: 800;
  color: var(--accent-purple);
  letter-spacing: 0.05em;
  margin-bottom: 0.35rem;
}

.mnemonic-hook {
  font-size: 1rem;
  color: var(--text-primary);
  margin-bottom: 0.35rem;
}

.hook-text {
  font-weight: 800;
  color: var(--accent-purple);
}

.mnemonic-expansion {
  font-size: 0.88rem;
  color: var(--text-secondary);
}

/* See Also Links */
.see-also-box {
  margin: 1.25rem 0;
  padding: 0.75rem 1rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.see-also-label {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--text-muted);
}

.see-also-links {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.see-also-link {
  font-size: 0.8rem;
  color: var(--accent-blue);
  text-decoration: none;
  background: var(--bg-card);
  padding: 0.2rem 0.5rem;
  border-radius: 0.35rem;
  border: 1px solid var(--border-color);
}

.see-also-link:hover {
  border-color: var(--accent-blue);
}

/* Code Blocks & Prism */
.code-block-wrapper {
  position: relative;
  margin: 1.25rem 0;
  border-radius: 0.75rem;
  overflow: hidden;
  border: 1px solid var(--border-color);
  background: var(--bg-code);
}

.code-title-bar {
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-color);
  padding: 0.45rem 1rem;
  font-size: 0.78rem;
  font-family: var(--font-mono);
  color: var(--text-muted);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.code-lang-tag {
  text-transform: uppercase;
  font-weight: 700;
  font-size: 0.65rem;
  background: var(--bg-subtle);
  padding: 0.1rem 0.4rem;
  border-radius: 0.25rem;
}

pre[class*="language-"] {
  margin: 0 !important;
  padding: 1rem 1.25rem !important;
  font-family: var(--font-mono) !important;
  font-size: 0.85rem !important;
  background: var(--bg-code) !important;
  overflow-x: auto;
}

.copy-btn {
  position: absolute;
  top: 0.5rem;
  right: 0.75rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-size: 0.75rem;
  font-family: var(--font-sans);
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  cursor: pointer;
  opacity: 0;
  transition: all 0.2s;
  z-index: 10;
}

.code-block-wrapper:hover .copy-btn {
  opacity: 1;
}

/* FAQ / Flashcard Accordions */
.faq-accordion {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 0.75rem;
  margin-bottom: 0.75rem;
  overflow: hidden;
  transition: all 0.2s;
}

.faq-accordion[open] {
  border-color: var(--accent-blue);
}

.faq-summary {
  padding: 1rem 1.25rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  user-select: none;
  font-size: 0.95rem;
  color: var(--text-primary);
}

.faq-question-text {
  flex: 1;
}

.faq-pills {
  display: flex;
  gap: 0.35rem;
  flex-wrap: wrap;
}

.faq-answer {
  padding: 1.25rem;
  border-top: 1px solid var(--border-color);
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.6;
  background: var(--bg-surface);
}

/* Spaced Repetition Rating Strip */
.rating-strip {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-top: 1rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--border-color);
  flex-wrap: wrap;
}

.rating-prompt {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.rating-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  font-family: var(--font-sans);
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.6rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-got-it:hover, .rating-btn.rated-got-it {
  background: rgba(52, 211, 153, 0.15);
  border-color: var(--accent-emerald);
  color: var(--accent-emerald);
}

.btn-shaky:hover, .rating-btn.rated-shaky {
  background: rgba(251, 191, 36, 0.15);
  border-color: var(--accent-amber);
  color: var(--accent-amber);
}

.btn-no-idea:hover, .rating-btn.rated-no-idea {
  background: rgba(244, 63, 94, 0.15);
  border-color: var(--accent-rose);
  color: var(--accent-rose);
}

/* Navigation Footer */
.page-nav-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border-color);
  flex-wrap: wrap;
  gap: 1rem;
}

.nav-btn {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  text-decoration: none;
  padding: 0.65rem 1.25rem;
  border-radius: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}

.nav-btn:hover {
  background: var(--bg-subtle);
  border-color: var(--accent-blue);
  color: var(--accent-blue);
}

/* Print Styles */
@media print {
  header, .sidebar-toc, .bottom-nav, .back-to-top-btn, .page-nav-footer, .rating-strip {
    display: none !important;
  }
  body, .app-container, .main-body {
    background: #fff !important;
    color: #000 !important;
    padding: 0 !important;
    max-width: 100% !important;
  }
  .section-block, .hero-card, .table-container, .callout {
    border: 1px solid #ccc !important;
    box-shadow: none !important;
  }
}
"""

JS_SCRIPTS = """
<script>
// Study Material Suite - Interactive Engine & Learning System
// Implements Dual-Mode, Self-Test, Spaced Repetition, ScrollSpy & Mobile Drawer

function initTheme() {
  const savedTheme = localStorage.getItem('study_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeBtn(savedTheme);
}

function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('study_theme', next);
  updateThemeBtn(next);
}

function updateThemeBtn(theme) {
  const btns = document.querySelectorAll('.theme-toggle-btn');
  btns.forEach(btn => {
    btn.innerHTML = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
  });
}

// Dual-Mode Study Engine (Sprint vs Deep Dive)
function initMode() {
  const savedMode = localStorage.getItem('study_mode') || 'sprint';
  setStudyMode(savedMode, false);
}

function setStudyMode(mode, save = true) {
  document.documentElement.setAttribute('data-mode', mode);
  if (save) localStorage.setItem('study_mode', mode);

  const sprintBtns = document.querySelectorAll('#sprintModeBtn');
  const deepBtns = document.querySelectorAll('#deepModeBtn');
  
  if (mode === 'sprint') {
    sprintBtns.forEach(b => b.classList.add('active'));
    deepBtns.forEach(b => b.classList.remove('active'));
    const bottomLbl = document.getElementById('bottomNavModeLabel');
    if (bottomLbl) bottomLbl.innerText = 'Sprint';
  } else {
    sprintBtns.forEach(b => b.classList.remove('active'));
    deepBtns.forEach(b => b.classList.add('active'));
    const bottomLbl = document.getElementById('bottomNavModeLabel');
    if (bottomLbl) bottomLbl.innerText = 'Deep';
  }
}

function cycleStudyMode() {
  const cur = document.documentElement.getAttribute('data-mode') || 'sprint';
  const next = cur === 'sprint' ? 'deep' : 'sprint';
  setStudyMode(next);
}

// Test Mode (Collapse all Q&A and prompt recall)
function initTestMode() {
  const isTest = localStorage.getItem('study_test_mode') === 'active';
  if (isTest) applyTestMode(true);
}

function toggleTestMode() {
  const current = document.documentElement.getAttribute('data-test-mode');
  const next = current === 'active' ? 'normal' : 'active';
  applyTestMode(next === 'active');
  localStorage.setItem('study_test_mode', next);
}

function applyTestMode(active) {
  const btn = document.getElementById('testModeBtn');
  if (active) {
    document.documentElement.setAttribute('data-test-mode', 'active');
    if (btn) btn.classList.add('active');
    document.querySelectorAll('.faq-accordion').forEach(el => el.removeAttribute('open'));
  } else {
    document.documentElement.removeAttribute('data-test-mode');
    if (btn) btn.classList.remove('active');
  }
}

// Mobile Slide-out Drawer
function toggleMobileDrawer() {
  const drawer = document.getElementById('mobileDrawer');
  const overlay = document.getElementById('mobileDrawerOverlay');
  if (!drawer || !overlay) return;
  drawer.classList.toggle('active');
  overlay.classList.toggle('active');
}

// ScrollSpy & Reading Progress
function initReadingProgress() {
  const progressBar = document.getElementById('readingProgressBar');
  const backToTop = document.getElementById('backToTopBtn');
  
  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
    
    if (progressBar) progressBar.style.width = scrolled + '%';
    if (backToTop) {
      if (winScroll > 500) backToTop.classList.add('visible');
      else backToTop.classList.remove('visible');
    }
  }, { passive: true });
}

function initScrollSpy() {
  const sections = document.querySelectorAll('.section-block[id]');
  const tocLinks = document.querySelectorAll('.toc-link');
  if (!sections.length || !tocLinks.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        tocLinks.forEach(link => {
          if (link.getAttribute('href') === '#' + id) link.classList.add('active');
          else link.classList.remove('active');
        });
      }
    });
  }, { rootMargin: '-10% 0px -75% 0px' });

  sections.forEach(sec => observer.observe(sec));
}

// Section Progress Tracking
function initSectionProgress(moduleId) {
  const checks = document.querySelectorAll('.section-check');
  checks.forEach(check => {
    const anchor = check.dataset.anchor;
    const key = `sect_${moduleId}_${anchor}`;
    if (localStorage.getItem(key) === 'done') {
      check.checked = true;
    }
  });
}

function toggleSectionDone(anchor, isDone) {
  const path = window.location.pathname;
  const modFile = path.substring(path.lastIndexOf('/') + 1);
  const moduleId = modFile.replace('.html', '');
  const key = `sect_${moduleId}_${anchor}`;
  if (isDone) localStorage.setItem(key, 'done');
  else localStorage.removeItem(key);
}

// Spaced Repetition Rating Engine
function rateFlashcard(qid, rating, btn) {
  const now = Date.now();
  const queue = JSON.parse(localStorage.getItem('study_review_queue') || '{}');
  queue[qid] = { rating, timestamp: now };
  localStorage.setItem('study_review_queue', JSON.stringify(queue));

  const parentStrip = btn.closest('.rating-strip');
  if (parentStrip) {
    parentStrip.querySelectorAll('.rating-btn').forEach(b => {
      b.classList.remove('rated-got-it', 'rated-shaky', 'rated-no-idea');
    });
    btn.classList.add(`rated-${rating.replace('_', '-')}`);
  }
}

// QuickNav Select
function initQuickNav() {
  const select = document.getElementById('quickNavSelect');
  if (select) {
    select.addEventListener('change', (e) => {
      if (e.target.value) window.location.href = e.target.value;
    });
  }
}

// Copy Buttons for Code
function initCopyButtons() {
  document.querySelectorAll('pre[class*="language-"]').forEach(pre => {
    const wrapper = pre.closest('.code-block-wrapper');
    if (!wrapper) return;
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.innerText = 'Copy';
    wrapper.appendChild(btn);

    btn.addEventListener('click', () => {
      const code = pre.querySelector('code') ? pre.querySelector('code').innerText : pre.innerText;
      navigator.clipboard.writeText(code).then(() => {
        btn.innerText = 'Copied!';
        setTimeout(() => btn.innerText = 'Copy', 2000);
      });
    });
  });
}

// KaTeX Auto-Render Initializer (§1.2 Fix)
function initKatex() {
  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\\\[', right: '\\\\]', display: true},
        {left: '\\\\(', right: '\\\\)', display: false}
      ],
      throwOnError: false
    });
  }
}

// Keyboard Navigation Shortcuts
function initKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;
    if (e.key === 't') toggleTheme();
    else if (e.key === 'm') cycleStudyMode();
    else if (e.key === 'k' && (e.ctrlKey || e.metaKey)) {
      e.preventDefault();
      // focus search if on index or open quicknav
      const qn = document.getElementById('quickNavSelect');
      if (qn) qn.focus();
    }
  });
}

// DOM Readiness Bootloader
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMode();
  initTestMode();
  initQuickNav();
  initCopyButtons();
  initReadingProgress();
  initScrollSpy();
  initKeyboardShortcuts();
  
  // Render math when KaTeX is loaded
  if (window.renderMathInElement) {
    initKatex();
  } else {
    window.addEventListener('load', initKatex);
  }
});
</script>
"""

def render_page(module_id, page_title, toc_items, content_html, prev_link=None, prev_title=None, next_link=None, next_title=None):
    """
    Renders a unified responsive HTML page incorporating Dual-Mode, KaTeX math,
    mobile navigation drawer, sticky header with toggles, and breadcrumb pathing.
    """
    meta = next((m for m in MODULES_META if m["id"] == module_id), None)
    track_code = meta["track"] if meta else "A"
    track_name = meta["track_name"] if meta else "Core CS"
    
    # Quick nav select options
    quick_opts = '<option value="">⚡ Switch Topic...</option>'
    for m in MODULES_META:
        sel = ' selected' if m["id"] == module_id else ''
        quick_opts += f'<option value="{m["file"]}"{sel}>{m["icon"]} {m["title"]}</option>'
        
    # TOC List (both sidebar and mobile drawer)
    toc_html = ""
    for anchor, label in toc_items:
        toc_html += f'<li><a href="#{anchor}" class="toc-link">{label}</a></li>\n'
        
    # Target companies pills
    company_pills = "".join([f'<span class="pill pill-blue">{c}</span>' for c in (meta["companies"] if meta else [])])
    
    # Bottom Navigation Footer Links
    footer_html = '<div class="page-nav-footer">'
    if prev_link:
        footer_html += f'<a href="{prev_link}" class="nav-btn">← {prev_title}</a>'
    else:
        footer_html += '<a href="index.html" class="nav-btn">← Dashboard Hub</a>'
        
    if next_link:
        footer_html += f'<a href="{next_link}" class="nav-btn" style="margin-left: auto;">{next_title} →</a>'
    else:
        footer_html += '<a href="index.html" class="nav-btn" style="margin-left: auto;">Back to Hub 🏠</a>'
    footer_html += '</div>'

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark" data-mode="sprint">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>{page_title} · Fast Interview Cheat Sheet</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- KaTeX Formula Support (§1.2 Fix) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>

  <!-- PrismJS Syntax Highlighting -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-c.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-cpp.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-sql.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-docker.min.js"></script>
  
  <style>
{CSS_STYLES}
  </style>
</head>
<body>

  <!-- Top 3px Reading Progress Bar -->
  <div class="reading-progress-bar" id="readingProgressBar"></div>

  <!-- Sticky Header -->
  <header>
    <div class="header-inner">
      <div style="display: flex; align-items: center; gap: 0.75rem;">
        <button class="hamburger-btn" onclick="toggleMobileDrawer()" aria-label="Toggle Navigation Drawer">☰</button>
        <a href="index.html" class="brand">
          <span>⚡ PrepPortal</span>
          <span class="brand-badge">Study Suite</span>
        </a>
      </div>
      
      <div class="header-actions">
        <!-- Dual-Mode Switch (Sprint 15m vs Deep 60m) -->
        <div class="mode-toggle-group">
          <button id="sprintModeBtn" class="mode-btn active" onclick="setStudyMode('sprint')">⚡ Sprint (15m)</button>
          <button id="deepModeBtn" class="mode-btn" onclick="setStudyMode('deep')">🧠 Deep (60m)</button>
        </div>

        <button id="testModeBtn" class="test-mode-btn" onclick="toggleTestMode()" title="Toggle Test Mode (Collapses answers)">🎓 Test Mode</button>
        
        <select id="quickNavSelect" class="nav-select">
          {quick_opts}
        </select>
        
        <button id="themeToggleBtn" class="theme-toggle-btn" onclick="toggleTheme()">☀️ Light</button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Overlay & Content -->
  <div class="mobile-drawer-overlay" id="mobileDrawerOverlay" onclick="toggleMobileDrawer()"></div>
  <div class="mobile-drawer" id="mobileDrawer">
    <div class="drawer-header">
      <span style="font-weight: 800; font-size: 1rem; color: var(--text-primary);">📑 Sections Navigation</span>
      <button class="drawer-close-btn" onclick="toggleMobileDrawer()">✕</button>
    </div>
    <ul class="toc-list" onclick="toggleMobileDrawer()">
      {toc_html}
    </ul>
    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="index.html" style="text-decoration: none; font-size: 0.85rem; color: var(--accent-blue); font-weight: 700;">← Return to Master Hub</a>
    </div>
  </div>

  <!-- Container -->
  <div class="app-container">
    
    <!-- Breadcrumb Orientation -->
    <nav class="breadcrumb-nav">
      <a href="index.html">Master Hub</a>
      <span class="breadcrumb-sep">›</span>
      <span>Track {track_code}: {track_name}</span>
      <span class="breadcrumb-sep">›</span>
      <span style="color: var(--text-primary); font-weight: 600;">{meta["short_title"] if meta else page_title}</span>
    </nav>

    <div class="content-wrapper">
      
      <!-- Sticky Sidebar TOC (Desktop) -->
      <aside class="sidebar-toc">
        <div class="toc-title">
          <span>Module Sections</span>
          <span style="font-size: 0.75rem;">⏱️ {meta["est_mins"] if meta else "15m"} / {meta["est_mins_deep"] if meta else "60m"}</span>
        </div>
        <ul class="toc-list">
          {toc_html}
        </ul>
        <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
          <a href="index.html" style="text-decoration: none; font-size: 0.85rem; color: var(--accent-blue); font-weight: 600; display: flex; align-items: center; gap: 0.35rem;">
            ← Return to Dashboard
          </a>
        </div>
      </aside>

      <!-- Main Body -->
      <main class="main-body">
        
        <!-- Hero Header -->
        <div class="hero-card">
          <div class="hero-header">
            <div class="hero-title-group">
              <div class="hero-icon">{meta["icon"] if meta else "📚"}</div>
              <div>
                <h1 class="hero-title">{meta["title"] if meta else page_title}</h1>
                <p class="hero-subtitle">{meta["desc"] if meta else "High-yield interview cheat sheet, mental model SVGs, and edge cases."}</p>
              </div>
            </div>
          </div>
          <div class="meta-pills">
            <span class="pill pill-emerald">⚡ 15-Min Sprint</span>
            <span class="pill pill-indigo">🧠 60-Min Deep Dive</span>
            <span class="pill pill-amber">Target Companies:</span>
            {company_pills}
          </div>
        </div>

        <!-- Rendered Content -->
        {content_html}

        <!-- Bottom Page Navigation -->
        {footer_html}

      </main>

    </div>
  </div>

  <!-- Mobile Fixed Bottom Nav -->
  <nav class="bottom-nav">
    <a href="index.html" class="bottom-nav-item"><span>🏠</span><span>Hub</span></a>
    <button onclick="toggleMobileDrawer()" class="bottom-nav-item"><span>📑</span><span>Sections</span></button>
    <button onclick="cycleStudyMode()" class="bottom-nav-item"><span>⚡</span><span id="bottomNavModeLabel">Sprint</span></button>
    <button onclick="toggleTheme()" class="bottom-nav-item"><span>🌙</span><span>Theme</span></button>
    <button onclick="window.scrollTo({{top:0, behavior:'smooth'}})" class="bottom-nav-item"><span>↑</span><span>Top</span></button>
  </nav>

  <!-- Back to Top FAB -->
  <button id="backToTopBtn" class="back-to-top-btn" onclick="window.scrollTo({{top:0, behavior:'smooth'}})" title="Back to top">↑</button>

{JS_SCRIPTS}
<script>
  document.addEventListener('DOMContentLoaded', () => {{
    initSectionProgress('{module_id}');
  }});
</script>
</body>
</html>
"""
