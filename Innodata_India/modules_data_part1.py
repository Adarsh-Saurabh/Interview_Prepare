# modules_data_part1.py - Innodata India Interview Preparation Suite (Modules 00, 01, 02)

modules_data_part1 = {
    "00_START_HERE": {
        "title": "Module 00: Company & Role Intel · Innodata India",
        "badge": "Strategy",
        "prev_link": None,
        "prev_title": None,
        "next_link": "01_Benchmark_Creation_Protocol.html",
        "next_title": "01: Benchmark & Gold-Sets",
        "markdown": r"""# Module 00: Company & Role Intel

## 1. Executive Intelligence & Business Context

**Innodata Inc. (NASDAQ: INOD)** is a global data engineering and artificial intelligence services company founded in 1990. While historically known for large-scale digital transformation and content authoring, the company underwent a massive strategic pivot starting in 2022–2023 to become a premier **Frontier AI Data Engineering & Evaluation Partner** for top hyperscalers and frontier AI labs (including Google, Microsoft, Meta, Amazon, and Anthropic).

### Why Frontier AI Labs Hire Innodata
Large Language Models (LLMs) and Vision-Language Models (VLMs) have reached near-saturation on generic web-crawled text (Common Crawl, Reddit, Wikipedia) and standard academic benchmarks (GSM8K, HumanEval, MMLU). Frontier labs face critical bottlenecks:
1. **The Multimodal Reasoning Gap**: Models excel at identifying cats or reading simple road signs, but fail catastrophically when asked to reason over complex technical drawings, CAD blueprints, electrical schematics, Piping and Instrumentation Diagrams (P&IDs), and architectural layouts.
2. **The "Googleability" Problem**: Public benchmarks suffer from severe data contamination (models have memorized test sets during pre-training).
3. **The Ground-Truth Necessity**: Supervised Fine-Tuning (SFT) and Reinforcement Learning from Verifiable Rewards (RLVR) require authentic, complex, and provably verifiable domain tasks with step-by-step reasoning proofs.

Innodata builds proprietary evaluation suites, synthetic data pipelines, and gold-standard benchmarks that evaluate models at human-expert capability frontiers.

---

## 2. On-Campus Placement Profile (NIT Rourkela Drive)

| Parameter | Placement Details |
| :--- | :--- |
| **Drive Target** | NIT Rourkela — Batch 2027 (On Campus) |
| **Target Role** | **Industrial Technical Visual Reasoning Specialist (Subject Matter Expert)** |
| **Engagement Model** | **3 Months Internship + PPO Conversion** |
| **Internship Stipend** | **₹60,000 – ₹70,000 / month** (B.Tech / M.Tech / Dual) |
| **PPO Conversion CTC** | **₹10.00 – ₹14.00 LPA** |
| **Job Location** | Noida, Uttar Pradesh (Corporate Delivery Center) |
| **Application Deadline**| 11:59 AM, 21st October 2026 |

---

## 3. The Core Mandate: Industrial Technical Visual Reasoning Specialist

The official Job Description (JD) outlines the core objective:
> *"Develop high-quality multimodal reasoning benchmarks based on authentic industrial and engineering artifacts... evaluate advanced structural, spatial, functional, and analytical reasoning skills... tasks that can only be solved through careful visual interpretation and domain expertise."*

### Key Responsibilities
* **Benchmark Content Development**: Source and synthesize authentic industrial artifacts (CAD models, P&IDs, floor plans, circuit schematics, assembly diagrams, network topologies).
* **Multi-Step Problem Formulation**: Design problems that require multi-hop analytical reasoning, troubleshooting, tolerance verification, and functional flow tracing.
* **Visual Essentiality Constraint**: Ensure the problem cannot be answered from the textual prompt alone or solved via generic web search ("non-Googleable"). The visual artifact must contain non-redundant, indispensable ground truth.
* **Rigorous Proof Trace Authoring**: Write verifiable, step-by-step mathematical, physical, or logical derivations establishing the single correct ground-truth answer.

---

## 4. Selection Process & Hiring Stages

```mermaid
flowchart LR
    A["Stage 1: Online Assessment"] --> B["Stage 2: Technical Task Round"]
    B --> C["Stage 3: Technical & Resume Defense"]
    C --> D["Stage 4: Managerial & HR Alignment"]
    D --> E["PPO Offer & Onboarding"]
```

### Stage 1: Diagnostic Assessment (Online)
* **Duration**: 60–90 minutes.
* **Focus**: Logical reasoning, technical reading comprehension, English SOP adherence, diagram interpretation, and basic algorithmic/math skills.
* **Key Filter**: Compliance with instructions. Scores below 90% on guideline adherence are screened out automatically.

### Stage 2: Technical Problem Authoring Round (Practical)
* **Task**: You are given an authentic engineering drawing (e.g., an industrial heat-exchanger P&ID or a multi-stage operational amplifier circuit).
* **Deliverable**:
  1. Author 2 high-difficulty, non-Googleable questions.
  2. Define the exact bounding box / spatial region of interest.
  3. Formulate the single objective ground-truth answer.
  4. Write the complete step-by-step worked derivation with explicit physical/logical laws applied.
  5. Provide 3 plausible distractor answers with explanations of the specific reasoning errors each represents.

### Stage 3: Technical Interview & Candidate Resume Defense
* **Format**: 45–60 minutes 1-on-1 with Senior Technical Lead / AI Engineering Manager.
* **Topics**:
  * Engineering diagram interpretation (ISA-5.1 standards, IEEE circuit symbols, topological graph theory).
  * Multimodal AI architecture basics (Vision Transformers, patch tokenization, spatial grounding).
  * Candidate project grilling: Deep dive into **Uplan** (Adversarial Document Intelligence), **Warehouse PathMapper** (Spatial graph heuristics), and **K-HUKI** (Computer Vision & HOG feature extraction).

### Stage 4: Managerial, HR & SOP Alignment
* **Format**: 30 minutes with HR / Delivery Operations Director.
* **Focus**: Attention to detail, maintaining $\ge 95\%$ accuracy during high-throughput repetitive benchmarking, communication skills, handling ambiguous client prompts, and PPO conversion roadmap.
"""
    },

    "01_Benchmark_Creation_Protocol": {
        "title": "Module 01: Benchmark & Gold-Set Design · Innodata India",
        "badge": "Protocol",
        "prev_link": "00_START_HERE.html",
        "prev_title": "00: Company & Role Intel",
        "next_link": "02_Technical_Engineering_Artifacts.html",
        "next_title": "02: Schematics, P&ID & Layouts",
        "markdown": r"""# Module 01: Benchmark & Gold-Set Problem Authoring Protocol

## 1. The Anatomy of an Authentic Industrial Benchmark Item

Every benchmark problem delivered to frontier AI labs follows a strict 4-part schema. Missing any single component invalidates the benchmark item.

```
+--------------------------------------------------------------------------+
| 1. Problem Statement (Clear, unambiguous prompt with visual dependency)  |
+--------------------------------------------------------------------------+
| 2. Authentic Engineering Artifact (CAD, Schematic, P&ID, Floorplan)     |
+--------------------------------------------------------------------------+
| 3. Objective Ground-Truth Answer (Scalar, tag, coordinates, sequence)    |
+--------------------------------------------------------------------------+
| 4. Worked Proof Trace (Step-by-step derivation with domain laws)         |
+--------------------------------------------------------------------------+
```

### The Inviolable Rule: Visual Essentiality
A benchmark item has **zero value** if an advanced model (like GPT-4o or Gemini 2.5 Pro) can answer it using text pre-training alone. 
* **Negative Test (Text-Only Baseline)**: When the prompt is fed to the model *without* the image, the model's accuracy should equal random guessing ($< 25\%$ on multiple choice, $\approx 0\%$ on open-ended numeric).
* **Positive Test (Multimodal Baseline)**: When fed image + prompt, the model must execute visual grounding across multiple sub-elements to derive the answer.

---

## 2. Engineering "Non-Googleable" High-Difficulty Problems

To ensure tasks cannot be solved by reverse-image search or web retrieval:

| Strategy | Mechanism | Example |
| :--- | :--- | :--- |
| **Counterfactual Perturbation** | Introduce a hypothetical fault or state change on an existing diagram. | *"If valve XV-204 is stuck at 30% open while pump P-101B trips, what is the maximum pressure reached at accumulator ACC-01?"* |
| **Multi-Hop Spatial Tracing** | Require following a physical or signal path through 3+ intermediate subsystems. | Tracing a pneumatic signal line through a solenoid, shuttle valve, and pressure regulator to a final control actuator. |
| **Cross-Modal Reconciliation** | Correlating a tabular specification sheet with a physical layout diagram. | Verifying if the breaker rating in Table 2 exceeds the busbar thermal limit depicted in the Single-Line Diagram (SLD). |
| **Topological Inversion** | Asking what component must be modified to achieve an inverted operational state. | Identifying which bypass line allows maintenance on heat exchanger E-102 without shutting down Reactor R-101. |

---

## 3. Full Production Example 1: Electrical Circuit Schematic

### Artifact Context
A multi-stage operational amplifier circuit containing:
* Stage 1: Non-inverting amplifier with gain $A_1 = 1 + \\frac{R_f}{R_1}$, where $R_f = 90\\,\\text{k}\\Omega, R_1 = 10\\,\\text{k}\\Omega$.
* Interstage: Passive low-pass $RC$ filter with $R_2 = 1.59\\,\\text{k}\\Omega, C_1 = 0.1\\,\\mu\\text{F}$.
* Stage 2: Inverting amplifier with gain $A_2 = -\\frac{R_4}{R_3}$, where $R_4 = 50\\,\\text{k}\\Omega, R_3 = 25\\,\\text{k}\\Omega$.
* Supply Rails: $V_{CC} = +15\\,\\text{V}, V_{EE} = -15\\,\\text{V}$. Saturation limits are $\\pm 13.5\\,\\text{V}$.

### Benchmark Item
* **Problem Statement**:
  > *"Examine the two-stage active analog processing circuit in Figure 1. A sinusoidal input signal $v_{in}(t) = 0.5\\sin(2\\pi \\cdot 1000\\,t)\\,\\text{V}$ is applied at terminal $IN$. Accounting for the interstage filter attenuation at frequency $f = 1000\\,\\text{Hz}$ and the op-amp supply saturation rails ($\pm 13.5\\,\\text{V}$), calculate the peak-to-peak output voltage $V_{out(p-p)}$ at terminal $OUT$. Round your answer to two decimal places."*

* **Ground-Truth Derivation (Step-by-Step Proof)**:
  1. **Stage 1 Voltage Gain**:
     $$A_1 = 1 + \\frac{R_f}{R_1} = 1 + \\frac{90\\times 10^3}{10\\times 10^3} = 10.0$$
     The peak voltage at the output of Stage 1 is:
     $$V_{peak,1} = A_1 \\times V_{in,peak} = 10.0 \\times 0.5\\,\\text{V} = 5.0\\,\\text{V}$$
  2. **Interstage Filter Frequency Response**:
     The cutoff frequency $f_c$ of the $RC$ filter is:
     $$f_c = \\frac{1}{2\\pi R_2 C_1} = \\frac{1}{2\\pi \\times 1.59\\times 10^3 \\times 0.1\\times 10^{-6}} \\approx 1000.9\\,\\text{Hz} \\approx 1000\\,\\text{Hz}$$
     At frequency $f = 1000\\,\\text{Hz}$, the transfer function magnitude $|H(f)|$ is:
     $$|H(f)| = \\frac{1}{\\sqrt{1 + \\left(\\frac{f}{f_c}\\right)^2}} = \\frac{1}{\\sqrt{1 + 1^2}} = \\frac{1}{\\sqrt{2}} \\approx 0.7071$$
     Voltage arriving at Stage 2 input:
     $$V_{peak,2\\_in} = V_{peak,1} \\times |H(1000)| = 5.0\\,\\text{V} \\times 0.7071 = 3.5355\\,\\text{V}$$
  3. **Stage 2 Voltage Gain**:
     $$A_2 = -\\frac{R_4}{R_3} = -\\frac{50\\times 10^3}{25\\times 10^3} = -2.0$$
     Unclipped output peak voltage:
     $$V_{out,peak} = |A_2| \\times V_{peak,2\\_in} = 2.0 \\times 3.5355\\,\\text{V} = 7.071\\,\\text{V}$$
  4. **Saturation Check**:
     $V_{out,peak} = 7.071\\,\\text{V} < V_{sat} (13.5\\,\\text{V})$. No clipping occurs.
  5. **Peak-to-Peak Calculation**:
     $$V_{out(p-p)} = 2 \\times V_{out,peak} = 2 \\times 7.071\\,\\text{V} = 14.14\\,\\text{V}$$
* **Objective Answer**: `14.14 V` (Tolerance: $[14.10, 14.18]$).

---

## 4. Full Production Example 2: Chemical Process P&ID

### Artifact Context
A distillation column overhead reflux accumulator system with automated pressure relief, bypass throttling, and emergency shutoff valves (ESDV).

### Benchmark Item
* **Problem Statement**:
  > *"Refer to the overhead condenser piping loop in P&ID Sheet 4B. Pressure transmitter PT-304 signals high-pressure alarm PAH-304 at $6.8\\,\\text{bar}$. According to the interlock logic diagram, which combination of automatic valves will immediately change state, and what is the resulting flow destination of the volatile vapor stream?"*

* **Ground-Truth Derivation**:
  1. Inspect instrument bubble `PT-304` on reflux drum `D-301`. Follow electrical signal line (dashed line) to SIS logic solver `I-304`.
  2. Logic solver `I-304` triggers output interlock `I-04`:
     * Energizes solenoid valve `SOV-304A` to vent air from pneumatic actuator on fail-closed control valve `PCV-304`.
     * Valve `PCV-304` transitions to **100% OPEN** within 1.5 seconds.
     * De-energizes solenoid valve `SOV-302` on suction of booster pump `P-302A/B`, tripping both motors.
  3. Trace the discharge piping downstream of `PCV-304`: Line `6"-HC-3041-A1A` leads directly to the **Low-Pressure Flare Header (FL-01)**, bypassing the tertiary absorption column.
* **Objective Answer**: `PCV-304 opens; P-302A/B trip; flow routes to Low-Pressure Flare Header FL-01`.
"""
    },

    "02_Technical_Engineering_Artifacts": {
        "title": "Module 02: Schematics, P&ID & Layouts · Innodata India",
        "badge": "Artifacts",
        "prev_link": "01_Benchmark_Creation_Protocol.html",
        "prev_title": "01: Benchmark & Gold-Sets",
        "next_link": "03_Multimodal_AI_and_VLM_Foundations.html",
        "next_title": "03: VLMs & Visual Reasoning",
        "markdown": r"""# Module 02: Technical Engineering Artifact Interpretation

## 1. Electrical & Electronics Schematics (IEEE/IEC Standards)

Understanding engineering symbology allows an SME to author problems that expose VLM reasoning failures.

### Standard Schematic Conventions
* **Junctions vs. Crossings**: A solid black dot ($\bullet$) indicates an electrical connection. Crossing lines without a dot represent unjoined, insulated bypass conductors. *Frontier VLMs frequently hallucinate connections at simple crossings.*
* **Power & Ground Rails**: Analog ground ($\triangledown$), digital ground ($\stackrel{\text{DGND}}{\underline{\hspace{3mm}}}$), earth ground ($\frac{\mathbf{\downarrow}}{\mathbf{-}}$), and supply rails ($V_{CC}, V_{DD}, V_{EE}, V_{SS}$).
* **Active Semiconductor Elements**:
  * **BJT**: Base ($B$), Collector ($C$), Emitter ($E$). Arrow pointing outward on emitter = NPN; pointing inward = PNP.
  * **MOSFET**: Gate ($G$), Drain ($D$), Source ($S$), Substrate ($B$). Channel type designated by arrow on source/bulk.
  * **Operational Amplifiers**: Inverting input ($-$), non-inverting input ($+$), output ($V_o$), supply pins ($V^+, V^-$).

```
        Non-Inverting Amplifier                   Inverting Amplifier
              +15V                                       +15V
               |                                          |
             |\\ |                                       |\\ |
  Vin ----+--|+ \\                                   +---|- \\
          |  |  \\------ Vout              Vin -[R1]-+   |  \\------ Vout
          |  |- /                                   |   |  /
          |  |/ |                                   +---|+ /
          |    |                                    |   |/ |
          |   -15V                                 GND    |
          |                                              -15V
          +-[R1]-+                                        |
                 |                                        +-[Rf]-+
                GND                                              |
                                                                Vout
```

---

## 2. Piping & Instrumentation Diagrams (P&ID) — ISA-5.1 Standards

P&IDs represent process piping, vessel equipment, control valves, and electronic/pneumatic feedback loops.

### Instrument Bubble Identification (Tagging Convention)
Instrument tags consist of two parts: a **functional letter code** followed by a **loop number** (e.g., `FIC-101`).

| First Letter (Measured Variable) | Second Letter (Modifier) | Subsequent Letters (Readout/Function) |
| :--- | :--- | :--- |
| **F** — Flow Rate | **D** — Differential | **A** — Alarm (e.g., FAH = Flow Alarm High) |
| **P** — Pressure | **F** — Ratio / Fraction | **C** — Controller |
| **T** — Temperature | **Q** — Totalizer / Integrate | **I** — Indicator |
| **L** — Level | **S** — Safety (e.g., PSV) | **T** — Transmitter |
| **A** — Analysis (pH, gas) | **J** — Power / Scan | **V** — Control Valve |

### Line Type Symbology
* **Major Process Piping**: Solid thick line (`――――――――`).
* **Electrical Signal**: Dashed line (`- - - - - - -`).
* **Pneumatic / Air Supply**: Line with double diagonal slash (`―//―//―//―`).
* **Software / Data Link**: Thin line with hollow bubbles or alternating dashes/dots (`―o―o―o―`).
* **Hydraulic Signal**: Line with periodic `L` marks.

### Valve Fail-Safe Modes
* **Fail Open (FO)**: Actuator arrow points down into valve body. Loss of pneumatic air pressure causes valve spring to force it wide open (used for cooling loops and relief vents).
* **Fail Closed (FC)**: Actuator arrow points away from valve body. Loss of signal shuts the valve completely (used for fuel feed lines and toxic chemical supplies).
* **Fail Locked (FL)**: Valve remains frozen in its last commanded position.

---

## 3. Industrial Floorplans & Warehouse CAD Layouts

Floorplans evaluate spatial, dimensional, and topological navigation constraints.

```mermaid
flowchart TD
    subgraph Warehouse CAD Grid [10,000 x 10,000 Spatial Coordinate System]
        Dock[Inbound Loading Dock A] --> Staging[Automated Staging Area]
        Staging --> MainAisle["Main Corridor (Aisle W-1) Width: 4.2m"]
        MainAisle --> PickBay1["Pick Bay Zone A (Heavy Pallets)"]
        MainAisle --> PickBay2["Pick Bay Zone B (High-Density Racks)"]
        PickBay1 --> ChokePoint{"Fire Egress Choke Point (Clearance: 1.8m)"}
        PickBay2 --> ChokePoint
        ChokePoint --> Outbound[Outbound Shipping Dock B]
    end
```

### Spatial Reasoning Dimensions
1. **Clearance & Collision Checks**: Evaluating whether equipment (forklifts, AGVs, mobile robots) of given dimensions ($L \times W \times H$) can traverse tight aisle radii without violating safety envelopes.
2. **Topological Graph Extraction**: Converting continuous CAD drawings into a directed graph $G = (V, E)$, where vertices $V$ represent aisle intersections/dock doors, and directed edges $E$ represent allowable travel routes.
3. **Choke Point & Bottleneck Identification**: Locating points in the floor plan where capacity drops below inbound arrival rates, causing queue accumulation.
"""
    }
}
