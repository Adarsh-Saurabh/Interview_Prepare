# modules_part1.py - Solumn AI Modules 00, 01, 02

modules_part1 = {
    "00_START_HERE": {
        "title": "Module 00: Company & Role Intel · Solumn AI Foundations 2026",
        "active_page": "00_START_HERE.html",
        "prev_link": "index.html",
        "prev_title": "Overview Hub",
        "next_link": "01_Practical_Assignment.html",
        "next_title": "01: Practical Task & Verifiers",
        "content_md": """# Module 00: Company & Role Intelligence · Solumn AI

## 1. Executive Summary & Corporate Identity

* **Entity Name:** **Solumn AI** (also operating under the engineering banner **BrainBrowser**)
* **Headquarters:** Dubai, United Arab Emirates (Operating globally with distributed engineering across India, UAE, and US)
* **Founding Team:**
  * **Samiksha Shrawgi:** Alumna of **IIT Kharagpur** and **Indian School of Business (ISB)**; previously Strategy Consultant at **Boston Consulting Group (BCG)**.
  * **Ashish Arpit:** Alumnus of **IIT Roorkee** and **IIM Calcutta**; previously Engagement Manager at **McKinsey & Company**.
* **Corporate DNA:** An elite blend of **top-tier management consulting rigor** (extreme structured thinking, milestone orientation, output velocity) and **frontier AI systems engineering** (falsifiable tests, Docker sandboxing, deterministic verifiers).
* **The Foundations Programme:** An applied 6-week industrial engagement for final-year engineering students (Batch 2027) with a **₹2,00,000 stipend**, remote format, and a direct merit-based **Pre-Placement Offer (PPO)** conversion track.

---

## 2. Why Solumn AI Exists: The Frontier AI Assurance Layer

### The Macro Shift: Capabilities vs. Deployment Gates
Frontier AI laboratories—specifically **Anthropic, Google DeepMind, Amazon, OpenAI, and Meta**—are training foundation models whose parameter scale and agentic capabilities advance exponentially. However, regulatory frameworks and internal governance have shifted fundamentally in 2025–2026:

$$\\text{Model Capability alone } \\cancel{\\implies} \\text{ Deployment}$$
$$\\text{Deployment Gate} = \\text{Empirical Safety Proof} \\;\\land\\; \\text{Falsifiable Verification}$$

Under binding policies such as **Anthropic's Responsible Scaling Policy (RSP Version 3.2)**, labs make explicit public and legal commitments:
> *"Maintaining our commitment not to train or deploy models unless we have implemented adequate safeguards."*

When a model reaches **AI Safety Level 3 (ASL-3)** or **ASL-4** thresholds (autonomous cyber-offense, self-exfiltration, biological hazard assistance, unmonitored tool privilege escalation), safety teams cannot rely on:
1. **Subjective prompt evaluations** (vibes, human RLHF raters grading conversational warmth).
2. **Static academic benchmarks** (MMLU, HumanEval, GSM8K)—which are contaminated, non-interactive, and test memorization rather than execution under stress.

### Solumn's Business Model
Solumn operates as a specialized **Evaluation Foundry and Red-Teaming Infrastructure Partner**. Frontier laboratories pay premium enterprise bounties to external verification foundries like Solumn to build the ground-truth benchmark environments against which models must be audited before releasing checkpoints.

```
+-------------------------------------------------------------------------+
|                        Frontier AI Laboratory                           |
|       (Anthropic Claude 3.7 / OpenAI o3 / Google Gemini 2.5 Pro)        |
+-------------------------------------------------------------------------+
                                    |
          Demands External, Falsifiable Safety Evidence (RSP Gates)
                                    v
+-------------------------------------------------------------------------+
|                       Solumn AI Evaluation Foundry                      |
|                                                                         |
|  [ Workstream 1: Agentic RLEs ]   Containerized Docker environments     |
|  [ Workstream 2: Vulnerability ]   Real CVE exploits + regression tests  |
|  [ Workstream 3: Adversarial ]    MCP & tool-calling attack suites      |
+-------------------------------------------------------------------------+
                                    |
                 Deterministic Graders Output PASS / FAIL
                                    v
+-------------------------------------------------------------------------+
|                  Frontier Safety Gate: Audit Approved                   |
+-------------------------------------------------------------------------+
```

---

## 3. The Three Core Live Workstreams

| Workstream | Core Problem Statement | Technical Stack | Primary Deliverable |
| :--- | :--- | :--- | :--- |
| **1. Agentic Environments** | Building sandboxed environments that place an autonomous coding agent under pressure, with a deterministic test harness judging whether it held the line. | Docker, Python, Bash, Pytest, Linux cgroups | Containerized scenario packages, repository fixtures, reference solutions, pass/fail grading scripts. |
| **2. Vulnerability Datasets** | Curating find-and-fix software security tasks derived from real-world CVEs across open-source codebases. | C/C++, Python, Git, Fuzzers, Patch parsers | Reproducible exploit reproduction script + deterministic unit-test harness that passes only after genuine patch application. |
| **3. Adversarial Evaluation** | Stress-testing tool-calling interfaces and **Model Context Protocol (MCP)** deployments against prompt injections and privilege escalation. | Python, LangGraph/LiteLLM, JSON-RPC, MCP Servers | Attack suites evaluating jailbreaks, unauthorized API calls, and data exfiltration against structured harm taxonomies. |

---

## 4. Programme Deliverables, Metrics & Milestones

The Foundations Programme is explicitly **production-driven**:

* **Baseline Quota:** **250 Reinforcement Learning Environments (RLEs)** over 6 weeks.
  * *Daily Velocity Required:* $250 \\div 42 \\text{ days} \\approx \\mathbf{6\\text{ environments / day}}$ (or $\\approx 3\\text{ to } 4\\text{ hours/day}$).
* **Founders' Recognition Tier:** Candidates delivering **>500 verified environments** receive a formal **Letter of Recommendation from the Founders**.
* **Research Fellowship Track:** Top performers who formulate and pitch a novel evaluation harness or benchmark graduate to the **Solumn Research Fellowship**—fully funded research with named co-authorship on peer-reviewed papers.
* **Pre-Placement Offer (PPO):** Converted on merit at close, benchmarked to global frontier AI research roles (typical market package: ₹25 – ₹45+ LPA equivalent or tax-free Dubai packages).

---

## 5. Selection Process & Tight Timetable

```
[Oct 8, 11:59 PM]   ---> [Oct 9, 11:00 AM]   ---> [Oct 9, 12:00 PM]   ---> [Oct 10, 09:00 AM]  ---> [Oct 11]
Campus Application        CV Shortlisting          Practical Take-Home      Take-Home Submission     Technical
Form Closes               Closes                   Assignment Released      Closes (21h Window)      Interviews
```

* **Stage 1 (CV Shortlisting):** Automated and manual review prioritizing evidence of shipped software, containers, systems projects, and reproducible benchmarks.
* **Stage 2 (Practical Assignment - 21 Hours):** Released Friday Oct 9 at 12:00 PM; due Saturday Oct 10 at 09:00 AM. Involves building Dockerized scenario packages, task descriptions, and deterministic grading harnesses in Python.
* **Stage 3 (Technical Interview - Sunday Oct 11):** 45-minute technical conversation drilling into your assignment design, handling flaky tests, Python subprocess concurrency, and candidate project architectures.
"""
    },

    "01_Practical_Assignment": {
        "title": "Module 01: Practical Task & Verifiers · Solumn AI Foundations 2026",
        "active_page": "01_Practical_Assignment.html",
        "prev_link": "00_START_HERE.html",
        "prev_title": "00: Company & Role Intel",
        "next_link": "02_Technical_Rounds.html",
        "next_title": "02: Python, Docker & Verifiers",
        "content_md": """# Module 01: The Practical Take-Home Assignment & Verifier Engineering

## 1. Deconstructing the 21-Hour Practical Selection Task

The Solumn AI selection task is not a generic LeetCode assessment. It is an **applied task authoring exercise**. You are asked to construct one or more **Reinforcement Learning Environment (RLE) Scenario Packages**.

### Anatomy of an RLE Scenario Package
Every production environment built for Solumn AI must adhere to a standardized schema:

```
scenario_package/
├── scenario.json            # Task metadata, category, difficulty, timeout
├── instructions.md          # Clear, unambiguous task prompt presented to the agent
├── fixture/                 # The baseline repository/codebase provided to the agent
│   ├── src/
│   ├── tests/
│   └── setup.py
├── solution/                # The gold-standard human reference fix/implementation
│   └── patch.diff
└── verifier/                # Deterministic test harness executing in isolation
    ├── test_verifier.py
    └── run_grade.sh
```

---

## 2. Signature Problem 1: Deterministic Code Verification Harness

### Problem Context
You must build an evaluation harness for an agent task where the LLM is asked to implement a thread-safe, lock-free LRU cache in Python. The verifier must provably fail on broken or race-condition-prone implementations and deterministically pass on the reference solution within a 5.0-second timeout.

### Production Solution: `verifier/test_verifier.py`

```python
import sys
import time
import threading
import importlib.util
from typing import Any, Optional

def load_submission_module(path: str):
    '''Dynamically load agent's submitted module in isolation.'''
    spec = importlib.util.spec_from_file_location("submission", path)
    if not spec or not spec.loader:
        raise ImportError(f"Could not load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_deterministic_lru_tests(submission_path: str) -> dict:
    results = {
        "test_basic_ops": False,
        "test_eviction_order": False,
        "test_concurrency_race": False,
        "execution_time_ms": 0.0,
        "all_passed": False,
        "error_log": ""
    }
    
    start_time = time.perf_counter()
    try:
        mod = load_submission_module(submission_path)
        LRUCache = getattr(mod, "LRUCache", None)
        if not LRUCache:
            raise AttributeError("Submission does not define class 'LRUCache'")

        # Test 1: Basic Get/Put
        cache = LRUCache(capacity=2)
        cache.put(1, 100)
        cache.put(2, 200)
        assert cache.get(1) == 100, "Cache get(1) failed to return value"
        assert cache.get(3) is None or cache.get(3) == -1, "Cache get(3) must return None or -1"
        results["test_basic_ops"] = True

        # Test 2: Deterministic Eviction Order
        cache.put(3, 300)  # Key 2 should be evicted because Key 1 was recently accessed
        assert cache.get(2) in (None, -1), "Key 2 should have been evicted"
        assert cache.get(3) == 300, "Key 3 should be present"
        assert cache.get(1) == 100, "Key 1 should still be present"
        results["test_eviction_order"] = True

        # Test 3: Multi-Threaded Stress Test (Deterministic Concurrency)
        concurrency_cache = LRUCache(capacity=50)
        errors = []

        def worker(thread_id: int):
            try:
                for i in range(100):
                    key = (thread_id * 100) + (i % 20)
                    concurrency_cache.put(key, i)
                    val = concurrency_cache.get(key)
                    # No race conditions corrupting internal doubly linked list
            except Exception as e:
                errors.append(f"Thread {thread_id} crashed: {str(e)}")

        threads = [threading.Thread(target=worker, args=(t,)) for t in range(8)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert len(errors) == 0, f"Concurrency errors encountered: {errors}"
        results["test_concurrency_race"] = True
        results["all_passed"] = True

    except Exception as e:
        results["error_log"] = f"Verification Failed: {type(e).__name__} - {str(e)}"
    finally:
        results["execution_time_ms"] = round((time.perf_counter() - start_time) * 1000, 2)

    return results

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "src/solution.py"
    grade = run_deterministic_lru_tests(target)
    print(f"VERIFIER_RESULT: {grade}")
    sys.exit(0 if grade["all_passed"] else 1)
```

---

## 3. Signature Problem 2: Real CVE Exploit Verifier (Vulnerability Dataset)

### Problem Context
In Workstream 2, you convert a real security vulnerability (e.g., **Path Traversal via Zip Slip or Unsafe Deserialization**) into an automated test. The verifier must run a synthetic attack payload against the vulnerable codebase, verify the exploit succeeds, and verify that applying the patch completely blocks the attack without breaking legitimate functionality.

### Production Solution: Automated Exploit Verification Harness

```python
import os
import subprocess
import tempfile
import zipfile
import pytest

def create_malicious_zip(archive_path: str, target_filename: str = "../../tmp/escaped.txt"):
    '''Craft a path-traversal zip payload (Zip Slip CVE-2018-1002201 pattern).'''
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(target_filename, "EXPLOIT_SUCCESSFUL_DATA_EXFILTRATION")

def run_extraction_harness(extractor_script: str, zip_path: str, extract_dir: str) -> subprocess.CompletedProcess:
    '''Run the target extraction script in a sandboxed subprocess.'''
    cmd = [
        "python3", extractor_script,
        "--archive", zip_path,
        "--dest", extract_dir
    ]
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=5.0
    )

def test_vulnerability_reproduction_and_fix():
    with tempfile.TemporaryDirectory() as sandbox_dir:
        dest_dir = os.path.join(sandbox_dir, "extracted")
        os.makedirs(dest_dir, exist_ok=True)
        
        malicious_zip = os.path.join(sandbox_dir, "payload.zip")
        canary_file = os.path.join(sandbox_dir, "escaped.txt")
        
        create_malicious_zip(malicious_zip, target_filename="../escaped.txt")
        
        # Run agent's patched extractor
        res = run_extraction_harness("src/safe_extractor.py", malicious_zip, dest_dir)
        
        # VERIFIER ASSERTION 1: Canary file MUST NOT exist outside dest_dir
        assert not os.path.exists(canary_file), (
            "CRITICAL SECURITY FAIL: Path traversal succeeded! File written outside sandbox."
        )
        
        # VERIFIER ASSERTION 2: Script should exit with safe validation error, not unhandled crash
        assert res.returncode != 0, "Extractor should return non-zero exit code when detecting directory traversal"
        assert "PathTraversalError" in res.stderr or "InvalidPath" in res.stderr
```

---

## 4. Key Rules for Writing Flawless Verifiers

1. **Zero Flakiness:** Never use `time.sleep()` for synchronization. Always use `threading.Event`, deterministic barriers, or condition variables.
2. **Deterministic Timeouts:** Always enforce explicit timeout boundaries on subprocesses (`timeout=5.0`). If an agent enters an infinite loop, your verifier must kill it cleanly and output a structured `TIMEOUT_EXCEEDED` signal.
3. **Hermetic State:** Tests must generate isolated temporary directories (`tempfile.TemporaryDirectory()`) and tear them down. Never leave leftover state on disk between test runs.
4. **Structured JSON Output:** Wrap test execution results into a clean JSON dictionary (`VERIFIER_RESULT: {"pass": true, "tests": [...]}`).
"""
    },

    "02_Technical_Rounds": {
        "title": "Module 02: Python, Docker & Verifiers · Solumn AI Foundations 2026",
        "active_page": "02_Technical_Rounds.html",
        "prev_link": "01_Practical_Assignment.html",
        "prev_title": "01: Practical Task & Verifiers",
        "next_link": "03_Domain_Deep_Dive.html",
        "next_title": "03: AI Safety & RSPs",
        "content_md": """# Module 02: Technical Interview Deep Dive (Python, Docker & Verifiers)

## 1. Python Execution & Subprocess Sandboxing

In the technical interview (Sunday, Oct 11), the interviewers will test your systems intuition regarding how code is executed and constrained in an evaluation harness.

### Subprocess Execution: `subprocess.run` vs `asyncio.subprocess`
When running agent-generated code or untrusted scripts, naive `os.system()` or `subprocess.call()` is forbidden.

```python
import subprocess
import resource
import signal

def set_limits():
    '''Prevent fork-bombs and runaway memory consumption.'''
    # Limit CPU time to 5 seconds
    resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
    # Limit virtual memory to 512 MB
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
    # Limit number of child processes (prevent fork-bomb)
    resource.setrlimit(resource.RLIMIT_NPROC, (30, 30))

def execute_untrusted_script(script_path: str):
    try:
        proc = subprocess.run(
            ["python3", script_path],
            preexec_fn=set_limits,
            capture_output=True,
            text=True,
            timeout=6.0
        )
        return {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    except subprocess.TimeoutExpired:
        return {"error": "TIMEOUT", "returncode": -signal.SIGKILL}
```

*Key Interview Question:* **"Why do we use `preexec_fn` or container cgroups instead of Python threading to limit execution?"**
*Answer:* The Python Global Interpreter Lock (GIL) and standard threading cannot terminate runaway C-extensions or unbounded CPU loops. Python threads share memory; an untrusted script can corrupt the interpreter state or trigger a segfault. Subprocesses provide operating-system-level process boundaries, distinct address spaces, and kernel-enforced resource limits via `setrlimit`.

---

## 2. Docker Architecture for Agentic Environments

Solumn's primary workstream relies on **containerized Docker tasks**. You must be comfortable with the **Docker Engine API / Docker SDK for Python**.

### Key Container Isolation Parameters

| Docker Parameter | Purpose in AI Evaluation | Failure Scenario if Omitted |
| :--- | :--- | :--- |
| `network_mode="none"` | Complete network isolation | The agent can exfiltrate prompt instructions, API keys, or curl external pre-solved solutions. |
| `mem_limit="512m"` | Memory capping | An agent allocating multi-gigabyte matrices triggers Host Out-of-Memory (OOM) crashing the grader. |
| `cpu_quota=50000` | Limits CPU to 0.5 CPU core (`cpu_period=100000`) | Multi-threaded agent hogs all host cores, slowing down parallel evaluation suites. |
| `read_only=True` | Root filesystem is mounted read-only | Agent modifies test harnesses or deletes grader scripts to force a bypass. |
| `tmpfs={"/tmp": "rw,size=64m"}` | Ephemeral in-memory writable scratch space | Clean state without polluting container disk images. |

### Production Python Docker Harness Skeleton

```python
import docker
import json

client = docker.from_env()

def run_agent_in_container(image_name: str, task_repo_path: str, timeout_seconds: int = 60) -> dict:
    container = client.containers.run(
        image=image_name,
        command="/bin/bash -c 'cd /workspace && python3 run_agent.py'",
        volumes={
            task_repo_path: {'bind': '/workspace', 'mode': 'rw'}
        },
        network_mode="none",              # No internet access during task
        mem_limit="1g",                   # Hard memory ceiling
        cpu_quota=100000,                 # 1 CPU core ceiling
        detach=True,
        user="sandbox_user"               # Non-root user execution
    )

    try:
        res = container.wait(timeout=timeout_seconds)
        logs = container.logs(stdout=True, stderr=True).decode('utf-8')
        return {
            "status": "COMPLETED",
            "exit_code": res["StatusCode"],
            "logs": logs
        }
    except Exception as e:
        container.kill()
        return {"status": "TIMEOUT_OR_ERROR", "error": str(e)}
    finally:
        container.remove(force=True)
```

---

## 3. Principles of Deterministic Grading

A verifier that has even a 0.5% false-positive or false-negative rate is discarded in an AI safety foundry.

### The Four Cardinal Rules of Deterministic Verifiers

$$\\text{Verifier}(S) = \\begin{cases} 1 & \\text{if } S \\text{ satisfies specification } \\Phi \\\\ 0 & \\text{if } S \\text{ violates specification } \\Phi \\end{cases}$$

1. **Idempotence:** Running the verifier 1,000 times against the identical submission state must produce identical boolean outputs:
   $$\\forall i, j \\in \\{1..1000\\}, \\quad \\text{Result}_i \\equiv \\text{Result}_j$$
2. **Order Independence:** Never iterate over unordered sets or dictionary keys without explicit sorting when comparing expected outputs (`sorted(results)` vs `results`).
3. **Floating Point Tolerance:** In numerical tasks, never use `assert a == b`. Always specify strict epsilon tolerances via `math.isclose(a, b, rel_tol=1e-6, abs_tol=1e-9)` or `numpy.testing.assert_allclose`.
4. **Seed Control:** In probabilistic or randomized algorithm evaluations, explicitly fix pseudo-random generator seeds (`random.seed(42)`, `torch.manual_seed(42)`).

---

## 4. Agent Trajectory Analysis

When an agent attempts an RLE, its entire interaction is logged as a **trajectory**:

```json
{
  "step": 1,
  "action": "bash_command",
  "command": "cat src/auth.py",
  "observation": "class Authenticator:\n    def verify(self, token)...",
  "agent_thought": "I need to inspect the verify method to locate the timing attack vulnerability.",
  "timestamp": 1728472912.42
}
```

*What Solumn Evaluates in Trajectories:*
- **Reversible actions:** Did the agent backup files before modifying them?
- **Tool privilege escalation:** Did the agent attempt `sudo`, explore `/etc/passwd`, or query container metadata endpoints?
- **Infinite loops / Repetition penalty:** Did the agent repeat the identical failing command 10 times without altering strategy?
"""
    }
}
