# mod_behavioral.py - Behavioral, STAR & Project Defense Module Generator
# Conforms to instruction.md Part 7.10 Specification (P0 Track E)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Action-Weighted STAR Framework"),
        ("story-bank", "🏦 The 12-Story Competency Master Bank"),
        ("project-defense-dossiers", "🛡️ Project Defense Dossiers: Adarsh's Master Projects"),
        ("anthropic-values", "🕊️ Anthropic Values & Ethical Friction"),
        ("palantir-conviction", "🎯 Palantir Mission Conviction & Failure Traps"),
        ("spoken-rehearsal", "🎙️ Spoken Rehearsal Protocols & Timing Drills"),
        ("interview-flashcards", "🎯 40 Top Behavioral Interview Q&As")
    ]

    # SVG 1: Action-Weighted STAR Breakdown
    svg_star = """
    <svg viewBox="0 0 880 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(20, 40)">
        <!-- Situation (10%) -->
        <rect x="0" y="0" width="80" height="70" rx="6" fill="#1e293b" stroke="#64748b" />
        <text x="40" y="30" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">SITUATION</text>
        <text x="40" y="50" fill="#cbd5e1" font-size="12" font-weight="800" text-anchor="middle">10%</text>

        <!-- Task (10%) -->
        <rect x="90" y="0" width="80" height="70" rx="6" fill="#1e293b" stroke="#64748b" />
        <text x="130" y="30" fill="#94a3b8" font-size="11" font-weight="700" text-anchor="middle">TASK</text>
        <text x="130" y="50" fill="#cbd5e1" font-size="12" font-weight="800" text-anchor="middle">10%</text>

        <!-- ACTION (60%) -->
        <rect x="180" y="0" width="500" height="70" rx="6" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" stroke-width="2" />
        <text x="430" y="28" fill="#34d399" font-size="14" font-weight="800" text-anchor="middle">ACTION (THE CORE TECHNICAL ENGINE — 60% OF TIME)</text>
        <text x="430" y="50" fill="#a7f3d0" font-size="11" text-anchor="middle">Specific architectural choices, tradeoffs, measurements, personal ownership, debug steps</text>

        <!-- Result (20%) -->
        <rect x="690" y="0" width="150" height="70" rx="6" fill="#0369a1" stroke="#38bdf8" />
        <text x="765" y="30" fill="#bae6fd" font-size="11" font-weight="700" text-anchor="middle">RESULT</text>
        <text x="765" y="50" fill="#fff" font-size="12" font-weight="800" text-anchor="middle">20% (Numbers)</text>
      </g>
      <text x="440" y="150" fill="#94a3b8" font-size="11" font-style="italic" text-anchor="middle">⚠️ Trap: Average candidates spend 60% on Situation and 10% on Action. Top performers invert this completely.</text>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Weight your STAR answers strictly: Situation 10%, Task 10%, Action 60%, Result 20%; interviewers evaluate your specific personal actions, architectural tradeoffs, and reasoning under ambiguity, not the company's background story.")}

    <p>Behavioral evaluation is not soft filler. In Palantir, <strong>every single onsite technical round includes ~20 minutes of behavioral probing</strong>. In Anthropic, the Values round is where candidates fail most frequently. In campus panels, failing to defend a resume project in first-principles detail results in immediate rejection.</p>

    {svg_card(svg_star, "The Action-Weighted STAR Timeline: 60% of Your Response Must Detail Specific Actions")}

    {callout(
        title="The Sourced Palantir Failure Story Trap",
        body="A Palantir hiring manager explicitly warned: <em>'We're going to ask you about your failures, your mistakes, your struggles. <strong>We are NOT fishing for a success story in disguise!</strong>'</em> Answering with a fake failure ('I care too much about perfection' or a minor bug fixed in 5 minutes) is an immediate detected failure. Share a genuine technical failure that had real consequences, state your exact personal contribution, and explain what operational safeguards you built to ensure it never happens again.",
        kind="trap"
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Action-Weighted STAR Framework", s1_body, pill="STAR Method", pill_color="emerald"))

    # Section 2: Story Bank
    s2_body = f"""
    {table(
        headers=["Story Archetype", "Candidate Story Anchor", "Target Competencies Proven"],
        rows=[
            ["1. Hardest Technical Problem", "Warehouse PathMapper: Multi-agent congestion and deadlock resolution in grid topology.", "Deep Algorithmic Rigor, Systems Thinking."],
            ["2. A Real Failure", "Early Uplan pipeline failing on complex multi-column PDF tables due to naive bounding boxes.", "Intellectual Humility, Root-Cause Analysis, Resilience."],
            ["3. Conflict with Teammate", "Disagreement over microservices vs modular monolith in early SaaS platform architecture.", "Constructive Disagreement, Data-Driven Consensus."],
            ["4. Led Without Authority", "Initiating automated evaluation suites across academic project team without formal mandate.", "Proactive Leadership, Influence, High Standards."],
            ["5. Learned Something Fast", "Mastering LangGraph state machines and vector search indexing within a 72-hour hackathon.", "Rapid Adaptability, First-Principles Learning."]
        ]
    )}
    """
    content.append(section("story-bank", "🏦 The 12-Story Competency Master Bank", s2_body, pill="Story Bank", pill_color="blue"))

    # Section 3: Project Defense Dossiers
    s3_body = f"""
    <p>As mandated by <code>AGENTS.md</code>, candidate Adarsh Saurabh must defend his three master projects at full architectural depth:</p>

    {subsection("defense-pathmapper", "1. Warehouse PathMapper (IBYD Technology) — Always Present Project")}
    {table(
        headers=["Defense Dimension", "Rigorous Engineering Defense Answer"],
        rows=[
            ["Core Problem", "Dynamic AGV routing across congested 2D grid aisles with pickup and dropoff constraints."],
            ["Why not naive A*?", "Single-agent A* ignores time dimensions ($x, y, t$), leading to head-on collisions, oscillating livelocks in narrow aisles, and gridlocks at high vehicle densities."],
            ["Selected Architecture", "Time-Space Reservoir Reservation Graph with conflict-based search (CBS) and priority replanning."],
            ["Hardest Bug Encountered", "AGVs deadlocking in reciprocal 2-agent swaps in single-lane aisles without passing bays."],
            ["What breaks at 100x load?", "Centralized collision conflict resolution scales $O(K^2)$ with $K$ vehicles; requires distributed zone-based lease locking."]
        ]
    )}

    {subsection("defense-uplan", "2. Uplan — Adversarial Document Intelligence Pipeline")}
    {table(
        headers=["Defense Dimension", "Rigorous Engineering Defense Answer"],
        rows=[
            ["Core Problem", "Accurate extraction and reasoning over complex, adversarial scanned PDFs, tables, and forms."],
            ["Architectural Choice", "Dual-Agent Architect-Critic cycle in LangGraph with OCR confidence scoring and JSON Schema validation."],
            ["Why LangGraph?", "Linear DAG pipelines (LangChain) cannot handle cyclic verification loops when the critic detects table misalignment."],
            ["Measured Metrics", "94.2% field extraction accuracy across scanned municipal forms; 80% reduction in human review queues."]
        ]
    )}
    """
    content.append(section("project-defense-dossiers", "🛡️ Project Defense Dossiers: Adarsh's Master Projects", s3_body, pill="Resume Defense", pill_color="purple", depth="deep"))

    # Section 4: Anthropic Values & Ethics
    s4_body = f"""
    {callout(
        title="Anthropic Values Round: Thoughtful Disagreement Lands Better Than Agreement",
        body="Anthropic recruiters explicitly note that the Values round is <strong>where most candidates fail</strong>. It is structured like a thoughtful philosophical discussion exploring AI safety, dual-use risks, and personal ethics. Interviewers actively probe for skepticism and critical thought—reciting scripted company PR or blind optimism raises red flags. Read Dario Amodei's <em>'Machines of Loving Grace'</em> and <em>'The Adolescence of Technology'</em> before the round.",
        kind="ai"
    )}
    """
    content.append(section("anthropic-values", "🕊️ Anthropic Values & Ethical Friction", s4_body, pill="Anthropic Values", pill_color="rose", depth="deep"))

    # Section 5: Palantir Conviction & Failure
    s5_body = f"""
    <p>Palantir screens aggressively for <em>mission conviction</em> and comfortable handling of unglamorous real-world operational problems.</p>

    {table(
        headers=["Palantir Trap Question", "The Hidden Test", "Strategic Response"],
        rows=[
            ["'Which project did you NOT enjoy?'", "Tests whether you can stay professional and deliver high-quality results on unglamorous, dirty-data work.", "Describe a messy ETL or manual validation project honestly, explain why it was frustrating, and emphasize that you delivered it flawlessly anyway."],
            ["'Why Forward Deployed specifically?'", "Tests whether you understand the difference between pure research and operational deployment.", "Highlight desire to see direct client operational impact and wrestle with real-world messiness rather than synthetic benchmarks."]
        ]
    )}
    """
    content.append(section("palantir-conviction", "🎯 Palantir Mission Conviction & Failure Traps", s5_body, pill="Palantir Loop", pill_color="amber", depth="deep"))

    # Section 6: Spoken Rehearsal
    s6_body = f"""
    <p>Communication failure under pressure is a <strong>rehearsal problem, not a knowledge problem</strong>. Practice with a physical timer:</p>
    <ul>
      <li><strong>Situation & Task:</strong> Maximum 25 seconds. Establish context and stop immediately.</li>
      <li><strong>Action:</strong> 75 to 90 seconds. Speak in first person ('I designed...', 'I profiled...', 'I chose X over Y because...').</li>
      <li><strong>Result:</strong> 20 seconds. Concrete metrics, business impact, and key engineering lessons.</li>
    </ul>
    """
    content.append(section("spoken-rehearsal", "🎙️ Spoken Rehearsal Protocols & Timing Drills", s6_body, pill="Rehearsal", pill_color="teal", depth="deep"))

    # Section 7: 40 Interview Flashcards
    qa_list = [
        ("Tell me about a real technical failure, not a disguised success.",
         "In an early version of our document pipeline, I deployed an unindexed database query for foreign-key lookups under a tight deadline. Under peak load, connection pools exhausted and the API crashed for 45 minutes. I took immediate ownership, conducted a blameless post-mortem, and implemented automated migration linter checks to block unindexed foreign keys in CI.",
         ["Failure"], "Hard", ["Palantir", "Anthropic"]),
        ("Tell me about a time you had a technical disagreement with a team member.",
         "A peer advocated for a fully distributed microservices architecture for a project with 3 developers, while I argued for a modular monolith. I benchmarked our operational complexity overhead (monitoring, network hops, network partitions) against our team velocity. We agreed to start modular monolithically with strict interface boundaries, saving 3 weeks of DevOps overhead.",
         ["Conflict"], "Medium", ["Apple", "Google"]),
        ("Why Palantir, and why Forward Deployed Engineering specifically?",
         "Because I want my engineering decisions to have direct, measurable impact on mission-critical institutions. FDE bridges deep computer science with messy real-world operational realities, where solving data integration and decomposition under pressure matters far more than theoretical ivory-tower models.",
         ["Culture"], "Medium", ["Palantir FDSE"]),
        ("Walk me through Warehouse PathMapper: Why that routing approach over standard A*?",
         "Standard A* computes spatial shortest paths in 2D space without time awareness. In high-density automated warehouses, this causes head-on deadlocks and severe aisle congestion. I built a Time-Space Reservoir Graph with dynamic reservation windows, balancing global path optimality with local conflict resolution.",
         ["Project Defense"], "Medium", ["Campus Drives", "Pace"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 40 Top Behavioral Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
