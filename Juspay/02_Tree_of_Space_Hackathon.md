# 02: Tree of Space Hackathon ? Juspay Technologies

---

## 1. Problem Formulation & Exact API Specification

Let the resource hierarchy be modeled as a rooted, directed, acyclic $N$-ary tree $T = (V, E)$, where $|V| = N$ and the root is $r \in V$.
For any node $u \in V$:
- $\text{depth}(u)$ is the path length from $r$ to $u$, with $\text{depth}(r) = 0$. The tree height is $H = \max_{u \in V} \text{depth}(u) \le N$.
- $\mathcal{A}(u) = \{ v \in V \mid v \text{ lies on the unique simple path from } r \text{ to } u, v \ne u \}$ denotes the set of **ancestors** of $u$. $|\mathcal{A}(u)| = \text{depth}(u) \le H$.
- $\mathcal{D}(u) = \{ v \in V \mid u \in \mathcal{A}(v) \}$ denotes the set of **descendants** of $u$.
- $\mathcal{C}(u) = \{ v \in V \mid (u, v) \in E \}$ denotes the immediate children of $u$.

Each node $u \in V$ maintains the dynamic state tuple $\langle \sigma(u), \omega(u), c(u), \mathcal{L}(u) \rangle$:
1. $\sigma(u) \in \{\text{UNLOCKED}, \text{LOCKED}\}$: Locking state.
2. $\omega(u) \in \mathbb{N} \cup \{\bot\}$: Owner identity (`uid`), where $\bot$ denotes unowned.
3. $c(u) = |\{ v \in \mathcal{D}(u) \mid \sigma(v) = \text{LOCKED} \}| \in \mathbb{N}_0$: Descendant lock counter.
4. $\mathcal{L}(u) = \{ v \in \mathcal{D}(u) \mid \sigma(v) = \text{LOCKED} \} \subseteq \mathcal{D}(u)$: Set of locked descendant pointers. Note that $|\mathcal{L}(u)| = c(u)$.

### 1.1 Safety Invariants
At all times $t \ge 0$, the system must satisfy the following invariants:

$$\textbf{Invariant 1 (Ancestor-Descendant Exclusivity): } \forall u, v \in V \text{ with } u \in \mathcal{A}(v), \quad \neg(\sigma(u) = \text{LOCKED} \land \sigma(v) = \text{LOCKED})$$

$$\textbf{Invariant 2 (Counter-Set Consistency): } \forall u \in V, \quad c(u) = |\mathcal{L}(u)| = \sum_{v \in \mathcal{C}(u)} \left( \mathbb{I}(\sigma(v) = \text{LOCKED}) + c(v) \right)$$

$$\textbf{Invariant 3 (Identity Ownership): } \forall u \in V, \quad \sigma(u) = \text{LOCKED} \implies \omega(u) \ne \bot$$

$$\textbf{Invariant 4 (Subtree Disjointness): } \text{If } \sigma(u) = \text{LOCKED} \text{ and } \sigma(v) = \text{LOCKED} \ (u \ne v), \text{ then } \mathcal{D}(u) \cap \mathcal{D}(v) = \emptyset \land u \notin \mathcal{A}(v) \land v \notin \mathcal{A}(u)$$

---

## 2. API Semantics & Asymptotic Complexity Proofs

### 2.1 `lock(u, uid) -> bool`
- **Preconditions**:
  1. $\sigma(u) = \text{UNLOCKED}$
  2. $c(u) = 0 \iff \forall v \in \mathcal{D}(u), \sigma(v) = \text{UNLOCKED}$ ($O(1)$ check)
  3. $\forall a \in \mathcal{A}(u), \sigma(a) = \text{UNLOCKED}$ ($O(\text{depth})$ check)
- **State Transition**:
  - $\sigma(u) \leftarrow \text{LOCKED}, \omega(u) \leftarrow \text{uid}$
  - $\forall a \in \mathcal{A}(u): c(a) \leftarrow c(a) + 1, \quad \mathcal{L}(a) \leftarrow \mathcal{L}(a) \cup \{ u \}$
- **Worst-Case Complexity**: **$O(\text{depth}(u)) = O(H)$**.

### 2.2 `unlock(u, uid) -> bool`
- **Preconditions**:
  1. $\sigma(u) = \text{LOCKED}$
  2. $\omega(u) = \text{uid}$
- **State Transition**:
  - $\sigma(u) \leftarrow \text{UNLOCKED}, \omega(u) \leftarrow \bot$
  - $\forall a \in \mathcal{A}(u): c(a) \leftarrow c(a) - 1, \quad \mathcal{L}(a) \leftarrow \mathcal{L}(a) \setminus \{ u \}$
- **Worst-Case Complexity**: **$O(\text{depth}(u)) = O(H)$**.

### 2.3 `upgradeLock(u, uid) -> bool`
- **Preconditions**:
  1. $\sigma(u) = \text{UNLOCKED}$
  2. $c(u) > 0$ (has at least 1 locked descendant)
  3. $\forall v \in \mathcal{L}(u), \omega(v) = \text{uid}$ (all locked descendants locked by `uid`)
  4. $\forall a \in \mathcal{A}(u), \sigma(a) = \text{UNLOCKED}$ (no locked ancestors)
- **State Transition**:
  - Let $k = c(u) = |\mathcal{L}(u)|$.
  - Unlock all $v \in \mathcal{L}(u)$ and clear descendant entries from intermediate nodes.
  - Set $\sigma(u) \leftarrow \text{LOCKED}, \omega(u) \leftarrow \text{uid}, c(u) \leftarrow 0, \mathcal{L}(u) \leftarrow \emptyset$.
  - For ancestors $a \in \mathcal{A}(u)$: $c(a) \leftarrow c(a) - k + 1$, replace descendant IDs with $\{ u \}$.
- **Worst-Case Complexity**: **$O(\text{depth}(u) + k)$**.

---

## 3. Concurrency Edge Cases & Top-Down Deadlock Freedom

### 3.1 Concurrency Edge Cases
1. **Sibling vs. Sibling Race**: Threads simultaneously lock two sibling nodes, creating a read-modify-write lost update race on the parent's $c(\text{parent})$.
2. **Ancestor vs. Descendant Split-Brain**: Thread 1 calls `lock(P)` while Thread 2 concurrently calls `lock(C)`. Without atomic exclusion, both check validity simultaneously and both lock, violating Invariant 1.
3. **AB-BA Deadlock**: Thread 1 traverses Bottom-Up (Leaf to Root) while Thread 2 traverses Top-Down (Root to Leaf), causing Coffman circular wait.

### 3.2 Canonical Lock Ordering Protocol
To prevent deadlocks without a bottleneck global lock, all mutex acquisitions follow a strict total order $\prec$:
$$u \prec v \iff (\text{depth}(u) < \text{depth}(v)) \lor (\text{depth}(u) = \text{depth}(v) \land \text{id}(u) < \text{id}(v))$$
**Theorem**: Sorted lock acquisition along $\prec$ guarantees that the Wait-For Graph $G_W$ is acyclic. Deadlock is mathematically impossible.

---

## 4. Production C++20 Thread-Safe Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <mutex>
#include <algorithm>
#include <memory>

class ThreadSafeTreeOfSpace {
public:
    struct Node {
        int id;
        std::string name;
        int depth;
        Node* parent;
        std::vector<Node*> children;

        bool isLocked;
        int lockedBy;
        int lockedDescendantCount;
        std::unordered_set<Node*> lockedDescendants;

        mutable std::mutex mtx;

        Node(int id, std::string name, int depth, Node* parent = nullptr)
            : id(id), name(std::move(name)), depth(depth), parent(parent),
              isLocked(false), lockedBy(-1), lockedDescendantCount(0) {}
    };

private:
    std::vector<std::unique_ptr<Node>> allNodes;
    std::unordered_map<std::string, Node*> nameToNode;

    std::vector<Node*> getAncestors(Node* node) {
        std::vector<Node*> ancestors;
        Node* curr = node->parent;
        while (curr != nullptr) {
            ancestors.push_back(curr);
            curr = curr->parent;
        }
        return ancestors;
    }

    std::vector<std::unique_lock<std::mutex>> acquireLocksSorted(std::vector<Node*> nodes) {
        // Sort strictly by depth ascending, then id ascending
        std::sort(nodes.begin(), nodes.end(), [](Node* a, Node* b) {
            if (a->depth != b->depth) return a->depth < b->depth;
            return a->id < b->id;
        });
        nodes.erase(std::unique(nodes.begin(), nodes.end()), nodes.end());

        std::vector<std::unique_lock<std::mutex>> locks;
        locks.reserve(nodes.size());
        for (Node* n : nodes) {
            locks.emplace_back(n->mtx);
        }
        return locks;
    }

public:
    ThreadSafeTreeOfSpace(const std::vector<std::string>& names, int m) {
        int n = names.size();
        allNodes.reserve(n);
        for (int i = 0; i < n; ++i) {
            int parentIdx = (i == 0) ? -1 : (i - 1) / m;
            Node* parentNode = (parentIdx == -1) ? nullptr : allNodes[parentIdx].get();
            int depth = (parentNode == nullptr) ? 0 : parentNode->depth + 1;
            allNodes.push_back(std::make_unique<Node>(i, names[i], depth, parentNode));
            nameToNode[names[i]] = allNodes.back().get();
            if (parentNode) {
                parentNode->children.push_back(allNodes.back().get());
            }
        }
    }

    bool lock(const std::string& name, int uid) {
        auto it = nameToNode.find(name);
        if (it == nameToNode.end()) return false;
        Node* target = it->second;

        std::vector<Node*> nodesToLock = getAncestors(target);
        nodesToLock.push_back(target);

        auto locks = acquireLocksSorted(nodesToLock);

        if (target->isLocked) return false;
        if (target->lockedDescendantCount > 0) return false;

        for (Node* anc : getAncestors(target)) {
            if (anc->isLocked) return false;
        }

        target->isLocked = true;
        target->lockedBy = uid;

        for (Node* anc : getAncestors(target)) {
            anc->lockedDescendantCount++;
            anc->lockedDescendants.insert(target);
        }

        return true;
    }

    bool unlock(const std::string& name, int uid) {
        auto it = nameToNode.find(name);
        if (it == nameToNode.end()) return false;
        Node* target = it->second;

        std::vector<Node*> nodesToLock = getAncestors(target);
        nodesToLock.push_back(target);

        auto locks = acquireLocksSorted(nodesToLock);

        if (!target->isLocked || target->lockedBy != uid) return false;

        target->isLocked = false;
        target->lockedBy = -1;

        for (Node* anc : getAncestors(target)) {
            anc->lockedDescendantCount--;
            anc->lockedDescendants.erase(target);
        }

        return true;
    }

    bool upgradeLock(const std::string& name, int uid) {
        auto it = nameToNode.find(name);
        if (it == nameToNode.end()) return false;
        Node* target = it->second;

        std::vector<Node*> pathNodes = getAncestors(target);
        pathNodes.push_back(target);

        auto pathLocks = acquireLocksSorted(pathNodes);

        if (target->isLocked || target->lockedDescendantCount == 0) return false;
        for (Node* anc : getAncestors(target)) {
            if (anc->isLocked) return false;
        }
        for (Node* desc : target->lockedDescendants) {
            if (desc->lockedBy != uid) return false;
        }

        std::vector<Node*> allAffected = pathNodes;
        for (Node* desc : target->lockedDescendants) {
            allAffected.push_back(desc);
        }

        pathLocks.clear();
        auto fullLocks = acquireLocksSorted(allAffected);

        if (target->isLocked || target->lockedDescendantCount == 0) return false;
        for (Node* anc : getAncestors(target)) {
            if (anc->isLocked) return false;
        }
        for (Node* desc : target->lockedDescendants) {
            if (desc->lockedBy != uid) return false;
        }

        std::vector<Node*> descendantsToUnlock(target->lockedDescendants.begin(),
                                               target->lockedDescendants.end());
        int k = descendantsToUnlock.size();

        for (Node* desc : descendantsToUnlock) {
            desc->isLocked = false;
            desc->lockedBy = -1;
            Node* curr = desc->parent;
            while (curr != target && curr != nullptr) {
                curr->lockedDescendantCount--;
                curr->lockedDescendants.erase(desc);
                curr = curr->parent;
            }
        }

        target->isLocked = true;
        target->lockedBy = uid;
        target->lockedDescendantCount = 0;
        target->lockedDescendants.clear();

        for (Node* anc : getAncestors(target)) {
            for (Node* desc : descendantsToUnlock) {
                anc->lockedDescendants.erase(desc);
            }
            anc->lockedDescendants.insert(target);
            anc->lockedDescendantCount -= (k - 1);
        }

        return true;
    }
};
```
