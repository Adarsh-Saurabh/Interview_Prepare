#!/usr/bin/env python3
"""
build_apple_modules.py
Generates all Markdown (.md) and HTML (.html) modules for Apple
AI & ML SDE and SDET Intern Interview Preparation Portal.
"""

import os
import markdown
from template import render_apple_page

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
modules_data = {}

# =============================================================================
# MODULE 00: Company & Role Intel
# =============================================================================
modules_data["00_START_HERE"] = {
    "title": "00: Apple Company & Role Intelligence",
    "prev_link": "index.html",
    "prev_title": "Overview & Hub",
    "next_link": "01_Online_Test.html",
    "next_title": "01: Signature OA Coding Problems",
    "markdown": """# 00: Apple Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Apple Inc.** (Cupertino, California; the world's most valuable consumer technology and integrated software-hardware enterprise).
* **Campus Placement Drive**: National Institute of Technology, Rourkela (Batch 2027).
* **Internship Model**: **6 Months Internship + Pre-Placement Offer (PPO) Conversion**.
* **Offered Job Roles**:
  1. **AI & ML and Software Development Engineering Intern**
  2. **Software Development Engineer in Test (SDET) Intern**
* **Compensation Structure**:
  * **Monthly Stipend**: **₹1,05,000 / month (1.05 LPM)**
  * **CTC on PPO Conversion**: **₹80,00,000 (80 LPA)** — top-tier compensation tier across global big tech.
* **Eligible Branches & Degrees**: B.Tech, M.Tech, Dual Degree, Int MSc — All Branches (CGPA $\\ge 6.0$, No active backlogs).
* **Major India R&D Engineering Centers**:
  * **Bengaluru**: Minsk Square (brand-new 15-story state-of-the-art innovation center) and Manyata Tech Park. Focus: Hardware-software co-design, CoreOS, Apple Intelligence, Siri & Speech, Camera Algorithms, and Enterprise Applications.
  * **Hyderabad**: WaveRock / Financial District. Focus: Apple Maps, Geospatial Data Intelligence, Enterprise Cloud Services, and Quality Engineering.

---

## 2. Apple's Core Engineering Philosophy

Apple does not operate like conventional software companies. To ace Apple interviews, you must embody their core technical and product tenets:

```
                  ┌──────────────────────────────────────────────┐
                  │          Apple Engineering Culture           │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐           ┌──────────────────┐
│   Craftsmanship  │           │  Privacy by      │           │     The DRI      │
│   & Detail       │           │  Design          │           │     Model        │
│ "Pixels & nanos  │           │ On-device compute│           │ Directly         │
│  matter"         │           │ Zero data logging│           │ Responsible Ind. │
└──────────────────┘           └──────────────────┘           └──────────────────┘
```

1. **Obsessive Craftsmanship & User Experience**: At Apple, software engineering is not merely about algorithmic correctness; it is about determinism, battery efficiency, zero frame-drops, microsecond latency, and uncompromising aesthetic polish.
2. **Privacy as a Fundamental Human Right**: Apple prioritizes on-device computation over sending user data to the cloud. Models must run locally on the Apple Neural Engine (ANE) with minimal memory footprint. When cloud compute is necessary, it uses **Private Cloud Compute (PCC)** with cryptographic verification and zero retention.
3. **The Directly Responsible Individual (DRI)**: There are no committee decisions. Every feature, test suite, and module has exactly one named engineer who owns it end-to-end. In your interview, you must speak in terms of personal ownership ("I designed...", "I diagnosed...", "I benchmarked..."), not vague group efforts.
4. **Hardware-Software-Silicon Co-Design**: Apple designs the chips (Apple Silicon M-series, A-series), the OS (Darwin / macOS / iOS), the compilers (LLVM / Clang / Swift), and the end applications. Software engineers and SDETs understand memory hierarchy, cache lines, and hardware acceleration.

---

## 3. The Two Target Tracks: Breakdown & Expectations

### Track A: AI & ML and Software Development Engineering Intern
* **What the Team Builds**:
  * On-device intelligence features powering iOS, macOS, and visionOS (e.g., Apple Intelligence, Siri contextual semantic understanding, Writing Tools, Image Playground, real-time audio/vision processing).
  * High-performance machine learning inference pipelines using **Core ML**, **Metal Performance Shaders (MPS)**, and the **Apple Neural Engine (ANE)**.
  * Low-latency C++/Python backend and platform services for Private Cloud Compute, distributed model evaluation, and media processing.
* **What Interviewers Test**:
  * Strong foundational Data Structures & Algorithms (Trees, Graphs, Dynamic Programming, Heaps, String processing).
  * Systems proficiency: Memory management (pointers, references, RAII, ARC), object-oriented programming, and multi-threading.
  * Machine learning fundamentals: Model quantization (INT8/INT4), latency-memory trade-offs, transformers, attention mechanisms, embeddings, and vector similarity search.

### Track B: Software Development Engineer in Test (SDET) Intern
* **What the Team Builds**:
  * Industrial-grade automation frameworks for continuous testing across millions of permutations of hardware, OS builds, and localized features.
  * Test execution harnesses, mock servers, automated regression pipelines, performance profiling suites, and flaky test detection engines.
  * Deep API validation, stress/load testing, memory leak detection using Apple Instruments, and CI/CD integration for internal builds.
* **What Interviewers Test**:
  * Coding proficiency equivalent to SDEs (LeetCode Medium DSA, string manipulation, hash structures, graph traversal).
  * Automation design principles: Page Object Model (POM), test data factories, parameterized testing, and clean architecture.
  * Systems debugging: Analyzing race conditions, memory leaks, out-of-order event delivery, and root-cause analysis.
  * Core QA methodology: Boundary value analysis, equivalence partitioning, state transition testing, test pyramid implementation, and performance benchmarking.

---

## 4. Campus Recruitment Pipeline & Stage-by-Stage Strategy

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Step 1: OA    │ ──► │  Round 1: DSA   │ ──► │ Round 2: Deep   │ ──► │ Round 3: Fit &  │
│  HackerRank /   │     │  Live Coding &  │     │ Systems / Domain│     │ Managerial      │
│  Codility (90m) │     │  Edge Cases     │     │ & Architecture  │     │ Culture & DRI   │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Stage 1: Online Assessment (OA)
* **Format**: 90 to 120 minutes on HackerRank or Codility.
* **Components**:
  * **2 to 3 Coding Problems**: Typically 1 Easy-Medium (strings/arrays/hash maps) and 1 to 2 Medium-Hard problems (Dynamic Programming, Graphs, Tree manipulation, or LRU/LFU cache variants).
  * **15 to 25 Technical MCQs**: Testing Operating Systems (processes vs threads, virtual memory, paging, locks), Computer Networks (TCP/UDP, HTTP protocols), DBMS (SQL queries, indexing), and OOPs (C++/Java/Python internals).
* **Passing Strategy**: High score requires 100% test cases passing on all coding problems within optimal time complexity, plus solid accuracy on CS MCQs.

### Stage 2: Technical Interview 1 (Data Structures, Algorithms & Edge Cases)
* **Format**: 45 to 60 minutes on Webex with CoderPad.
* **Focus**: The interviewer presents 1–2 algorithmic problems. They look for:
  * **Think-Out-Loud Protocol**: Never jump straight into writing code. State your assumptions, clarify edge cases (empty inputs, negative numbers, overflow, scale limits), discuss brute-force vs optimal approach, and state Time/Space complexity.
  * **Production-Grade Code**: Clean variable naming, modular helper functions, absence of global variables, and robust edge-case handling.
  * **Dry-Run Walkthrough**: Tracing code with a concrete example before running it.

### Stage 3: Technical Interview 2 (Systems, Domain & Resume Grilling)
* **Format**: 45 to 60 minutes with a Senior Engineer or Tech Lead.
* **Focus**:
  * Deep dive into resume projects (**Warehouse PathMapper**, **Uplan**, **Alternative Data Radar**).
  * Systems questions: Memory layout, smart pointers, ARC vs GC, concurrency primitives, sockets, and caching.
  * For AI/ML track: Model quantization, on-device latency optimization, multi-agent pipelines, LangGraph, token compression.
  * For SDET track: Building an automation framework from scratch, designing test suites for complex distributed systems, debugging memory leaks, handling flaky tests.

### Stage 4: Techno-Managerial & Behavioral (The Apple Fit Round)
* **Format**: 30 to 45 minutes with an Engineering Manager or Director.
* **Focus**:
  * Evaluating cultural alignment with Apple's craftsmanship, extreme ownership (DRI), and privacy values.
  * Behavioral questions using the STAR framework (Situation, Task, Action, Result).
  * "Why Apple?": A compelling personal narrative connecting your engineering passions to Apple's ecosystem.
"""
}

# =============================================================================
# MODULE 01: Online Test (Signature OA Problems)
# =============================================================================
modules_data["01_Online_Test"] = {
    "title": "01: Apple Signature OA Coding Problems",
    "prev_link": "00_START_HERE.html",
    "prev_title": "00: Company & Role Intel",
    "next_link": "02_Technical_Rounds.html",
    "next_title": "02: Systems, Memory & OS",
    "markdown": """# 01: Apple Signature OA Coding Problems

Apple's Online Assessment and first-round technical interviews emphasize clean, modular, and edge-case-robust implementations. This module provides 5 signature problems frequently asked in Apple campus drives, accompanied by optimal $O(1)$ / $O(n)$ solutions in both **Python** and **C++**.

---

## Problem 1: Thread-Safe LRU Cache with $O(1)$ Operations

### Problem Statement
Design a data structure that follows the constraints of a **Least Recently Used (LRU) cache**.
Implement the `LRUCache` class:
* `LRUCache(int capacity)`: Initialize the LRU cache with positive size `capacity`.
* `int get(int key)`: Return the value of the `key` if the key exists, otherwise return `-1`.
* `void put(int key, int value)`: Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.
* The functions `get` and `put` must each run in **$O(1)$ average time complexity**.
* The implementation must be **thread-safe** to simulate Apple OS-level cache services.

### Algorithmic Architecture
* A **Hash Map** (`std::unordered_map` / `dict`) maps each `key` to its corresponding node in a **Doubly Linked List**.
* The **Doubly Linked List** maintains access order. The most recently used item is placed right after a sentinel `head` node, and the least recently used item sits right before a sentinel `tail` node.
* A **Mutex** (`std::mutex` / `threading.Lock`) protects all read and write mutations against race conditions.

```
[head] <---> [Node: MRU] <---> [Node] <---> [Node: LRU] <---> [tail]
  ▲                                                            ▲
  │                       Sentinel Nodes                       │
```

### Production C++ Implementation

```cpp
#include <iostream>
#include <unordered_map>
#include <mutex>
#include <memory>

class LRUCache {
private:
    struct Node {
        int key;
        int value;
        Node* prev;
        Node* next;
        Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
    };

    int capacity;
    std::unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;
    mutable std::mutex mtx; // Thread safety lock

    void addNode(Node* node) {
        // Insert node right after head (MRU position)
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }

    void removeNode(Node* node) {
        // Unlink node from doubly linked list
        Node* prevNode = node->prev;
        Node* nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }

    void moveToHead(Node* node) {
        removeNode(node);
        addNode(node);
    }

    Node* popTail() {
        // Evict least recently used (node before tail)
        Node* res = tail->prev;
        removeNode(res);
        return res;
    }

public:
    LRUCache(int cap) : capacity(cap) {
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;
    }

    ~LRUCache() {
        std::lock_guard<std::mutex> lock(mtx);
        Node* curr = head;
        while (curr) {
            Node* temp = curr->next;
            delete curr;
            curr = temp;
        }
    }

    int get(int key) {
        std::lock_guard<std::mutex> lock(mtx);
        auto it = cache.find(key);
        if (it == cache.end()) {
            return -1;
        }
        Node* node = it->second;
        moveToHead(node);
        return node->value;
    }

    void put(int key, int value) {
        std::lock_guard<std::mutex> lock(mtx);
        auto it = cache.find(key);
        if (it != cache.end()) {
            Node* node = it->second;
            node->value = value;
            moveToHead(node);
        } else {
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            addNode(newNode);
            if (cache.size() > static_cast<size_t>(capacity)) {
                Node* tailNode = popTail();
                cache.erase(tailNode->key);
                delete tailNode;
            }
        }
    }
};
```

### Production Python Implementation

```python
import threading

class Node:
    __slots__ = ('key', 'val', 'prev', 'next')
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._lock = threading.Lock()

    def _add_to_head(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _move_to_head(self, node: Node) -> None:
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

    def get(self, key: int) -> int:
        with self._lock:
            if key not in self.cache:
                return -1
            node = self.cache[key]
            self._move_to_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        with self._lock:
            if key in self.cache:
                node = self.cache[key]
                node.val = value
                self._move_to_head(node)
            else:
                new_node = Node(key, value)
                self.cache[key] = new_node
                self._add_to_head(new_node)
                if len(self.cache) > self.capacity:
                    lru = self._pop_tail()
                    del self.cache[lru.key]
```

* **Complexity**: Time: $O(1)$ for both `get` and `put`. Space: $O(\\text{capacity})$.

---

## Problem 2: In-Place String Compression & Token Boundary Parsing

### Problem Statement
Given an array of characters `chars`, compress it using the following algorithm:
Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:
* If the group's length is `1`, append the character to `s`.
* Otherwise, append the character followed by the group's length.
The compressed string `s` must **not be returned directly**, but instead be **stored in the input character array `chars` in-place**. Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.
Return the new length of the array after in-place compression.
Constraint: You must use **$O(1)$ extra memory space**.

### Algorithmic Architecture
* Two-pointer approach: `write_idx` tracks where the next compressed character should be placed; `read_idx` scans through contiguous runs of identical characters.
* When a run of length $k$ is identified:
  1. Write `chars[read_idx]` to `chars[write_idx++]`.
  2. If $k > 1$, convert $k$ to a string or characters and write each digit into `chars[write_idx++]`.

### Optimal C++ Solution

```cpp
#include <vector>
#include <string>

class Solution {
public:
    int compress(std::vector<char>& chars) {
        int n = chars.size();
        int writeIdx = 0;
        int readIdx = 0;

        while (readIdx < n) {
            char currChar = chars[readIdx];
            int count = 0;

            // Count contiguous occurrences of currChar
            while (readIdx < n && chars[readIdx] == currChar) {
                readIdx++;
                count++;
            }

            // Write character
            chars[writeIdx++] = currChar;

            // Write digits if count > 1
            if (count > 1) {
                std::string countStr = std::to_string(count);
                for (char c : countStr) {
                    chars[writeIdx++] = c;
                }
            }
        }

        return writeIdx;
    }
};
```

### Optimal Python Solution

```python
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write_idx = 0
        read_idx = 0

        while read_idx < n:
            curr_char = chars[read_idx]
            count = 0

            while read_idx < n and chars[read_idx] == curr_char:
                read_idx += 1
                count += 1

            chars[write_idx] = curr_char
            write_idx += 1

            if count > 1:
                for digit in str(count):
                    chars[write_idx] = digit
                    write_idx += 1

        return write_idx
```

* **Complexity**: Time: $O(n)$ where $n$ is length of `chars`. Space: strictly $O(1)$ auxiliary space.

---

## Problem 3: Word Break with Trie-Optimized Dynamic Programming (Siri NLP Parsing)

### Problem Statement
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.
Notice that the same word in the dictionary may be reused multiple times in the segmentation.

### Algorithmic Architecture
* **Standard DP**: `dp[i]` is `true` if `s[0...i-1]` can be segmented. Evaluating `dp[i]` naively takes $O(n^2)$ substring slices.
* **Trie-Optimized DP**: Insert all dictionary words into a Prefix Trie. For each starting index $i$ where `dp[i] == true`, traverse the Trie starting from `s[i]`. If a path hits an `is_word` terminal at character index $j$, set `dp[j + 1] = true`. This prevents redundant substring allocations and achieves $O(n \\cdot L)$ where $L$ is the maximum word length.

### Production C++ Solution

```cpp
#include <iostream>
#include <vector>
#include <string>

struct TrieNode {
    TrieNode* children[26] = {nullptr};
    bool isWord = false;
};

class Solution {
private:
    TrieNode* root;

    void insert(const std::string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!curr->children[idx]) {
                curr->children[idx] = new TrieNode();
            }
            curr = curr->children[idx];
        }
        curr->isWord = true;
    }

public:
    Solution() : root(new TrieNode()) {}

    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        for (const auto& w : wordDict) {
            insert(w);
        }

        int n = s.size();
        std::vector<bool> dp(n + 1, false);
        dp[0] = true; // Base case: empty prefix

        for (int i = 0; i < n; i++) {
            if (!dp[i]) continue;

            TrieNode* curr = root;
            for (int j = i; j < n; j++) {
                int idx = s[j] - 'a';
                if (!curr->children[idx]) {
                    break; // No matching prefix in Trie
                }
                curr = curr->children[idx];
                if (curr->isWord) {
                    dp[j + 1] = true;
                }
            }
        }

        return dp[n];
    }
};
```

---

## Problem 4: Build Dependency Graph & Task Scheduler with Cycle Detection

### Problem Statement
Apple's build system (Xcode / `xcodebuild`) compiles thousands of target libraries with interdependencies.
Given $N$ tasks labeled from $0$ to $N-1$ and a list of directed prerequisites `[u, v]` indicating task $v$ must be completed before task $u$ can start.
1. Determine if all tasks can be finished without entering a **deadlock cycle**.
2. If possible, return the valid compilation sequence (Topological Ordering). If impossible, return an empty array.

### Algorithmic Architecture
* Model dependencies as a Directed Graph: edge $v \\to u$.
* Apply **Kahn's Algorithm (BFS with In-Degrees)**:
  1. Compute the in-degree of all vertices.
  2. Enqueue all vertices with in-degree $0$.
  3. While queue is non-empty, pop vertex $curr$, append to result list, and decrement in-degree of all neighbors.
  4. If a neighbor reaches in-degree $0$, push it to queue.
  5. If the number of processed nodes equals $N$, no cycle exists. Otherwise, a circular dependency exists.

### Optimal Python Solution

```python
from collections import deque, defaultdict
from typing import List

class BuildSystemScheduler:
    def findOrder(self, numTasks: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numTasks

        for u, v in prerequisites:
            # v must run before u: edge v -> u
            adj[v].append(u)
            in_degree[u] += 1

        queue = deque([i for i in range(numTasks) if in_degree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numTasks:
            return order
        return [] # Cycle detected (deadlock)
```

* **Complexity**: Time: $O(V + E)$ where $V = \\text{numTasks}$ and $E = \\text{len(prerequisites)}$. Space: $O(V + E)$.

---

## Problem 5: Jump Game with Greedy Sliding Window

### Problem Statement
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.
Return `true` if you can reach the last index, or `false` otherwise.

### Optimal Greedy Solution ($O(n)$ Time, $O(1)$ Space)

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    bool canJump(std::vector<int>& nums) {
        int n = nums.size();
        int maxReach = 0;

        for (int i = 0; i < n; i++) {
            if (i > maxReach) {
                return false; // Trapped at a 0
            }
            maxReach = std::max(maxReach, i + nums[i]);
            if (maxReach >= n - 1) {
                return true;
            }
        }
        return true;
    }
};
```
"""
}

# =============================================================================
# MODULE 02: Technical Rounds (Systems, Memory & OS)
# =============================================================================
modules_data["02_Technical_Rounds"] = {
    "title": "02: Systems, Memory Management & OS Internals",
    "prev_link": "01_Online_Test.html",
    "prev_title": "01: Signature OA Problems",
    "next_link": "03_Domain_Deep_Dive.html",
    "next_title": "03: Apple AI & SDET Infra",
    "markdown": """# 02: Systems, Memory Management & OS Internals

Apple engineers build software close to the metal. Whether you are applying for **AI & ML SDE** or **SDET**, technical interviews at Apple rigorously probe memory layout, concurrency primitives, synchronization, and operating system mechanics.

---

## 1. Memory Management: ARC vs GC vs RAII

Apple platforms (iOS, macOS) utilize **Automatic Reference Counting (ARC)** rather than tracing Garbage Collection (like Java or Go).

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ Feature                 │ ARC (Swift / Objective-C│ Tracing GC (Java/Go)    │ C++ RAII                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Deallocation Timing     │ Deterministic (Instant) │ Non-deterministic (Stop-│ Deterministic (Scope    │
│                         │ when count hits 0       │ the-world pauses)       │ exit)                   │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Runtime CPU Overhead    │ Zero GC pauses; atomic  │ Periodic CPU spikes for │ Zero runtime tracking   │
│                         │ ref count increments    │ mark-and-sweep          │ overhead                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Memory Footprint        │ Minimal; immediate      │ Higher; delayed memory  │ Strict, explicit cache  │
│                         │ reclamation             │ reclamation             │ locality                │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ Retain Cycle Risk       │ High (needs weak/unowned│ Low (GC automatically   │ Prevented by clean      │
│                         │ references)             │ collects cyclic graphs) │ ownership & weak_ptr    │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Retain Cycles & Reference Types
* **Strong Reference**: Increments the reference count by 1. Object remains in memory as long as strong count $> 0$.
* **Weak Reference**: Does **not** increment the reference count. When the referenced object deallocates, the pointer is automatically zeroed out (`nil`). In Swift/Obj-C, a weak reference is always an optional.
* **Unowned Reference**: Does not increment reference count, but assumes the object will never be deallocated while accessed. Accessing a deallocated unowned reference results in an immediate crash (equivalent to a raw dangling pointer).

### C++ Smart Pointers Internals
1. `std::unique_ptr<T>`:
   * Exclusive ownership model.
   * Exactly the size of a raw pointer (zero memory overhead).
   * Non-copyable, only movable (`std::move`). Destroys object when out of scope.
2. `std::shared_ptr<T>`:
   * Shared ownership model.
   * Stores two pointers (16 bytes on 64-bit): Pointer to raw object, and pointer to the **Control Block**.
   * The Control Block contains:
     - Strong Reference Count (`std::atomic<long>`)
     - Weak Reference Count (`std::atomic<long>`)
     - Custom Deleter / Allocator
   * Thread Safety: Modifying the reference count is atomic and thread-safe. Modifying the underlying object itself is **not** thread-safe.
3. `std::weak_ptr<T>`:
   * Non-owning observer. Does not keep the object alive.
   * Can be promoted to `std::shared_ptr` via `.lock()` if the object is still alive. Used to break circular dependencies.

---

## 2. C++ Object Memory Layout & Virtual Tables (`vtable`)

When a class declares or inherits at least one virtual function, the C++ compiler injects runtime polymorphism machinery:

```
[Stack / Heap Object Instance]
┌─────────────────────────────────┐
│  vptr (Virtual Table Pointer)   │ ──► [Virtual Table (vtable) in .rodata]
├─────────────────────────────────┤     ┌───────────────────────────────────┐
│  member_var_1                   │     │  &Derived::virtual_method_1()     │
├─────────────────────────────────┤     ├───────────────────────────────────┤
│  member_var_2                   │     │  &Derived::virtual_method_2()     │
└─────────────────────────────────┘     └───────────────────────────────────┘
```

### Essential Virtual Concepts to Defend
1. **Virtual Destructor**: If a class has virtual methods, its destructor **must** be marked `virtual`. If you delete a derived class object through a base class pointer without a virtual destructor, only the base destructor runs, causing resource/memory leaks.
2. **Object Slicing**: Occurs when you assign a derived class instance to a base class object **by value** (instead of pointer or reference). The derived portion is sliced off, and polymorphic behavior is lost because `vptr` points to the base class table.
3. **Struct Padding & Memory Alignment**:
   * Hardware reads memory in words (4 or 8 bytes). Data must be aligned to addresses that are multiples of its size.
   * Order matters: Placing a `char` (1 byte), `double` (8 bytes), and `int` (4 bytes) sequentially results in 24 bytes due to padding. Reordering as `double` (8), `int` (4), `char` (1) results in 16 bytes.

---

## 3. Concurrency, Synchronization & Multi-Threading

### Processes vs Threads
* **Process**: An isolated execution environment with its own dedicated virtual memory space, file descriptor table, and page tables. Context switching between processes requires invalidating or swapping Translation Lookaside Buffer (TLB) entries, making it expensive ($1000+$ CPU cycles).
* **Thread**: A lightweight execution stream within a process. Threads share the same address space, heap, static data, and open file descriptors, but each thread has its own **Stack**, **Program Counter (PC)**, and **Registers**. Context switching is faster ($100-200$ CPU cycles).

### Synchronization Primitives & Trade-Offs

```
┌──────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Primitive        │ How It Works                    │ Best Use Case                   │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Mutex            │ Puts thread to sleep via OS     │ Long critical sections; I/O     │
│                  │ scheduler if lock unavailable   │ or disk operations.             │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Spinlock         │ Busy-waits in a tight CPU loop  │ Ultra-short critical sections   │
│                  │ (`while(test_and_set)`)         │ where sleep context switch is   │
│                  │                                 │ more expensive than waiting.    │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Semaphore        │ Integer counter controlling     │ Resource pools (e.g., max 10    │
│                  │ access to $N$ shared resources  │ database connections).          │
├──────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ `std::atomic`    │ Hardware-enforced atomic        │ Single variable counters, lock- │
│                  │ instructions (e.g., CMPXCHG)    │ free ring buffers, flags.       │
└──────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

### False Sharing & Cache Lines
* Modern CPUs access memory in **Cache Lines** (typically 64 bytes on ARM Apple Silicon and x86).
* **False Sharing**: Occurs when two threads running on different CPU cores modify completely independent variables that happen to reside on the same 64-byte cache line. The CPU cache coherence protocol (MESI/MOESI) invalidates the cache line back and forth, degrading multi-threaded throughput.
* **Fix**: Force data alignment to separate cache lines using `alignas(64)` in C++.

---

## 4. Networking Protocols & Socket I/O Multiplexing

### TCP 3-Way Handshake & 4-Way Teardown
```
Client                              Server
  │               SYN                 │
  ├──────────────────────────────────►│  1. Client sends SYN (seq = x)
  │             SYN-ACK               │
  │◄──────────────────────────────────┤  2. Server responds SYN-ACK (seq = y, ack = x + 1)
  │               ACK                 │
  ├──────────────────────────────────►│  3. Client sends ACK (ack = y + 1) -> ESTABLISHED
  │                                   │
  │               FIN                 │
  ├──────────────────────────────────►│  1. Initiator sends FIN
  │               ACK                 │
  │◄──────────────────────────────────┤  2. Receiver acknowledges ACK
  │               FIN                 │
  │◄──────────────────────────────────┤  3. Receiver finishes sending data, sends FIN
  │               ACK                 │
  ├──────────────────────────────────►│  4. Initiator sends ACK -> Enters TIME_WAIT (2MSL)
```
* **Why TIME_WAIT is 2MSL (Maximum Segment Lifetime)**: Ensures the final ACK is reliably delivered to the receiver. If the ACK is lost, the receiver will retransmit its FIN, which the client can still acknowledge during TIME_WAIT, preventing stray packets from corrupting new connections.

### I/O Multiplexing: `select` vs `epoll` vs `kqueue`
* `select()` / `poll()`: $O(N)$ scanning over the entire file descriptor list on every event. Unscalable for high concurrency.
* `epoll()` (Linux): $O(1)$ event notification using red-black trees and ready lists in the kernel.
* `kqueue()` (macOS / Darwin / iOS): Apple's kernel event notification mechanism. Handles file descriptors, signals, timers, and asynchronous I/O with $O(1)$ complexity.
"""
}

# =============================================================================
# MODULE 03: Domain Deep Dive (Apple AI/ML & SDET Infra)
# =============================================================================
modules_data["03_Domain_Deep_Dive"] = {
    "title": "03: Apple AI Architecture & SDET Quality Engineering",
    "prev_link": "02_Technical_Rounds.html",
    "prev_title": "02: Systems, Memory & OS",
    "next_link": "04_Candidate_Resume_Grilling.html",
    "next_title": "04: Resume Defense & Traps",
    "markdown": """# 03: Apple AI Architecture & SDET Quality Engineering

This module breaks down the domain intelligence for both hiring tracks: **Apple Intelligence On-Device AI Pipelines** and **Industrial SDET Automation Architecture**.

---

## PART I: Apple Intelligence & Core ML Architecture

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Apple Intelligence Engine                       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                 ┌──────────────────┴──────────────────┐
                 ▼                                     ▼
   ┌───────────────────────────┐         ┌───────────────────────────┐
   │    On-Device AI (~3B)     │         │ Private Cloud Compute     │
   │  • Apple Neural Engine    │         │ • Stateless Apple Silicon │
   │  • LoRA Adapters          │         │ • Cryptographic auditing  │
   │  • 4-bit/8-bit Quantized  │         │ • Non-retention guarantee │
   └───────────────────────────┘         └───────────────────────────┘
```

### 1. The Dual-Tier Execution Model
* **On-Device Foundation Model (~3B Parameters)**:
  * Designed to run directly on Apple Silicon (iPhone 15 Pro+, M1+ Macs/iPads).
  * Consumes under 4GB RAM to prevent evicting active user applications.
  * Optimized using **Post-Training Quantization (PTQ)** and **Quantization-Aware Training (QAT)** down to 4-bit and mixed 2-bit/4-bit weights.
* **Private Cloud Compute (PCC)**:
  * Used for complex reasoning tasks that exceed on-device compute limits.
  * Runs on custom Apple Silicon servers with hardware-enforced Secure Enclave.
  * **Zero Retention**: User data is processed strictly in volatile RAM and instantly destroyed. Independent security researchers can cryptographically inspect the exact OS image running on PCC.

### 2. LoRA (Low-Rank Adaptation) Dynamic Adapter Swapping
Instead of maintaining separate multi-gigabyte models for writing, proofreading, notification summaries, and code completion:
* A single, frozen on-device base model is shared across all features.
* Task-specific capabilities are injected on the fly via tiny **LoRA adapters** (typically tens of megabytes):
$$W_{\\text{adapted}} = W_0 + \\Delta W = W_0 + B \\cdot A$$
where $W_0 \\in \\mathbb{R}^{d \\times k}$ is the frozen weight matrix, and $B \\in \\mathbb{R}^{d \\times r}, A \\in \\mathbb{R}^{r \\times k}$ with rank $r \\ll \\min(d, k)$.
* Adapters are memory-mapped (`mmap`) into RAM in milliseconds as user intent shifts.

### 3. Core ML Compilation Pipeline
```
[PyTorch / HuggingFace Model]
              │
              ▼  (coremltools.convert)
[.mlpackage / MIL Intermediate Representation]
              │
              ▼  (Static Analysis & Graph Optimization)
[Partitioned Subgraphs]
   ├── Subgraph 1 ──► Apple Neural Engine (ANE) - Fixed matrix ops
   ├── Subgraph 2 ──► Metal Performance Shaders (MPS) - GPU compute
   └── Subgraph 3 ──► CPU / AMX (Apple Matrix Coprocessor)
```

---

## PART II: SDET Quality Engineering & Industrial Automation

```
                          ┌─────────────────────────┐
                          │   UI / End-to-End       │  ▲  Slowest,
                          │   (XCUITest, Appium)    │  │  High Maintenance
                          ├─────────────────────────┤  │
                          │   Service & API Layer   │  │
                          │   (REST, gRPC, Mocks)   │  │
                          ├─────────────────────────┤  │
                          │   Unit & Logic Tests    │  ▼  Fastest,
                          │   (pytest, XCTest)      │     High Reliability
                          └─────────────────────────┘
```

### 1. Page Object Model (POM) Design Pattern
* **Rule**: Test scripts must **never** hardcode UI element locators (accessibility IDs, XPaths) or UI gestures directly in test assertions.
* **Separation of Concerns**:
  * **Page Class**: Encapsulates the UI structure, element locators, and user interactions (e.g., `login_page.enter_credentials()`).
  * **Test Script**: Implements business assertions and test logic (e.g., `assert profile_page.is_displayed()`).
* **Benefit**: If Apple redesigns a UI button or alters an accessibility identifier, only one line in the Page Class changes, leaving hundreds of automated tests intact.

### 2. Modern Python SDET Automation Framework Structure

```python
# test_framework/pages/base_page.py
from abc import ABC, abstractmethod
import time

class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator: tuple, timeout: int = 10):
        # Polls for element presence with explicit wait
        start = time.time()
        while time.time() - start < timeout:
            el = self.driver.find_element(*locator)
            if el and el.is_visible():
                return el
            time.sleep(0.2)
        raise TimeoutError(f"Element {locator} not found within {timeout}s")

# test_framework/tests/test_authentication.py
import pytest

class TestAuthentication:
    @pytest.fixture(autouse=True)
    def setup_teardown(self, app_driver):
        # Fixture sets up clean isolated state per test
        self.driver = app_driver
        yield
        self.driver.reset_app_state()

    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password,expected_status", [
        ("valid_user@apple.com", "CorrectPass123!", True),
        ("invalid_user@apple.com", "WrongPass!", False),
        ("", "EmptyUserPass!", False)
    ])
    def test_login_flow(self, username, password, expected_status):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        assert login_page.is_logged_in() == expected_status
```

### 3. Flaky Test Mitigation Strategies
In large-scale continuous integration systems at Apple (running millions of tests per day):
1. **Quarantine Pipeline**: Any test that exhibits non-deterministic pass/fail behavior on the identical commit is automatically quarantined from the blocking merge queue to unblock developers.
2. **Deterministic Timeouts**: Replace arbitrary `sleep(5)` statements with **Explicit Polling Waits** that check for condition satisfaction.
3. **Hermetic Test Environments**: Every test execution runs with fresh mock data, ephemeral test accounts, and mocked network stubs to prevent shared-state corruption.
4. **Statistical Root-Cause Analysis**: Track failure variance across device types, OS build numbers, and network latencies to isolate environmental bugs from true regressions.
"""
}

# =============================================================================
# MODULE 04: Candidate Resume Grilling
# =============================================================================
modules_data["04_Candidate_Resume_Grilling"] = {
    "title": "04: Candidate Resume Defense & Traps",
    "prev_link": "03_Domain_Deep_Dive.html",
    "prev_title": "03: Apple AI & SDET Infra",
    "next_link": "05_System_Design_or_HIL.html",
    "next_title": "05: LLD & Test Architecture",
    "markdown": """# 04: Candidate Resume Defense & Traps

This module prepares **Adarsh Saurabh** (`225EC6021`) to defend every line of his academic background and projects under rigorous grilling by Apple senior engineers.

---

## 1. Candidate Academic Profile Defense

### Academic Credentials
* **M.Tech in Signal and Image Processing**, National Institute of Technology, Rourkela (2025 – 2027) | **CGPA: 8.28**
* **B.Tech in Computer Science and Engineering**, Guru Ghasidas University, Bilaspur (2020 – 2024) | **CGPA: 8.5**
* **Matriculation CBSE**, Jawahar Navodaya Vidyalaya, Sitamarhi (2017) | **CGPA: 8.8**

### How to Leverage the M.Tech + B.Tech Synergy at Apple
* **The Pitch**:
  > *"My undergraduate degree in Computer Science gave me a rigorous foundation in algorithms, operating systems, memory management, and distributed systems. My M.Tech in Signal and Image Processing at NIT Rourkela deepened my mastery of the mathematical underpinnings of modern machine learning — linear algebra, Fourier transforms, digital filters, tensor decomposition, and numerical optimization. At Apple, where machine learning is tightly integrated with hardware accelerators like the Apple Neural Engine (ANE) and Metal Performance Shaders, having both systems engineering depth and signal-level mathematical intuition allows me to optimize algorithms from mathematical formulation down to cache-line and silicon efficiency."*

---

## 2. Project 1: Warehouse PathMapper (Mandatory Project)

### Master Resume Claim
* *Delivered a dynamic warehouse mapping solution as a freelance engagement, translating operational pathfinding needs into a heuristic-based routing system.*
* *Scaled the routing engine to warehouses as large as 10,000×10,000 units, computing optimal paths through 10,000+ locations simultaneously in under 0.5 seconds on an i5 laptop CPU.*

### Apple Engineering Grilling & Defenses

#### Trap 1: *"Why did you use a heuristic instead of standard Dijkstra or A* algorithm?"*
* **Candidate Defense**:
  > *"Standard Dijkstra or pure A* on a 10,000×10,000 grid represents $10^8$ nodes. Running single-source shortest path across 10,000 pick locations creates a metric Traveling Salesperson Problem (TSP) with $10^4$ stops, which is NP-hard. Running exhaustive graph search would require gigabytes of memory and minutes of compute. Instead, I abstracted the warehouse into a hierarchical spatial graph: long parallel aisles with defined entry/exit choke points. By exploiting the rectilinear Manhattan geometry and combining A* corridor pathing with a 2-opt heuristic tour optimizer, the search space was pruned by over 99%, allowing sub-0.5 second execution on a standard commodity CPU."*

#### Trap 2 (SDET Track): *"How would you architect an automated regression suite to test this pathfinding engine?"*
* **Candidate Defense**:
  > *"I would structure the test suite into 4 levels:*
  > 1. *Mathematical Unit Invariant Tests: Asserting triangle inequality holds across all computed distances ($d(A, B) \\le d(A, C) + d(C, B)$) and paths never cross obstacle coordinates.*
  > 2. *Boundary & Stress Tests: Testing edge grids (1×1 grid, single aisle, 10,000×10,000 grid with 0 obstacles, and dense obstacle mazes).*
  > 3. *Property-Based Testing (using Hypothesis): Generating 10,000 random obstacle permutations and validating that computed paths are continuous and non-self-intersecting.*
  > 4. *Performance Regression Benchmarking: Measuring execution time variance and peak memory allocation using profiling tools to ensure no commit introduces latency degradation beyond 500ms."*

---

## 3. Project 2: Uplan — Adversarial Document Intelligence Pipeline

### Master Resume Claim
* *Architected an adversarial multi-agent workflow in LangGraph using modern AI tools (Gemini 2.5 Pro specialists) to check visa document coherence; reduced manual verification workload by 85% with detailed failure rebuttal generation.*
* *Designed structural encoding system using Gemini 2.0 Flash to compile page-level document metadata into a typed semantic graph (98% token compression) and integrated a zero-hallucination mathematical rule check engine.*

### Apple Engineering Grilling & Defenses

#### Trap 1: *"How does an adversarial multi-agent system prevent LLM hallucinations?"*
* **Candidate Defense**:
  > *"In Uplan, an affirmative agent parses documents and extracts applicant claims, while a separate adversarial specialist actively attempts to falsify or detect contradictions across documents (e.g., date mismatches between employment letters and bank statements). Most importantly, we do not let LLMs perform arithmetic or logical validation. We use Gemini 2.0 Flash strictly as a structured semantic parser that maps raw text into a typed schema graph. All financial thresholds, date intervals, and eligibility constraints are evaluated by a deterministic Python mathematical rule engine. If an inconsistency is detected, the adversarial agent generates an evidence-grounded failure rebuttal referencing exact document coordinates."*

#### Trap 2: *"How do you test a non-deterministic multi-agent pipeline in continuous integration?"*
* **Candidate Defense**:
  > *"Testing non-deterministic LLM pipelines requires separating parsing accuracy from agent orchestration:*
  > 1. *Golden Dataset Evaluation: A curated dataset of 200 ground-truth visa dossiers with known synthetic fraud/contradiction cases.*
  > 2. *Deterministic Mock Stubs: In CI unit tests, LLM API calls are intercepted with recorded mock responses to verify LangGraph state transitions, retry loops, and error handlers deterministically.*
  > 3. *Semantic Drift Metrics: In nightly regression runs with live models, we measure output stability using exact schema validation (Pydantic), constraint verification rates, and embedding-based semantic similarity (BERTScore)."*

---

## 4. Project 3: Alternative Data Radar

### Master Resume Claim
* *Engineered an automated data collection backend in Next.js to gather public web signals (careers and pricing data), routing requests via Bright Data Web Unlocker to bypass anti-scraping mechanisms.*
* *Implemented AI-driven analysis to calculate a 0–100 corporate health score stored in a SQL database, presenting pre-earnings intelligence and warning alerts in a responsive Recharts dashboard.*

### Apple Engineering Grilling & Defenses

#### Trap 1: *"How do you handle rate-limiting, proxy rotation, and network failures in automated data collection?"*
* **Candidate Defense**:
  > *"We integrated Bright Data's Web Unlocker proxy pool, but resilient architecture requires handling failures at the application layer. We implemented an asynchronous worker queue with exponential backoff and jitter ($t = \\text{base} \\times 2^{\\text{attempt}} + \\text{random}$). Requests were tagged with correlation IDs. If an endpoint responded with 429 (Too Many Requests) or CAPTCHAs, the request was re-queued with alternative proxy headers. Incomplete or malformed HTML payloads were validated through schema parsing before hitting the downstream SQL ingestion pipeline."*

#### Trap 2 (SDET Track): *"How would you test the accuracy and reliability of the 0–100 corporate health score algorithm?"*
* **Candidate Defense**:
  > *"The health score is a composite weighted metric of hiring trends, employee sentiment, and pricing volatility. I would test it via:*
  > 1. *Boundary Analysis: Feeding extreme inputs (zero job openings, 100% negative sentiment) and verifying the score clamps gracefully to 0 without division-by-zero crashes.*
  > 2. *Sensitivity & Monotonicity Testing: Verifying that an increase in positive signals strictly results in a non-decreasing score.*
  > 3. *Database Integrity Tests: Ensuring ACID compliance during high-concurrency ingestion and verifying that foreign key relationships between companies and historical telemetry snapshots are maintained."*
"""
}

# =============================================================================
# MODULE 05: System Design & LLD
# =============================================================================
modules_data["05_System_Design_or_HIL"] = {
    "title": "05: Low-Level System Design & Test Architecture",
    "prev_link": "04_Candidate_Resume_Grilling.html",
    "prev_title": "04: Resume Defense & Traps",
    "next_link": "06_Managerial_and_HR.html",
    "next_title": "06: Apple Culture & Values",
    "markdown": """# 05: Low-Level System Design & Test Architecture

This module details two production-grade system designs matching Apple's hiring tracks:
1. **AI/ML Track**: On-Device ML Inference Pipeline & Thermal-Aware Telemetry Dispatcher.
2. **SDET Track**: Distributed Automated Test Execution Harness with Flaky Test Quarantine.

---

## DESIGN 1 (AI/ML): On-Device ML Inference Pipeline

### Problem Definition
Design an on-device inference management system for iOS/macOS that accepts ML inference requests from multiple concurrent apps, optimizes execution on the **Apple Neural Engine (ANE)**, dynamically batches inputs, and throttles compute when device thermals rise.

### Architectural Diagram

```
[App 1 (Camera)]     [App 2 (Siri)]     [App 3 (Photos)]
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Inference Request Queue      │
          │   (Priority-Sorted Task Heap)    │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Dynamic Batching Engine      │
          │  (Timeout-Window / Max-Batch)    │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │     Thermal & Power Governor     │ ◄── [Device Thermal State API]
          │  (Nominal / Fair / Serious /     │
          │   Critical -> Throttling/Skip)   │
          └────────────────┬─────────────────┘
                           ▼
          ┌──────────────────────────────────┐
          │       Core ML Execution Unit     │
          │   ANE / MPS GPU / Accelerate CPU │
          └──────────────────────────────────┘
```

### Key Components & Requirements
1. **Priority Scheduling**: Foreground user interactions (e.g., Camera real-time face tracking) receive `CRITICAL` priority; background indexing (e.g., Photos facial clustering) runs at `BACKGROUND` priority.
2. **Dynamic Batching**: If multiple inference requests for the same model arrive within a $5\\text{ms}$ window, batch them up to batch size $B=8$ to maximize ANE tensor utilization.
3. **Thermal Throttling**: Query the OS thermal state. If thermal state is `SERIOUS` or `CRITICAL`, drop background tasks and throttle batch frequency to prevent device overheating and thermal shutdown.

### Working Python Scaffold Implementation

```python
import time
import heapq
import threading
from typing import List, Any
from dataclasses import dataclass, field

@dataclass(order=True)
class InferenceRequest:
    priority: int  # 0: Critical (User-Facing), 1: High, 2: Background
    timestamp: float = field(compare=True)
    task_id: str = field(compare=False)
    input_tensor: Any = field(compare=False)
    callback: Any = field(compare=False)

class OnDeviceInferenceEngine:
    def __init__(self, max_batch_size: int = 8, batch_timeout_sec: float = 0.005):
        self.max_batch_size = max_batch_size
        self.batch_timeout = batch_timeout_sec
        self.queue: List[InferenceRequest] = []
        self.lock = threading.Lock()
        self.running = True
        self.worker_thread = threading.Thread(target=self._dispatch_loop, daemon=True)
        self.worker_thread.start()

    def submit_request(self, task_id: str, priority: int, input_tensor: Any, callback: Any) -> None:
        req = InferenceRequest(
            priority=priority,
            timestamp=time.time(),
            task_id=task_id,
            input_tensor=input_tensor,
            callback=callback
        )
        with self.lock:
            heapq.heappush(self.queue, req)

    def _get_thermal_state(self) -> str:
        # Simulates querying Apple ProcessInfo.thermalState
        return "Nominal"

    def _dispatch_loop(self) -> None:
        while self.running:
            batch = []
            start_time = time.time()

            while time.time() - start_time < self.batch_timeout and len(batch) < self.max_batch_size:
                with self.lock:
                    if self.queue:
                        thermal = self._get_thermal_state()
                        # If thermal is critical, skip background tasks
                        if thermal == "Critical" and self.queue[0].priority > 0:
                            continue
                        batch.append(heapq.heappop(self.queue))
                    else:
                        break
                time.sleep(0.001)

            if batch:
                self._execute_batch(batch)

    def _execute_batch(self, batch: List[InferenceRequest]) -> None:
        # Hardware execution on Apple Neural Engine (ANE)
        inputs = [b.input_tensor for b in batch]
        # Simulated tensor inference
        results = [f"Inferred_{inp}" for inp in inputs]
        for req, res in zip(batch, results):
            if req.callback:
                req.callback(res)
```

---

## DESIGN 2 (SDET): Distributed Test Execution Harness with Flaky Quarantine

### Problem Definition
Design a high-throughput, distributed test execution framework that runs thousands of XCUITest and integration tests across a matrix of real iOS devices and simulators, isolating flaky tests automatically to prevent pipeline stalls.

### Architecture Overview

```
[Developer Git Push] ──► [CI Orchestrator (Jenkins / GitHub Actions)]
                                   │
                                   ▼
                 ┌──────────────────────────────────┐
                 │      Test Dispatcher Engine      │
                 │   • Reads test suite metadata    │
                 │   • Queries Flaky Test Quarantine│
                 └─────────────────┬────────────────┘
                                   │
                 ┌─────────────────┴─────────────────┐
                 ▼                                   ▼
   ┌───────────────────────────┐       ┌───────────────────────────┐
   │    Main Test Runner       │       │  Quarantine Sandbox Pool  │
   │  (Gatekeeper for merges)  │       │  (Non-blocking diagnosis) │
   └─────────────┬─────────────┘       └─────────────┬─────────────┘
                 │                                   │
                 └─────────────────┬─────────────────┘
                                   ▼
                 ┌──────────────────────────────────┐
                 │        Worker Agent Farm         │
                 │  • iPhone 15 / 16 Simulators     │
                 │  • Physical Test Devices         │
                 │  • macOS Runner Nodes            │
                 └─────────────────┬────────────────┘
                                   ▼
                 ┌──────────────────────────────────┐
                 │    Artifact & Telemetry Store    │
                 │  Crash dumps, video, logs, traces│
                 └──────────────────────────────────┘
```

### Core Design Rules
1. **Flaky Test Quarantine**: If a test passes 2 times and fails 1 time on the exact same commit, its flaky variance score triggers quarantine. The test continues running in a non-blocking sandbox pool to accumulate diagnostic traces, but does not block developer pull requests.
2. **Exponential Backoff with Jitter for Retries**:
$$t_{\\text{retry}} = \\min(t_{\\text{max}}, t_{\\text{base}} \\cdot 2^{\\text{attempt}}) + \\text{random}(0, 1)$$
3. **Artifact Isolation**: Each test run captures stdout, stderr, sysdiagnose dumps, and video screen captures into a structured object bucket keyed by `[commit_sha]/[test_id]/[run_index]`.
"""
}

# =============================================================================
# MODULE 06: Managerial & HR (Apple Culture & Values)
# =============================================================================
modules_data["06_Managerial_and_HR"] = {
    "title": "06: Apple Culture, Values & Behavioral Rounds",
    "prev_link": "05_System_Design_or_HIL.html",
    "prev_title": "05: LLD & Test Architecture",
    "next_link": "07_Quick_Reference.html",
    "next_title": "07: Rapid Recall CheatSheet",
    "markdown": """# 06: Apple Culture, Values & Behavioral Rounds

Apple's final interview rounds evaluate how you think, how you collaborate across functional silos, and whether you embody Apple's uncompromising product and engineering values.

---

## 1. The Core Tenets of Apple Culture

```
┌────────────────────────────────────────────────────────────────────────┐
│                      Apple's 5 Cultural Pillars                        │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Craftsmanship: Good enough is never good enough.                    │
│ 2. Directly Responsible Individual (DRI): Extreme personal ownership.   │
│ 3. Privacy by Design: Fundamental human right, not a compliance box.   │
│ 4. Constructive Debate: "Disagree and commit" with evidence.           │
│ 5. Simplicity: Relentlessly strip away unnecessary complexity.         │
└────────────────────────────────────────────────────────────────────────┘
```

### The DRI Concept in Action
* At Apple, projects do not succeed or fail because of "the team" — they succeed or fail because of the **DRI**.
* In interviews, avoid passive or diffuse language ("we decided", "our team thought"). Instead, speak with crisp accountability:
  * *"I owned the spatial heuristic module."*
  * *"I diagnosed the cache line false-sharing bottleneck."*
  * *"When the API failed, I took responsibility for implementing the backoff retry strategy."*

---

## 2. High-Yield Behavioral Scenarios (STAR Method)

### Question 1: *"Tell me about a time you had a technical disagreement with a teammate or lead. How did you resolve it?"*
* **Situation**: During the development of the Uplan multi-agent pipeline, my teammate proposed having the LLM directly perform mathematical validation of applicant financial statements using prompt engineering.
* **Task**: I recognized that LLMs are probabilistic token predictors and inherently prone to subtle arithmetic hallucinations, which would violate our zero-hallucination requirement.
* **Action**: Instead of engaging in subjective debates, I designed a rapid empirical benchmark: 50 bank statements with subtle balance mismatches. The pure LLM approach missed 18% of calculation discrepancies. I presented the benchmark data to the team and proposed a hybrid architecture: using Gemini strictly for semantic schema extraction, followed by an exact, deterministic Python mathematical rule-check engine.
* **Result**: My teammate immediately supported the data-backed approach. The hybrid engine achieved 100% mathematical verification accuracy with zero hallucinations and reduced verification latency by 85%.

### Question 2: *"Describe a situation where you had to work under extreme ambiguity without complete specifications."*
* **Situation**: In my freelance engagement for the Warehouse PathMapper project, the client operated a massive warehouse facility but did not have formal CAD diagrams or standardized grid coordinates.
* **Task**: I was tasked with building an optimal routing engine for 10,000 locations without clear spatial mapping parameters or obstruction coordinates.
* **Action**: Rather than waiting for complete documentation, I took the initiative as DRI. I conducted structured interviews with warehouse floor operators to identify physical routing constraints (one-way aisles, forklift turning radii, packing station choke points). I translated these physical constraints into a configurable coordinate grid abstraction and built an interactive visual prototype in under a week to validate operational assumptions directly with the client.
* **Result**: The client verified the spatial model within two iterations. The resulting heuristic routing engine computed optimal paths through 10,000+ points in under 0.5 seconds on a standard CPU.

### Question 3: *"Why do you want to join Apple over other big tech or financial technology firms?"*
* **Candidate Response**:
  > *"Most technology companies treat hardware and software as separate commodities, often relying on massive cloud infrastructure to brute-force solve computational problems at the expense of user privacy. Apple is unique because it designs the complete vertical stack: custom Apple Silicon, Darwin OS internals, Core ML compilers, and end-user hardware. My dual background — B.Tech in Computer Science and M.Tech in Signal Processing — makes this hardware-software integration natural for me. I want to build on-device intelligence and automation frameworks where algorithmic optimization, memory efficiency, and battery life directly impact hundreds of millions of users without compromising their personal privacy."*

---

## 3. High-Impact Questions to Ask Your Apple Interviewer
At the end of your interview, ask questions that demonstrate strategic insight:
1. *"How does your team navigate the trade-off between on-device ANE execution constraints and Private Cloud Compute for emerging multimodal features?"*
2. *"As Apple software continues to scale across heterogeneous silicon (M-series, A-series, S-series), how do your automation test harnesses ensure deterministic performance regression detection across such diverse hardware targets?"*
3. *"What does exceptional ownership look like for an intern operating as a DRI in your organization during the first 90 days?"*
"""
}

# =============================================================================
# MODULE 07: Quick Reference (CheatSheet)
# =============================================================================
modules_data["07_Quick_Reference"] = {
    "title": "07: Rapid Recall CheatSheet",
    "prev_link": "06_Managerial_and_HR.html",
    "prev_title": "06: Apple Culture & Values",
    "next_link": "README.html",
    "next_title": "3-Day Study Roadmap",
    "markdown": """# 07: Rapid Recall CheatSheet

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
* **Quantization**: INT4 / INT8 reducing model memory footprint from $\\sim 12\\text{GB}$ (FP32) to $\\le 2\\text{GB}$.
* **LoRA Rank Equation**:
$$\\Delta W = B \\cdot A, \\quad B \\in \\mathbb{R}^{d \\times r}, A \\in \\mathbb{R}^{r \\times k} \\quad (r \\ll \\min(d, k))$$
* **Private Cloud Compute (PCC)**: Custom Apple Silicon nodes, cryptographic attestations, zero data logging.

---

## 3. SDET & Testing Rapid Reference

* **Test Pyramid**: $70\\%$ Unit Tests $\\to$ $20\\%$ Integration/API Tests $\\to$ $10\\%$ UI Tests.
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
* **PathMapper**: 10,000×10,000 grid, 10,000+ points in $<0.5\\text{s}$, spatial heuristic search.
* **Uplan**: Multi-agent LangGraph with Gemini 2.5 Pro, 85% workload reduction, 98% token compression.
* **Alternative Data Radar**: Automated scraping backend with Bright Data proxy routing, 0–100 health score in SQL.
"""
}

# =============================================================================
# MODULE: README (3-Day Study Roadmap)
# =============================================================================
modules_data["README"] = {
    "title": "3-Day Study Roadmap: Apple Recruitment",
    "prev_link": "07_Quick_Reference.html",
    "prev_title": "07: Rapid Recall CheatSheet",
    "next_link": "index.html",
    "next_title": "Overview & Hub",
    "markdown": """# 3-Day Intensive Study Roadmap: Apple Recruitment

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
"""
}

# =============================================================================
# INDEX HUB PAGE CONTENT
# =============================================================================
index_html_content = """
<div style="margin-bottom: 2rem;">
  <div style="display: inline-block; padding: 4px 12px; background: rgba(0, 113, 227, 0.12); border: 1px solid #0071e3; border-radius: 9999px; font-size: 0.85rem; font-weight: 700; color: #0071e3; margin-bottom: 0.75rem;">
    ON-CAMPUS RECRUITMENT • NIT ROURKELA 2027
  </div>
  <h1 style="font-size: 2.2rem; font-weight: 800; margin: 0 0 0.5rem 0; letter-spacing: -0.02em;">
    Apple Recruitment Preparation Portal
  </h1>
  <p style="font-size: 1.05rem; color: var(--text-muted); margin: 0;">
    Roles: <strong>AI & ML and Software Development Engineering Intern</strong> & <strong>SDET Intern</strong><br>
    Package: <strong>80 LPA CTC on PPO Conversion</strong> • <strong>₹1,05,000 / month Stipend (1.05 LPM)</strong>
  </p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-bottom: 2.5rem;">
  <a href="00_START_HERE.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 00</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Company & Role Intel</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Apple Intelligence, DRI philosophy, IS&T, 80 LPA CTC breakdown, and campus hiring stages.</p>
    </div>
  </a>

  <a href="01_Online_Test.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 01</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Signature OA Problems</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">5 Signature coding problems: LRU Cache, String Compression, Word Break, Task Scheduler, Jump Game.</p>
    </div>
  </a>

  <a href="02_Technical_Rounds.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 02</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Systems, Memory & OS</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">ARC vs GC, C++ smart pointers, vtable layout, concurrency, false sharing, socket multiplexing.</p>
    </div>
  </a>

  <a href="03_Domain_Deep_Dive.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 03</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Apple AI & SDET Infra</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">On-device ~3B models, Private Cloud Compute, Core ML, Page Object Model, and flaky test mitigation.</p>
    </div>
  </a>

  <a href="04_Candidate_Resume_Grilling.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 04</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Resume Defense & Traps</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Defending PathMapper (10k grid), Uplan multi-agent pipeline, and Alternative Data Radar.</p>
    </div>
  </a>

  <a href="05_System_Design_or_HIL.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 05</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">LLD & Test Architecture</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">On-Device Inference Pipeline & Distributed Automated Test Execution Harness with Quarantine.</p>
    </div>
  </a>

  <a href="06_Managerial_and_HR.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 06</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Apple Culture & Values</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Directly Responsible Individual (DRI), craftsmanship, privacy by design, and behavioral STAR stories.</p>
    </div>
  </a>

  <a href="07_Quick_Reference.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Module 07</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">Rapid Recall CheatSheet</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">C++ memory cheat sheet, Python test fixtures, Core ML equations, and candidate metrics.</p>
    </div>
  </a>

  <a href="README.html" style="text-decoration: none; color: inherit;">
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; transition: transform 0.15s, border-color 0.15s;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #0071e3; text-transform: uppercase;">Study Guide</span>
      <h3 style="margin: 6px 0 8px 0; font-size: 1.15rem;">3-Day Study Roadmap</h3>
      <p style="margin: 0; font-size: 0.88rem; color: var(--text-muted);">Hour-by-hour preparation schedule for coding, systems, domain, resume defense, and HR.</p>
    </div>
  </a>
</div>
"""

def main():
    print("Building Apple Interview Preparation Suite...")
    for key, mod in modules_data.items():
        md_file = os.path.join(BASE_DIR, f"{key}.md")
        html_file = os.path.join(BASE_DIR, f"{key}.html")

        # 1. Write Markdown file
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(mod["markdown"])
        print(f"  [MD] Created {key}.md")

        # 2. Render Markdown to HTML
        body_html = markdown.markdown(
            mod["markdown"],
            extensions=["fenced_code", "tables", "nl2br"]
        )

        # Wrap tables in responsive table-wrapper
        body_html = body_html.replace("<table>", '<div class="table-wrapper"><table>').replace("</table>", '</table></div>')

        full_html = render_apple_page(
            title=mod["title"],
            active_page=f"{key}.html",
            content_html=body_html,
            prev_link=mod["prev_link"],
            prev_title=mod["prev_title"],
            next_link=mod["next_link"],
            next_title=mod["next_title"]
        )

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"  [HTML] Rendered {key}.html")

    # Render index.html hub page
    index_file = os.path.join(BASE_DIR, "index.html")
    index_full_html = render_apple_page(
        title="Overview & Hub • Apple Interview Preparation",
        active_page="index.html",
        content_html=index_html_content,
        prev_link="../index.html",
        prev_title="All Companies Hub",
        next_link="00_START_HERE.html",
        next_title="00: Company Deep Dive"
    )
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_full_html)
    print("  [HUB] Rendered index.html")

    print("\nAll Apple interview preparation modules generated successfully!")

if __name__ == "__main__":
    main()
