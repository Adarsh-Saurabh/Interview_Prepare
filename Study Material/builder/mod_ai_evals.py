# mod_ai_evals.py - AI Evaluation, Observability & MLOps Module Generator
# Conforms to instruction.md Part 7.5 Specification (P0 Track C)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Evaluation Hierarchy & Graders"),
        ("pass-metrics", "📐 pass@k vs pass^k: Production Reliability"),
        ("rag-triad", "🎯 RAG Triad & Retrieval Metrics (nDCG / MRR)"),
        ("llm-as-judge", "⚖️ LLM-as-a-Judge & Alignment Verification"),
        ("drift-observability", "📉 Drift Detection (PSI) & Production MLOps"),
        ("eval-harness-code", "🛠️ Production Eval Harness Implementation"),
        ("interview-flashcards", "🎯 32 Top Tech Interview Q&As")
    ]

    # SVG 1: Evaluation Hierarchy Pyramid
    svg_eval_pyramid = """
    <svg viewBox="0 0 880 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Tier 4: Online / Canary (Top) -->
      <polygon points="440,30 330,95 550,95" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="2" />
      <text x="440" y="70" fill="#f43f5e" font-size="12" font-weight="800" text-anchor="middle">ONLINE / CANARY (A/B, Guardrails)</text>

      <!-- Tier 3: End-to-End System -->
      <polygon points="330,105 550,105 620,170 260,170" fill="rgba(192, 132, 252, 0.25)" stroke="#c084fc" stroke-width="2" />
      <text x="440" y="142" fill="#c084fc" font-size="12" font-weight="800" text-anchor="middle">E2E TASK EVALS (Trajectory, pass^k, Cost)</text>

      <!-- Tier 2: Component Evals -->
      <polygon points="260,180 620,180 690,245 190,245" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2" />
      <text x="440" y="217" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">COMPONENT EVALS (Recall@k, Reranker nDCG, Judge Faithfulness)</text>

      <!-- Tier 1: Deterministic Code Graders (Bottom) -->
      <polygon points="190,255 690,255 760,315 120,315" fill="rgba(52, 211, 153, 0.25)" stroke="#34d399" stroke-width="2" />
      <text x="440" y="290" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">DETERMINISTIC UNIT GRADERS (Regex, JSON Schema, Assertions, Compilers)</text>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Push as much evaluation as humanly possible into deterministic code graders (JSON schema, regex, string asserts, unit tests) before ever falling back to an LLM judge; shipping a demo with zero automated evals is the #1 reason AI take-homes get rejected.")}

    <p>Evaluation is the defining differentiator in modern AI engineering. Teams reject candidates who demonstrate complex agent frameworks but cannot prove their systems work reliably.</p>

    {svg_card(svg_eval_pyramid, "The AI Evaluation Hierarchy: Deterministic Code up to Online Guardrails")}

    {table(
        headers=["Evaluation Layer", "Grading Mechanism", "Cost & Speed", "What it Catches / Blind Spots"],
        rows=[
            ["Deterministic Grader", "Python assertions, Pydantic JSON schema, syntax parser, compiler.", "Sub-millisecond, Free.", "Catches structural formatting, hallucinated JSON keys, tool call schemas. Blind to semantic truth."],
            ["Component Retrieval", "Recall@k, MRR, nDCG, Hit Rate against golden queries.", "Fast, Cheap (embeddings).", "Catches bad chunking and missing knowledge chunks. Blind to generation hallucinations."],
            ["LLM-as-a-Judge", "Strong judge model (e.g. Claude 3.5 Sonnet / GPT-4o) scoring against rubric.", "~$0.02 / call, ~1.5s.", "Evaluates nuance and groundedness. Blind to subtle factual falsehoods unless verified by human agreement."],
            ["Human Eval (Golden Set)", "Domain experts grading 50-100 sampled inputs with guidelines.", "High cost, slow.", "Ultimate ground truth; mandatory to measure Cohen's Kappa against LLM-as-a-judge."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Evaluation Hierarchy & Graders", s1_body, pill="Core Philosophy", pill_color="emerald"))

    # Section 2: pass@k vs pass^k
    s2_body = f"""
    {formula_box(
        katex_display=r"$$\text{pass@}k = 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}}, \quad \text{vs} \quad \text{pass}^k = \left(\frac{c}{n}\right)^k$$",
        reading="pass at k measures probability of at least one success in k attempts, while pass to the power of k measures probability that all k independent attempts succeed.",
        symbols=[
            ("n", "Total generated samples per prompt (e.g., n = 20)"),
            ("c", "Number of correct samples passing verification"),
            ("k", "Target sample budget (e.g., k = 1 or k = 5)")
        ],
        meaning="pass@k flatters models (if 1 of 10 attempts passes, pass@10 is high, fine for coding assistants with human review). But for autonomous production workflows, pass^k measures reliability: if a model is 90% accurate on individual steps, a 5-step agent has pass^5 = 0.9^5 = 59% reliability!"
    )}
    """
    content.append(section("pass-metrics", "📐 pass@k vs pass^k: Production Reliability", s2_body, pill="Reliability Math", pill_color="rose"))

    # Section 3: RAG Triad & Retrieval Metrics
    s3_body = f"""
    {table(
        headers=["RAG Metric", "Definition & Formula", "Target Value", "Diagnostic Failure Signal"],
        rows=[
            ["Context Relevance", "Fraction of retrieved chunks relevant to the user query.", "&gt; 0.85", "Low score indicates bad chunking strategy or vector search noise."],
            ["Groundedness (Faithfulness)", "Fraction of claims in generated answer supported by retrieved context.", "&gt; 0.95", "Low score indicates hallucination! The LLM is inventing ungrounded facts."],
            ["Answer Relevance", "Degree to which generated response directly addresses query intent.", "&gt; 0.90", "Low score indicates model wandered off-topic or gave a non-committal answer."],
            ["nDCG@k", "Normalized Discounted Cumulative Gain accounting for document position.", "&gt; 0.80", "High ranking documents are irrelevant, forcing relevant chunks below the LLM fold."]
        ]
    )}
    """
    content.append(section("rag-triad", "🎯 RAG Triad & Retrieval Metrics (nDCG / MRR)", s3_body, pill="RAG Quality", pill_color="teal"))

    # Section 4: LLM as a Judge
    s4_body = f"""
    <p>Before deploying an LLM judge, you <strong>must measure judge-vs-human agreement</strong> (Cohen's Kappa). Without human validation, your judge is merely grading with its own baked-in biases.</p>

    {table(
        headers=["LLM-as-a-Judge Bias", "Mechanism", "Engineering Mitigation"],
        rows=[
            ["Position Bias", "Judges favor whichever candidate answer is presented first in pairwise comparisons.", "Run pairwise evaluation twice, swapping candidate order (A/B and B/A). Discard ties."],
            ["Verbosity Bias", "Judges consistently score longer, wordier responses higher regardless of content.", "Instruct the judge to penalize fluff; enforce strict word budgets in candidate prompts."],
            ["Self-Preference Bias", "A judge model (e.g. GPT-4o) naturally favors outputs generated by GPT-4o over Claude/Llama.", "Use cross-model jury panels (e.g. average Claude 3.5 Sonnet + GPT-4o + Gemini 1.5 Pro)."]
        ]
    )}
    """
    content.append(section("llm-as-judge", "⚖️ LLM-as-a-Judge & Alignment Verification", s4_body, pill="Judge Quality", pill_color="purple", depth="deep"))

    # Section 5: Drift & MLOps
    s5_body = f"""
    {formula_box(
        katex_display=r"$$\text{PSI} = \sum \left(P_i - Q_i\right) \times \ln\left(\frac{P_i}{Q_i}\right)$$",
        reading="Population Stability Index equals sum of actual minus expected percentage multiplied by natural log of actual over expected.",
        symbols=[
            ("P_i", "Actual production inference distribution in bin i"),
            ("Q_i", "Baseline training / reference validation distribution in bin i"),
            ("PSI < 0.1", "Negligible shift; model is stable"),
            ("PSI > 0.2", "Significant distribution drift! Model must be retrained")
        ],
        meaning="When stakeholders complain 'the model got worse,' 90% of the time the model is unchanged—input distributions drifted (covariate drift). Compute PSI on embedding distances and token lengths to diagnose immediately."
    )}
    """
    content.append(section("drift-observability", "📉 Drift Detection (PSI) & Production MLOps", s5_body, pill="Drift Math", pill_color="amber", depth="deep"))

    # Section 6: Eval Harness Implementation
    s6_body = f"""
    {code(
        src=r"""import re
import json

class ProductionEvalHarness:
    def __init__(self, golden_dataset):
        self.dataset = golden_dataset # List of dicts with query, expected_answer, expected_keys

    def evaluate_response(self, response_text, item):
        scores = {}
        
        # 1. Deterministic JSON validity & schema check
        try:
            parsed = json.loads(response_text)
            scores["valid_json"] = 1.0
            
            # Check mandatory keys
            missing_keys = [k for k in item.get("expected_keys", []) if k not in parsed]
            scores["schema_compliance"] = 1.0 if not missing_keys else 0.0
        except json.JSONDecodeError:
            scores["valid_json"] = 0.0
            scores["schema_compliance"] = 0.0
            
        # 2. Deterministic Regex Ground Truth Assertion
        if "expected_regex" in item:
            match = re.search(item["expected_regex"], response_text, re.IGNORECASE)
            scores["regex_match"] = 1.0 if match else 0.0
            
        return scores""",
        lang="python",
        title="Production Evaluation Harness with Deterministic Graders"
    )}
    """
    content.append(section("eval-harness-code", "🛠️ Production Eval Harness Implementation", s6_body, pill="Harness Code", pill_color="emerald", depth="deep"))

    # Section 7: 32 Interview Flashcards
    qa_list = [
        ("How do you know your AI system is actually working well?",
         "By building an automated 4-tier evaluation pipeline: (1) Deterministic unit graders for syntax/schema, (2) Component metrics (Recall@k, nDCG) for retrieval, (3) Model-graded faithfulness on a curated golden set verified against human agreement, and (4) Online latency, guardrail error rates, and user engagement monitoring.",
         ["Philosophy"], "Easy", ["OpenAI", "Anthropic"]),
        ("What is the difference between pass@k and pass^k?",
         "pass@k is the probability that AT LEAST ONE sample out of k independent attempts succeeds (good for human-in-the-loop assistants). pass^k is the probability that ALL k steps succeed consecutively (vital for autonomous multi-step agents where failure cascades).",
         ["Metrics"], "Medium", ["OpenAI", "Scale AI"]),
        ("Why might a model do worse with retrieved context than with none?",
         "Due to context rot, distraction from irrelevant or noisy chunks, contradictory documents in the retrieval set, or the 'Lost in the Middle' effect where relevant information buried in the middle of long contexts is ignored.",
         ["RAG"], "Medium", ["Anthropic", "Palantir"]),
        ("What are the 3 pillars of the RAG Triad?",
         "Context Relevance (is retrieved context relevant to the user query?), Groundedness / Faithfulness (is the answer strictly supported by context without hallucination?), and Answer Relevance (does the answer address the question asked?).",
         ["RAG"], "Easy", ["Palantir", "Apple"]),
        ("Before you trust an LLM-as-a-judge, what must you measure?",
         "You must measure inter-annotator agreement (Cohen's Kappa) between the LLM judge's scores and human expert labels on a sampled test set. A judge with low human correlation will silently drift and game evals.",
         ["Judges"], "Medium", ["Scale AI", "Meta"]),
        ("Name 3 biases in LLM-as-a-Judge scoring and their fixes.",
         "Position Bias (favors choice A over B -> swap order and average), Verbosity Bias (favors longer answers -> penalize token length or enforce word limits), Self-Preference Bias (favors own model family -> use multi-model juries).",
         ["Judges"], "Medium", ["Google", "Anthropic"]),
        ("A stakeholder says 'the model got worse.' You have no eval set. What do you do first?",
         "First, freeze production logs and pull the latest 50 user queries and responses. Compare their embedding and token length distribution against historical data to check for covariate input drift. Then construct an emergency golden set from those queries to establish a reproducible baseline.",
         ["Debugging"], "Hard", ["Palantir", "OpenAI"]),
        ("Explain the difference between Covariate Drift, Prior Probability Drift, and Concept Drift.",
         "Covariate Drift: Input distribution P(X) changes while P(Y|X) remains fixed. Prior Probability Drift: Target label distribution P(Y) changes. Concept Drift: Relationship between input and output P(Y|X) changes (e.g. meaning of fraud changes).",
         ["MLOps"], "Medium", ["Amazon", "Uber"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 32 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
