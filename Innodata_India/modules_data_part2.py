# modules_data_part2.py - Innodata India Interview Preparation Suite (Modules 03, 04, 05)

modules_data_part2 = {
    "03_Multimodal_AI_and_VLM_Foundations": {
        "title": "Module 03: VLMs & Visual Reasoning · Innodata India",
        "badge": "VLM AI",
        "prev_link": "02_Technical_Engineering_Artifacts.html",
        "prev_title": "02: Schematics, P&ID & Layouts",
        "next_link": "04_Coding_and_Automated_Verifiers.html",
        "next_title": "04: Python & C++ Verifiers",
        "markdown": r"""# Module 03: Multimodal AI & Vision-Language Model (VLM) Foundations

## 1. How Vision-Language Models Process Technical Artifacts

To create benchmarks that push the limits of frontier models, an SME must understand the underlying tokenization and vision-language integration pipelines.

```mermaid
flowchart LR
    A["Raw Engineering Image (e.g. 3840x2160 P&ID)"] --> B["Dynamic Image Tiler / Slicer"]
    B --> C["High-Res Patches (e.g., 336x336 tiles) + Global Thumbnail"]
    C --> D["Vision Encoder (CLIP / SigLIP / DinoV2)"]
    D --> E["Multimodal Projector (MLP / Cross-Attention)"]
    E --> F["LLM Decoder Backbone (GPT-4o / Claude 3.5 / Gemini)"]
    F --> G["Textual Reasoning Trace & Answer"]
```

### The Visual Tokenization Pipeline
1. **Patch Slicing**: An image of dimensions $W \times H$ is split into discrete non-overlapping or overlapping patches of size $P \times P$ (typically $14 \times 14$ or $16 \times 16$ pixels).
   The number of visual tokens $N$ produced per tile is:
   $$N = \\left(\\frac{W}{P}\\right) \\times \\left(\\frac{H}{P}\\right)$$
2. **Patch Embedding**: Each 2D patch is flattened into a 1D vector and linearly projected into an embedding space of dimension $D$, concatenated with a learnable 2D positional embedding vector.
3. **Cross-Modal Projection**: The visual tokens from the Vision Transformer (ViT) are passed through a 2-layer MLP projection adapter or Perceiver Resampler to match the embedding dimension of the autoregressive language model decoder.

---

## 2. Coordinate Grounding & Spatial Representations

Frontier models (like Gemini 2.5 Pro and GPT-4o) represent spatial locations using **normalised bounding box coordinates**:

$$\\text{bbox} = [y_{\\min}, x_{\\min}, y_{\\max}, x_{\\max}]$$

Where each coordinate is an integer in the range $[0, 1000]$:
$$y_{\\min} = \\left\\lfloor \\frac{Y_{\\min}}{H} \\times 1000 \\right\\rfloor, \\quad x_{\\min} = \\left\\lfloor \\frac{X_{\\min}}{W} \\times 1000 \\right\\rfloor$$

### Why Bounding Box Grounding Matters in Benchmarks
When authoring benchmark items, Innodata requires SMEs to provide verified visual evidence bounding boxes. If a model predicts an answer but attends to the wrong quadrant of a 10-megabyte schematic, it indicates **spurious correlation or lucky guessing** rather than true visual reasoning.

---

## 3. The 5 Signature Failure Modes of Frontier VLMs

| Failure Mode | Mechanism | Vulnerable Engineering Domain |
| :--- | :--- | :--- |
| **1. Topological Disconnection** | VLMs perceive proximity as connectivity. If two lines cross without a junction dot, the model frequently assumes they are electrically or hydraulically coupled. | Circuit schematics, pneumatic control loops, piping networks. |
| **2. Directional Inversion** | Models confuse arrowheads on valve bodies or diodes with the orientation of adjacent text labels, reversing flow direction. | P&IDs (upstream vs. downstream), check valves, hydraulic rams. |
| **3. Small-Text Resolution Loss** | Sub-pixel characters in technical fonts (e.g., distinguishing between `0.01uF` and `0.01mF`, or `10k` and `100k`) get blurred during ViT patch pooling. | Component part numbers, tolerance ratings, wire gauge callouts. |
| **4. Spatial Coordinate Hallucination** | When prompted to locate component tags in crowded diagrams, models hallucinate coordinates biased toward the center of the image canvas. | Plant layouts, high-density PCB silkscreens, architectural blueprints. |
| **5. Multi-Hop Reasoning Drift** | By step 3 or 4 of a complex derivation, the autoregressive language model loses attention over earlier visual tokens, falling back on generic pre-training priors. | Multi-stage op-amps, cascading gear trains, safety interlock chains. |
"""
    },

    "04_Coding_and_Automated_Verifiers": {
        "title": "Module 04: Python & C++ Verifiers · Innodata India",
        "badge": "Harnesses",
        "prev_link": "03_Multimodal_AI_and_VLM_Foundations.html",
        "prev_title": "03: VLMs & Visual Reasoning",
        "next_link": "05_Candidate_Resume_Grilling.html",
        "next_title": "05: Candidate Resume Defense",
        "markdown": r"""# Module 04: Production Python & C++ Verifiers & Test Harnesses

## 1. Automated Schema Validation for Benchmark Items

Innodata's data pipeline enforces programmatic quality gates. Below is the production Python validator verifying benchmark integrity, bounding box normalization, and proof completeness.

```python
import json
import re
from typing import Dict, Any, List

class BenchmarkItemValidator:
    REQUIRED_FIELDS = ["item_id", "domain", "problem_statement", "visual_artifact", "ground_truth", "worked_solution"]
    
    @staticmethod
    def validate_item(item: Dict[str, Any]) -> List[str]:
        errors = []
        # 1. Structural schema completeness
        for field in BenchmarkItemValidator.REQUIRED_FIELDS:
            if field not in item:
                errors.append(f"Missing required field: '{field}'")
                
        if errors:
            return errors
            
        # 2. Visual essentiality check (heuristic keyword detection)
        prompt = item["problem_statement"]
        if len(prompt.strip()) < 30:
            errors.append("Problem statement too short (<30 chars)")
            
        # 3. Ground truth formatting
        gt = item["ground_truth"]
        if not gt.get("answer"):
            errors.append("Ground truth 'answer' cannot be empty")
            
        # 4. Bounding box normalization check [ymin, xmin, ymax, xmax] in [0, 1000]
        bboxes = item["visual_artifact"].get("evidence_bboxes", [])
        if not bboxes:
            errors.append("At least one evidence bounding box is required")
        for idx, bbox in enumerate(bboxes):
            if len(bbox) != 4:
                errors.append(f"BBox {idx} must have 4 coordinates [ymin, xmin, ymax, xmax]")
                continue
            ymin, xmin, ymax, xmax = bbox
            if not (0 <= ymin < ymax <= 1000 and 0 <= xmin < xmax <= 1000):
                errors.append(f"BBox {idx} coordinates out of range [0, 1000] or invalid: {bbox}")
                
        # 5. Worked solution step verification
        solution = item["worked_solution"]
        steps = solution.get("steps", [])
        if len(steps) < 2:
            errors.append(f"Worked solution must have at least 2 structured steps; found {len(steps)}")
            
        return errors

# Production test run
sample_item = {
    "item_id": "INNO-ELEC-2026-001",
    "domain": "Electrical Engineering",
    "problem_statement": "Examine the active analog filter in Figure 1. Given Vin(t) = 0.5sin(2000pi*t) V, determine Vout(p-p).",
    "visual_artifact": {
        "file_name": "schematic_dual_opamp.png",
        "evidence_bboxes": [[150, 220, 480, 560], [510, 600, 890, 920]]
    },
    "ground_truth": {
        "answer": "14.14 V",
        "tolerance_range": [14.10, 14.18],
        "type": "numeric_with_unit"
    },
    "worked_solution": {
        "steps": [
            "Compute Stage 1 gain A1 = 1 + Rf/R1 = 1 + 90k/10k = 10.0.",
            "Calculate interstage filter attenuation at f=1000Hz: |H| = 1/sqrt(2) = 0.7071.",
            "Compute Stage 2 inverting gain A2 = -R4/R3 = -50k/25k = -2.0.",
            "Verify saturation: Vpeak = 10 * 0.5 * 0.7071 * 2 = 7.071V < 13.5V.",
            "Calculate peak-to-peak: 2 * 7.071V = 14.14V."
        ],
        "final_proof": "Vout(p-p) = 14.14 V"
    }
}

validator = BenchmarkItemValidator()
errs = validator.validate_item(sample_item)
print("Validation Result:", "PASSED" if not errs else errs)
```

---

## 2. Python Topological Network Verifier (NetworkX)

Engineering schematics and P&IDs can be programmatically verified by modeling the components as an attributed directed graph.

```python
import networkx as nx

def build_pid_hydraulic_network():
    G = nx.DiGraph()
    
    # Add equipment nodes
    G.add_node("R-101", type="Reactor", state="Active")
    G.add_node("P-101A", type="Pump", state="Running", rated_flow=120)
    G.add_node("P-101B", type="Pump", state="Standby", rated_flow=120)
    G.add_node("V-101", type="ManualValve", state="Open")
    G.add_node("FCV-102", type="ControlValve", state="50% Open")
    G.add_node("V-103", type="ManualValve", state="Closed") # Bypass
    G.add_node("E-101", type="HeatExchanger", state="Normal")
    G.add_node("D-102", type="StorageDrum", state="Active")
    
    # Add piping connections (Edges with line specs)
    G.add_edge("R-101", "V-101", pipe_id="6-P-1001", diameter_in=6)
    G.add_edge("V-101", "P-101A", pipe_id="6-P-1002A", diameter_in=6)
    G.add_edge("V-101", "P-101B", pipe_id="6-P-1002B", diameter_in=6)
    G.add_edge("P-101A", "FCV-102", pipe_id="4-P-1003", diameter_in=4)
    G.add_edge("FCV-102", "E-101", pipe_id="4-P-1004", diameter_in=4)
    G.add_edge("P-101A", "V-103", pipe_id="4-P-BYPASS", diameter_in=4)
    G.add_edge("V-103", "E-101", pipe_id="4-P-BYPASS_RETURN", diameter_in=4)
    G.add_edge("E-101", "D-102", pipe_id="6-P-1005", diameter_in=6)
    
    return G

def find_active_flow_paths(G, source, target):
    \"\"\"Finds all paths where all intermediate valves are Open.\"\"\"
    valid_paths = []
    for path in nx.all_simple_paths(G, source, target):
        path_open = True
        for node in path:
            state = G.nodes[node].get("state", "")
            if state == "Closed" or state == "Standby":
                path_open = False
                break
        if path_open:
            valid_paths.append(path)
    return valid_paths

net = build_pid_hydraulic_network()
active_paths = find_active_flow_paths(net, "R-101", "D-102")
print("Verified Active Process Stream:", active_paths)
```

---

## 3. High-Performance C++ Geometric & Graph Engine

In high-throughput benchmark auditing, continuous CAD bounding boxes and spatial adjacency graphs are checked using C++ for sub-millisecond execution.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

struct BoundingBox {
    int ymin, xmin, ymax, xmax;
    
    bool intersects(const BoundingBox& o) const {
        return !(xmin >= o.xmax || xmax <= o.xmin || ymin >= o.ymax || ymax <= o.ymin);
    }
    
    double intersectionOverUnion(const BoundingBox& o) const {
        int interX1 = std::max(xmin, o.xmin);
        int interY1 = std::max(ymin, o.ymin);
        int interX2 = std::min(xmax, o.xmax);
        int interY2 = std::min(ymax, o.ymax);
        
        if (interX2 <= interX1 || interY2 <= interY1) return 0.0;
        double interArea = (interX2 - interX1) * (interY2 - interY1);
        double areaA = (xmax - xmin) * (ymax - ymin);
        double areaB = (o.xmax - o.xmin) * (o.ymax - o.ymin);
        return interArea / (areaA + areaB - interArea);
    }
};

class SchematicGraph {
public:
    int numVertices;
    std::vector<std::vector<int>> adj;
    std::vector<std::string> componentNames;

    SchematicGraph(int n) : numVertices(n), adj(n), componentNames(n) {}

    void addConnection(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // Bidirectional electrical trace
    }

    bool isElectricallyConnected(int start, int end) {
        std::vector<bool> visited(numVertices, false);
        std::queue<int> q;
        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (curr == end) return true;

            for (int neighbor : adj[curr]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        return false;
    }
};

int main() {
    BoundingBox pred{100, 100, 300, 300};
    BoundingBox groundTruth{120, 110, 310, 290};
    std::cout << "BBox IoU Score: " << pred.intersectionOverUnion(groundTruth) << "\\n";

    SchematicGraph sg(5);
    sg.addConnection(0, 1); // Vin -> R1
    sg.addConnection(1, 2); // R1 -> OpAmp Input
    sg.addConnection(2, 3); // OpAmp Output -> Filter
    sg.addConnection(3, 4); // Filter -> Vout

    std::cout << "Trace Vin to Vout Connected: " 
              << (sg.isElectricallyConnected(0, 4) ? "YES" : "NO") << "\\n";
    return 0;
}
```
"""
    },

    "05_Candidate_Resume_Grilling": {
        "title": "Module 05: Resume Defense & Traps · Innodata India",
        "badge": "Defense",
        "prev_link": "04_Coding_and_Automated_Verifiers.html",
        "prev_title": "04: Python & C++ Verifiers",
        "next_link": "06_System_Design_Benchmark_Pipeline.html",
        "next_title": "06: Eval Pipeline Architecture",
        "markdown": r"""# Module 05: Candidate Resume Grilling & Defensive Strategies

## 1. Candidate Background Defense: M.Tech Signal Processing + B.Tech CSE

As **Adarsh Saurabh** (Roll: `225EC6021`), you hold an exceptionally synergistic combination:
* **M.Tech in Signal and Image Processing (NIT Rourkela, 2025–2027, CGPA: 8.28)**: Provides rigorous mathematical grounding in spatial frequency, 2D continuous/discrete convolution, image gradient orientation, Fourier/Laplace analysis, and structural pattern recognition.
* **B.Tech in Computer Science and Engineering (GGU Bilaspur, 2020–2024, CGPA: 8.5)**: Provides algorithmic optimization, data structures, graph theory, multi-threading, and systems engineering.

### Expected Strategic Trap: "Why apply for Visual Reasoning SME instead of traditional SWE?"
* **Flawed Answer**: *"I just need an internship and this role looked interesting."* (Instant rejection).
* **Winning Pivot**:
  > *"Traditional SWE builds CRUD pipelines; the frontier bottleneck of modern AI is evaluation and multimodal reasoning. In this role, my Signal and Image Processing research background at NIT Rourkela allows me to dissect complex engineering artifacts—schematics, spatial diagrams, and CAD drawings—at the mathematical and structural level. Combined with my B.Tech CSE foundation, I don't just solve problems manually; I can design deterministic programmatic verifiers and synthetic evaluation harnesses that scale Innodata's benchmark throughput for frontier labs."*

---

## 2. Project Defense 1: Uplan — Adversarial Document Intelligence Pipeline

### The Project Reality
* **Stack**: Python, Gemini API, LangGraph, Streamlit.
* **Core Achievement**: Architected an adversarial multi-agent workflow in LangGraph utilizing Gemini 2.5 Pro specialists to check visa document coherence; reduced manual verification workload by 85% with detailed failure rebuttal generation.
* **Key Innovation**: Designed structural encoding system using Gemini 2.0 Flash to compile page-level document metadata into a typed semantic graph (98% token compression) and integrated a zero-hallucination mathematical rule check engine.

### Interview Grilling & Defense
* **Q: "How does Uplan's typed semantic graph translate to Innodata's visual benchmark tasks?"**
  * **Defense**: *"In Uplan, raw document images are filled with high-dimensional noise. Rather than feeding raw OCR dumps into a model, I engineered a structural encoding pipeline that translated visual geometry (headers, signatures, stamps, tables) into typed semantic graph nodes with spatial relational edges (e.g., `ABOVE`, `CONTAINS`, `CROSS_REFERENCES`). This exact paradigm is required when converting CAD blueprints or P&IDs into verified ground-truth DAGs for multimodal AI benchmarking."*
* **Q: "What do you mean by 'zero-hallucination mathematical rule check engine'?"**
  * **Defense**: *"LLMs are notorious for arithmetic drift when computing date durations or balance reconciliations. In Uplan, I decoupled reasoning from calculation: the language model was strictly restricted to extracting symbolic variables into a typed Pydantic schema, while an external deterministic Python rule engine executed all mathematical validations. In benchmark authoring, this ensures that the ground-truth worked proof trace is mathematically irrefutable."*

---

## 3. Project Defense 2: Warehouse PathMapper (IBYD Technology)

### The Project Reality
* **Stack**: Python, Algorithms, Data Analysis.
* **Core Achievement**: Delivered a dynamic warehouse mapping solution as a freelance engagement, translating operational pathfinding needs into a heuristic-based routing system. Scaled the engine to warehouses as large as $10,000 \times 10,000$ units, computing optimal paths through 10,000+ locations in under 0.5s on a standard CPU.

### Interview Grilling & Defense
* **Q: "Innodata evaluates CAD floorplans and architectural layouts. How did you model physical constraints in PathMapper?"**
  * **Defense**: *"A continuous $10,000 \times 10,000$ coordinate grid is too computationally expensive for exhaustive search ($10^8$ cells). I abstracted the physical floorplan into a sparse topological adjacency graph where only allowable transit corridors, rack intersections, and docking gates became vertices. Obstacles, one-way aisle rules, and AGV turning radius clearances were encoded as dynamic edge weights and directional constraints. When benchmarking VLMs on floorplans, this allows me to instantly test whether a model's predicted navigation path violates physical wall boundaries."*

---

## 4. Project Defense 3: K-HUKI (Unsupervised Keyframe Identifier)

### The Project Reality
* **Stack**: Python, Computer Vision, Machine Learning.
* **Core Achievement**: Built keyframe extraction system with HOG (Histogram of Oriented Gradients) features and unsupervised learning achieving 96.45% accuracy; developed preprocessing architecture 11x faster than ResNet-based approaches.

### Interview Grilling & Defense
* **Q: "Why did you choose HOG features over deep learning embeddings like ResNet or ViT?"**
  * **Defense**: *"Deep neural networks like ResNet-50 require heavy matrix multiplications and GPU acceleration, introducing massive latency. HOG captures edge and corner structural orientations directly from image gradient vectors ($\nabla I_x, \nabla I_y$). In industrial diagrams, line geometry and orientation matter far more than texture or semantic color. HOG provided 11x faster preprocessing with zero GPU dependency while capturing the structural contours of the visual artifact with 96.45% accuracy."*
"""
    }
}
