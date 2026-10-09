# Module 02: Technical Interview Deep Dive (Python, Docker & Verifiers)

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

$$\text{Verifier}(S) = \begin{cases} 1 & \text{if } S \text{ satisfies specification } \Phi \\ 0 & \text{if } S \text{ violates specification } \Phi \end{cases}$$

1. **Idempotence:** Running the verifier 1,000 times against the identical submission state must produce identical boolean outputs:
   $$\forall i, j \in \{1..1000\}, \quad \text{Result}_i \equiv \text{Result}_j$$
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
  "observation": "class Authenticator:
    def verify(self, token)...",
  "agent_thought": "I need to inspect the verify method to locate the timing attack vulnerability.",
  "timestamp": 1728472912.42
}
```

*What Solumn Evaluates in Trajectories:*
- **Reversible actions:** Did the agent backup files before modifying them?
- **Tool privilege escalation:** Did the agent attempt `sudo`, explore `/etc/passwd`, or query container metadata endpoints?
- **Infinite loops / Repetition penalty:** Did the agent repeat the identical failing command 10 times without altering strategy?
