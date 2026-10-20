# Module 01: Benchmark & Gold-Set Problem Authoring Protocol

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
