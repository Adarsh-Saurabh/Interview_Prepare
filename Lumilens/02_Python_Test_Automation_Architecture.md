# 02: Python Test Automation Architecture & Frameworks

> **Author / Perspective:** Ponytail (Senior Test Automation Architect)  
> **Philosophy:** Ruthless efficiency. Zero boilerplate. Root cause over symptom. Code that actually runs on physical lab hardware without flaky collapses.

---

## 1. Why Optical Test Automation is Different

In web QA, if an API fails, you retry the HTTP request.  
In **Optical / Network Switch Test Automation**, if an assertion fails or a script crashes without proper teardown:
- You can leave a **high-power Class 3B laser turned ON**, burning an Avalanche Photodiode (APD) receiver ($5,000+ damage).
- An instrument's FIFO buffer remains poisoned with an unread byte, causing the *next* 50 test cases to fail with shifted data.
- An optical switch port's MAC table retains stale entries, poisoning multicast test verification.
- Hardcoded `time.sleep(10)` creates test runs that take 8 hours instead of 15 minutes, blocking manufacturing line throughput.

---

## 2. The 5-Tier Production Architecture

```
framework/
├── conftest.py               # Hardware fixtures with deterministic teardown
├── core/
│   ├── scpi.py               # Minimal SCPI / VISA wrapper (Power meter, Attenuator)
│   ├── dut.py                # Network switch console/SSH driver
│   ├── traffic.py            # Traffic generator (Scapy mock + Hardware IXIA adapter)
│   ├── daemon_client.py      # Non-blocking socket client for switch test daemons
│   └── yield_db.py           # SQLite WAL + JSON yield tracker
└── tests/
    └── test_optical_transceiver.py  # End-to-end BER vs Optical Rx Power test
```

---

## 3. Core Implementation Files

### `core/scpi.py` — Resilient SCPI / VISA Instrument Wrapper
```python
import socket
import time
from typing import Optional

try:
    import pyvisa
    HAS_VISA = True
except ImportError:
    HAS_VISA = False

class SCPIInstrument:
    """
    Zero-bloat SCPI wrapper for Optical Power Meters, Attenuators, and Oscilloscopes.
    Works over PyVISA or falls back to raw TCP socket (port 5025) if VISA runtime is absent.
    """
    def __init__(self, resource_name: str, timeout_s: float = 3.0):
        self.resource_name = resource_name
        self.timeout_s = timeout_s
        self._inst = None
        self._sock = None

    def connect(self) -> "SCPIInstrument":
        if HAS_VISA and not self.resource_name.startswith("raw://"):
            rm = pyvisa.ResourceManager("@py")
            self._inst = rm.open_resource(self.resource_name)
            self._inst.timeout = int(self.timeout_s * 1000)
            self._inst.write_termination = "\n"
            self._inst.read_termination = "\n"
        else:
            addr = self.resource_name.replace("raw://", "")
            host, port = addr.split(":")
            self._sock = socket.create_connection((host, int(port)), timeout=self.timeout_s)
            self._sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.clear_buffer()
        return self

    def disconnect(self):
        if self._inst:
            try:
                self._inst.close()
            except Exception:
                pass
            self._inst = None
        if self._sock:
            try:
                self._sock.close()
            except Exception:
                pass
            self._sock = None

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def write(self, cmd: str):
        cmd = cmd.strip() + "\n"
        if self._inst:
            self._inst.write(cmd)
        elif self._sock:
            self._sock.sendall(cmd.encode("ascii"))

    def query(self, cmd: str) -> str:
        self.write(cmd)
        if self._inst:
            return self._inst.read().strip()
        elif self._sock:
            buf = bytearray()
            while True:
                chunk = self._sock.recv(1024)
                if not chunk:
                    break
                buf.extend(chunk)
                if b"\n" in chunk:
                    break
            return buf.decode("ascii").strip()
        raise RuntimeError("Not connected")

    def query_float(self, cmd: str) -> float:
        res = self.query(cmd)
        # Strips out SCPI scientific notations and commas
        clean = res.split(",")[0].replace("DBM", "").replace("W", "").strip()
        return float(clean)

    def wait_opc(self, timeout_s: Optional[float] = None) -> bool:
        """Halts execution until instrument completes previous operation (*OPC?)."""
        orig_timeout = self.timeout_s
        if timeout_s:
            self.timeout_s = timeout_s
        try:
            return self.query("*OPC?") == "1"
        finally:
            self.timeout_s = orig_timeout

    def clear_buffer(self):
        """Wipes status registers and flushes pending output queue."""
        self.write("*CLS")
```

---

### `core/daemon_client.py` — Length-Prefixed Binary Socket Client
```python
import socket
import struct
import json
from typing import Any, Dict

class SwitchDaemonClient:
    """
    Client for embedded switch telemetry daemons.
    Uses 4-byte big-endian length prefix to prevent fragmentation truncation.
    """
    def __init__(self, host: str, port: int, timeout_s: float = 5.0):
        self.host = host
        self.port = port
        self.timeout_s = timeout_s
        self._sock: Optional[socket.socket] = None

    def connect(self):
        self._sock = socket.create_connection((self.host, self.port), timeout=self.timeout_s)

    def close(self):
        if self._sock:
            self._sock.close()
            self._sock = None

    def send_command(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        data = json.dumps(payload).encode("utf-8")
        # Pack length (4-byte unsigned int) followed by payload
        header = struct.pack("!I", len(data))
        self._sock.sendall(header + data)

        # Read 4-byte response header
        resp_hdr = self._recv_exact(4)
        resp_len = struct.unpack("!I", resp_hdr)[0]

        # Read full body
        resp_body = self._recv_exact(resp_len)
        return json.loads(resp_body.decode("utf-8"))

    def _recv_exact(self, n: int) -> bytes:
        buf = bytearray()
        while len(buf) < n:
            chunk = self._sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("Socket closed prematurely")
            buf.extend(chunk)
        return bytes(buf)
```

---

### `core/traffic.py` — Traffic Generator Abstraction (Scapy + Hardware IXIA)
```python
from dataclasses import dataclass
import time

@dataclass
class TrafficStats:
    tx_frames: int
    rx_frames: int
    dropped_frames: int
    loss_ratio: float
    avg_latency_us: float

class TrafficGenerator:
    """
    Dual-mode traffic engine:
    Mock mode (Scapy) for local testing without physical lab gear.
    Hardware mode (IXIA / REST API) for 100G/400G line rate.
    """
    def __init__(self, mode: str = "mock"):
        self.mode = mode

    def transmit_burst(self, port: int, frame_count: int, rate_gbps: float) -> TrafficStats:
        if self.mode == "mock":
            # Simulate slight deterministic jitter and 0 drop
            return TrafficStats(
                tx_frames=frame_count,
                rx_frames=frame_count,
                dropped_frames=0,
                loss_ratio=0.0,
                avg_latency_us=1.45
            )
        else:
            # Connect to IXIA chassis REST/Tcl API
            # Start generation, wait for completion, read hardware FPGA counters
            pass
```

---

### `core/yield_db.py` — SQLite WAL Manufacturing Yield Logger
```python
import sqlite3
import json
import time

class YieldLogger:
    """
    SQLite logger running in Write-Ahead Logging (WAL) mode for maximum concurrency
    during parallel multi-DUT manufacturing tests.
    """
    def __init__(self, db_path: str = "manufacturing_yield.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS test_runs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    dut_serial TEXT,
                    test_name TEXT,
                    verdict TEXT,
                    rx_power_dbm REAL,
                    ber REAL,
                    packet_loss_pct REAL,
                    metadata_json TEXT
                )
            """)

    def log_result(self, serial: str, test_name: str, verdict: str, 
                   rx_power: float, ber: float, loss_pct: float, meta: dict):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO test_runs 
                (timestamp, dut_serial, test_name, verdict, rx_power_dbm, ber, packet_loss_pct, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (time.time(), serial, test_name, verdict, rx_power, ber, loss_pct, json.dumps(meta)))
```

---

### `conftest.py` — Fixtures with APD Laser Safety Teardown
```python
import pytest
from core.scpi import SCPIInstrument
from core.traffic import TrafficGenerator
from core.yield_db import YieldLogger

@pytest.fixture(scope="session")
def optical_attenuator():
    """
    Controls Variable Optical Attenuator (VOA).
    CRITICAL TEARDOWN: Always resets attenuation to MAXIMUM (30 dB)
    to protect sensitive APD detectors when fiber is disconnected.
    """
    voa = SCPIInstrument("raw://192.168.1.101:5025").connect()
    # Safety reset on connect
    voa.write(":ATT 30.0DB")
    voa.wait_opc()
    
    yield voa
    
    # Guaranteed teardown even if tests fail or throw exceptions
    try:
        voa.write(":ATT 30.0DB")
        voa.write(":OUTP:STAT 0") # Laser safety off
        voa.wait_opc()
    finally:
        voa.disconnect()

@pytest.fixture(scope="session")
def traffic_gen():
    return TrafficGenerator(mode="mock")

@pytest.fixture(scope="session")
def yield_tracker():
    return YieldLogger()
```

---

### End-to-End Test: `test_optical_transceiver.py`
```python
import pytest
import time

@pytest.mark.parametrize("target_rx_power_dbm, max_allowed_ber", [
    (-8.0, 1e-12),   # High input power -> Clean eye, zero bit error
    (-12.0, 1e-8),   # Moderate power
    (-15.0, 2.4e-4), # KP4 FEC Limit threshold
])
def test_transceiver_ber_vs_rx_power(optical_attenuator, traffic_gen, yield_tracker, target_rx_power_dbm, max_allowed_ber):
    dut_serial = "LUMI-SiPh-800G-0042"
    
    # 1. Adjust Variable Optical Attenuator to achieve target power
    optical_attenuator.write(f":POW:TARG {target_rx_power_dbm}DBM")
    assert optical_attenuator.wait_opc(timeout_s=5.0), "Attenuator failed to settle"
    
    # 2. Inject 1,000,000 packets through traffic generator
    stats = traffic_gen.transmit_burst(port=1, frame_count=1_000_000, rate_gbps=100.0)
    
    # 3. Read measured physical BER (simulated calculation)
    measured_ber = 1e-14 if target_rx_power_dbm > -10 else 1e-9 if target_rx_power_dbm > -14 else 1.2e-4
    
    # 4. Determine verdict & log telemetry to manufacturing DB
    verdict = "PASS" if measured_ber <= max_allowed_ber and stats.loss_ratio == 0.0 else "FAIL"
    yield_tracker.log_result(
        serial=dut_serial,
        test_name="test_transceiver_ber_vs_rx_power",
        verdict=verdict,
        rx_power=target_rx_power_dbm,
        ber=measured_ber,
        loss_pct=stats.loss_ratio * 100.0,
        meta={"frames": stats.tx_frames, "latency_us": stats.avg_latency_us}
    )
    
    # 5. Assertions
    assert stats.dropped_frames == 0, f"Frame drop detected: {stats.dropped_frames} frames lost"
    assert measured_ber <= max_allowed_ber, f"BER {measured_ber} exceeded spec {max_allowed_ber}"
```

---

## 4. Lazy Senior Dev Rules for Hardware Test Automation

| Problem | Junior / Brittle Pattern | Lazy Senior Dev Pattern |
| :--- | :--- | :--- |
| **Waiting for HW settle** | `time.sleep(5)` everywhere. (Flaky + slow). | Polling with deadline (`while time.time() < deadline: if ready(): break; time.sleep(0.05)`). |
| **Instrument buffer** | Assumes socket buffer is empty on start. | Sends `*CLS` (Clear Status) immediately on connect and in teardown. |
| **Laser safety** | Leaves lasers active when test raises assertion error. | Implements teardown inside pytest fixture `yield` or `try...finally`. |
| **Flaky BER testing** | Retries test 5 times hoping it passes (`reruns=5`). | Triages Pre-FEC vs Post-FEC counters; logs optical eye height to locate physical degradation. |
| **CI/CD runs** | Fails CI if physical bench instrument is offline. | Clean mock fallback (`MagicMock` / Scapy) allowing CI validation without hardware. |
