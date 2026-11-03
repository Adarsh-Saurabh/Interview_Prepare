# mod_llm_internals.py - LLM & Transformer Internals Module Generator
# Conforms to instruction.md Part 7.4 Specification (P0 Track C)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Transformer Anatomy & Attention"),
        ("attention-architectures", "🧠 Attention Matrix: MHA vs MQA vs GQA"),
        ("kv-cache-math", "📐 KV Cache Memory Scaling & Inference Latency"),
        ("post-training-matrix", "🎯 Post-Training: SFT, DPO, GRPO & RLVR"),
        ("peft-quantization", "⚡ LoRA, QLoRA & Serving Optimization"),
        ("info-theory-corner", "∑ Information Theory Corner (Candidate Edge)"),
        ("interview-flashcards", "🎯 35 Top Tech Interview Q&As")
    ]

    # SVG 1: MHA vs MQA vs GQA Layout
    svg_gqa = """
    <svg viewBox="0 0 880 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- MHA -->
      <rect x="30" y="20" width="250" height="250" rx="8" fill="#111827" stroke="#38bdf8" stroke-width="1.5" />
      <text x="155" y="45" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Multi-Head Attention (MHA)</text>
      <text x="155" y="65" fill="#94a3b8" font-size="10" text-anchor="middle">8 Query Heads : 8 Key/Value Heads</text>
      
      <g transform="translate(45, 80)">
        <rect x="0" y="0" width="220" height="30" rx="4" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" />
        <text x="110" y="20" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7</text>

        <rect x="0" y="45" width="220" height="30" rx="4" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" />
        <text x="110" y="65" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">K0 K1 K2 K3 K4 K5 K6 K7</text>

        <rect x="0" y="90" width="220" height="30" rx="4" fill="rgba(251, 191, 36, 0.2)" stroke="#fbbf24" />
        <text x="110" y="110" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">V0 V1 V2 V3 V4 V5 V6 V7</text>

        <text x="110" y="150" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">1:1 Ratio — Highest KV Cache RAM</text>
      </g>

      <!-- GQA -->
      <rect x="315" y="20" width="250" height="250" rx="8" fill="#111827" stroke="#a855f7" stroke-width="2" />
      <text x="440" y="45" fill="#c084fc" font-size="13" font-weight="800" text-anchor="middle">Grouped-Query (GQA - Llama 3)</text>
      <text x="440" y="65" fill="#94a3b8" font-size="10" text-anchor="middle">8 Query Heads : 2 Key/Value Heads</text>

      <g transform="translate(330, 80)">
        <rect x="0" y="0" width="220" height="30" rx="4" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" />
        <text x="110" y="20" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Q0 Q1 Q2 Q3 | Q4 Q5 Q6 Q7</text>

        <rect x="0" y="45" width="105" height="30" rx="4" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" />
        <text x="52" y="65" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">K_Group 0</text>
        <rect x="115" y="45" width="105" height="30" rx="4" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" />
        <text x="167" y="65" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">K_Group 1</text>

        <rect x="0" y="90" width="105" height="30" rx="4" fill="rgba(251, 191, 36, 0.2)" stroke="#fbbf24" />
        <text x="52" y="110" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">V_Group 0</text>
        <rect x="115" y="90" width="105" height="30" rx="4" fill="rgba(251, 191, 36, 0.2)" stroke="#fbbf24" />
        <text x="167" y="110" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">V_Group 1</text>

        <text x="110" y="150" fill="#34d399" font-size="10" font-weight="700" text-anchor="middle">4:1 Ratio — 75% KV RAM Cut (Gold Standard)</text>
      </g>

      <!-- MQA -->
      <rect x="600" y="20" width="250" height="250" rx="8" fill="#111827" stroke="#34d399" stroke-width="1.5" />
      <text x="725" y="45" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">Multi-Query Attention (MQA)</text>
      <text x="725" y="65" fill="#94a3b8" font-size="10" text-anchor="middle">8 Query Heads : 1 Key/Value Head</text>

      <g transform="translate(615, 80)">
        <rect x="0" y="0" width="220" height="30" rx="4" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" />
        <text x="110" y="20" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7</text>

        <rect x="0" y="45" width="220" height="30" rx="4" fill="rgba(52, 211, 153, 0.2)" stroke="#34d399" />
        <text x="110" y="65" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Single Shared Key Head</text>

        <rect x="0" y="90" width="220" height="30" rx="4" fill="rgba(251, 191, 36, 0.2)" stroke="#fbbf24" />
        <text x="110" y="110" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Single Shared Value Head</text>

        <text x="110" y="150" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="middle">8:1 Ratio — Minimal RAM but Quality Loss</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Transformer generation is memory-bandwidth bound, not compute-bound: decoding one token requires loading all weights and the entire KV cache from GPU VRAM into SRAM, which is why PagedAttention and GQA define modern inference.")}

    {formula_box(
        katex_display=r"$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$",
        reading="Attention equals softmax of query times key transpose divided by square root of key dimension, multiplied by values.",
        symbols=[
            ("Q", "Queries matrix of shape [Batch, Sequence_Len, d_k]"),
            ("K", "Keys matrix of shape [Batch, Sequence_Len, d_k]"),
            ("V", "Values matrix of shape [Batch, Sequence_Len, d_v]"),
            ("d_k", "Hidden dimension per attention head (typically 64 or 128)")
        ],
        meaning="Dividing by sqrt(d_k) prevents dot products from growing excessively large for large dimensions. Without scaling, large dot products push the softmax function into regions with near-zero gradients (saturation), freezing backpropagation."
    )}

    {table(
        headers=["Component / Stage", "Legacy Architecture", "Modern Frontier LLM (Llama 3 / Mistral)", "Engineering Justification"],
        rows=[
            ["Normalization", "Post-LayerNorm", "Pre-RMSNorm", "RMSNorm drops mean-centering, saving 7% GPU FLOPs; Pre-norm ensures stable gradient flow."],
            ["Positional Encoding", "Absolute Learned / Sinusoidal", "Rotary Position Embeddings (RoPE)", "RoPE encodes relative token distances via complex 2D vector rotations; enables context extension (YaRN)."],
            ["Activation Function", "ReLU / Standard GELU", "SwiGLU (Swish-Gated Linear Unit)", "Gating mechanism provides smoother gradients and empirically higher benchmark accuracy."],
            ["Attention Mechanism", "Full Multi-Head (MHA)", "Grouped-Query Attention (GQA)", "Sharing Key/Value heads across query groups cuts KV cache VRAM footprint by 75%."],
            ["Bias Terms", "Linear layer biases included", "No biases (bias=False on all projections)", "Dropping biases reduces parameter footprint and improves training stability at scale."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Transformer Anatomy & Attention", s1_body, pill="Core Architecture", pill_color="rose"))

    # Section 2: MHA vs MQA vs GQA
    s2_body = f"""
    <p>In auto-regressive text generation, previous tokens' Keys and Values are cached in GPU memory (the KV Cache) so they don't need recomputing at each decode step. MHA stores full KV heads for every query head, blowing past GPU VRAM limits at 32k context.</p>

    {svg_card(svg_gqa, "Attention Head Topologies: MHA (Full), GQA (Grouped-Query), MQA (Multi-Query)")}

    {table(
        headers=["Attention Variant", "Query Heads", "Key/Value Heads", "KV Cache Size Relative to MHA", "Production Adoption"],
        rows=[
            ["Multi-Head Attention (MHA)", "$H$", "$H$", "$1.0\\times$ (Baseline)", "GPT-3, Original Transformer, ViT."],
            ["Grouped-Query Attention (GQA)", "$H$", "$G = H / 4$ or $H / 8$", "$0.25\\times$ (75% savings)", "Llama 2/3 (70B), Mistral 7B, Gemma."],
            ["Multi-Query Attention (MQA)", "$H$", "$1$", "$1 / H \\approx 0.03\\times$ (97% savings)", "PaLM, StarCoder (slight perplexity degradation)."]
        ]
    )}
    """
    content.append(section("attention-architectures", "🧠 Attention Matrix: MHA vs MQA vs GQA", s2_body, pill="Memory Optimization", pill_color="purple"))

    # Section 3: KV Cache Math
    s3_body = f"""
    {formula_box(
        katex_display=r"$$\text{Memory}_{\text{KV}} = 2 \times n_{\text{layers}} \times n_{\text{KV\_heads}} \times d_{\text{head}} \times \text{seq\_len} \times \text{batch} \times \text{bytes\_per\_elem}$$",
        reading="KV Cache memory equals two times layers times KV heads times head dimension times sequence length times batch size times precision bytes.",
        symbols=[
            ("2", "Factor of 2 accounts for both Keys and Values"),
            ("n_layers", "Total transformer layers in model (e.g. 80 layers in 70B)"),
            ("n_KV_heads", "Number of distinct Key-Value heads (8 in GQA)"),
            ("seq_len", "Context length in tokens (e.g. 8,192 tokens)"),
            ("bytes_per_elem", "2 bytes for FP16 / BF16, 1 byte for FP8")
        ],
        meaning="KV Cache scales linearly with sequence length and batch size. For a 70B model with 8K context and batch 16, MHA requires 160 GB VRAM (exceeding an 80GB A100 GPU), while GQA drops this to ~20 GB!"
    )}

    {worked_example(
        title="Calculating KV Cache Memory for Llama 3 70B (8K Context, Batch 16 in FP16)",
        steps=[
            ("Identify Model Parameters", "Layers $L = 80$, KV heads $n_{kv} = 8$ (GQA), Head dimension $d = 128$, Seq length $S = 8,192$, Batch $B = 16$, FP16 precision = 2 bytes."),
            ("Apply Formula", r"$$\text{Memory} = 2 \times 80 \times 8 \times 128 \times 8,192 \times 16 \times 2$$"),
            ("Calculate Total Bytes", r"$$\text{Memory} = 42,949,672,960\text{ bytes} \approx 40.0\text{ GB}$$")
        ],
        answer="Under GQA, the KV cache requires exactly 40.0 GB of VRAM. If this model used MHA (64 KV heads), it would require 320 GB of VRAM, making inference impossible on a single node without tensor parallelism!"
    )}
    """
    content.append(section("kv-cache-math", "📐 KV Cache Memory Scaling & Inference Latency", s3_body, pill="Capacity Math", pill_color="emerald"))

    # Section 4: Post-Training Matrix
    s4_body = f"""
    {decision_matrix(
        title="Post-Training Alignment Algorithms",
        options=[
            ("Supervised Fine-Tuning (SFT)", "Teaching format adherence, system prompt compliance, tool schemas, and domain terminology.", "Alleviating hallucinations or teaching reasoning (SFT causes model to overfit to output distribution)."),
            ("Direct Preference Optimization (DPO)", "General preference alignment without running a separate reward model or RL critic network.", "Mathematical and logical verification tasks (DPO can cause length bias and verbosity hacking)."),
            ("Group Relative Policy Optimization (GRPO)", "Verifiable reasoning domains (Math, Coding, Competitive Logic). Drops the critic network entirely by group-normalizing rewards.", "Subjective creative writing where rule-based ground-truth verification is impossible."),
            ("Reinforcement Learning with Verifiable Rewards (RLVR)", "Theorem proving and programming benchmarks where an automated compiler/test suite produces binary 0/1 correctness.", "Ambiguous conversational interactions with human nuance.")
        ]
    )}

    {callout(
        title="Why GRPO (DeepSeekMath / R1) Drops the Critic Network",
        body="In standard PPO, a second 'Critic' neural network (value model) matching the policy model's size must be kept in VRAM to estimate state value baseline $V(s)$. GRPO samples a group of $G$ candidate outputs for the same prompt, computes their task reward, and normalizes advantage across the group: $A_i = \\frac{R_i - \\text{mean}(R)}{\\text{std}(R)}$. This <strong>slashes training VRAM by ~50%</strong> and eliminates unstable value-function training!",
        kind="ai"
    )}
    """
    content.append(section("post-training-matrix", "🎯 Post-Training: SFT, DPO, GRPO & RLVR", s4_body, pill="Post-Training", pill_color="indigo", depth="deep"))

    # Section 5: PEFT & Quantization
    s5_body = f"""
    {subsection("peft-lora-math", "Low-Rank Adaptation (LoRA) Architecture")}
    <p>LoRA freezes pretrained weight matrix $W_0 \\in \\mathbb{{R}}^{{d \\times k}}$ and injects low-rank trainable matrices: $W = W_0 + \\frac{{\\alpha}}{{r}} (B \\cdot A)$, where $A \\sim \\mathcal{{N}}(0, \\sigma^2) \\in \\mathbb{{R}}^{{r \\times k}}$ and $B = 0 \\in \\mathbb{{R}}^{{d \\times r}}$ with rank $r \\ll d$.</p>
    
    {code(
        src=r"""# Scaled Dot-Product Attention in Pure PyTorch with Causal Mask
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    # Q, K, V shape: [batch, heads, seq_len, head_dim]
    d_k = Q.size(-1)
    
    # Compute attention scores
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    
    if mask is not None:
        # Apply -inf mask before softmax to prevent seeing future tokens
        scores = scores.masked_fill(mask == 0, float('-inf'))
        
    attn_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attn_weights, V)
    return output, attn_weights""",
        lang="python",
        title="PyTorch Scaled Dot-Product Attention"
    )}
    """
    content.append(section("peft-quantization", "⚡ LoRA, QLoRA & Serving Optimization", s5_body, pill="PEFT & Code", pill_color="emerald", depth="deep"))

    # Section 6: Information Theory Corner (Candidate Edge)
    s6_body = f"""
    <p>OpenAI coding and deep-dive technical rounds frequently test <strong>information theory fundamentals</strong> (implementing continuous KL divergence, cross-entropy minimization, perplexity bounds). This directly maps to your M.Tech Signal Processing coursework.</p>

    {table(
        headers=["Concept", "Mathematical Formula", "Engineering Interpretation in LLMs"],
        rows=[
            ["Entropy $H(X)$", "$-\\sum p(x) \\log_2 p(x)$", "Average information / uncertainty in the token distribution. A uniform distribution over vocabulary $V$ has $H = \\log_2 |V|$."],
            ["Cross-Entropy", "$-\\sum y_i \\log \\hat{y}_i$", "Training loss for predicting the next token. Equal to expected negative log-likelihood of ground-truth token."],
            ["KL Divergence $D_{\\text{KL}}(P \\parallel Q)$", "$\\sum P(x) \\log \\frac{P(x)}{Q(x)}$", "Relative entropy. Measures penalty in RLHF/DPO to prevent policy model $\\pi_\\theta$ from drifting away from base model $\\pi_{\\text{ref}}$."],
            ["Perplexity (PPL)", "$\\exp(\\text{Cross-EntropyLoss})$", "Geometric average branching factor. PPL of 10 means the model is as confused as picking among 10 equally likely words."]
        ]
    )}

    {code(
        src=r"""import numpy as np

def kl_divergence_continuous(p_samples, q_samples, bins=100):
    # Verbatim OpenAI drill: Compute KL divergence between two continuous empirical distributions
    min_val = min(np.min(p_samples), np.min(q_samples))
    max_val = max(np.max(p_samples), np.max(q_samples))
    
    p_hist, edges = np.histogram(p_samples, bins=bins, range=(min_val, max_val), density=True)
    q_hist, _ = np.histogram(q_samples, bins=bins, range=(min_val, max_val), density=True)
    
    # Epsilon smoothing to prevent division by zero or log(0)
    eps = 1e-12
    p_prob = (p_hist + eps) / np.sum(p_hist + eps)
    q_prob = (q_hist + eps) / np.sum(q_hist + eps)
    
    return np.sum(p_prob * np.log(p_prob / q_prob))""",
        lang="python",
        title="Continuous Empirical KL Divergence (OpenAI Drill)"
    )}
    """
    content.append(section("info-theory-corner", "∑ Information Theory Corner (Candidate Edge)", s6_body, pill="M.Tech Differentiator", pill_color="purple", depth="deep"))

    # Section 7: 35 Interview Flashcards
    qa_list = [
        ("Why do we divide attention scores by sqrt(d_k)?",
         "For large d_k, dot products grow large in magnitude, pushing the softmax function into regions with near-zero gradients (saturation), resulting in vanishing gradients during training.",
         ["Transformer"], "Easy", ["Anthropic", "OpenAI"]),
        ("What is the KV Cache and why does it matter for autoregressive generation?",
         "During token generation, tokens attend to all previous tokens. Caching previous Keys and Values prevents recomputing past activations, reducing per-token generation complexity from O(N^2) to O(N).",
         ["Inference"], "Easy", ["Meta", "Apple"]),
        ("Compare MHA, MQA, and GQA. Why did Llama 3 adopt GQA?",
         "MHA has 1 KV head per Query head (highest RAM). MQA has 1 KV head for all Query heads (lowest RAM, quality degradation). GQA groups Query heads to share KV heads, slashing KV cache memory by 75% with minimal quality loss.",
         ["Architecture"], "Medium", ["Meta", "Mistral"]),
        ("What is RoPE (Rotary Position Embedding) and why is it preferred over learned embeddings?",
         "RoPE multiplies 2D chunks of Query/Key vectors by a 2D rotation matrix. It preserves relative token distance naturally via dot product trigonometry, has zero trainable parameters, and enables context extrapolation.",
         ["Embeddings"], "Medium", ["Anthropic", "Google"]),
        ("Why does GRPO drop the critic network, and how does it estimate advantage?",
         "GRPO generates a group of G candidate answers for a single prompt, scores them, and computes advantage by normalizing rewards across the group: A_i = (R_i - mean(R)) / std(R). This eliminates the critic model, saving ~50% VRAM.",
         ["Alignment", "RL"], "Hard", ["DeepSeek", "OpenAI"]),
        ("What is LoRA and how does it achieve parameter-efficient fine-tuning?",
         "LoRA freezes base weights W0 and decomposes weight updates into two low-rank matrices: delta_W = (alpha / r) * B * A, where r << d. This reduces trainable parameters by >99% and merges into W0 at inference with zero latency penalty.",
         ["PEFT"], "Medium", ["Apple AI", "Meta"]),
        ("What is PagedAttention and what problem does it solve in vLLM?",
         "In standard inference, KV cache requires contiguous virtual memory, causing 60-80% memory fragmentation and memory waste. PagedAttention divides the KV cache into non-contiguous fixed-size memory blocks (virtual memory paging), boosting serving throughput by 2x-4x.",
         ["Serving"], "Hard", ["vLLM", "Anyscale"]),
        ("What is the mathematical relationship between Perplexity and Cross-Entropy loss?",
         "Perplexity is the exponentiated cross-entropy loss: PPL = exp(Loss). It represents the effective vocabulary size the model is uncertain between at each token.",
         ["Info Theory"], "Easy", ["OpenAI", "DeepMind"]),
        ("What is context rot in long-context LLMs?",
         "The phenomenon where an LLM's retrieval accuracy and reasoning degrade significantly as context size grows towards the maximum window limit, long before hitting the hard context boundary.",
         ["Context"], "Medium", ["Anthropic", "Perplexity"]),
        ("Explain the difference between Speculative Decoding draft and target models.",
         "A small, fast 'draft model' speculatively generates K tokens autoregressively. The large 'target model' evaluates all K tokens in a single parallel forward pass, accepting valid tokens and regenerating on first mismatch, achieving 2x-3x speedup.",
         ["Latency"], "Hard", ["Google", "Apple"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 35 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
