# 3-Day Intensive Study Roadmap: Apple Recruitment

A battle-tested 3-day sprint designed for **Adarsh Saurabh** to conquer the Apple On-Campus placement drive at NIT Rourkela for **AI & ML SDE Intern** and **SDET Intern** (80 LPA PPO).

---

## Day 1: Algorithmic Rigor & Signature OA Coding (8 Hours)
* **Morning (4 Hours)**:
  * Master **LRU Cache** implementation with thread-safety (`std::mutex` and Python locks) from Module 01.
  * Implement **String Compression** in-place with $O(1)$ memory.
  * Practice **Word Break** with Trie-optimized Dynamic Programming.
* **Afternoon (4 Hours)**:
  * Solve **Task Scheduler / Course Schedule** (Cycle detection in DAG using Kahn's algorithm and DFS).
  * Solve **Jump Game / Min Jumps** using greedy sliding window.
  * Review LeetCode Mediums: Merging K sorted lists, LRU Cache, Binary Tree boundary traversal, Subarray sum equals K.

---

## Day 2: Systems, Memory, OS & Domain Deep Dive (8 Hours)
* **Morning (4 Hours)**:
  * Study **Module 02**: ARC vs Garbage Collection vs RAII, retain cycles, weak vs unowned references.
  * Review C++ smart pointers (`unique_ptr`, `shared_ptr`, `weak_ptr`), memory layout of objects, `vtable`/`vptr`, and memory alignment (`alignas(64)`).
  * Master Concurrency: Mutex vs Spinlock vs Semaphore vs Atomic operations, cache line false sharing.
* **Afternoon (4 Hours)**:
  * Study **Module 03**: Apple Intelligence on-device foundation models vs Private Cloud Compute (PCC), LoRA adapter swapping, Core ML compilation.
  * Study SDET Architecture: Page Object Model (POM), test pyramid, parameterized tests with `pytest`, flaky test isolation, and profiling with Apple Instruments.
  * Study Networking: TCP 3-way handshake, 4-way termination, TIME_WAIT (2MSL), and `epoll()` vs `kqueue()`.

---

## Day 3: Resume Defense, LLD & Apple Culture Polish (6 Hours)
* **Morning (3 Hours)**:
  * Review **Module 04**: Defend **Warehouse PathMapper**, **Uplan**, and **Alternative Data Radar** against senior engineer traps.
  * Practice explaining your dual background: M.Tech Signal Processing @ NIT Rourkela + B.Tech CSE.
* **Afternoon (3 Hours)**:
  * Review **Module 05**: Trace the Low-Level Designs (On-Device Inference Pipeline and Distributed Test Execution Harness).
  * Review **Module 06**: Rehearse STAR-format responses for Apple behavioral scenarios (disagreements, handling ambiguity, extreme ownership as a DRI).
  * Memorize **Module 07 CheatSheet** metrics and key formulas.
