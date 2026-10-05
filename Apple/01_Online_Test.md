# 01: Apple Signature OA Coding Problems

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

* **Complexity**: Time: $O(1)$ for both `get` and `put`. Space: $O(\text{capacity})$.

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
* **Trie-Optimized DP**: Insert all dictionary words into a Prefix Trie. For each starting index $i$ where `dp[i] == true`, traverse the Trie starting from `s[i]`. If a path hits an `is_word` terminal at character index $j$, set `dp[j + 1] = true`. This prevents redundant substring allocations and achieves $O(n \cdot L)$ where $L$ is the maximum word length.

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
* Model dependencies as a Directed Graph: edge $v \to u$.
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

* **Complexity**: Time: $O(V + E)$ where $V = \text{numTasks}$ and $E = \text{len(prerequisites)}$. Space: $O(V + E)$.

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
