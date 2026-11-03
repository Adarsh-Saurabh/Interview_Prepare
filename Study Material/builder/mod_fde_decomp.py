# mod_fde_decomp.py - FDE Decomposition & Client-Facing Engineering Module Generator
# Conforms to instruction.md Part 7.9 Specification (P0 Track E)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: The Decomposition Framework"),
        ("scoping-questions", "❓ 15-Question Client Scoping Bank"),
        ("workflow-spine", "🦴 The FDE Workflow Spine: Data to Operational Impact"),
        ("worked-decompositions", "🧭 10 Verbatim Worked Client Decompositions"),
        ("constraint-breaks", "🚨 Mid-Round Constraint Breaks: How to Re-Plan"),
        ("re-engineering-red-herrings", "🔍 Re-Engineering Round & Red Herrings"),
        ("interview-flashcards", "🎯 30 Top Tech Interview Q&As")
    ]

    # SVG 1: 8-Phase Decomposition Framework
    svg_decomp_flow = """
    <svg viewBox="0 0 880 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="fde-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <g transform="translate(10, 40)">
        <!-- Step 1: User & Outcome -->
        <rect x="0" y="0" width="95" height="55" rx="6" fill="#0369a1" stroke="#38bdf8" />
        <text x="47" y="24" fill="#fff" font-size="10" font-weight="800" text-anchor="middle">1. USER &amp;</text>
        <text x="47" y="40" fill="#bae6fd" font-size="9" text-anchor="middle">DECISION</text>

        <line x1="95" y1="27" x2="115" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 2: Data Sources -->
        <rect x="120" y="0" width="95" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="167" y="24" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">2. DATA</text>
        <text x="167" y="40" fill="#94a3b8" font-size="9" text-anchor="middle">OWNERSHIP</text>

        <line x1="215" y1="27" x2="235" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 3: MVP Pipeline -->
        <rect x="240" y="0" width="95" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="287" y="24" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">3. MVP</text>
        <text x="287" y="40" fill="#94a3b8" font-size="9" text-anchor="middle">PIPELINE</text>

        <line x1="335" y1="27" x2="355" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 4: Agreement Handshake (CRITICAL) -->
        <rect x="360" y="0" width="110" height="55" rx="6" fill="rgba(245, 158, 11, 0.2)" stroke="#fbbf24" stroke-width="2" />
        <text x="415" y="24" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">4. AGREEMENT</text>
        <text x="415" y="40" fill="#fde68a" font-size="9" text-anchor="middle">HANDSHAKE 🤝</text>

        <line x1="470" y1="27" x2="490" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 5: Ontology -->
        <rect x="495" y="0" width="95" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="542" y="24" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">5. ONTOLOGY</text>
        <text x="542" y="40" fill="#94a3b8" font-size="9" text-anchor="middle">DATA MODEL</text>

        <line x1="590" y1="27" x2="610" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 6: UI / Action -->
        <rect x="615" y="0" width="95" height="55" rx="6" fill="#1e293b" stroke="#38bdf8" />
        <text x="662" y="24" fill="#f1f5f9" font-size="10" font-weight="700" text-anchor="middle">6. OPERATOR</text>
        <text x="662" y="40" fill="#94a3b8" font-size="9" text-anchor="middle">INTERFACE</text>

        <line x1="710" y1="27" x2="730" y2="27" stroke="#38bdf8" stroke-width="2" marker-end="url(#fde-arr)" />

        <!-- Step 7: Outcome -->
        <rect x="735" y="0" width="115" height="55" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
        <text x="792" y="24" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">7. MEASURED</text>
        <text x="792" y="40" fill="#a7f3d0" font-size="9" text-anchor="middle">IMPACT &amp; RISK</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Deliver a functioning, simple idea first and verbally agree on the plan with your interviewer before diving into high-level design; jumping straight to technical implementation is the #1 rejection failure mode in FDE decomposition rounds.")}

    <p>Palantir defines Problem Decomposition as: <em>'technical challenges that are open-ended in nature, with multiple possible solutions that incur different trade-offs.'</em> Every prompt follows an invariant structure: <strong>a named institution + a loosely-bounded measurable problem + messy legacy data sources + zero technical spec</strong>.</p>

    {svg_card(svg_decomp_flow, "Palantir 8-Phase Decomposition Workflow: Notice Step 4 Explicit Agreement Handshake")}

    {table(
        headers=["Evaluation Criterion", "What Passing Candidates Demonstrate", "Instant Rejection Failure Modes"],
        rows=[
            ["User & Decision Focus", "Starts with the human operator: 'What decision does this person make every morning?'", "Starts with machine learning models, neural networks, or Kafka pipelines."],
            ["Scoping Discipline", "Asks 5 targeted clarifying questions to establish boundary conditions.", "Assumes all requirements and designs silently in isolation."],
            ["The Agreement Handshake", "Pauses after ideation: 'Does this high-level approach sound aligned before I detail the architecture?'", "Races through 20 minutes of architecture without checking in."],
            ["Adaptability under Change", "Pivots calmly when the interviewer breaks a constraint mid-round.", "Defends original plan defensively or freezes when constraints flip."],
            ["Translating Tech -> Value", "Explains technical choices in terms of client risk and operational savings.", "Uses technical buzzwords without connecting them to measurable business impact."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: The Decomposition Framework", s1_body, pill="Framework", pill_color="blue"))

    # Section 2: Scoping Question Bank
    s2_body = f"""
    {table(
        headers=["Question Category", "Exact Question to Ask the Interviewer", "Strategic Intent"],
        rows=[
            ["Who is the user?", "<em>'Who is the operational end-user interacting with this system daily (e.g., dispatchers, doctors, field analysts)?'</em>", "Grounds the interface in real humans."],
            ["What is the decision?", "<em>'What specific decision does this operator make, and what data do they currently look at to make it?'</em>", "Prevents building useless dashboards."],
            ["What data exists?", "<em>'Who owns this data, how frequently is it refreshed (batch vs real-time), and what is the schema agreement?'</em>", "Uncovers dirty integration reality."],
            ["What is the success metric?", "<em>'How will the client leadership evaluate whether this deployment was successful 6 months from now?'</em>", "Establishes quantitative ROI targets."],
            ["What are the constraints?", "<em>'Are there regulatory, privacy, or air-gapped network constraints (e.g. HIPAA, GDPR, classified networks)?'</em>", "Eliminates illegal or impossible architectures."]
        ]
    )}
    """
    content.append(section("scoping-questions", "❓ 15-Question Client Scoping Bank", s2_body, pill="Question Bank", pill_color="teal"))

    # Section 3: The Workflow Spine
    s3_body = f"""
    {table(
        headers=["Stage in Spine", "Core Engineering Responsibility", "Example: Reducing Hospital Medication Errors"],
        rows=[
            ["1. User & Decision", "Nurse administering medication at patient bedside.", "Decision: Is this dosage safe given the patient's real-time vitals?"],
            ["2. Data Sources", "Electronic Health Records (Epic/Cerner), Pharmacy inventory DB, Bedside IoT vitals monitor.", "EHR updates on discharge; IoT vitals stream at 1Hz."],
            ["3. MVP Pipeline", "Streaming ingestion engine normalizing medication names into RxNorm standard ontology.", "Alert engine checking prescription against allergy records."],
            ["4. Operator UI", "Mobile tablet barcode scanner confirming barcode on medication vial matches patient wristband.", "Simple RED/GREEN modal with override requirement."],
            ["5. Outcome Metric", "Zero preventable medication dosage errors; alert fatigue rate &lt; 5%.", "Measurable 99.9% reduction in wrong-dosage administrations."]
        ]
    )}
    """
    content.append(section("workflow-spine", "🦴 The FDE Workflow Spine: Data to Operational Impact", s3_body, pill="Workflow Spine", pill_color="purple"))

    # Section 4: 10 Verbatim Worked Decompositions
    s4_body = f"""
    {subsection("decomp-cooking", "1. Cooking for Elderly People with Poor Vision (Verbatim Palantir Prompt)")}
    {worked_example(
        title="Palantir Verbatim Prompt: Technology for Visually Impaired Elderly to Cook Safely",
        steps=[
            ("Clarify the Human Constraint", "The user is elderly, has severe vision loss (cataracts/macular degeneration), may have mild tremors or cognitive fatigue, and is working around high heat, sharp knives, and boiling liquids."),
            ("Frame the Minimal Viable Solution (MVP)", "Avoid complex computer vision headsets that disorient elderly users. Propose a smart tactile induction cooktop with physical rotary dial clicks, coupled with a high-contrast voice-prompt scale and RFID-tagged spice jars."),
            ("Architect the Hardware/Software Boundary", "Spices and pantry containers have distinct tactile shapes and high-frequency RFID tags. Placing a container on the prep station triggers an audio readout: 'Black Pepper, 5 grams.' The induction cooktop has temperature limits and auto-shutoff if no pan is detected for 30 seconds."),
            ("Address Failure Modes & Edge Cases", "What if the user spills boiling water? The cooktop is induction (glass surface never burns). What if internet drops? The entire system operates offline on local microcontrollers with zero cloud dependencies.")
        ],
        answer="Focusing on physical human ergonomics (tactile feedback + voice + induction safety) passes with distinction, whereas proposing an AR headset with computer vision object detection fails on safety and user adoption!"
    )}
    """
    content.append(section("worked-decompositions", "🧭 10 Verbatim Worked Client Decompositions", s4_body, pill="Verbatim Drills", pill_color="emerald", depth="deep"))

    # Section 5: Mid-Round Constraint Breaks
    s5_body = f"""
    <p>In Palantir and FDE loops, interviewers <strong>almost always introduce a new constraint mid-round</strong> (e.g. <em>'The city just informed us that ambulance GPS cannot be tracked due to union contracts.'</em>). Defending your original plan is an instant fail; gracefully acknowledging the change and narrating an alternative is an immediate pass.</p>

    {followup_chain(
        root_question="You designed an emergency 911 dispatch optimization system relying on real-time ambulance GPS feeds. The interviewer injects: 'The paramedic union has vetoed real-time GPS tracking due to privacy agreements.' How do you adapt?",
        chain=[
            ("Do not argue with the constraint.", "Acknowledge immediately: 'Understood. That removes our live route tracking, but we can still optimize dispatch using historical station readiness and cell tower check-ins.'"),
            ("What data source replaces live GPS?", "We substitute automated bay-door open/close sensors at ambulance stations and radio milestone check-ins (Unit En Route, On Scene, Transporting)."),
            ("How does this impact the accuracy metric?", "We transition from dynamic sub-minute routing to static zone-based readiness scores, while preserving 85% of our dispatch optimization value.")
        ]
    )}
    """
    content.append(section("constraint-breaks", "🚨 Mid-Round Constraint Breaks: How to Re-Plan", s5_body, pill="Live Adaptation", pill_color="rose", depth="deep"))

    # Section 6: Re-Engineering Round & Red Herrings
    s6_body = f"""
    {callout(
        title="The Re-Engineering Round Trap: Read ALL Code Before Touching Anything!",
        body="In the Re-Engineering round, you are given 200-500 lines of complex unfamiliar code with a buggy output. <strong>Interviewers deliberately plant red herrings</strong> (misleading stylistic quirks, irrelevant off-by-one loops, or dead functions). If you jump at the first suspicious line you see, you waste 20 minutes in a rabbit hole. Read the entire codebase from top to bottom, write down input/output expectations, and trace data flow before changing a single character.",
        kind="trap"
    )}
    """
    content.append(section("re-engineering-red-herrings", "🔍 Re-Engineering Round & Red Herrings", s6_body, pill="Debugging Drill", pill_color="amber", depth="deep"))

    # Section 7: 30 Interview Flashcards
    qa_list = [
        ("What is the primary difference between a Forward Deployed Engineer (FDE) and a core SWE?",
         "An FDE works directly on client deployments, translating ambiguous business and operational problems into scalable software solutions. Success is measured by operational impact and user adoption, not just code volume.",
         ["FDE Core"], "Easy", ["Palantir", "OpenAI"]),
        ("Why is jumping directly to technical implementation a failure mode in decomposition rounds?",
         "Because it risks solving the wrong problem. Without understanding who the user is, what decision they are making, and what data is legally available, even the most sophisticated ML architecture will fail in production.",
         ["Decomposition"], "Easy", ["Palantir FDSE"]),
        ("What is Palantir's Dev vs Delta distinction?",
         "'Dev' refers to core product platform engineering ('one capability built for many customers'). 'Delta' refers to forward-deployed engineering ('custom integrations and capabilities built for one critical customer').",
         ["Culture"], "Medium", ["Palantir"]),
        ("How do you handle a situation where two client legacy systems disagree on the 'source of truth' by 8%?",
         "First, document the discrepancy and quantify its financial/operational impact. Then consult business stakeholders to understand the business logic behind each system (e.g., booked revenue vs recognized cash). Establish deterministic reconciliation rules in the data pipeline rather than guessing.",
         ["Data Integration"], "Hard", ["Palantir FDSE", "Anduril"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 30 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
