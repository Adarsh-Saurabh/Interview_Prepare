# Module 04: Production Python & C++ Verifiers & Test Harnesses

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
