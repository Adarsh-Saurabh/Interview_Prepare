# Module 01: The Practical Take-Home Assignment & Verifier Engineering

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
