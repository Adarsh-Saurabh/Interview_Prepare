# mod_ml_core.py - Classical ML & Deep Learning Core Module Generator
# Conforms to instruction.md Part 7.3 Specification (P0 Track C)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: ML Map, Bias-Variance & Optimizers"),
        ("bias-variance-svg", "📐 Bias-Variance Decomposition & Learning Curves"),
        ("l1-l2-geometry", "🎯 L1 vs L2 Regularization & Sparsity Geometry"),
        ("numpy-backprop", "💻 NumPy 2-Layer Neural Network From Scratch"),
        ("tree-methods-xgboost", "🌲 Trees, Ensembles & XGBoost Second-Order Math"),
        ("normalization-dynamics", "⚡ BatchNorm vs LayerNorm vs RMSNorm Dynamics"),
        ("ml-system-design", "🏗️ 9-Step ML System Design Framework (Recite Out Loud)"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: Bias-Variance Tradeoff Curve
    svg_bias_variance = """
    <svg viewBox="0 0 880 320" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="optZone" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#10b981" stop-opacity="0.02"/>
        </linearGradient>
      </defs>
      <rect x="20" y="20" width="840" height="280" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
      <!-- Axes -->
      <line x1="80" y1="260" x2="800" y2="260" stroke="#64748b" stroke-width="2"/>
      <line x1="80" y1="260" x2="80" y2="40" stroke="#64748b" stroke-width="2"/>
      <text x="790" y="280" fill="#94a3b8" font-size="12" font-weight="600" text-anchor="end">Model Capacity / Complexity →</text>
      <text x="70" y="50" fill="#94a3b8" font-size="12" font-weight="600" text-anchor="end" transform="rotate(-90 70,50)">Expected Test Error →</text>
      
      <!-- Optimal Zone -->
      <rect x="380" y="40" width="120" height="220" fill="url(#optZone)" stroke="#10b981" stroke-dasharray="4,4"/>
      <text x="440" y="60" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Optimal Capacity</text>
      <text x="440" y="75" fill="#94a3b8" font-size="10" text-anchor="middle">Min Total Error</text>

      <!-- Bias Squared Curve (Decreasing) -->
      <path d="M 100 80 Q 250 200 440 220 T 780 240" fill="none" stroke="#38bdf8" stroke-width="3"/>
      <text x="140" y="110" fill="#38bdf8" font-size="12" font-weight="700">Bias² (Underfitting)</text>

      <!-- Variance Curve (Increasing) -->
      <path d="M 100 245 Q 350 240 440 215 T 780 60" fill="none" stroke="#f43f5e" stroke-width="3"/>
      <text x="760" y="90" fill="#f43f5e" font-size="12" font-weight="700" text-anchor="end">Variance (Overfitting)</text>

      <!-- Total Error Curve (U-Shape) -->
      <path d="M 100 70 Q 250 180 440 160 T 780 50" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-dasharray="6,3"/>
      <text x="440" y="145" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">Total Error = Bias² + Var + σ²</text>

      <!-- Irreducible Error baseline -->
      <line x1="80" y1="240" x2="800" y2="240" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3,3"/>
      <text x="790" y="235" fill="#c084fc" font-size="10" text-anchor="end">Irreducible Error (σ² Noise Floor)</text>
    </svg>
    """

    # SVG 2: L1 vs L2 Sparsity Geometry
    svg_l1_l2 = """
    <svg viewBox="0 0 880 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="20" y="20" width="840" height="260" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
      <!-- L1 Diamond -->
      <g transform="translate(60, 40)">
        <text x="160" y="20" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">L1 Lasso: Diamond Ball (|w1| + |w2| ≤ C)</text>
        <line x1="60" y1="140" x2="260" y2="140" stroke="#64748b" stroke-width="1.5"/>
        <line x1="160" y1="40" x2="160" y2="240" stroke="#64748b" stroke-width="1.5"/>
        <polygon points="160,80 220,140 160,200 100,140" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="2"/>
        <!-- Loss Contours hitting corner -->
        <ellipse cx="230" cy="70" rx="60" ry="40" fill="none" stroke="#f59e0b" stroke-width="1.5" transform="rotate(-20 230 70)"/>
        <ellipse cx="230" cy="70" rx="90" ry="60" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" transform="rotate(-20 230 70)"/>
        <!-- Intersection point on axis -->
        <circle cx="160" cy="80" r="5" fill="#f43f5e"/>
        <text x="175" y="80" fill="#f43f5e" font-size="11" font-weight="700">Corner on Axis: w1 = 0</text>
        <text x="160" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Sharp corners hit contours on axes → Exact Sparsity</text>
      </g>

      <!-- L2 Circle -->
      <g transform="translate(480, 40)">
        <text x="160" y="20" fill="#a855f7" font-size="14" font-weight="800" text-anchor="middle">L2 Ridge: Circular Ball (w1² + w2² ≤ C)</text>
        <line x1="60" y1="140" x2="260" y2="140" stroke="#64748b" stroke-width="1.5"/>
        <line x1="160" y1="40" x2="160" y2="240" stroke="#64748b" stroke-width="1.5"/>
        <circle cx="160" cy="140" r="55" fill="rgba(168, 85, 247, 0.15)" stroke="#a855f7" stroke-width="2"/>
        <!-- Loss Contours hitting curved arc -->
        <ellipse cx="230" cy="70" rx="60" ry="40" fill="none" stroke="#f59e0b" stroke-width="1.5" transform="rotate(-20 230 70)"/>
        <!-- Intersection point off axis -->
        <circle cx="205" cy="105" r="5" fill="#34d399"/>
        <text x="215" y="110" fill="#34d399" font-size="11" font-weight="700">Tangent off-axis: w1 ≠ 0, w2 ≠ 0</text>
        <text x="160" y="235" fill="#94a3b8" font-size="11" text-anchor="middle">Smooth sphere shrinks all weights → Small but non-zero</text>
      </g>
    </svg>
    """

    # SVG 3: 9-Step ML System Design Flowchart
    svg_ml_design = """
    <svg viewBox="0 0 900 240" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="880" height="220" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
      <g transform="translate(25, 30)">
        <!-- Step 1 to 5 row 1 -->
        <rect x="0" y="0" width="150" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="75" y="25" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">1. Problem Formulation</text>
        <text x="75" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Business goal, framing</text>

        <line x1="150" y1="30" x2="175" y2="30" stroke="#64748b" stroke-width="2" marker-end="url(#arr)"/>

        <rect x="175" y="0" width="150" height="60" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
        <text x="250" y="25" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">2. Metrics Definition</text>
        <text x="250" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Offline (AUC) vs Online (CTR)</text>

        <line x1="325" y1="30" x2="350" y2="30" stroke="#64748b" stroke-width="2"/>

        <rect x="350" y="0" width="150" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="425" y="25" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">3. Data &amp; Collection</text>
        <text x="425" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Labeling, negative sampling</text>

        <line x1="500" y1="30" x2="525" y2="30" stroke="#64748b" stroke-width="2"/>

        <rect x="525" y="0" width="150" height="60" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="600" y="25" fill="#f43f5e" font-size="11" font-weight="800" text-anchor="middle">4. Feature Engineering</text>
        <text x="600" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Embeddings, Leakage checks</text>

        <line x1="675" y1="30" x2="700" y2="30" stroke="#64748b" stroke-width="2"/>

        <rect x="700" y="0" width="150" height="60" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
        <text x="775" y="25" fill="#a855f7" font-size="11" font-weight="800" text-anchor="middle">5. Model Dev &amp; Offline</text>
        <text x="775" y="45" fill="#94a3b8" font-size="9" text-anchor="middle">Baseline, GBDT vs Deep Net</text>
        
        <!-- Row 2 -->
        <rect x="80" y="100" width="160" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="160" y="125" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">6. Prediction Service</text>
        <text x="160" y="145" fill="#94a3b8" font-size="9" text-anchor="middle">Batch vs Online (p99 latency)</text>

        <line x1="240" y1="130" x2="275" y2="130" stroke="#64748b" stroke-width="2"/>

        <rect x="275" y="100" width="160" height="60" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
        <text x="355" y="125" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">7. Online Eval &amp; A/B</text>
        <text x="355" y="145" fill="#94a3b8" font-size="9" text-anchor="middle">Interleaving, Canaries</text>

        <line x1="435" y1="130" x2="470" y2="130" stroke="#64748b" stroke-width="2"/>

        <rect x="470" y="100" width="160" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="550" y="125" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">8. Monitoring &amp; Drift</text>
        <text x="550" y="145" fill="#94a3b8" font-size="9" text-anchor="middle">Covariate shift, PSI, Alerts</text>

        <line x1="630" y1="130" x2="665" y2="130" stroke="#64748b" stroke-width="2"/>

        <rect x="665" y="100" width="160" height="60" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
        <text x="745" y="125" fill="#f43f5e" font-size="11" font-weight="800" text-anchor="middle">9. Continual Learning</text>
        <text x="745" y="145" fill="#94a3b8" font-size="9" text-anchor="middle">Daily retraining, Shadow rollouts</text>
      </g>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P0 Track C", "rose"), ("AI / ML Loop", "indigo"), ("Applied Scientist", "teal"), ("15-Min Sprint", "amber")])
        + callout(
            "The Machine Learning Ground Truth for Big Tech Loops",
            "Classical ML and Deep Learning core fundamentals are the absolute floor in technical rounds at Google DeepMind, OpenAI, Anthropic, Apple AI, and Qualcomm. Interviewers immediately test whether you understand the bias-variance decomposition, optimization geometry, loss surface dynamics, and practical system design - or if you only know how to call HuggingFace APIs.",
            "important"
        )
        + numbers_card("Machine Learning & Deep Learning Core Metrics", [
            ("Bias² + Var + σ²", "Expected Test Error", "Full decomposition into bias squared, variance, and irreducible noise floor"),
            ("O(N d)", "Linear Regression Gradient Step", "Per-epoch batch gradient descent complexity on N samples with d features"),
            ("2-Layer Net", "Verbatim Coding Problem", "NumPy forward and backward pass implementation tested at OpenAI & DeepMind"),
            ("9 Steps", "Universal ML System Design", "Standardized framework for recommendation, fraud, and retrieval rounds")
        ])
        + subsection(
            "algo-matrix",
            "Algorithm Selection Matrix: When to Use & When to Avoid",
            table(
                ["Algorithm", "Best Suited For", "Avoid When", "Key Hyperparameters", "Time / Space"],
                [
                    ["Linear / Logistic", "Tabular data, sparse text (BoW), strict interpretability", "High non-linearity, complex feature interactions", "C (1/λ), penalty (L1/L2)", "O(nd) / O(d)"],
                    ["Random Forest", "Tabular, mixed types, noisy features, robust baseline", "Extremely high dimensions, real-time <5ms latency", "n_estimators, max_depth, max_features", "O(M·n·log(n)·d) / High"],
                    ["XGBoost / LightGBM", "Kaggle champion for tabular data, heterogeneous features", "Unstructured data (vision/audio), pure streaming data", "learning_rate, max_depth, subsample, reg_lambda", "O(M·n·d) / Moderate"],
                    ["SVM (RBF Kernel)", "High dimensions, small sample size (n < 10k), clear margins", "Large datasets (n > 50k - quadratic kernel gram matrix)", "C, gamma (1/2σ²)", "O(n²d) to O(n³) / O(n²)"],
                    ["k-Nearest Neighbors", "Low-dimensional non-parametric baseline, recommendation", "High dimensions (Curse of dimensionality), low-latency", "k, metric (cosine, euclidean)", "O(nd) query / O(nd)"],
                    ["K-Means Clustering", "Spherical, balanced, convex clusters with known k", "Non-convex shapes (use DBSCAN), varied cluster densities", "k, init='k-means++', n_init", "O(k·n·d·iter) / O(nd)"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "optimizer-progression",
            "Optimizer Evolution: How Each Fixes the Predecessor's Fatal Flaw",
            table(
                ["Optimizer", "Update Rule Intuition", "Fatal Flaw It Fixes", "Remaining Flaw"],
                [
                    ["Vanilla SGD", r"$\theta_{t+1} = \theta_t - \eta \nabla L$", "Batch gradient too slow on huge datasets", "Oscillates heavily in ravines, slow progress"],
                    ["SGD + Momentum", r"$v_t = \gamma v_{t-1} + \eta \nabla L; \theta = \theta - v_t$", "Adds velocity to barrel through ravines and flat plateaus", "Overshoots valleys without anticipation"],
                    ["Nesterov (NAG)", r"$v_t = \gamma v_{t-1} + \eta \nabla L(\theta - \gamma v_{t-1})$", "Looks ahead before taking momentum step to damp oscillations", "Same uniform learning rate for all parameters"],
                    ["Adagrad", r"$G_t = G_{t-1} + g_t^2; \theta = \theta - \frac{\eta}{\sqrt{G_t + \epsilon}} g_t$", "Adapts per-parameter LR for sparse vs frequent features", "G_t accumulates monotonically → LR shrinks to 0 early!"],
                    ["RMSProp", r"$v_t = \beta v_{t-1} + (1-\beta) g_t^2$ (Exponential Moving Average)", "Fixes Adagrad's dying learning rate with leaky EMA history", "Lacks momentum; noisy updates on stochastic minibatches"],
                    ["Adam", r"$m_t = EMA(g_t), v_t = EMA(g_t^2)$, bias-corrected", "Combines 1st moment (momentum) + 2nd moment (adaptive scale)", "Weight decay under L2 is corrupted by adaptive variance"],
                    ["AdamW", r"$\theta_{t+1} = \theta_t(1 - \eta \lambda) - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$", "Decouples weight decay from adaptive gradient scaling", "Standard for Transformers & Deep Learning worldwide!"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "activations-comparison",
            "Activation Functions Comparison: Saturation & Gradient Flow",
            table(
                ["Activation", "Formula", "Output Range", "Zero-Centered?", "Interview Traps & Dynamics"],
                [
                    ["Sigmoid", r"$\sigma(z) = \frac{1}{1 + e^{-z}}$", "(0, 1)", "❌ No (all positive)", "Vanishing gradient when |z| > 4 (max σ' is only 0.25!). Causes zig-zag updates."],
                    ["Tanh", r"$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$", "(-1, 1)", "✅ Yes", "Still saturates at extremes, causing vanishing gradients in deep networks."],
                    ["ReLU", r"$\max(0, z)$", "[0, ∞)", "❌ No", "Dying ReLU problem: if neuron outputs negative, gradient is 0 forever."],
                    ["LeakyReLU", r"$\max(\alpha z, z), \alpha \approx 0.01$", "(-∞, ∞)", "Partial", "Prevents dying ReLU by allowing a small gradient leak in the negative regime."],
                    ["GELU", r"$z \cdot \Phi(z) \approx z \cdot \sigma(1.702 z)$", "(-0.17, ∞)", "Partial", "Smooth, probabilistic gating. Used in BERT, GPT-2/3, ViT."],
                    ["SwiGLU", r"$\text{Swish}(xW) \otimes (xV)$", "(-∞, ∞)", "Partial", "Gated Linear Unit. State-of-the-art in LLaMA 2/3, Mistral, PaLM."]
                ]
            ),
            depth="sprint"
        )
    )

    # Section 2: Bias-Variance & Regularization
    bv_html = (
        subsection(
            "bias-variance-decomp",
            "The Formal Bias-Variance Decomposition Derivation",
            formula_box(
                r"\mathbb{E}[(y - \hat{f}(x))^2] = (\mathbb{E}[\hat{f}(x)] - f(x))^2 + \mathbb{E}[(\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2] + \sigma^2",
                "Expected squared test error equals bias squared plus model variance plus irreducible noise",
                [
                    ("Bias²", "Error from flawed model assumptions or insufficient model capacity (underfitting)."),
                    ("Variance", "Sensitivity of the model to small fluctuations in the training set (overfitting)."),
                    ("σ²", "Irreducible data noise variance from measurement noise or latent unobserved factors.")
                ],
                "Total test error can never fall below the irreducible noise floor σ² regardless of model size or dataset scale."
            )
            + svg_card("Bias-Variance Tradeoff Curve & Model Capacity", svg_bias_variance)
            + callout(
                "Interview Derivation Walkthrough: Why Error Decomposes into Three Terms",
                r"Let true target $y = f(x) + \epsilon$ where $\mathbb{E}[\epsilon] = 0$ and $\text{Var}(\epsilon) = \sigma^2$. The estimator is $\hat{f}(x)$." + "\n"
                r"Expand $\mathbb{E}[(y - \hat{f})^2] = \mathbb{E}[(f + \epsilon - \hat{f})^2] = \mathbb{E}[((f - \hat{f}) + \epsilon)^2]$. "
                r"Because noise $\epsilon$ is independent of our model estimate $\hat{f}$, cross terms vanish: $\mathbb{E}[2(f - \hat{f})\epsilon] = 0$. "
                r"Now add and subtract $\mathbb{E}[\hat{f}]$ inside $(f - \hat{f})$: $(f - \mathbb{E}[\hat{f}] + \mathbb{E}[\hat{f}] - \hat{f})^2$. "
                r"Squaring yields $(f - \mathbb{E}[\hat{f}])^2$ [Bias²] + $\mathbb{E}[(\hat{f} - \mathbb{E}[\hat{f}])^2]$ [Variance] + cross terms which cancel out to 0, plus $\mathbb{E}[\epsilon^2] = \sigma^2$ [Irreducible Noise]!",
                "tip"
            )
            + table(
                ["Learning Curve Symptom", "Underlying Diagnosis", "Immediate Corrective Remedies"],
                [
                    ["High Train Error + High Validation Error (Both flat)", "High Bias (Underfitting)", "Increase model capacity, add features, polynomial features, decrease regularization (decrease λ, increase C)."],
                    ["Low Train Error + High Validation Error (Large Generalization Gap)", "High Variance (Overfitting)", "Add more training data, add regularization (L1/L2), dropout, feature selection, reduce model depth/width, early stopping."],
                    ["Both Train and Val Error slowly decreasing, plateau not reached", "Under-trained", "Train for more epochs, tune learning rate, verify optimizer convergence."],
                    ["Validation Error drops then climbs while Train Error drops to zero", "Classic Overfitting", "Check checkpoint at minimum val loss; implement Early Stopping with patience=5."]
                ]
            ),
            depth="deep"
        )
        + subsection(
            "l1-vs-l2-geom",
            "L1 (Lasso) vs L2 (Ridge) Regularization & Sparsity Geometry",
            svg_card("Geometric Proof: Why L1 Generates Exact Feature Sparsity", svg_l1_l2)
            + callout(
                "Why L1 Yields Sparsity (The Interview Proof)",
                r"Under constrained optimization (KKT conditions), minimizing MSE subject to a norm constraint $\Omega(w) \le C$ means finding the point where the elliptical loss contour first touches the norm boundary." + "\n"
                r"• L1 norm $\|w\|_1 \le C$ forms a diamond with sharp vertices along the coordinate axes ($w_i = 0$). The elliptical contours of the quadratic loss are far more likely to make tangent contact at these sharp coordinate corners, setting entire weights exactly to 0 (feature selection)." + "\n"
                r"• L2 norm $\|w\|_2^2 \le C$ is a smooth sphere/circle with continuous gradient everywhere. The point of tangency almost never falls on an axis, shrinking all weights proportionally toward zero without setting any to exact zero.",
                "tip"
            )
            + decision_matrix(
                "Regularization Technique Selection Guide",
                [
                    ("L1 (Lasso)", "Need exact feature selection or sparse interpretable model; lots of irrelevant features.", "Features are highly correlated (Lasso arbitrarily picks one and drops the rest)."),
                    ("L2 (Ridge)", "Features are dense and collinear; need smooth shrinkage without dropping variables.", "Need a sparse model or feature selection (Ridge leaves all weights non-zero)."),
                    ("ElasticNet", "Dataset has p >> n with groups of strongly correlated predictors.", "Simple low-dimensional models where L1 or L2 alone suffices with lower hyperparameter overhead."),
                    ("Dropout (p=0.1-0.5)", "Deep neural networks and dense MLPs to break co-adaptation between neurons.", "Small tabular neural nets or combined with BatchNorm (can destabilize variance statistics)."),
                    ("Weight Decay (AdamW)", "Training Transformers and deep networks with Adam optimizer.", "Non-adaptive SGD (where standard L2 penalty on loss is already mathematically identical).")
                ]
            ),
            depth="deep"
        )
    )

    # Section 3: Backprop from Scratch (NumPy)
    backprop_code = r'''import numpy as np

class TwoLayerMLP:
    """
    2-Layer Neural Network with ReLU activation built in pure NumPy.
    Forward and backward passes implemented from scratch.
    x (N, d_in) -> Linear(W1, b1) -> ReLU -> Linear(W2, b2) -> CrossEntropyLoss
    """
    def __init__(self, d_in: int, d_hidden: int, d_out: int, lr: float = 0.01):
        # He initialization for ReLU layer, Xavier for output layer
        self.W1 = np.random.randn(d_in, d_hidden) * np.sqrt(2.0 / d_in)
        self.b1 = np.zeros((1, d_hidden))
        self.W2 = np.random.randn(d_hidden, d_out) * np.sqrt(1.0 / d_hidden)
        self.b2 = np.zeros((1, d_out))
        self.lr = lr

    def forward(self, X: np.ndarray) -> np.ndarray:
        """Forward pass caching intermediate activations for backprop."""
        self.X = X                                      # (N, d_in)
        self.Z1 = np.dot(X, self.W1) + self.b1         # (N, d_hidden)
        self.A1 = np.maximum(0, self.Z1)               # ReLU activation
        self.Z2 = np.dot(self.A1, self.W2) + self.b2   # Logits (N, d_out)
        
        # Numerically stable Softmax
        exp_shifted = np.exp(self.Z2 - np.max(self.Z2, axis=1, keepdims=True))
        self.probs = exp_shifted / np.sum(exp_shifted, axis=1, keepdims=True)
        return self.probs

    def backward(self, y_true: np.ndarray) -> float:
        """
        Backward pass using analytical chain rule.
        y_true: integer class labels (N,) or one-hot (N, d_out)
        """
        N = self.X.shape[0]
        
        # 1. Gradient of Softmax + Cross-Entropy Loss w.r.t Z2: dL/dZ2 = (p - y) / N
        dZ2 = self.probs.copy()
        if y_true.ndim == 1:
            dZ2[np.arange(N), y_true] -= 1.0
        else:
            dZ2 -= y_true
        dZ2 /= N

        # 2. Gradients w.r.t W2, b2
        dW2 = np.dot(self.A1.T, dZ2)                   # (d_hidden, d_out)
        db2 = np.sum(dZ2, axis=0, keepdims=True)       # (1, d_out)

        # 3. Backprop through Linear 2 into A1
        dA1 = np.dot(dZ2, self.W2.T)                   # (N, d_hidden)

        # 4. Backprop through ReLU: dL/dZ1 = dA1 * (Z1 > 0)
        dZ1 = dA1 * (self.Z1 > 0)                      # (N, d_hidden)

        # 5. Gradients w.r.t W1, b1
        dW1 = np.dot(self.X.T, dZ1)                    # (d_in, d_hidden)
        db1 = np.sum(dZ1, axis=0, keepdims=True)       # (1, d_hidden)

        # 6. Parameter update with SGD
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2

        # Compute Cross-Entropy Loss
        if y_true.ndim == 1:
            correct_logprobs = -np.log(self.probs[np.arange(N), y_true] + 1e-12)
        else:
            correct_logprobs = -np.sum(y_true * np.log(self.probs + 1e-12), axis=1)
        return float(np.mean(correct_logprobs))

# Verification
if __name__ == "__main__":
    X_dummy = np.random.randn(32, 10)
    y_dummy = np.random.randint(0, 3, size=32)
    model = TwoLayerMLP(d_in=10, d_hidden=16, d_out=3, lr=0.05)
    for epoch in range(5):
        probs = model.forward(X_dummy)
        loss = model.backward(y_dummy)
        print(f"Epoch {epoch}: Loss = {loss:.4f}")
'''

    backprop_section = subsection(
        "numpy-backprop",
        "NumPy 2-Layer Neural Network: Analytical Forward & Backward Pass",
        callout(
            "Verbatim Coding Interview Problem (OpenAI / Anthropic / Google)",
            "Interviewer instruction: 'Implement a two-layer feedforward neural network in plain NumPy without PyTorch or Autograd. Include ReLU activation, softmax output, and write out the analytical gradient updates.'",
            "important"
        )
        + code(backprop_code, "python", "two_layer_mlp_scratch.py")
        + formula_box(
            r"\frac{\partial \mathcal{L}}{\partial Z_2} = \hat{y} - y, \quad \frac{\partial \mathcal{L}}{\partial W_2} = A_1^T \frac{\partial \mathcal{L}}{\partial Z_2}, \quad \frac{\partial \mathcal{L}}{\partial Z_1} = \left(\frac{\partial \mathcal{L}}{\partial Z_2} W_2^T\right) \odot \mathbb{I}(Z_1 > 0)",
            "Gradient of cross-entropy loss with respect to output logits is predicted probabilities minus true class labels",
            [
                (r"\partial \mathcal{L} / \partial Z_2", "Logit error vector (y_hat - y). The exponential and log cleanly cancel."),
                (r"\partial \mathcal{L} / \partial W_2", "Outer product of hidden activations A1 and output error gradient."),
                (r"\partial \mathcal{L} / \partial Z_1", "Backpropagated error through W2 gated element-wise by the indicator function for positive pre-activations.")
            ],
            "Cross-entropy paired with softmax yields an exceptionally clean error residual that avoids flat gradient saturation regions."
        ),
        depth="deep"
    )

    # Section 4: Tree Methods & XGBoost
    trees_section = subsection(
        "tree-methods-xgboost",
        "Tree Methods: Decision Trees, Random Forests & XGBoost Second-Order Math",
        table(
            ["Criterion", "Mathematical Formulation", "Split Logic", "When Preferred"],
            [
                ["Gini Impurity", r"$G = 1 - \sum_{k=1}^K p_k^2$", "Measures probability of incorrectly classifying a randomly chosen element", "CART default; faster computation (no logarithms)"],
                ["Entropy", r"$H = - \sum_{k=1}^K p_k \log_2(p_k)$", "Information-theoretic measure of disorder/uncertainty in node", "ID3, C4.5; slightly more balanced splits"],
                ["Information Gain", r"$IG(D, A) = H(D) - \sum_{v} \frac{|D_v|}{|D|} H(D_v)$", "Reduction in entropy achieved by partitioning dataset on feature A", "Standard split criterion for classification trees"],
                ["Variance Reduction", r"$\Delta = \text{Var}(D) - \sum_v \frac{|D_v|}{|D|} \text{Var}(D_v)$", "Minimizes residual sum of squares across daughter partitions", "Regression trees (CART)"]
            ]
        )
        + callout(
            "XGBoost's Mathematical Edge: Second-Order Taylor Expansion & Regularized Objective",
            r"Unlike traditional gradient boosting which fits residuals via first-order gradient descent, XGBoost approximates the loss using a 2nd-order Taylor expansion:" + "\n"
            r"$$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$" + "\n"
            r"where $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}_i)$ (gradient) and $h_i = \partial_{\hat{y}^{(t-1)}}^2 l(y_i, \hat{y}_i)$ (hessian)." + "\n"
            r"With tree complexity regularization $\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$, the optimal leaf weight is directly solvable in closed form:" + "\n"
            r"$$w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}, \quad \text{Optimal Score} = -\frac{1}{2} \sum_{j=1}^T \frac{(\sum g_i)^2}{\sum h_i + \lambda} + \gamma T$$" + "\n"
            "This closed-form split gain enables fast greedy search, exact sparsity-aware handling for missing values, and built-in L2 regularization!",
            "tip"
        )
        + table(
            ["Feature / Paradigm", "Random Forest (Bagging)", "Gradient Boosted Trees (Boosting)", "XGBoost Specifics"],
            [
                ["Ensemble Strategy", "Parallel: independent trees trained on bootstrap samples", "Sequential: each tree trains on residual errors of previous", "Sequential 2nd-order Taylor optimization"],
                ["Error Reduction Target", "Reduces **Variance** (averaging decorrelated trees)", "Reduces **Bias** (progressively correcting residual errors)", "Reduces Bias while regularizing tree complexity"],
                ["Feature Subsampling", r"Random subset of features considered at each split ($m = \sqrt{d}$)", "Typically uses all features (or fixed fraction)", "Column subsampling at tree and node level (like RF)"],
                ["Handling Missing Values", "Imputation required before training", "Surrogate splits or median fill", "Sparsity-aware default split direction learned automatically"],
                ["Pruning Strategy", "Grow deep, unpruned trees to minimize individual bias", "Constrained shallow trees (max_depth 3-6)", "Prunes backwards from max depth using $\\gamma$ threshold"]
            ]
        ),
        depth="deep"
    )

    # Section 5: Normalization Dynamics
    normalization_section = subsection(
        "normalization-dynamics",
        "Deep Learning Normalization Dynamics: BatchNorm vs LayerNorm vs RMSNorm",
        table(
            ["Method", "Dimension Normalized Over", "Batch Size Dependency", "Inference Behavior", "Primary Use Case"],
            [
                ["Batch Normalization (BN)", "(N, H, W) per channel across the minibatch", "❌ High: fails completely when batch size < 8 or varied", "Requires running mean & variance tracked during training", "Convolutional Neural Networks (ResNet, ConvNeXt)"],
                ["Layer Normalization (LN)", "(C, H, W) or (d_model) across all channels per sample", "✅ Zero: completely independent of batch size", "Identical calculation at training and inference time", "NLP, Transformers, RNNs, Small-batch vision"],
                ["Group Normalization (GN)", "Groups channels into G groups, normalizes across each group per sample", "✅ Zero", "Identical at train and inference", "Object detection, segmentation with batch size = 1 or 2"],
                ["RMSNorm", r"$\frac{x}{\sqrt{\frac{1}{d}\sum x_i^2 + \epsilon}} \odot \gamma$ (No mean centering)", "✅ Zero", "Identical at train and inference; saves 7-10% latency", "Modern LLMs (LLaMA 2/3, Mistral, Gemma)"]
            ]
        )
        + callout(
            "Why Transformers Choose LayerNorm Over BatchNorm",
            "1. **Variable Sequence Length**: NLP sentences have varying lengths within a minibatch. Padding tokens distort batch statistics.\n"
            "2. **Online / Streaming Latency**: At inference time, generating tokens is strictly a batch size of 1. LayerNorm calculates mean and variance on the single incoming token vector with zero stored runtime states.\n"
            "3. **Cross-Sample Independence**: In multi-GPU distributed data parallel (DDP) training, BatchNorm requires Cross-GPU SyncBN communication overhead, whereas LayerNorm is 100% localized to each worker.",
            "important"
        )
        + table(
            ["Initialization Method", "Formula / Variance", "Target Activation", "Why It Prevents Vanishing Gradients"],
            [
                ["Xavier / Glorot Uniform", r"$W \sim U\left(-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right)$", "Tanh, Sigmoid, Linear", "Maintains activation variance equal across layers under linear/symmetric activations: $\\text{Var}(W) = \\frac{2}{n_{in} + n_{out}}$."],
                ["He / Kaiming Normal", r"$W \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n_{in}}}\right)$", "ReLU, LeakyReLU, GELU", "Compensates for the fact that ReLU zeroes out half the activations (expectation 0.5), requiring $2/n_{in}$ variance to prevent vanishing variance!"]
            ]
        ),
        depth="deep"
    )

    # Section 6: 9-Step ML System Design Framework
    system_design_section = subsection(
        "ml-system-design",
        "The 9-Step ML System Design Framework: Universal Interview Blueprint",
        svg_card("The 9-Step ML Production System Design Pipeline", svg_ml_design)
        + callout(
            "Recite Out Loud in Any Big Tech ML System Design Round",
            "When given an open-ended problem like 'Design TikTok Video Recommendation' or 'Design Stripe Fraud Detection', immediately anchor your response on this 9-step progression:\n"
            "1. **Problem Formulation**: Clarify business objectives, translate business KPIs into ML task (binary classification, ranking, multi-task), define input/output.\n"
            "2. **Metrics Definition**: Offline metrics (AUC-ROC, PR-AUC, NDCG@K, MRR) vs Online business metrics (CTR, Conversion Rate, Watch Time, Revenue, Chargeback Rate).\n"
            "3. **Data Collection & Ground Truth**: Data sources, feedback loop (explicit vs implicit), negative sampling strategies, delayed feedback handling.\n"
            "4. **Feature Engineering**: User features, Item features, Context/Real-time features, Embeddings (two-tower), and Data Leakage prevention.\n"
            "5. **Model Architecture & Offline Eval**: Two-stage retrieval + heavy ranker (Candidate Generation → Ranking → Diversity Reranking), GBDT vs Deep Neural Net.\n"
            "6. **Prediction Service & Serving**: Online vs Offline batch scoring, p99 latency SLAs (<50ms), Model quantization (FP16/INT8), Caching layers (Redis).\n"
            "7. **Online Testing & Deployment**: Shadow mode deployment, Canary rollouts, A/B testing, Interleaving for rapid ranking validation.\n"
            "8. **Monitoring & Drift Detection**: Data drift (Covariate shift), Concept drift, Population Stability Index (PSI), Latency and throughput alerts.\n"
            "9. **Continual Learning & Retraining**: Daily batch retraining, Streaming online updates, handling cold start for new users/items.",
            "tip"
        )
        + worked_example(
            title="Production ML Case Study: Real-Time Fraud Detection System (Stripe / Cred)",
            steps=[
                ("Problem Formulation & Latency SLA", "Predict the probability of an unauthorized credit card transaction within a hard 30ms SLA before payment gateway authorization."),
                ("Metrics Strategy under Extreme Imbalance", "Given 0.01% fraud prevalence, standard ROC-AUC is misleading. Optimize Precision-Recall AUC (PR-AUC) and enforce False Positive Rate < 0.1% at 99% Recall to protect legitimate checkout conversion."),
                ("Feature Store & Velocity Calculations", "Real-time sliding window aggregations via Redis (e.g. transaction count from IP in past 5 minutes, geographic velocity between current and prior transaction, merchant category risk)."),
                ("Model Architecture & Negative Sampling", "LightGBM / XGBoost for sub-10ms inference latency. Apply hard negative mining to heavily sample legitimate transactions that resemble fraud patterns."),
                ("Deployment & Dual-Lane Fallback", "In-memory Redis feature store. Dual-lane architecture: if ML scoring exceeds 25ms timeout, automatically fallback to deterministic rule engine.")
            ],
            answer="Combines sub-10ms GBDT serving with real-time Redis velocity features and dual-lane fail-safe rules, ensuring high fraud recall without checkout latency degradation."
        ),
        depth="deep"
    )

    # Section 7: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield ML Core Interview Flashcards & Defenses",
        flashcard(
            "Why is PR-AUC preferred over ROC-AUC in extreme class imbalance?",
            "ROC-AUC plots True Positive Rate vs False Positive Rate. When negative samples massively outnumber positive samples (e.g., 99.9% legit, 0.1% fraud), the False Positive Rate denominator (FP + TN) is dominated by TN. Even if the model makes 10,000 false positives, FPR remains tiny, creating an illusory high ROC-AUC! PR-AUC plots Precision (TP / (TP + FP)) vs Recall, directly penalizing false positives and accurately reflecting model degradation.",
            "P0 Applied Scientist"
        )
        + flashcard(
            "Explain the difference between Bagging and Boosting in terms of Bias and Variance.",
            "Bagging (Bootstrap Aggregating, e.g. Random Forest) trains independent base learners on random bootstrap samples with replacement and averages their outputs. Averaging decorrelated estimators strictly reduces **Variance** while leaving Bias roughly unchanged. Boosting (e.g. AdaBoost, GBDT, XGBoost) trains learners sequentially, where each new learner fits the residual errors/gradients of previous models. This iterative correction reduces **Bias**.",
            "P0 Big Tech"
        )
        + flashcard(
            "What causes the Dying ReLU problem, and how do modern architectures solve it?",
            "If a neuron receives an input such that W·x + b < 0, ReLU outputs 0 and its gradient is exactly 0. During backprop, no gradient flows back to update its weights. If all training samples cause negative activation, the neuron becomes permanently inactive ('dead') for the rest of training. Solutions: (1) He/Kaiming initialization to avoid negative saturation, (2) LeakyReLU or Parametric ReLU (PReLU) allowing small slope α in negative regime, (3) GELU or SwiGLU smooth activations.",
            "P0 Deep Learning"
        )
        + flashcard(
            "Why does AdamW outperform Adam on Transformers and Deep Networks?",
            "In classic L2 regularization with standard SGD, weight decay and L2 penalty are mathematically identical. However, in adaptive optimizers like Adam, the gradient update is scaled by the inverse root of the second moment (1 / sqrt(v_t)). When L2 regularization is added directly to the loss function, the weight decay penalty is also scaled by 1 / sqrt(v_t), meaning parameters with large historical gradients receive *less* weight decay! AdamW decouples weight decay, applying θ ← θ(1 - ηλ) directly to the weights outside the adaptive gradient update.",
            "P0 LLM / Deep Learning"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: Classical ML & Deep Learning Core", sprint_html)
        + section("bias-variance-decomp", "📐 Bias-Variance Decomposition & Regularization Geometry", bv_html)
        + section("numpy-backprop", "💻 NumPy 2-Layer Neural Network From Scratch", backprop_section)
        + section("tree-methods-xgboost", "🌲 Trees, Ensembles & XGBoost Second-Order Math", trees_section)
        + section("normalization-dynamics", "⚡ Deep Learning Normalization Dynamics", normalization_section)
        + section("ml-system-design", "🏗️ The 9-Step ML System Design Framework", system_design_section)
        + section("interview-flashcards", "🎯 High-Yield ML Core Interview Flashcards", flashcards_html)
    )

    return {"toc": toc, "content": content}
