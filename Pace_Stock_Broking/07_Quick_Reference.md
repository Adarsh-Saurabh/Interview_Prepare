# 07: Caveman Quant CheatSheet & Formula Vault

## 1. Latency Numbers Every Quant Dev Must Know

```
┌───────────────────────────────────────┬─────────────────────────┐
│ Operation                             │ Latency                 │
├───────────────────────────────────────┼─────────────────────────┤
│ CPU L1 Cache Reference                │ 0.5 - 1 ns              │
│ Branch Mispredict                     │ 3 - 5 ns                │
│ CPU L2 Cache Reference                │ 3 - 4 ns                │
│ Mutex Lock / Unlock                   │ 15 - 25 ns              │
│ CPU L3 Cache Reference                │ 10 - 20 ns              │
│ Main Memory (DRAM) Access             │ 50 - 100 ns             │
│ PCIe Bus Transfer                     │ 100 - 250 ns            │
│ Kernel Bypass Network Tick (OpenOnload)│ 250 - 450 ns           │
│ Linux OS Context Switch / Page Fault  │ 1,500 - 3,500 ns        │
│ Standard Linux Socket recv() syscall  │ 2,000 - 4,000 ns        │
│ Mumbai NSE to BKC Colo Roundtrip      │ < 10,000 ns (10 µs)     │
│ Mumbai to London Optical Fiber        │ ~ 60,000,000 ns (60 ms) │
└───────────────────────────────────────┴─────────────────────────┘
```

---

## 2. Modern C++ Low-Latency Commandments
1. **Never allocate heap memory (`new` / `malloc`) on the critical path:** Always use pre-allocated static arrays or memory pools.
2. **Eliminate dynamic polymorphism:** Replace `virtual` functions with templates (CRTP).
3. **Pass objects by `const &`:** Avoid redundant copy constructor invocations.
4. **Pad structures to 64 bytes (`alignas(64)`):** Prevent multithreaded false sharing.
5. **Never use `std::endl`:** Always use `'
'` to avoid forcing redundant I/O buffer flushes.
6. **Prefer sequential array iteration (Row-Major):** Exploit CPU hardware prefetchers.
7. **Use `std::atomic` with relaxed or acquire-release semantics:** Avoid heavy sequential consistency barriers unless strictly necessary.

---

## 3. Mathematical Formula Vault

* **Bayes Theorem:**
  $$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$
* **Expected Value of Discrete Random Variable:**
  $$E[X] = \sum_{i} x_i \cdot P(X = x_i)$$
* **Variance & Covariance:**
  $$\text{Var}(X) = E[X^2] - (E[X])^2, \quad \text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$
* **Order Book Spread & Mid-Price:**
  $$\text{Mid-Price} = \frac{P_{\text{best\_ask}} + P_{\text{best\_bid}}}{2}$$
* **Order Book Imbalance (OBI):**
  $$\text{OBI} = \frac{Q_{\text{bid}} - Q_{\text{ask}}}{Q_{\text{bid}} + Q_{\text{ask}}} \in [-1, +1]$$
