# 01: Online Test Graph Mastery ? Juspay Technologies

---

## 1. Juspay OA Graph Architecture: The "Functional Graph" Paradigm

All three classic Juspay OA graph problems operate on **Directed Functional Graphs** (graphs where every vertex has an out-degree of at most 1).
Formally: $G = (V, E)$ where $|V| = N$ and $E = \{ (i, \text{edges}[i]) \mid \text{edges}[i] \ne -1 \}$.

```
Typical Functional Graph Component:
[Node 0] ??? [Node 1] ??? [Node 2] ??? [Node 5]
                           ?      ?
                           ?      ?
                        [Node 3] ??
(Trees feeding into a single directed cycle, plus isolated nodes)
```

**Key Mathematical Properties of Functional Graphs:**
1. Every weakly-connected component contains **at most one directed cycle**.
2. All nodes not in the cycle form directed trees rooted on the cycle (directed towards the cycle).
3. Traversal from any node either terminates at a dead-end (`-1`) or enters a cycle within at most $N$ steps.
4. Optimal time complexity for all queries is strictly **$O(N)$**; Space is strictly **$O(N)$**.

---

## 2. Problem 1: Maximum Weight Node

### 2.1 Problem Statement
You are given a directed graph of $N$ nodes (indexed $0$ to $N-1$). Each node $i$ has at most one outgoing edge directed to $\text{edges}[i]$. If $\text{edges}[i] == -1$, node $i$ has no outgoing edge.
The **weight** of a node $u$ is defined as the sum of all node indices $i$ that have a direct edge pointing to $u$:
$$\text{Weight}(u) = \sum_{i \in V, \text{edges}[i] = u} i$$
Find the node with the **maximum weight**. If multiple nodes have the same maximum weight, return the node with the **maximum index**. If no node has incoming edges, return `-1` or `0` (handle both platform conventions).

### 2.2 Optimal Algorithm & Complexity
- **Time Complexity**: $O(N)$ ? single linear sweep through `edges`.
- **Auxiliary Space**: $O(N)$ ? array of size $N$ to accumulate weights.

### 2.3 Production C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int maxWeightCell(int n, const std::vector<int>& edges) {
    // Accumulator for incoming edge source indices
    std::vector<long long> weights(n, 0);

    for (int src = 0; src < n; ++src) {
        int dst = edges[src];
        if (dst >= 0 && dst < n) {
            weights[dst] += src;
        }
    }

    long long maxWeight = -1;
    int bestNode = -1;

    // Iterate 0 to n-1. In case of ties, select the larger index
    for (int i = 0; i < n; ++i) {
        if (weights[i] >= maxWeight) {
            maxWeight = weights[i];
            bestNode = i;
        }
    }

    return (maxWeight == 0 && bestNode == -1) ? -1 : bestNode;
}

int main() {
    std::vector<int> edges = {4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21};
    int n = edges.size();
    std::cout << "Max Weight Node: " << maxWeightCell(n, edges) << std::endl;
    return 0;
}
```

### 2.4 Production Python 3 Implementation
```python
from typing import List

def max_weight_cell(n: int, edges: List[int]) -> int:
    weights = [0] * n
    for src in range(n):
        dst = edges[src]
        if 0 <= dst < n:
            weights[dst] += src

    max_weight = -1
    best_node = -1

    for node in range(n):
        if weights[node] >= max_weight:
            max_weight = weights[node]
            best_node = node

    return best_node
```

---

## 3. Problem 2: Nearest Meeting Cell (Shortest Meeting Point)

### 3.1 Problem Statement
You are given a directed graph of $N$ nodes (each node has at most 1 outgoing edge `edges[i]`).
Given two node indices $C_1$ and $C_2$, find a common node $u$ reachable from both $C_1$ and $C_2$ such that the maximum distance from either starting node to $u$ is minimized:
$$\min_{u \in \text{Reachable}(C_1) \cap \text{Reachable}(C_2)} \max(d(C_1, u), d(C_2, u))$$
If multiple nodes have the same minimum max-distance, return the node with the **smallest index**. If no such node exists, return `-1`.

### 3.2 Algorithm
1. Compute the distance array `dist1` from $C_1$ using a single path traversal. Since each node has $\le 1$ outgoing edge, follow the chain until reaching `-1` or encountering an already-visited node (cycle).
2. Compute the distance array `dist2` from $C_2$ similarly.
3. Iterate $u = 0 \dots N-1$. If both `dist1[u] != -1` and `dist2[u] != -1`, evaluate $\max(\text{dist1}[u], \text{dist2}[u])$. Maintain the minimum distance and smallest index.

### 3.3 Complexity
- **Time**: $O(N)$ ? exactly two traversals of length at most $N$.
- **Space**: $O(N)$ ? two distance vectors of size $N$.

### 3.4 Production C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

std::vector<int> getDistances(int startNode, int n, const std::vector<int>& edges) {
    std::vector<int> dist(n, -1);
    std::vector<bool> visited(n, false);

    int curr = startNode;
    int d = 0;

    while (curr != -1 && !visited[curr]) {
        visited[curr] = true;
        dist[curr] = d++;
        curr = edges[curr];
    }
    return dist;
}

int nearestMeetingCell(int n, const std::vector<int>& edges, int c1, int c2) {
    std::vector<int> dist1 = getDistances(c1, n, edges);
    std::vector<int> dist2 = getDistances(c2, n, edges);

    int minMaxDist = INT_MAX;
    int bestNode = -1;

    for (int i = 0; i < n; ++i) {
        if (dist1[i] != -1 && dist2[i] != -1) {
            int currentMax = std::max(dist1[i], dist2[i]);
            if (currentMax < minMaxDist) {
                minMaxDist = currentMax;
                bestNode = i;
            }
        }
    }

    return bestNode;
}
```

### 3.5 Production Python 3 Implementation
```python
from typing import List

def get_distances(start_node: int, n: int, edges: List[int]) -> List[int]:
    dist = [-1] * n
    visited = [False] * n
    curr = start_node
    d = 0
    while curr != -1 and not visited[curr]:
        visited[curr] = True
        dist[curr] = d
        d += 1
        curr = edges[curr]
    return dist

def nearest_meeting_cell(n: int, edges: List[int], c1: int, c2: int) -> int:
    dist1 = get_distances(c1, n, edges)
    dist2 = get_distances(c2, n, edges)

    min_max_dist = float('inf')
    best_node = -1

    for i in range(n):
        if dist1[i] != -1 and dist2[i] != -1:
            max_d = max(dist1[i], dist2[i])
            if max_d < min_max_dist:
                min_max_dist = max_d
                best_node = i

    return best_node
```

---

## 4. Problem 3: Largest Sum Cycle

### 4.1 Problem Statement
You are given a directed graph of $N$ nodes where each node has at most one outgoing edge `edges[i]`.
Find the **maximum sum of node values/indices in any directed cycle**. If no cycle exists, return `-1`.

### 4.2 Algorithm (In-Degree Elimination & Cycle Summation)
A functional graph consists of trees rooted on cycles.
1. **Kahn's Topological Trimming**: Compute the in-degree of all nodes. Nodes with `in_degree == 0` cannot be part of any cycle. Push them to a BFS queue.
2. When dequeuing node $u$, decrement the in-degree of its successor $v = \text{edges}[u]$. If `in_degree[v] == 0`, enqueue $v$.
3. After the queue is empty, **all remaining nodes with in-degree > 0 belong strictly to cycles**.
4. Iterate through unvisited nodes with `in_degree > 0`. Follow each cycle, summing node indices, and mark nodes as visited. Track the maximum cycle sum.

### 4.3 Complexity
- **Time**: $O(N)$ ? every node is processed at most twice.
- **Space**: $O(N)$ ? in-degree and visited arrays.

### 4.4 Production C++20 Implementation
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

long long largestSumCycle(int n, const std::vector<int>& edges) {
    std::vector<int> inDegree(n, 0);

    for (int i = 0; i < n; ++i) {
        if (edges[i] != -1) {
            inDegree[edges[i]]++;
        }
    }

    std::queue<int> q;
    for (int i = 0; i < n; ++i) {
        if (inDegree[i] == 0) {
            q.push(i);
        }
    }

    std::vector<bool> visited(n, false);

    // Kahn's algorithm eliminates all non-cycle paths
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        visited[u] = true;
        int v = edges[u];
        if (v != -1) {
            inDegree[v]--;
            if (inDegree[v] == 0) {
                q.push(v);
            }
        }
    }

    long long maxCycleSum = -1;

    // Remaining unvisited nodes belong strictly to cycles
    for (int i = 0; i < n; ++i) {
        if (!visited[i] && inDegree[i] > 0) {
            long long currentCycleSum = 0;
            int curr = i;

            while (!visited[curr]) {
                visited[curr] = true;
                currentCycleSum += curr;
                curr = edges[curr];
            }

            maxCycleSum = std::max(maxCycleSum, currentCycleSum);
        }
    }

    return maxCycleSum;
}

int main() {
    std::vector<int> edges = {4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21};
    int n = edges.size();
    std::cout << "Largest Sum Cycle: " << largestSumCycle(n, edges) << std::endl;
    return 0;
}
```

### 4.5 Production Python 3 Implementation
```python
from typing import List
from collections import deque

def largest_sum_cycle(n: int, edges: List[int]) -> int:
    in_degree = [0] * n
    for dst in edges:
        if dst != -1:
            in_degree[dst] += 1

    q = deque([i for i in range(n) if in_degree[i] == 0])
    visited = [False] * n

    while q:
        u = q.popleft()
        visited[u] = True
        v = edges[u]
        if v != -1:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    max_cycle_sum = -1

    for i in range(n):
        if not visited[i] and in_degree[i] > 0:
            cycle_sum = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                cycle_sum += curr
                curr = edges[curr]
            max_cycle_sum = max(max_cycle_sum, cycle_sum)

    return max_cycle_sum
```
