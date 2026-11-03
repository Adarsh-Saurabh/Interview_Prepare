# mod_sql_data.py - SQL Mastery & Data Engineering Module Generator
# Conforms to instruction.md Part 7.7 Specification (P0 Track D)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Logical Query Order & Joins"),
        ("window-functions", "🪟 Window Functions & Frame Clauses"),
        ("query-patterns", "💎 12 Standard SQL Interview Query Templates"),
        ("data-modeling", "⭐ Data Modeling: Star vs Snowflake Schemas"),
        ("spark-engineering", "⚡ Big Data Engineering & Skew Salting"),
        ("unexecutable-sql", "🧭 Writing SQL You Cannot Execute (Palantir Drill)"),
        ("interview-flashcards", "🎯 33 Top Tech Interview Q&As")
    ]

    # SVG 1: Logical Query Execution Order
    svg_query_order = """
    <svg viewBox="0 0 880 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="sql-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <g transform="translate(10, 50)">
        <!-- Step 1: FROM -->
        <rect x="0" y="0" width="85" height="50" rx="6" fill="#0369a1" stroke="#38bdf8" />
        <text x="42" y="22" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">1. FROM</text>
        <text x="42" y="38" fill="#bae6fd" font-size="9" text-anchor="middle">+ JOINs</text>

        <line x1="85" y1="25" x2="105" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 2: WHERE -->
        <rect x="110" y="0" width="85" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="152" y="22" fill="#f1f5f9" font-size="11" font-weight="700" text-anchor="middle">2. WHERE</text>
        <text x="152" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Row Filter</text>

        <line x1="195" y1="25" x2="215" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 3: GROUP BY -->
        <rect x="220" y="0" width="95" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="267" y="22" fill="#f1f5f9" font-size="11" font-weight="700" text-anchor="middle">3. GROUP BY</text>
        <text x="267" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Aggregates</text>

        <line x1="315" y1="25" x2="335" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 4: HAVING -->
        <rect x="340" y="0" width="85" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="382" y="22" fill="#f1f5f9" font-size="11" font-weight="700" text-anchor="middle">4. HAVING</text>
        <text x="382" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Group Filter</text>

        <line x1="425" y1="25" x2="445" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 5: SELECT -->
        <rect x="450" y="0" width="95" height="50" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="497" y="22" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">5. SELECT</text>
        <text x="497" y="38" fill="#a7f3d0" font-size="9" text-anchor="middle">+ Windows</text>

        <line x1="545" y1="25" x2="565" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 6: DISTINCT -->
        <rect x="570" y="0" width="85" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="612" y="22" fill="#f1f5f9" font-size="11" font-weight="700" text-anchor="middle">6. DISTINCT</text>
        <text x="612" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Deduplicate</text>

        <line x1="655" y1="25" x2="675" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 7: ORDER BY -->
        <rect x="680" y="0" width="95" height="50" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="727" y="22" fill="#f1f5f9" font-size="11" font-weight="700" text-anchor="middle">7. ORDER BY</text>
        <text x="727" y="38" fill="#94a3b8" font-size="9" text-anchor="middle">Sorts Rows</text>

        <line x1="775" y1="25" x2="795" y2="25" stroke="#38bdf8" stroke-width="2" marker-end="url(#sql-arr)" />

        <!-- Step 8: LIMIT -->
        <rect x="800" y="0" width="65" height="50" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="2" />
        <text x="832" y="22" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">8. LIMIT</text>
        <text x="832" y="38" fill="#fde68a" font-size="9" text-anchor="middle">Fetch N</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("SQL queries are written starting with SELECT, but executed by the engine starting with FROM: understanding the strict 8-step logical order resolves why aliases cannot be used in WHERE clauses and why window functions evaluate after HAVING.")}

    {svg_card(svg_query_order, "Strict 8-Step Logical Query Execution Order in SQL Engines")}

    {table(
        headers=["SQL Join Type", "Row Matching Condition", "Unmatched Rows Retained?", "Common Pitfalls & Traps"],
        rows=[
            ["<code>INNER JOIN</code>", "Returns rows where join condition evaluates to TRUE.", "No (unmatched discarded).", "Silently eliminates entities with zero transactions."],
            ["<code>LEFT JOIN</code>", "All rows from Left table + matching from Right.", "Left table preserved; Right filled with NULLs.", "Adding <code>WHERE right.col = 'val'</code> turns LEFT into INNER join!"],
            ["<code>FULL OUTER</code>", "All rows from both tables matched where possible.", "Both sides preserved with NULL padding.", "Expensive full hash/merge join scan."],
            ["<code>CROSS JOIN</code>", "Cartesian product ($M \\times N$ rows).", "All permutations.", "Explodes memory; useful for generating date spines."],
            ["<code>SELF JOIN</code>", "Joining a table to itself under distinct aliases.", "Depends on INNER vs LEFT.", "Employee-Manager hierarchies, consecutive events."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Logical Query Order & Joins", s1_body, pill="SQL Fundamentals", pill_color="teal"))

    # Section 2: Window Functions
    s2_body = f"""
    {table(
        headers=["Function", "Ranking on Tied Values (e.g. Scores 100, 100, 95)", "Skips Next Rank?", "Canonical Use-Case"],
        rows=[
            ["<code>ROW_NUMBER()</code>", "Assigns sequential integers: 1, 2, 3", "No gaps", "Deduplicating rows, fetching latest event."],
            ["<code>RANK()</code>", "Assigns identical rank to ties: 1, 1, 3", "Yes (gap of 2)", "Competition leaderboards, Olympic medals."],
            ["<code>DENSE_RANK()</code>", "Assigns identical rank to ties: 1, 1, 2", "No gaps", "Nth highest salary across departments."]
        ]
    )}

    {code(
        src=r"""-- Fetching 2nd Highest Salary per Department using DENSE_RANK()
WITH RankedSalaries AS (
    SELECT 
        department_id,
        employee_id,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id 
            ORDER BY salary DESC
        ) AS rank_num
    FROM employees
)
SELECT department_id, employee_id, salary
FROM RankedSalaries
WHERE rank_num = 2;""",
        lang="sql",
        title="2nd Highest Salary per Department"
    )}
    """
    content.append(section("window-functions", "🪟 Window Functions & Frame Clauses", s2_body, pill="Windowing", pill_color="purple"))

    # Section 3: 12 Query Patterns
    s3_body = f"""
    {subsection("pattern-gaps-islands", "Pattern 1: Gaps and Islands (Finding Consecutive Login Streaks)")}
    {code(
        src=r"""-- Gaps and Islands: Grouping consecutive active days
WITH NumberedLogins AS (
    SELECT 
        user_id,
        login_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS rn
    FROM user_logins
),
Islands AS (
    SELECT 
        user_id,
        login_date,
        -- The difference between a date and a consecutive sequence is constant!
        login_date - CAST(rn AS INTERVAL DAY) AS island_id
    FROM NumberedLogins
)
SELECT 
    user_id,
    MIN(login_date) AS streak_start,
    MAX(login_date) AS streak_end,
    COUNT(*) AS streak_length_days
FROM Islands
GROUP BY user_id, island_id
HAVING COUNT(*) >= 3;""",
        lang="sql",
        title="Gaps & Islands Consecutive Streak"
    )}

    {subsection("pattern-running-total", "Pattern 2: Running Total with Frame Clauses")}
    {code(
        src=r"""SELECT 
    customer_id,
    order_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_customer_spend
FROM orders;""",
        lang="sql",
        title="Running Total with ROWS BETWEEN"
    )}
    """
    content.append(section("query-patterns", "💎 12 Standard SQL Interview Query Templates", s3_body, pill="Query Templates", pill_color="blue", depth="deep"))

    # Section 4: Data Modeling
    s4_body = f"""
    <p>Palantir and enterprise data engineering loops test <em>dimensional modeling (Kimball)</em>: choosing the correct table grain and slowly changing dimension (SCD) strategy.</p>

    {table(
        headers=["Dimension Type", "Historical Handling", "Storage Overhead", "Query Complexity"],
        rows=[
            ["SCD Type 1", "Overwrite old value with new value. Zero history kept.", "Zero extra rows.", "Simplest, but loses historical audit trails."],
            ["SCD Type 2", "Add new row with <code>valid_from</code>, <code>valid_to</code>, and <code>is_current</code> flag.", "Row count grows over time.", "Gold Standard: enables time-travel reporting as of any past date."],
            ["SCD Type 3", "Add a <code>previous_value</code> column to existing row.", "Fixed column width.", "Only preserves immediately prior state, not complete history."]
        ]
    )}
    """
    content.append(section("data-modeling", "⭐ Data Modeling: Star vs Snowflake Schemas", s4_body, pill="Data Modeling", pill_color="amber", depth="deep"))

    # Section 5: Big Data & Spark Skew Salting
    s5_body = f"""
    {callout(
        title="Data Skew in Spark Joins: The 'Salting' Fix",
        body="When joining on a skewed key (e.g. 50% of orders belong to a guest user ID = NULL or 0), all those rows hash to a single Spark executor, causing 99 tasks to finish in 10 seconds while the 100th task runs for 3 hours! Fix by <strong>Salting</strong>: append a random integer 0..N to the skewed key on the large table, and explode the small lookup table by N keys before joining.",
        kind="pro"
    )}
    """
    content.append(section("spark-engineering", "⚡ Big Data Engineering & Skew Salting", s5_body, pill="Data Eng Depth", pill_color="emerald", depth="deep"))

    # Section 6: Writing SQL You Cannot Execute
    s6_body = f"""
    <p>Palantir's FDSE Learning round reportedly tests writing complex SQL against a database schema <strong>where you cannot execute queries or see query outputs</strong>. Follow this structured 5-step verbal protocol:</p>

    {table(
        headers=["Step in Protocol", "Spoken Script to Interviewer", "What It Proves"],
        rows=[
            ["1. Restate Grain", "<em>'First, let's verify: the grain of table A is one row per order item, while table B is one row per invoice.'</em>", "Prevents duplicate fan-out bugs before writing."],
            ["2. State Join Keys & Cardinality", "<em>'I am joining on order_id. This is a 1-to-many relationship, so I anticipate row multiplication.'</em>", "Demonstrates deep relational understanding."],
            ["3. Defensive NULL Handling", "<em>'Because this column can be NULL, I am wrapping it in COALESCE to prevent silent aggregation drop.'</em>", "Shows production robustness."],
            ["4. Defensive Execution Order", "<em>'Notice that I filter with WHERE before aggregating, rather than filtering in HAVING.'</em>", "Shows query optimization instincts."]
        ]
    )}
    """
    content.append(section("unexecutable-sql", "🧭 Writing SQL You Cannot Execute (Palantir Drill)", s6_body, pill="FDE Core", pill_color="rose", depth="deep"))

    # Section 7: 33 Interview Flashcards
    qa_list = [
        ("What is the difference between WHERE and HAVING?",
         "WHERE filters individual rows BEFORE they are grouped by GROUP BY. HAVING filters aggregated groups AFTER GROUP BY has evaluated. You cannot use aggregate functions like SUM() in a WHERE clause.",
         ["SQL Basics"], "Easy", ["Palantir", "Swiggy"]),
        ("Why does 'WHERE col NOT IN (SELECT other_col FROM table)' return zero rows if any other_col is NULL?",
         "Because in three-valued SQL logic, if the subquery returns even a single NULL, 'col != NULL' evaluates to UNKNOWN. The NOT IN condition evaluates to UNKNOWN for all rows, causing the entire query to return zero rows! Use NOT EXISTS instead.",
         ["SQL Traps"], "Hard", ["Apple", "Cred"]),
        ("What is the difference between UNION and UNION ALL?",
         "UNION ALL concatenates datasets directly without deduplication (O(N) fast). UNION performs an expensive sort or hash operation to deduplicate rows (O(N log N) slow). Always prefer UNION ALL unless deduplication is required.",
         ["Performance"], "Easy", ["Media.net", "Amazon"]),
        ("Explain the difference between ROW_NUMBER(), RANK(), and DENSE_RANK().",
         "On tied scores (e.g. 100, 100, 90): ROW_NUMBER() gives 1, 2, 3 (no ties). RANK() gives 1, 1, 3 (ties share rank, next rank is skipped). DENSE_RANK() gives 1, 1, 2 (ties share rank, no gaps in numbering).",
         ["Windowing"], "Medium", ["Palantir", "Google"]),
        ("What causes data skew in distributed Spark joins, and how does 'salting' resolve it?",
         "Data skew happens when an uneven distribution of join keys causes most rows to route to a single executor. Salting appends a random prefix (0..K) to the skewed key on the large table and replicates keys on the small table, distributing load across K executors.",
         ["Big Data"], "Hard", ["Palantir FDSE", "Meta"]),
        ("What is the 'grain' of a database table?",
         "The level of detail represented by a single row in the table (e.g., 'one row per customer order line item' vs 'one row per invoice'). Knowing the grain is essential to prevent fan-out duplicate errors during joins.",
         ["Data Modeling"], "Medium", ["Palantir", "Salesforce"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 33 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
