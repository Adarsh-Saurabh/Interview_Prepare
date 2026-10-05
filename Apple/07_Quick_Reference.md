# 07: Rapid Recall CheatSheet

A high-density reference sheet designed for rapid revision right before your Apple interviews.

---

## 1. Core Systems & Memory Architecture

```
┌─────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Concept                         │ Key Formula / Technical Tenet                          │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ Pointer Size                    │ 8 bytes on 64-bit architecture (ARM64 / x86_64)       │
│ Cache Line Size                 │ 64 bytes (`alignas(64)` avoids false sharing)          │
│ Virtual Memory Page Size        │ 4 KB (Standard Linux) / 16 KB (Apple Silicon default)  │
│ Virtual Table Overhead          │ 8 bytes per object (`vptr`) pointing to class `vtable`  │
│ Shared Pointer Size             │ 16 bytes: 8 bytes raw pointer + 8 bytes control block  │
│ Unique Pointer Size             │ 8 bytes: zero memory overhead over raw pointer         │
└─────────────────────────────────┴────────────────────────────────────────────────────────┘
```

### Essential C++ Code Snippets

```cpp
// 1. Thread-safe Singleton (Meyers' Singleton)
class AppleService {
public:
    static AppleService& getInstance() {
        static AppleService instance; // Thread-safe in C++11
        return instance;
    }
private:
    AppleService() = default;
};

// 2. Custom Deleter with unique_ptr
auto fileCloser = [](FILE* fp) { if (fp) fclose(fp); };
std::unique_ptr<FILE, decltype(fileCloser)> filePtr(fopen("log.txt", "r"), fileCloser);
```

---

## 2. Apple AI & Machine Learning Metrics

* **On-Device Base Model**: ~3B parameter model running on Apple Neural Engine (ANE).
* **Quantization**: INT4 / INT8 reducing model memory footprint from $\sim 12\text{GB}$ (FP32) to $\le 2\text{GB}$.
* **LoRA Rank Equation**:
$$\Delta W = B \cdot A, \quad B \in \mathbb{R}^{d \times r}, A \in \mathbb{R}^{r \times k} \quad (r \ll \min(d, k))$$
* **Private Cloud Compute (PCC)**: Custom Apple Silicon nodes, cryptographic attestations, zero data logging.

---

## 3. SDET & Testing Rapid Reference

* **Test Pyramid**: $70\%$ Unit Tests $\to$ $20\%$ Integration/API Tests $\to$ $10\%$ UI Tests.
* **Page Object Model (POM)**:
  * Pages contain locators and action methods.
  * Tests contain assertions and scenarios.
* **Explicit Wait Polling**:
```python
def wait_until(condition_func, timeout=10, interval=0.2):
    start = time.time()
    while time.time() - start < timeout:
        res = condition_func()
        if res: return res
        time.sleep(interval)
    raise TimeoutError("Condition not satisfied")
```

---

## 4. Candidate Snapshot for Defense

* **Name**: Adarsh Saurabh | **Roll**: `225EC6021` | **Phone**: `+91 7004428313`
* **M.Tech (2025–2027)**: Signal and Image Processing, NIT Rourkela | **CGPA: 8.28**
* **B.Tech (2020–2024)**: Computer Science and Engineering, GGU Bilaspur | **CGPA: 8.5**
* **PathMapper**: 10,000×10,000 grid, 10,000+ points in $<0.5\text{s}$, spatial heuristic search.
* **Uplan**: Multi-agent LangGraph with Gemini 2.5 Pro, 85% workload reduction, 98% token compression.
* **Alternative Data Radar**: Automated scraping backend with Bright Data proxy routing, 0–100 health score in SQL.
