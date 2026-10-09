# Module 07: Rapid Recall CheatSheet & Syntax Vault

## 1. Python Subprocess & Sandboxing Snippets

### Secure Isolated Execution with Timeout
```python
import subprocess, signal

def run_isolated(cmd: list[str], cwd: str, timeout_sec: float = 5.0):
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False
        )
        return {"code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    except subprocess.TimeoutExpired:
        return {"code": -signal.SIGKILL, "error": "TIMEOUT_EXCEEDED"}
```

---

## 2. Docker Python SDK Essential Snippets

### Creating Sandboxed Container with Resource Constraints
```python
import docker

client = docker.from_env()

container = client.containers.run(
    image="python:3.11-slim",
    command=["pytest", "/tests"],
    volumes={"/host/repo": {"bind": "/workspace", "mode": "rw"}},
    network_mode="none",              # Total network isolation
    mem_limit="512m",                 # 512MB RAM cap
    cpu_quota=50000,                  # 0.5 CPU core (cpu_period=100000)
    pids_limit=50,                    # Fork-bomb prevention
    read_only=True,                   # Immutable root filesystem
    tmpfs={"/tmp": "rw,size=32m"},    # Ephemeral scratch space
    detach=True
)
```

---

## 3. Pytest Deterministic Assertion Patterns

```python
import pytest
import math
from decimal import Decimal

# 1. Deterministic float comparison
def test_float_tolerance():
    assert math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)

# 2. Strict timeout per test
@pytest.mark.timeout(2.0)
def test_execution_latency():
    pass

# 3. Hermetic temporary directory
def test_file_integrity(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("content")
    assert p.read_text() == "content"
```

---

## 4. Frontier Safety Framework Cheat Table

| Framework | Core Metric / Level | Mandatory Gate Requirement |
| :--- | :--- | :--- |
| **Anthropic RSP v3.2** | **ASL-3** (Cyber, CBRN, Autonomous Agent tools) | Red-teaming audits, air-gapped evaluation, third-party foundry proof. |
| **Google DeepMind** | **Critical Capability Levels (CCLs)** | Continuous monitoring against self-replication and zero-day cyber tools. |
| **OpenAI / Frontier Forum** | **Preparedness Framework (High Risk)** | Model weights locked until mitigation reduces risk below Medium threshold. |
