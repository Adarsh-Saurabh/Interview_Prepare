# mod_math_ml.py - Math Foundations for Machine Learning Module Generator
# Conforms to instruction.md Part 7.6 Specification (P1 Track C)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Linear Algebra & SVD"),
        ("bayes-probability", "🎲 Bayes' Theorem & Base-Rate Fallacy"),
        ("mle-map-derivation", "📐 MLE vs MAP & Regularization Equivalences"),
        ("info-theory-kl", "∑ Information Theory: Forward vs Reverse KL"),
        ("signal-ml-bridge", "📡 Signal Processing to ML Bridge (M.Tech Edge)"),
        ("numerical-stability", "🔢 Numerical Stability & Log-Sum-Exp"),
        ("interview-flashcards", "🎯 30 Top Tech Interview Q&As")
    ]

    # SVG 1: SVD Geometric Transformation
    svg_svd = """
    <svg viewBox="0 0 880 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="svd-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <g transform="translate(20, 30)">
        <!-- Stage 1: Unit Circle -->
        <rect x="0" y="0" width="160" height="150" rx="8" fill="#111827" stroke="#1e293b" />
        <circle cx="80" cy="75" r="45" fill="none" stroke="#38bdf8" stroke-width="2" />
        <text x="80" y="135" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">1. Input Unit Circle</text>

        <!-- Arrow V^T -->
        <line x1="165" y1="75" x2="225" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#svd-arr)" />
        <text x="195" y="65" fill="#c084fc" font-size="11" font-weight="800" text-anchor="middle">V^T (Rotate)</text>

        <!-- Stage 2: Rotated -->
        <rect x="230" y="0" width="160" height="150" rx="8" fill="#111827" stroke="#1e293b" />
        <circle cx="310" cy="75" r="45" fill="none" stroke="#c084fc" stroke-width="2" stroke-dasharray="4,4" />
        <text x="310" y="135" fill="#c084fc" font-size="11" font-weight="700" text-anchor="middle">2. Orthonormal Basis</text>

        <!-- Arrow Sigma -->
        <line x1="395" y1="75" x2="455" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#svd-arr)" />
        <text x="425" y="65" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Sigma (Scale)</text>

        <!-- Stage 3: Stretched Ellipse -->
        <rect x="460" y="0" width="160" height="150" rx="8" fill="#111827" stroke="#1e293b" />
        <ellipse cx="540" cy="75" rx="60" ry="25" fill="none" stroke="#fbbf24" stroke-width="2" />
        <text x="540" y="135" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">3. Singular Values</text>

        <!-- Arrow U -->
        <line x1="625" y1="75" x2="685" y2="75" stroke="#38bdf8" stroke-width="2" marker-end="url(#svd-arr)" />
        <text x="655" y="65" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">U (Rotate)</text>

        <!-- Stage 4: Output Rotated Ellipse -->
        <rect x="690" y="0" width="160" height="150" rx="8" fill="#111827" stroke="#064e3b" stroke-width="1.5" />
        <ellipse cx="770" cy="75" rx="60" ry="25" fill="none" stroke="#34d399" stroke-width="2" transform="rotate(-30 770 75)" />
        <text x="770" y="135" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">4. Final A*x Ellipse</text>
      </g>
    </svg>
    """

    content = []

    # Section 1: Sprint Core
    s1_body = f"""
    {one_liner("Singular Value Decomposition (SVD) states that any real matrix A decomposes into A = U Sigma V^T: geometrically, any linear mapping represents an orthonormal rotation (V^T), an axis-aligned scaling along singular values (Sigma), and a final rotation (U).")}

    <p>Mathematics in Applied Scientist and AI roles is not abstract theorem-proving; it tests geometric intuition, optimization guarantees, and information-theoretic proofs.</p>

    {svg_card(svg_svd, "SVD Geometric Decomposition: Rotate -> Scale -> Rotate")}

    {formula_box(
        katex_display=r"$$A = U \Sigma V^T = \sum_{i=1}^r \sigma_i u_i v_i^T$$",
        reading="Matrix A factors into orthogonal matrix U times diagonal matrix Sigma times orthogonal matrix V transpose.",
        symbols=[
            ("U", "Left singular vectors (eigenvectors of A A^T, size M x M)"),
            ("Sigma", "Singular values in descending order sigma_1 >= sigma_2 >= ... >= 0 (size M x N)"),
            ("V^T", "Right singular vectors (eigenvectors of A^T A, size N x N)"),
            ("r", "Rank of matrix A (number of non-zero singular values)")
        ],
        meaning="Eckart-Young-Mirsky Theorem: The optimal rank-k approximation of matrix A that minimizes Frobenius norm error is obtained by truncating SVD to the top k singular values. This forms the mathematical backbone of PCA, Latent Semantic Analysis, and LoRA!"
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: Linear Algebra & SVD", s1_body, pill="Linear Algebra", pill_color="purple"))

    # Section 2: Bayes & Base-Rate Fallacy
    s2_body = f"""
    {formula_box(
        katex_display=r"$$P(A \mid B) = \frac{P(B \mid A) P(A)}{P(B)} = \frac{P(B \mid A) P(A)}{P(B \mid A) P(A) + P(B \mid \neg A) P(\neg A)}$$",
        reading="Posterior probability equals likelihood times prior divided by marginal evidence.",
        symbols=[
            ("P(A | B)", "Posterior probability (updated belief after seeing evidence B)"),
            ("P(B | A)", "Likelihood of seeing evidence B given condition A"),
            ("P(A)", "Prior probability of condition A before seeing evidence"),
            ("P(B)", "Total marginal probability of evidence B")
        ],
        meaning="Crucial in interview questions regarding rare events (fraud detection, medical diagnosis). When the prior P(A) is very small (0.1%), even a 99% accurate test yields a posterior under 10%!"
    )}

    {worked_example(
        title="Base-Rate Fallacy: Disease Diagnosis with 99% Test Accuracy and 0.1% Prevalence",
        steps=[
            ("Identify Priors and Likelihoods", "Prevalence $P(D) = 0.001$, so $P(\\neg D) = 0.999$. Test sensitivity (True Positive Rate) $P(+ \\mid D) = 0.99$. False Positive Rate $P(+ \\mid \\neg D) = 1 - 0.99 = 0.01$."),
            ("Apply Total Probability Law for Marginal P(+)", r"$$P(+) = P(+ \mid D) P(D) + P(+ \mid \neg D) P(\neg D) = (0.99)(0.001) + (0.01)(0.999) = 0.00099 + 0.00999 = 0.01098$$"),
            ("Calculate Posterior P(D | +)", r"$$P(D \mid +) = \frac{(0.99)(0.001)}{0.01098} = \frac{0.00099}{0.01098} \approx 0.09016 \approx 9.02\%$$")
        ],
        answer="Even though the test is 99% accurate, an individual testing positive has only a ~9% chance of actually having the disease! 91% of positive results are false positives because healthy people vastly outnumber sick people."
    )}
    """
    content.append(section("bayes-probability", "🎲 Bayes' Theorem & Base-Rate Fallacy", s2_body, pill="Probability", pill_color="amber"))

    # Section 3: MLE vs MAP
    s3_body = f"""
    <p>Interviews constantly ask: <em>'What is the probabilistic connection between MAP and L1/L2 regularization?'</em></p>

    {table(
        headers=["Estimation Framework", "Objective Function", "Assumed Prior Distribution", "Equivalent Regularization"],
        rows=[
            ["Maximum Likelihood (MLE)", "$\\arg\\max_\\theta \\log P(D \\mid \\theta)$", "Uniform Prior (All values equally likely).", "Standard Unregularized Linear Regression (OLS)."],
            ["Maximum A Posteriori (MAP)", "$\\arg\\max_\\theta [\\log P(D \\mid \\theta) + \\log P(\\theta)]$", "Zero-Mean Gaussian Prior: $\\mathcal{N}(0, \\sigma^2)$", "<strong>L2 Regularization (Ridge / Weight Decay)</strong>."],
            ["Maximum A Posteriori (MAP)", "$\\arg\\max_\\theta [\\log P(D \\mid \\theta) + \\log P(\\theta)]$", "Zero-Mean Laplace Prior: $\\text{Laplace}(0, b)$", "<strong>L1 Regularization (Lasso / Sparsity)</strong>."]
        ]
    )}
    """
    content.append(section("mle-map-derivation", "📐 MLE vs MAP & Regularization Equivalences", s3_body, pill="Estimation", pill_color="emerald", depth="deep"))

    # Section 4: Forward vs Reverse KL
    s4_body = f"""
    {table(
        headers=["KL Direction", "Formula", "Behavior on Bimodal Distribution", "Production Adoption"],
        rows=[
            ["Forward KL (Zero-Avoiding)", "$D_{\\text{KL}}(P \\parallel Q) = \\int P \\log \\frac{P}{Q}$", "<strong>Mass-Covering</strong>: Q stretches to cover all regions where P > 0, even placing mass in empty valleys.", "Maximum Likelihood training in standard language models."],
            ["Reverse KL (Zero-Forcing)", "$D_{\\text{KL}}(Q \\parallel P) = \\int Q \\log \\frac{Q}{P}$", "<strong>Mode-Seeking</strong>: Q locks onto a single peak of P where Q can match P closely, ignoring other modes.", "Variational Inference (VAE), RLHF / DPO policy alignment."]
        ]
    )}
    """
    content.append(section("info-theory-kl", "∑ Information Theory: Forward vs Reverse KL", s4_body, pill="Info Theory", pill_color="rose", depth="deep"))

    # Section 5: Signal to ML Bridge
    s5_body = f"""
    <p>Your M.Tech in Signal Processing provides a direct differentiator in questions connecting classic signal theory to modern generative models and vision:</p>

    {table(
        headers=["Signal Processing Foundation", "Core Theorem & Formula", "Modern Deep Learning Counterpart"],
        rows=[
            ["Convolution Theorem", "$\\mathcal{F}\\{f * g\\} = \\mathcal{F}\\{f\\} \\cdot \\mathcal{F}\\{g\\}$", "Spatial Conv2D is equivalent to point-wise frequency multiplication; Fourier Neural Operators (FNO)."],
            ["Nyquist-Shannon Sampling", "$f_s \\ge 2 f_{\\max}$ (Sampling frequency must double bandwidth)", "Aliasing in audio models; stride and downsampling without anti-aliasing blur filters."],
            ["Kalman Filtering", "Recursive Bayesian state estimation with Gaussian noise.", "State-Space Models (Mamba / S4) and linear recurrent attention layers."],
            ["Stochastic Differential Equations (SDEs)", "Itô calculus and reverse-time drift estimation.", "Score-based diffusion models (Song et al.) and flow matching."]
        ]
    )}
    """
    content.append(section("signal-ml-bridge", "📡 Signal Processing to ML Bridge (M.Tech Edge)", s5_body, pill="Signal Processing", pill_color="teal", depth="deep"))

    # Section 6: Numerical Stability
    s6_body = f"""
    {code(
        src=r"""import numpy as np

def stable_softmax(logits):
    # Subtracting the maximum prevents overflow into inf in exp()!
    # Mathematically identical because exp(x - c) / sum(exp(x - c)) == exp(x) / sum(exp(x))
    shifted_logits = logits - np.max(logits, axis=-1, keepdims=True)
    exp_logits = np.exp(shifted_logits)
    return exp_logits / np.sum(exp_logits, axis=-1, keepdims=True)""",
        lang="python",
        title="Numerically Stable Softmax Implementation"
    )}
    """
    content.append(section("numerical-stability", "🔢 Numerical Stability & Log-Sum-Exp", s6_body, pill="Math Code", pill_color="amber", depth="deep"))

    # Section 7: 30 Interview Flashcards
    qa_list = [
        ("What does SVD do geometrically, and how does it relate to PCA?",
         "SVD decomposes any real matrix into a rotation (V^T), scaling (Sigma), and second rotation (U). PCA performs an eigendecomposition on the centered covariance matrix (X^T X / (N-1)), where right singular vectors V of X correspond exactly to the principal components (eigenvectors).",
         ["SVD", "PCA"], "Medium", ["Google", "DeepMind"]),
        ("Prove that MAP estimation with a Gaussian prior is equivalent to L2-regularized MLE.",
         "Under Bayes' rule: log P(theta | D) = log P(D | theta) + log P(theta). For a Gaussian prior P(theta) ~ N(0, sigma^2), log P(theta) = - (1 / (2*sigma^2)) * ||theta||_2^2 + const. Maximizing the posterior is thus mathematically identical to maximizing log-likelihood minus lambda * ||theta||_2^2.",
         ["Regularization"], "Hard", ["OpenAI", "Meta"]),
        ("Why is Forward KL mass-covering while Reverse KL is mode-seeking?",
         "In Forward KL (P || Q), if P(x) > 0 but Q(x) -> 0, the integrand P log(P/Q) diverges to infinity, forcing Q to cover all modes of P. In Reverse KL (Q || P), if P(x) = 0 and Q(x) > 0, Q log(Q/P) explodes, forcing Q to remain zero anywhere P is zero (locking onto one mode).",
         ["Info Theory"], "Hard", ["DeepMind", "Anthropic"]),
        ("Why must softmax subtract the max element before exponentiating?",
         "In standard 32-bit floating point, exp(x) overflows to +inf when x > 88.7. Subtracting max(x) ensures the maximum exponent evaluated is exp(0) = 1.0, eliminating float overflow while preserving exact probability proportions.",
         ["Numerical"], "Easy", ["Apple AI", "Nvidia"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 30 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
