# Module 05: System Design — Scalable Agent Evaluation Foundry

## 1. System Design Problem Statement

**Design an Ephemeral Agent Evaluation Foundry Architecture capable of executing and grading 10,000 agent evaluation sessions per day with deterministic isolation, sub-second grader latency, and zero cross-tenant contamination.**

```
                                 [ EVALUATION FOUNDRY ARCHITECTURE ]

    +-------------------+
    | Frontier Model API|
    |  (Claude / o3)    |
    +---------+---------+
              | (Tool Calls / Bash Commands)
              v
    +-------------------+       Dispatch Job        +-----------------------+
    |   API Gateway /   | ------------------------> | Distributed Task Queue|
    |  Session Manager  |                           |     (Redis / Celery)  |
    +-------------------+                           +-----------+-----------+
                                                                |
                                                 Worker Pulls   v
    +-----------------------------------------------------------------------+
    |                       Worker Host Cluster                             |
    |                                                                       |
    |  +--------------------+   gRPC Exec   +----------------------------+  |
    |  |  Foundry Agent     | ------------> | Isolated Container Sandbox |  |
    |  |  Runner Controller |               |  (Docker / Firecracker)    |  |
    |  +---------+----------+               |  - net: none               |  |
    |            |                          |  - mem: 512MB              |  |
    |            | On Completion            |  - cpu: 0.5 core           |  |
    |            v                          +--------------+-------------+  |
    |  +--------------------+                              |                |
    |  | Deterministic      | <----------------------------+                |
    |  | Grader Harness     |  Extract Workspace State / Git Diff           |
    |  +---------+----------+                                               |
    +------------|----------------------------------------------------------+
                 |
                 v Structured JSON Score
    +-----------------------------------------------+
    |  Telemetry & Trajectory Store (Postgres / S3) |
    +-----------------------------------------------+
```

---

## 2. Key Architectural Components

### 1. The Ephemeral Sandbox Pool (Docker / Firecracker MicroVMs)
* **Warm Pool Architecture:** Cold-starting a Docker container takes ~800ms; booting a Python environment inside takes ~1.5s. To maintain high evaluation throughput, the worker maintains a pool of pre-warmed, paused containers.
* **Hermetic Lifecycle:**
  1. Worker claims pre-warmed container.
  2. Workspace snapshot is mounted via overlay filesystem (`overlayfs`).
  3. Network interfaces are destroyed (`veth` unlinked).
  4. Agent executes task commands.
  5. Grader runs test assertions.
  6. Container is destroyed and overlay filesystem is purged.

### 2. Network Isolation & Security Perimeter
Frontier coding agents can attempt malicious breakouts or query internal cloud metadata:
* **Blocking AWS/GCP Metadata:** `169.254.169.254` must be blocked via host `iptables` rules.
* **DNS Sinkholing:** In tasks requiring external package installations, all outgoing DNS requests must pass through an internal proxy whitelist allowing only specific package mirrors (`pypi.org`, `archive.ubuntu.com`).

---

## 3. High-Throughput Grading Pipeline in Python

```python
import asyncio
import time
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class EvalTask:
    task_id: str
    scenario_id: str
    container_id: str
    timeout_sec: float

@dataclass
class EvalResult:
    task_id: str
    passed: bool
    score: float
    duration_sec: float
    error_msg: str

class AsyncEvaluationDispatcher:
    def __init__(self, concurrency_limit: int = 16):
        self.semaphore = asyncio.Semaphore(concurrency_limit)
        
    async def grade_single_task(self, task: EvalTask) -> EvalResult:
        async with self.semaphore:
            start_time = time.perf_counter()
            try:
                # 1. Execute deterministic test runner in container asynchronously
                cmd = f"docker exec {task.container_id} pytest /verifier/test_suite.py --json-report"
                proc = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                
                # 2. Wait with strict timeout boundary
                stdout, stderr = await asyncio.wait_for(
                    proc.communicate(),
                    timeout=task.timeout_sec
                )
                
                duration = time.perf_counter() - start_time
                is_success = (proc.returncode == 0)
                
                return EvalResult(
                    task_id=task.task_id,
                    passed=is_success,
                    score=1.0 if is_success else 0.0,
                    duration_sec=round(duration, 3),
                    error_msg="" if is_success else stderr.decode('utf-8', errors='ignore')
                )
                
            except asyncio.TimeoutError:
                return EvalResult(
                    task_id=task.task_id,
                    passed=False,
                    score=0.0,
                    duration_sec=task.timeout_sec,
                    error_msg="TASK_TIMEOUT_EXCEEDED"
                )
            except Exception as e:
                return EvalResult(
                    task_id=task.task_id,
                    passed=False,
                    score=0.0,
                    duration_sec=round(time.perf_counter() - start_time, 3),
                    error_msg=f"DISPATCH_ERROR: {str(e)}"
                )

    async def batch_grade(self, tasks: list[EvalTask]) -> list[EvalResult]:
        return await asyncio.gather(*(self.grade_single_task(t) for t in tasks))
```

---

## 4. Grader Fault-Tolerance & Idempotence

1. **State Diff Extraction:** Rather than grading solely based on process exit codes, extract a `git diff` of the agent’s workspace. Grade the code AST (Abstract Syntax Tree) to verify that the agent didn't simply comment out the failing assertions:
   ```python
   import ast

   def check_no_cheating(code_str: str) -> bool:
       tree = ast.parse(code_str)
       for node in ast.walk(tree):
           # Verify agent didn't override assert keyword or mock the verifier
           if isinstance(node, ast.Attribute) and node.attr == '__builtins__':
               return False
       return True
   ```
2. **Double-Blind Grading:** Run the identical verifier against the original unmodified baseline repository. If the baseline passes, your verifier is broken (false positive).
