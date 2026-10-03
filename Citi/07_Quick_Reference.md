# 07: Rapid Recall CheatSheet

High-density summary tables for last-minute review before Online Assessment and Technical Interviews.

---

## 1. Algorithm Complexities & Data Structures

| Algorithm / Pattern | Best Time | Worst Time | Space | Signature FinTech Application |
| :--- | :--- | :--- | :--- | :--- |
| **Monotonic Deque (Sliding Window)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | $\mathcal{O}(W)$ | Streaming transaction anomaly detection & peak volume spikes |
| **Bellman-Ford (Arbitrage)** | $\mathcal{O}(V \cdot E)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V)$ | Foreign exchange (FX) negative cycle currency arbitrage |
| **Dual Heap (Min/Max)** | $\mathcal{O}(1)$ peek | $\mathcal{O}(\log N)$ insert | $\mathcal{O}(N)$ | Real-time continuous order book matching (Bid/Ask) |
| **A* Heuristic Search** | $\mathcal{O}(E)$ | $\mathcal{O}(V \log V)$ | $\mathcal{O}(V)$ | Low-latency spatial routing / Liquidity clearing pathfinding |
| **Kahn's Topological Sort** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | Payment dependency resolution & workflow pipeline DAGs |

---

## 2. React.js & Frontend Quick Recall

* **Hook Rules**: Only call hooks at top level; never inside loops, conditions, or nested functions.
* **`useEffect` vs `useLayoutEffect`**: `useEffect` runs asynchronously after render is painted; `useLayoutEffect` runs synchronously before DOM paint (use only for measuring layout).
* **`useMemo` vs `useCallback`**:
  * `useMemo(() => fn, deps)` caches a calculated **value**.
  * `useCallback(fn, deps)` caches a **function instance**.
* **Key Props in Lists**: Never use array index as key if list can be sorted, filtered, or prepended — causes reconciliation bugs.

---

## 3. MongoDB & SQL Indexing Rules

* **ESR Rule**: Compound indexes should be ordered **Equality $\rightarrow$ Sort $\rightarrow$ Range**.
* **ACID in MongoDB**: Supported on single documents out-of-the-box; multi-document transactions supported across replica sets via session transactions (`session.startTransaction()`).
* **Covered Query**: An execution where all fields requested in projection exist directly within the index; zero document fetches required.

---

## 4. Banking Acronyms Glossary

| Acronym | Definition & Operational Context |
| :--- | :--- |
| **TTS** | **Treasury and Trade Solutions**: Citi's flagship institutional cash management and trade services division. |
| **RTGS** | **Real-Time Gross Settlement**: Immediate, irrevocable transfer of funds on an individual gross basis. |
| **ACH** | **Automated Clearing House**: Net settlement batch processing system for recurring consumer/corporate payments. |
| **SWIFT** | **Society for Worldwide Interbank Financial Telecommunication**: Global messaging network connecting banks. |
| **ISO 20022**| Next-generation XML/JSON standard (`pacs.008`) replacing legacy SWIFT MT text messages. |
| **PCI-DSS** | **Payment Card Industry Data Security Standard**: Strict security baseline for cardholder data protection. |
| **mTLS** | **Mutual TLS**: Dual certificate handshake authenticating both client and server microservices. |
