# Module 08: Rapid Recall CheatSheet & Formula Reference

## 1. ISA-5.1 P&ID Letter Identification Table

| First Letter (Variable) | Meaning | Second Letter (Modifier) | Subsequent Letters (Function) |
| :---: | :--- | :---: | :--- |
| **A** | Analysis (pH, O2, Gas) | **D** (Differential) | **A** (Alarm) |
| **F** | Flow Rate | **F** (Ratio) | **C** (Controller) |
| **L** | Level (Liquid / Solid) | **Q** (Totalize / Integrate) | **I** (Indicator) |
| **P** | Pressure | **S** (Safety / Interlock) | **T** (Transmitter) |
| **T** | Temperature | **—** | **V** (Control Valve) |

*Examples*:
* `PT-101`: Pressure Transmitter
* `FIC-204`: Flow Indicating Controller
* `PSV-301`: Pressure Safety Valve
* `PAH-102`: Pressure Alarm High

---

## 2. Core Electrical Circuit Formulas

### Inverting Operational Amplifier
$$V_{out} = -\\frac{R_f}{R_{in}} \\cdot V_{in}$$

### Non-Inverting Operational Amplifier
$$V_{out} = \\left(1 + \\frac{R_f}{R_1}\\right) \\cdot V_{in}$$

### First-Order Passive Low-Pass RC Filter
* **Cutoff Frequency**:
  $$f_c = \\frac{1}{2\\pi R C}$$
* **Gain Magnitude at Frequency $f$**:
  $$|H(f)| = \\frac{1}{\\sqrt{1 + \\left(\\frac{f}{f_c}\\right)^2}}$$

---

## 3. Mathematical & Evaluation Formulas

### Bounding Box Normalisation ($[0, 1000]$ Coordinate Space)
$$y_{\\min} = \\left\\lfloor \\frac{Y_{\\min}}{H} \\times 1000 \\right\\rfloor, \\quad x_{\\min} = \\left\\lfloor \\frac{X_{\\min}}{W} \\times 1000 \\right\\rfloor$$

### Intersection over Union (IoU)
$$\\text{IoU} = \\frac{\\text{Area}(A \\cap B)}{\\text{Area}(A \\cup B)}$$

### Cohen's Kappa (Inter-Annotator Agreement)
$$\\kappa = \\frac{p_o - p_e}{1 - p_e}$$

### Vision Transformer (ViT) Patch Count
$$N = \\left\\lceil \\frac{W}{P} \\right\\rceil \\times \\left\\lceil \\frac{H}{P} \\right\\rceil$$

---

## 4. The 10-Point Benchmark Submission Audit Checklist

- [ ] **1. Visual Essentiality**: Can this question be answered without viewing the image? If yes $\\to$ **REWRITE**.
- [ ] **2. Non-Googleable**: Are the specific diagram labels and numerical values non-retrievable online?
- [ ] **3. Bounding Box Precision**: Does the evidence bounding box tightly encompass the target artifact without excess padding?
- [ ] **4. Normalization Range**: Are all coordinates strictly integers between $0$ and $1000$?
- [ ] **5. Unambiguous Ground Truth**: Is the answer definitive with explicit units and tolerance bounds?
- [ ] **6. Step-by-Step Proof**: Does the worked solution cite explicit physical/mathematical laws at every step?
- [ ] **7. Plausible Distractors**: Do incorrect options correspond to common VLM failure modes (e.g., directional inversion, OCR blur)?
- [ ] **8. Image Resolution**: Is the visual artifact rendered at $\\ge 300\\,\\text{DPI}$ without compression artifacts?
- [ ] **9. Guideline Compliance**: Does the item adhere to all client-specific nomenclature rules?
- [ ] **10. Independent Solvability**: Can a peer SME arrive at the exact same answer independently?
