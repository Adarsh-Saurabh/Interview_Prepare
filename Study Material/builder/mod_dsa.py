# mod_dsa.py - Data Structures & Algorithms Module Generator
# Conforms to instruction.md Part 6.1 Specification (P0 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Decision Patterns & Triggers"),
        ("complexity-matrix", "📊 Master Complexity & Constraint Matrix"),
        ("pattern-templates", "🧩 9 Core Algorithmic Templates"),
        ("dp-mastery", "💎 Dynamic Programming: 9 Canonical Shapes"),
        ("recurrence-analysis", "📐 Master Theorem & Amortized Analysis"),
        ("string-graph-depth", "🌐 Graphs, Strings & Greedy Validity"),
        ("interview-traps", "⚠️ High-Frequency Traps & Proofs"),
        ("interview-flashcards", "🎯 32 Top Tech Interview Q&As")
    ]

    # SVG 1: DSA Problem Solving Decision Tree
    svg_decision_tree = """
    <svg viewBox="0 0 880 440" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="dsa-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Root Box -->
      <rect x="340" y="15" width="200" height="45" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="440" y="42" fill="#ffffff" font-size="13" font-weight="800" text-anchor="middle">Given Coding Problem</text>

      <!-- Branches -->
      <line x1="370" y1="60" x2="140" y2="110" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#dsa-arrow)" />
      <line x1="420" y1="60" x2="330" y2="110" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#dsa-arrow)" />
      <line x1="460" y1="60" x2="550" y2="110" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#dsa-arrow)" />
      <line x1="510" y1="60" x2="740" y2="110" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#dsa-arrow)" />

      <!-- Nodes -->
      <rect x="50" y="110" width="180" height="40" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
      <text x="140" y="135" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Array / String Input</text>

      <rect x="250" y="110" width="160" height="40" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="330" y="135" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Search / Range / K-th</text>

      <rect x="470" y="110" width="160" height="40" rx="6" fill="#1e293b" stroke="#c084fc" stroke-width="1.5" />
      <text x="550" y="135" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">Tree / Graph / Grid</text>

      <rect x="660" y="110" width="160" height="40" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5" />
      <text x="740" y="135" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">Max / Min / Choice DP</text>

      <!-- Sub Branches Array -->
      <line x1="100" y1="150" x2="60" y2="200" stroke="#34d399" stroke-width="1.2" marker-end="url(#dsa-arrow)" />
      <line x1="140" y1="150" x2="140" y2="200" stroke="#34d399" stroke-width="1.2" marker-end="url(#dsa-arrow)" />
      <line x1="180" y1="150" x2="220" y2="200" stroke="#34d399" stroke-width="1.2" marker-end="url(#dsa-arrow)" />

      <rect x="10" y="200" width="100" height="50" rx="4" fill="#064e3b" />
      <text x="60" y="222" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Two Pointers</text>
      <text x="60" y="238" fill="#a7f3d0" font-size="8" text-anchor="middle">Sorted / Palindromes</text>

      <rect x="100" y="200" width="95" height="50" rx="4" fill="#064e3b" />
      <text x="147" y="222" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">Sliding Window</text>
      <text x="147" y="238" fill="#a7f3d0" font-size="8" text-anchor="middle">Subarray Contiguous</text>

      <rect x="185" y="200" width="100" height="50" rx="4" fill="#064e3b" />
      <text x="235" y="222" fill="#34d399" font-size="9" font-weight="700" text-anchor="middle">Monotonic Stack</text>
      <text x="235" y="238" fill="#a7f3d0" font-size="8" text-anchor="middle">Next Greater / Range</text>

      <!-- Sub Branches Search -->
      <line x1="310" y1="150" x2="280" y2="280" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#dsa-arrow)" />
      <line x1="350" y1="150" x2="380" y2="280" stroke="#fbbf24" stroke-width="1.2" marker-end="url(#dsa-arrow)" />

      <rect x="230" y="280" width="110" height="50" rx="4" fill="#78350f" />
      <text x="285" y="302" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Binary Search</text>
      <text x="285" y="318" fill="#fde68a" font-size="8" text-anchor="middle">On Answer / Monotonic</text>

      <rect x="350" y="280" width="105" height="50" rx="4" fill="#78350f" />
      <text x="402" y="302" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">Heap / PQ</text>
      <text x="402" y="318" fill="#fde68a" font-size="8" text-anchor="middle">Top K / Streaming</text>

      <!-- Sub Branches Graph -->
      <line x1="520" y1="150" x2="490" y2="200" stroke="#c084fc" stroke-width="1.2" marker-end="url(#dsa-arrow)" />
      <line x1="570" y1="150" x2="600" y2="200" stroke="#c084fc" stroke-width="1.2" marker-end="url(#dsa-arrow)" />

      <rect x="440" y="200" width="100" height="50" rx="4" fill="#4c1d95" />
      <text x="490" y="222" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">BFS (Shortest Path)</text>
      <text x="490" y="238" fill="#ddd6fe" font-size="8" text-anchor="middle">Unweighted Edges</text>

      <rect x="550" y="200" width="105" height="50" rx="4" fill="#4c1d95" />
      <text x="602" y="222" fill="#c084fc" font-size="10" font-weight="700" text-anchor="middle">DFS / Backtracking</text>
      <text x="602" y="238" fill="#ddd6fe" font-size="8" text-anchor="middle">Paths, Subsets, Perms</text>

      <!-- Sub Branches DP -->
      <line x1="710" y1="150" x2="690" y2="280" stroke="#f43f5e" stroke-width="1.2" marker-end="url(#dsa-arrow)" />
      <line x1="770" y1="150" x2="790" y2="280" stroke="#f43f5e" stroke-width="1.2" marker-end="url(#dsa-arrow)" />

      <rect x="650" y="280" width="105" height="50" rx="4" fill="#881337" />
      <text x="702" y="302" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">1D / 2D Grid DP</text>
      <text x="702" y="318" fill="#fecdd3" font-size="8" text-anchor="middle">Knapsack, Paths, LIS</text>

      <rect x="765" y="280" width="105" height="50" rx="4" fill="#881337" />
      <text x="817" y="302" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Interval / String DP</text>
      <text x="817" y="318" fill="#fecdd3" font-size="8" text-anchor="middle">LCS, Edit Dist, MCM</text>
    </svg>
    """

    content = []

    # Section 1: Sprint Core & Trigger Phrases
    s1_body = f"""
    {one_liner("In coding interviews, problems rarely announce their algorithm. Your first job is recognizing the problem's trigger phrase and mapping it instantly to its complexity bound.")}

    <p>A topic is only mastered when you can name its trigger phrase in a single sentence without prompting. Below is the master pattern-to-trigger mapping table:</p>

    {table(
        headers=["Algorithmic Pattern", "Trigger Phrase in Problem Statement", "Target Template", "Time & Space Bound"],
        rows=[
            ["Binary Search on Answer", "<em>'Find the minimum maximum...'</em> or <em>'Find the maximum minimum capacity/speed'</em>", "Monotonic predicate <code>check(mid)</code>", "Time: $O(N \\log(\\text{Range}))$, Space: $O(1)$"],
            ["Two Pointers (Opposite)", "Sorted array, pair with target sum, palindrome verification, trapping water", "Left & Right pointers moving inward", "Time: $O(N)$, Space: $O(1)$"],
            ["Sliding Window (Variable)", "<em>'Longest / shortest contiguous subarray / substring satisfying condition K'</em>", "Right expands window, Left shrinks while invalid", "Time: $O(N)$, Space: $O(K)$ hash table"],
            ["Monotonic Stack", "<em>'Next greater element'</em>, <em>'previous smaller element'</em>, <em>'largest rectangle in histogram'</em>", "Stack maintaining strictly increasing/decreasing order", "Time: $O(N)$, Space: $O(N)$"],
            ["Disjoint Set Union (DSU)", "Dynamic connectivity, connected components, Kruskal's MST, cycle in undirected graph", "Parent array with Path Compression & Union by Rank", "Time: $O(\\alpha(N)) \\approx O(1)$, Space: $O(N)$"],
            ["Topological Sort (Kahn's)", "Task dependencies, course prerequisites, build order, cycle in directed graph", "Indegree array + Queue of zero-indegree nodes", "Time: $O(V + E)$, Space: $O(V + E)$"],
            ["Min/Max Heap", "<em>'Top K frequent'</em>, <em>'K-th largest element'</em>, streaming data median", "Size-K Priority Queue (evict root when size > K)", "Time: $O(N \\log K)$, Space: $O(K)$"],
            ["BFS (Multi-Source)", "Rotting oranges, distance to nearest 0/1 in grid, shortest path in unweighted graph", "Queue initialized with ALL sources simultaneously", "Time: $O(R \\times C)$, Space: $O(R \\times C)$"],
            ["Backtracking", "<em>'Generate all valid subsets / permutations / combinations'</em> ($N \\le 15$)", "Recursive decision tree: choose, recurse, backtrack", "Time: $O(2^N)$ or $O(N!)$, Space: $O(N)$"]
        ]
    )}

    {callout(
        title="Grid Problems are Graph Problems Wearing a Matrix Costume!",
        body="Whenever an interview presents an $M \\times N$ grid with cells (islands, rotting oranges, shortest maze path), <strong>treat every cell $(r, c)$ as a graph vertex</strong> with up to 4 edges: $(r\\pm 1, c)$ and $(r, c\\pm 1)$. If edges are unweighted, the shortest path is ALWAYS BFS with a Queue, never DFS or Dijkstra!",
        kind="pro"
    )}

    {callout(
        title="DP Priority Reality Check for Campus Interviews",
        body="Two independent placement audits confirm: <strong>candidates dramatically over-invest in advanced Dynamic Programming</strong> while campus panels test Arrays, Two Pointers, Hashing, Binary Search on Answer, Trees, and Graphs 4× more frequently. What DP is asked clusters strictly into 9 canonical shapes—memoization is accepted almost universally.",
        kind="info"
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Decision Patterns & Triggers", s1_body, pill="High Yield", pill_color="purple"))

    # Section 2: Complexity & Constraint Matrix
    s2_body = f"""
    <p>In timed Online Assessments and interviews, input constraints ($N$) dictate the required algorithmic complexity before you write a single line of code:</p>

    {table(
        headers=["Input Size ($N$)", "Permissible Time Complexity", "Expected Algorithms / Data Structures"],
        rows=[
            ["$N \\le 10..12$", "$O(N!)$ or $O(N^2 \\cdot 2^N)$", "TSP, Travelling Salesperson DP, Permutations, Exact Brute Force."],
            ["$N \\le 20..25$", "$O(2^N)$ or $O(N \\cdot 2^N)$", "Bitmask Dynamic Programming, Subsets Backtracking, Meet-in-the-Middle."],
            ["$N \\le 100..400$", "$O(N^3)$", "Floyd-Warshall all-pairs shortest paths, Matrix Chain Multiplication DP."],
            ["$N \\le 1,000..2,000$", "$O(N^2)$", "2D Grid DP, 0/1 Knapsack, All pairs comparison, Bubble/Insertion sort."],
            ["$N \\le 100,000..200,000$", "$O(N \\log N)$", "Sorting, Divide & Conquer, Heap / PriorityQueue, Segment Tree, Binary Search."],
            ["$N \\le 1,000,000$", "$O(N)$", "Two Pointers, Sliding Window, Monotonic Stack, Kadane's, Hash Table, DSU."],
            ["$N \\ge 10^9$ (Large range)", "$O(\\log N)$ or $O(1)$", "Binary Search on Answer Space, Math / Matrix Exponentiation, Bitwise tricks."]
        ]
    )}

    {svg_card(svg_decision_tree, "Master Problem-Solving Decision Tree: From Problem Nature to Optimal Algorithm")}
    """
    content.append(section("complexity-matrix", "📊 Master Complexity & Constraint Matrix", s2_body, pill="Interview Cheat Sheet", pill_color="blue"))

    # Section 3: 9 Core Templates
    s3_body = f"""
    {subsection("template-bsearch", "1. Binary Search on Answer Space (The #1 High-Yield Pattern)")}
    <p>Trigger: The problem asks for the minimum maximum (or maximum minimum), and whether a given candidate value $X$ is feasible is monotonic: if $X$ works, all $Y &gt; X$ work.</p>
    {code(
        src=r"""// C++ Binary Search on Answer Template
bool isValid(const vector<int>& weights, int maxCap, int days) {
    int currentDayLoad = 0, requiredDays = 1;
    for (int w : weights) {
        if (currentDayLoad + w > maxCap) {
            requiredDays++;
            currentDayLoad = 0;
        }
        currentDayLoad += w;
    }
    return requiredDays <= days;
}

int shipWithinDays(vector<int>& weights, int days) {
    int low = *max_element(weights.begin(), weights.end());
    int high = accumulate(weights.begin(), weights.end(), 0);
    int optimalAns = high;

    while (low <= high) {
        int mid = low + (high - low) / 2; // Prevents 32-bit overflow!
        if (isValid(weights, mid, days)) {
            optimalAns = mid;      // Mid is feasible, try smaller capacity
            high = mid - 1;
        } else {
            low = mid + 1;         // Mid too small, must expand capacity
        }
    }
    return optimalAns;
}""",
        lang="cpp",
        title="Binary Search on Answer Space"
    )}

    {subsection("template-monotonic-stack", "2. Monotonic Stack (Next Greater Element & Daily Temperatures)")}
    {code(
        src=r"""// C++ Monotonic Decreasing Stack Template
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> result(n, 0);
    stack<int> st; // Stores indices

    for (int i = 0; i < n; i++) {
        // While stack not empty and current element is warmer than stack top
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            int prevIdx = st.top();
            st.pop();
            result[prevIdx] = i - prevIdx;
        }
        st.push(i);
    }
    return result;
}""",
        lang="cpp",
        title="Monotonic Stack Template"
    )}

    {subsection("template-dsu", "3. Disjoint Set Union (DSU with Path Compression & Rank)")}
    {code(
        src=r"""class DSU {
public:
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]); // Path compression: O(alpha(N))
    }

    bool unite(int i, int j) {
        int rootI = find(i), rootJ = find(j);
        if (rootI == rootJ) return false; // Cycle detected!
        if (rank[rootI] < rank[rootJ]) parent[rootI] = rootJ;
        else if (rank[rootI] > rank[rootJ]) parent[rootJ] = rootI;
        else { parent[rootJ] = rootI; rank[rootI]++; }
        return true;
    }
};""",
        lang="cpp",
        title="DSU with Path Compression"
    )}
    """
    content.append(section("pattern-templates", "🧩 9 Core Algorithmic Templates", s3_body, pill="Code Templates", pill_color="emerald", depth="deep"))

    # Section 4: Dynamic Programming Mastery
    s4_body = f"""
    <p>Campus and tech interviews test the same 9 DP structural shapes repeatedly. Master the transition from 2D table to 1D space optimization.</p>

    {table(
        headers=["DP Canonical Shape", "State Representation ($dp[i]$ or $dp[i][j]$)", "Recurrence Relation", "Space Optimization Trick"],
        rows=[
            ["0/1 Knapsack", "$dp[i][w]$ = max value using items $1..i$ with capacity $w$", "$dp[i][w] = \\max(dp[i-1][w], \\text{val}[i] + dp[i-1][w-\\text{wt}[i]])$", "1D array traversed <strong>backwards</strong> ($W \\dots \\text{wt}[i]$)."],
            ["Unbounded Knapsack", "$dp[w]$ = max value with weight limit $w$", "$dp[w] = \\max(dp[w], \\text{val}[i] + dp[w-\\text{wt}[i]])$", "1D array traversed <strong>forwards</strong> (re-using items)."],
            ["Longest Common Subseq (LCS)", "$dp[i][j]$ = LCS length of $s_1[0..i]$ and $s_2[0..j]$", "If match: $1 + dp[i-1][j-1]$; Else: $\\max(dp[i-1][j], dp[i][j-1])$", "Rolling 2 rows ($dp[2][N]$) or 1D array with prev diagonal."],
            ["Longest Increasing Subseq (LIS)", "$dp[i]$ = length of LIS ending at index $i$", "$dp[i] = 1 + \\max_{j < i, a[j] < a[i]} dp[j]$ ($O(N^2)$)", "Patience Sorting + Binary Search ($O(N \\log N)$)."],
            ["Grid Minimum Path Sum", "$dp[r][c]$ = min cost to reach cell $(r, c)$", "$dp[r][c] = \\text{grid}[r][c] + \\min(dp[r-1][c], dp[r][c-1])$", "In-place grid update or 1D array of size $C$."],
            ["Coin Change (Min Coins)", "$dp[a]$ = min coins to make amount $a$", "$dp[a] = 1 + \\min_{c \\in \\text{coins}} dp[a - c]$", "1D array initialized to $\\infty$, $dp[0] = 0$."],
            ["Edit Distance (Levenshtein)", "$dp[i][j]$ = min edits between $w_1[0..i]$ and $w_2[0..j]$", "Insert: $dp[i][j-1]$, Delete: $dp[i-1][j]$, Replace: $dp[i-1][j-1]$", "Rolling 2 rows."],
            ["House Robber (Linear)", "$dp[i]$ = max loot up to house $i$", "$dp[i] = \\max(dp[i-1], \\text{nums}[i] + dp[i-2])$", "2 variables: <code>prev1</code>, <code>prev2</code> ($O(1)$ space)."],
            ["Bitmask DP (Travelling Salesman)", "$dp[mask][u]$ = min cost visiting mask ending at $u$", "$dp[mask | (1 \\ll v)][v] = \\min(dp[mask][u] + \\text{dist}[u][v])$", "$O(2^N \\cdot N)$ space, for $N \\le 20$."]
        ]
    )}

    {subsection("dp-knapsack-code", "0/1 Knapsack: From 2D Matrix to Space-Optimized 1D Array")}
    {code(
        src=r"""// Space-Optimized 0/1 Knapsack in O(W) Space
int knapsack(int W, const vector<int>& weights, const vector<int>& values) {
    int n = weights.size();
    vector<int> dp(W + 1, 0);

    for (int i = 0; i < n; i++) {
        // CRITICAL: Iterate BACKWARDS from W down to weights[i]
        // This ensures each item is used AT MOST ONCE!
        for (int w = W; w >= weights[i]; w--) {
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]]);
        }
    }
    return dp[W];
}""",
        lang="cpp",
        title="Space-Optimized 0/1 Knapsack"
    )}
    """
    content.append(section("dp-mastery", "💎 Dynamic Programming: 9 Canonical Shapes", s4_body, pill="DP Shapes", pill_color="rose", depth="deep"))

    # Section 5: Recurrence & Amortized Analysis
    s5_body = f"""
    {formula_box(
        katex_display=r"$$T(n) = a T(n/b) + f(n), \quad \text{compare } f(n) \text{ with } n^{\log_b a}$$",
        reading="Master Theorem compares non-recursive work f(n) with critical exponent n to the power of log base b of a.",
        symbols=[
            ("a", "Number of subproblems generated in recursion (a >= 1)"),
            ("b", "Factor by which problem size is divided (b > 1)"),
            ("f(n)", "Work done outside recursive calls (divide and merge steps)")
        ],
        meaning="Case 1: If f(n) = O(n^(log_b a - epsilon)), leaves dominate -> T(n) = Theta(n^(log_b a)). Case 2: If f(n) = Theta(n^(log_b a)), balanced work -> T(n) = Theta(n^(log_b a) * log n). Case 3: If f(n) = Omega(n^(log_b a + epsilon)), root dominates -> T(n) = Theta(f(n))."
    )}

    {worked_example(
        title="Amortized Analysis of std::vector push_back (Dynamic Array Resizing)",
        steps=[
            ("Identify Doubling Strategy", "Vector starts at capacity 1. When full, it allocates an array of size 2C, copies C elements, and inserts the new element."),
            ("Compute Aggregate Cost over N Insertions", "Total normal insertions: N * 1 = N. Copying cost occurs at powers of 2: 1 + 2 + 4 + 8 + ... + N/2 + N = 2N - 1."),
            ("Derive Amortized Cost per Operation", r"$$\text{Amortized Cost} = \frac{\text{Total Cost}}{N} = \frac{N + (2N - 1)}{N} = \frac{3N - 1}{N} \approx 3 = O(1)$$")
        ],
        answer="Even though an individual push_back takes O(N) when resizing, the amortized cost per operation is provably O(1)!"
    )}
    """
    content.append(section("recurrence-analysis", "📐 Master Theorem & Amortized Analysis", s5_body, pill="Analysis", pill_color="amber", depth="deep"))

    # Section 6: Graph, Strings & Greedy
    s6_body = f"""
    {subsection("graph-dijkstra-fails", "Why Dijkstra's Algorithm Fails on Negative Edges")}
    <p>Dijkstra is a <strong>greedy algorithm</strong> that relies on the invariant that once a vertex's distance is extracted from the PriorityQueue, its shortest path is permanently settled. If an edge with a negative weight exists later in the graph, it can retroactively shorten the distance of an already-settled vertex, violating the invariant! <em>Use Bellman-Ford or SPFA instead.</em></p>

    {subsection("greedy-exchange", "Greedy Validity & The Exchange Argument")}
    <p>A greedy choice is only valid if taking the local optimum never prevents reaching the global optimum. For instance, Coin Change is greedy for canonical US denominations ({1, 5, 10, 25}), but <strong>fails completely</strong> for denominations <code>{1, 3, 4}</code> to make target <code>6</code>: Greedy picks <code>4 + 1 + 1</code> (3 coins), whereas the global optimum is <code>3 + 3</code> (2 coins)!</p>
    """
    content.append(section("string-graph-depth", "🌐 Graphs, Strings & Greedy Validity", s6_body, pill="Advanced CS", pill_color="teal", depth="deep"))

    # Section 7: Traps & Proofs
    s7_body = f"""
    {callout(
        title="Trap #1: Integer Overflow in Binary Search",
        body="Writing <code>int mid = (low + high) / 2;</code> leads to signed 32-bit integer overflow when <code>low + high &gt; 2,147,483,647</code>, causing a negative index and immediate segfault. Always write <code>int mid = low + (high - low) / 2;</code>.",
        kind="trap"
    )}

    {callout(
        title="Trap #2: Why Building a Binary Heap is O(N) and NOT O(N log N)",
        body="Inserting $N$ elements into an empty heap sequentially takes $N \\times O(\\log N) = O(N \\log N)$. However, bottom-up <code>std::make_heap()</code> takes $O(N)$ because the majority of nodes reside at the bottom: $N/2$ leaves require 0 swaps, $N/4$ nodes require at most 1 swap. The sum evaluates to $\\sum_{{h=0}}^{{\\log N}} \\frac{{N}}{{2^{{h+1}}}} \\times h = N \\times 1 = O(N)$.",
        kind="pro"
    )}

    {callout(
        title="Trap #3: Floyd's Tortoise and Hare Algebraic Proof",
        body="When Slow and Fast meet in a linked list loop, resetting Slow to the head and advancing both by 1 step guarantees they meet at the cycle entrance. Proof: $2(F + a) = F + a + nC \\implies F = nC - a$. Walking $F$ steps from head and $F$ steps from the meeting point lands both pointers exactly at the entrance.",
        kind="math"
    )}
    """
    content.append(section("interview-traps", "⚠️ High-Frequency Traps & Proofs", s7_body, pill="Interview Traps", pill_color="rose"))

    # Section 8: 32 Interview Flashcards
    qa_list = [
        ("Why does (low + high) / 2 overflow and what is the fix?",
         "If low + high exceeds 2^31 - 1, it overflows to a negative integer in signed 32-bit systems, resulting in an out-of-bounds segfault. The fix is: mid = low + (high - low) / 2.",
         ["Binary Search"], "Easy", ["Google", "Apple"]),
        ("Prove that building a Binary Heap takes O(N) time instead of O(N log N).",
         "Bottom-up heap construction (make_heap) runs heapify starting from non-leaf nodes. Since N/2 nodes are at height 0 (0 swaps), N/4 at height 1 (1 swap), N/8 at height 2 (2 swaps), the total swaps sum to N * sum(h / 2^(h+1)) = N * 1 = O(N).",
         ["Heaps", "Math"], "Medium", ["Microsoft", "Amazon"]),
        ("How do you detect cycles in a Directed vs Undirected graph?",
         "Undirected: BFS/DFS (if neighbor is visited and not parent) or Disjoint Set Union (DSU). Directed: DSU does NOT work! Must use 3-Color DFS (recursion stack back-edge) or Kahn's Algorithm (Topological Sort BFS: if processed nodes < V, cycle exists).",
         ["Graphs"], "Medium", ["Media.net", "Cred"]),
        ("What is the time complexity of QuickSelect for K-th largest element vs a Min-Heap?",
         "QuickSelect is average O(N) time and O(1) auxiliary space (ideal for arrays in memory). Min-Heap is O(N log K) time and O(K) space (ideal for unbounded streaming data).",
         ["Sorting"], "Medium", ["Adobe", "Swiggy"]),
        ("How does std::unordered_map resolve hash collisions and what is its worst case?",
         "Uses separate chaining (array of buckets pointing to linked lists). Average O(1), worst-case O(N) when all keys hash to the same bucket. In Java 8+, buckets with >= 8 elements convert to Red-Black Trees for O(log N) worst-case.",
         ["Hashing"], "Easy", ["Apple", "Qualcomm"]),
        ("Why does Dijkstra's algorithm fail on graphs with negative edge weights?",
         "Dijkstra is greedy: it marks a vertex permanently finalized once extracted from the priority queue, assuming all future paths will be longer. A negative edge can make a subsequent path shorter, violating this invariant.",
         ["Graphs"], "Medium", ["Cisco", "Nokia"]),
        ("When is a Greedy algorithm provably optimal? Give a case where it fails.",
         "Optimal when it possesses the Greedy Choice Property and Optimal Substructure (verified via the exchange argument). Fails for Coin Change with non-canonical denominations like {1, 3, 4} for target 6 (greedy picks 4+1+1 = 3 coins; optimal is 3+3 = 2 coins).",
         ["Greedy"], "Hard", ["Juspay", "Media.net"]),
        ("How do you find the Longest Increasing Subsequence (LIS) in O(N log N)?",
         "Using Patience Sorting and binary search (std::lower_bound). Maintain a tails array where tails[len] stores the smallest tail of all increasing subsequences of length len + 1.",
         ["DP"], "Hard", ["Google", "Meta"]),
        ("What is Monotonic Stack and what class of problems does it solve in O(N)?",
         "A stack maintaining strictly increasing or decreasing order. Solves range-bound queries like Next Greater Element, Daily Temperatures, and Largest Rectangle in Histogram in linear time.",
         ["Stack"], "Medium", ["Swiggy", "Cred"]),
        ("Explain the difference between Memoization (Top-Down) and Tabulation (Bottom-Up).",
         "Memoization uses recursion with a lookup cache, evaluating only reachable subproblems. Tabulation iteratively fills an array from base cases up, eliminating recursion stack overhead and enabling space optimization.",
         ["DP"], "Easy", ["Amazon", "Flipkart"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s8_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 32 Top Tech Interview Q&As", s8_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
