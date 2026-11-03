# mod_ml_cv.py - Machine Learning & Computer Vision Module Generator

def get_content():
    toc = [
        ("rapid-recall", "⚡ 10-Min Rapid Recall Sheet"),
        ("visual-diagrams", "📊 Visual CNN & HOG Architecture"),
        ("core-deep-dives", "🧠 Vision Math, Normalization & ResNet"),
        ("interview-traps", "⚠️ High-Frequency ML & CV Traps"),
        ("flashcards", "🎯 Interview Q&A Flashcards")
    ]

    # SVG 1: CNN Feature Extraction Pipeline
    svg_cnn = """
    <svg viewBox="0 0 860 280" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="cnn-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Input Image -->
      <rect x="20" y="70" width="90" height="90" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <text x="65" y="110" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">Input Image</text>
      <text x="65" y="130" fill="#94a3b8" font-size="10" text-anchor="middle">224x224x3</text>

      <line x1="110" y1="115" x2="145" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#cnn-arrow)" />

      <!-- Conv2D + ReLU + BN -->
      <rect x="150" y="55" width="115" height="120" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="207" y="85" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">Conv2D + BN</text>
      <text x="207" y="105" fill="#bae6fd" font-size="9" text-anchor="middle">64 Filters (3x3)</text>
      <text x="207" y="125" fill="#e0f2fe" font-size="9" text-anchor="middle">ReLU Activation</text>
      <text x="207" y="145" fill="#94a3b8" font-size="8" text-anchor="middle">224x224x64</text>

      <line x1="265" y1="115" x2="300" y2="115" stroke="#38bdf8" stroke-width="2" marker-end="url(#cnn-arrow)" />

      <!-- MaxPool -->
      <rect x="305" y="75" width="85" height="80" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="347" y="105" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">MaxPool</text>
      <text x="347" y="125" fill="#a7f3d0" font-size="9" text-anchor="middle">2x2 Stride 2</text>
      <text x="347" y="140" fill="#6ee7b7" font-size="8" text-anchor="middle">112x112x64</text>

      <line x1="390" y1="115" x2="425" y2="115" stroke="#34d399" stroke-width="2" marker-end="url(#cnn-arrow)" />

      <!-- Deep Feature Maps -->
      <rect x="430" y="85" width="105" height="60" rx="6" fill="#581c87" stroke="#c084fc" stroke-width="1.5" />
      <text x="482" y="110" fill="#c084fc" font-size="11" font-weight="800" text-anchor="middle">Deep Conv Layers</text>
      <text x="482" y="128" fill="#e9d5ff" font-size="9" text-anchor="middle">7x7x512</text>

      <line x1="535" y1="115" x2="570" y2="115" stroke="#c084fc" stroke-width="2" marker-end="url(#cnn-arrow)" />

      <!-- Global Avg Pool / Flatten -->
      <rect x="575" y="90" width="80" height="50" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
      <text x="615" y="112" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">GAP / Flatten</text>
      <text x="615" y="128" fill="#fde68a" font-size="9" text-anchor="middle">512 Vector</text>

      <line x1="655" y1="115" x2="690" y2="115" stroke="#fbbf24" stroke-width="2" marker-end="url(#cnn-arrow)" />

      <!-- Fully Connected & Softmax -->
      <rect x="695" y="70" width="135" height="90" rx="6" fill="#1e293b" stroke="#f43f5e" stroke-width="2" />
      <text x="762" y="100" fill="#f43f5e" font-size="12" font-weight="800" text-anchor="middle">Dense + Softmax</text>
      <text x="762" y="120" fill="#fecdd3" font-size="10" text-anchor="middle">K Class Probabilities</text>
      <text x="762" y="140" fill="#94a3b8" font-size="9" text-anchor="middle">Cross-Entropy Loss</text>

      <!-- Label -->
      <text x="430" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Standard Convolutional Neural Network (CNN) Feature Extractor Pipeline</text>
    </svg>
    """

    # SVG 2: HOG (Histogram of Oriented Gradients) Pipeline (Candidate's Project K-HUKI!)
    svg_hog = """
    <svg viewBox="0 0 860 220" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="hog-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#fb923c" />
        </marker>
      </defs>

      <!-- Step 1: Grayscale Image -->
      <rect x="20" y="60" width="130" height="70" rx="6" fill="#1e293b" stroke="#fb923c" stroke-width="1.5" />
      <text x="85" y="90" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">1. Input Frame</text>
      <text x="85" y="110" fill="#fed7aa" font-size="9" text-anchor="middle">Grayscale + Normalize</text>

      <line x1="150" y1="95" x2="190" y2="95" stroke="#fb923c" stroke-width="2" marker-end="url(#hog-arrow)" />

      <!-- Step 2: Gradients Gx, Gy -->
      <rect x="195" y="50" width="145" height="90" rx="6" fill="#7c2d12" stroke="#fb923c" stroke-width="1.5" />
      <text x="267" y="80" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">2. Gradient Vectors</text>
      <text x="267" y="100" fill="#fed7aa" font-size="9" text-anchor="middle">Sobel Filter: Gx, Gy</text>
      <text x="267" y="118" fill="#ffedd5" font-size="8" text-anchor="middle">Mag = &radic;(Gx&sup2;+Gy&sup2;), &theta;=atan2</text>

      <line x1="340" y1="95" x2="380" y2="95" stroke="#fb923c" stroke-width="2" marker-end="url(#hog-arrow)" />

      <!-- Step 3: Cell Histograms -->
      <rect x="385" y="50" width="145" height="90" rx="6" fill="#1e293b" stroke="#fb923c" stroke-width="1.5" />
      <text x="457" y="80" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">3. 8x8 Spatial Cells</text>
      <text x="457" y="100" fill="#fed7aa" font-size="9" text-anchor="middle">9 Orientation Bins</text>
      <text x="457" y="118" fill="#94a3b8" font-size="8" text-anchor="middle">Angles 0&deg; to 180&deg;</text>

      <line x1="530" y1="95" x2="570" y2="95" stroke="#fb923c" stroke-width="2" marker-end="url(#hog-arrow)" />

      <!-- Step 4: Block Normalization -->
      <rect x="575" y="50" width="135" height="90" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="642" y="80" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">4. 16x16 Blocks</text>
      <text x="642" y="100" fill="#a7f3d0" font-size="9" text-anchor="middle">2x2 Cells Block</text>
      <text x="642" y="118" fill="#6ee7b7" font-size="8" text-anchor="middle">L2-Hys Normalization</text>

      <line x1="710" y1="95" x2="745" y2="95" stroke="#34d399" stroke-width="2" marker-end="url(#hog-arrow)" />

      <!-- Step 5: Feature Vector -->
      <rect x="750" y="60" width="95" height="70" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="797" y="90" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">HOG Vector</text>
      <text x="797" y="110" fill="#bae6fd" font-size="8" text-anchor="middle">3780-D Vector</text>

      <!-- Caption -->
      <text x="430" y="180" fill="#fb923c" font-size="11" font-weight="600" text-anchor="middle">K-HUKI Engine: HOG Extraction Runs 11x Faster than ResNet for Real-Time Keyframe Detection</text>
    </svg>
    """

    content = f"""
    <!-- SECTION 1: RAPID RECALL -->
    <section id="rapid-recall" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚡ 10-Minute Rapid Recall Cheat Sheet</h2>
        <span class="pill pill-orange">Machine Learning & Vision</span>
      </div>

      <!-- Evaluation Metrics Table -->
      <h3 style="font-size: 1rem; color: var(--accent-orange); margin: 1rem 0 0.5rem;">1. Machine Learning Evaluation Metrics Cheat Sheet</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Metric</th>
              <th>Mathematical Formula</th>
              <th>When to Prioritize in Production</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Precision</strong></td>
              <td>$$\frac{{TP}}{{TP + FP}}$$</td>
              <td>When <strong>False Positives are expensive</strong> (e.g. Spam detection, YouTube content takedown, fraud alerts).</td>
            </tr>
            <tr>
              <td><strong>Recall (Sensitivity)</strong></td>
              <td>$$\frac{{TP}}{{TP + FN}}$$</td>
              <td>When <strong>False Negatives are fatal</strong> (e.g. Cancer detection, autonomous vehicle pedestrian detection!).</td>
            </tr>
            <tr>
              <td><strong>F1-Score</strong></td>
              <td>$$2 \times \frac{{\text{{Precision}} \times \text{{Recall}}}}{{\text{{Precision}} + \text{{Recall}}}}$$</td>
              <td>Harmonic mean; optimal for evaluating models on <strong>imbalanced classification datasets</strong>.</td>
            </tr>
            <tr>
              <td><strong>ROC-AUC</strong></td>
              <td>Area under True Positive Rate vs False Positive Rate curve.</td>
              <td>Measures model classification ranking ability across all decision thresholds.</td>
            </tr>
            <tr>
              <td><strong>mAP (Mean Average Precision)</strong></td>
              <td>$$\frac{{1}}{{|C|}} \sum_{{c \in C}} AP_c \text{{ at IoU}} \ge 0.50$$</td>
              <td>Standard benchmark for <strong>Object Detection</strong> (YOLO, Faster R-CNN) evaluating bounding box location + class accuracy.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Loss Functions & Optimizers -->
      <h3 style="font-size: 1rem; color: var(--accent-blue); margin: 1.5rem 0 0.5rem;">2. Optimizers & Loss Functions Matrix</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Optimizer / Loss</th>
              <th>Core Mathematical Idea</th>
              <th>Key Strengths &amp; Pitfalls</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Adam</strong> (Adaptive Moment Estimation)</td>
              <td>Maintains exponential moving averages of both past gradients ($m_t$, first moment) AND squared gradients ($v_t$, second moment).</td>
              <td>Fast initial convergence across sparse gradients; can struggle with generalization compared to tuned SGD.</td>
            </tr>
            <tr>
              <td><strong>AdamW</strong> (Decoupled Weight Decay)</td>
              <td>Decouples $L_2$ regularization weight decay from gradient moment updates ($w_{{t+1}} = w_t - \gamma \lambda w_t - \gamma \frac{{m_t}}{{\sqrt{{v_t}} + \epsilon}}$).</td>
              <td><strong>Industry Gold Standard</strong> for training modern Vision Transformers and LLMs!</td>
            </tr>
            <tr>
              <td><strong>Cross-Entropy Loss</strong></td>
              <td>$$L = - \sum y_i \log(\hat{{y}}_i)$$</td>
              <td>Penalizes confident wrong classifications logarithmically; standard for multi-class classification.</td>
            </tr>
            <tr>
              <td><strong>Focal Loss</strong></td>
              <td>$$FL(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)$$</td>
              <td>Dynamically scales loss down for well-classified easy background examples; dominates extreme class imbalance in object detection (RetinaNet).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: VISUAL DIAGRAMS -->
    <section id="visual-diagrams" class="section-block">
      <div class="section-head">
        <h2 class="section-title">📊 Visual CNN & HOG Architecture</h2>
        <span class="pill pill-emerald">Deep & Classical Vision</span>
      </div>

      <div class="svg-diagram-card">
        {svg_cnn}
        <div class="diagram-caption">Figure 9.1: Standard CNN Feature Hierarchy (Convolution &rarr; BatchNorm &rarr; MaxPool &rarr; GAP &rarr; Softmax).</div>
      </div>

      <div class="svg-diagram-card">
        {svg_hog}
        <div class="diagram-caption">Figure 9.2: HOG (Histogram of Oriented Gradients) Processing Pipeline — The Engine Behind Candidate's K-HUKI Project (NIT Rourkela).</div>
      </div>
    </section>

    <!-- SECTION 3: CORE DEEP DIVES -->
    <section id="core-deep-dives" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🧠 Vision Math, Normalization & ResNet</h2>
        <span class="pill pill-purple">Deep Learning Theory</span>
      </div>

      <!-- Conv Math Formula -->
      <h3 style="color: var(--accent-orange); font-size: 1.1rem; margin-top: 1rem;">1. Convolution Spatial Dimension & Receptive Field Formulas</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        Given an input feature map of size $I$, kernel size $K$, padding $P$, and stride $S$, the output dimension $O$ is:
      </p>
      $$O = \left\lfloor \frac{{I - K + 2P}}{{S}} \right\rfloor + 1$$
      
      <div class="callout callout-pro">
        <div class="callout-title">💡 Why Stack Two 3x3 Conv Layers Instead of One 5x5 Conv Layer? (VGG Principle)</div>
        <ol style="margin-left: 1.25rem;">
          <li><strong>Identical Effective Receptive Field:</strong> Two stacked $3 \times 3$ convolutions cover $3 + (3 - 1) = 5 \times 5$ spatial area!</li>
          <li><strong>28% Fewer Parameters:</strong> For $C$ channels, a $5 \times 5$ conv requires $5 \times 5 \times C^2 = 25C^2$ weights. Two $3 \times 3$ layers require $2 \times (3 \times 3 \times C^2) = \mathbf{{18C^2}}$ weights!</li>
          <li><strong>Greater Non-Linear Representational Power:</strong> Stacking two layers introduces two ReLU activation functions instead of one.</li>
        </ol>
      </div>

      <!-- BatchNorm vs LayerNorm -->
      <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-top: 2rem;">2. Batch Normalization vs Layer Normalization</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Batch Normalization (BatchNorm)</th>
              <th>Layer Normalization (LayerNorm)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Dimension of Normalization</strong></td>
              <td>Computes mean $\mu$ and variance $\sigma^2$ across the <strong>Batch dimension $N$</strong> for each channel independently: $(N, H, W)$.</td>
              <td>Computes mean $\mu$ and variance $\sigma^2$ across the <strong>Channel/Feature dimensions $(C, H, W)$</strong> for each individual sample in the batch.</td>
            </tr>
            <tr>
              <td><strong>Batch Size Sensitivity</strong></td>
              <td><strong>Extremely sensitive:</strong> Fails when batch size is small ($N &lt; 8$); batch statistics become noisy and drift.</td>
              <td><strong>Completely invariant to batch size</strong>; behaves identically whether batch size is 1 or 256!</td>
            </tr>
            <tr>
              <td><strong>Training vs Inference</strong></td>
              <td>Tracks exponential running mean and running variance during training; freezes them at test time (can cause train-test mismatch).</td>
              <td>Identical computation at both training and inference time!</td>
            </tr>
            <tr>
              <td><strong>Domain / Model Usage</strong></td>
              <td>Standard in Convolutional Networks (ResNet, ConvNeXt).</td>
              <td>Standard in <strong>Transformers, LLMs, and Vision Transformers (ViT)</strong>.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 4: INTERVIEW TRAPS -->
    <section id="interview-traps" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚠️ High-Frequency ML & CV Traps</h2>
        <span class="pill pill-rose">Recruiter Traps</span>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #1: Why ROC-AUC Misleads on Highly Imbalanced Data</div>
        <p><strong>The Trap:</strong> In fraud detection (99.9% legitimate, 0.1% fraud), a model achieves an impressive 0.98 ROC-AUC score, yet flags thousands of innocent transactions!</p>
        <p><strong>Why:</strong> ROC curves plot True Positive Rate ($TP / (TP+FN)$) against False Positive Rate ($FP / (FP+TN)$). Because the negative class is massive ($TN = 1,000,000$), a surge in false positives ($FP = 1,000$) causes negligible impact on FPR ($1000 / 1001000 \approx 0.00099$). Always use <strong>PR-AUC (Precision-Recall Curve)</strong>, which does not include $TN$ and exposes high false-positive rates immediately!</p>
      </div>

      <div class="callout callout-pro">
        <div class="callout-title">💡 How ResNet Skip Connections Eliminate Vanishing Gradients</div>
        <p>In a standard neural network, gradients pass through successive weight matrices during backpropagation via the chain rule: $\frac{{\partial L}}{{\partial x}} = \frac{{\partial L}}{{\partial y}} \cdot W$. If $|W| &lt; 1$, repeated multiplication causes gradients to exponentially decay to zero as depth exceeds 20 layers.</p>
        <p>In ResNet with residual skip connections $y = F(x) + x$, the gradient becomes:</p>
        $$\frac{{\partial y}}{{\partial x}} = \frac{{\partial F(x)}}{{\partial x}} + \mathbf{{1}}$$
        <p>Because of the $+1$ additive identity term, the error gradient can flow directly backward through the skip connection to shallow layers with <strong>zero signal attenuation</strong>, enabling networks to scale to 152+ layers successfully!</p>
      </div>
    </section>

    <!-- SECTION 5: FLASHCARDS -->
    <section id="flashcards" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🎯 Interview Q&A Flashcards (Self-Assessment)</h2>
        <span class="pill pill-blue">5 Questions</span>
      </div>

      <details class="faq-accordion">
        <summary>Q1: How does Non-Maximum Suppression (NMS) work in Object Detection?</summary>
        <div class="faq-body">
          Object detectors generate multiple redundant overlapping bounding boxes for the same object.<br>
          <strong>NMS Algorithm:</strong>
          <ol style="margin-left: 1.2rem;">
            <li>Sort all predicted bounding boxes by their confidence scores.</li>
            <li>Select the box with highest score, add it to final detections.</li>
            <li>Calculate <strong>Intersection over Union (IoU)</strong> between this selected box and all remaining candidate boxes.</li>
            <li>Discard any candidate box with $\text{{IoU}} &gt; \text{{Threshold}}$ (typically 0.50).</li>
            <li>Repeat until no candidate boxes remain.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q2: What is the 5-Stage Canny Edge Detection Algorithm?</summary>
        <div class="faq-body">
          <ol style="margin-left: 1.2rem;">
            <li><strong>Gaussian Blur:</strong> Smooths image to suppress high-frequency noise.</li>
            <li><strong>Gradient Intensity & Direction:</strong> Convolves with Sobel kernels to compute magnitude $G = \sqrt{{G_x^2 + G_y^2}}$ and angle $\theta = \arctan(G_y / G_x)$.</li>
            <li><strong>Non-Maximum Suppression (Thinning):</strong> Suppresses pixels that are not local maxima along the gradient direction, thinning edges to 1-pixel width.</li>
            <li><strong>Double Thresholding:</strong> Classifies edge pixels into Strong, Weak, or Non-edge based on High and Low thresholds ($T_{{high}}, T_{{low}}$).</li>
            <li><strong>Hysteresis Edge Tracking:</strong> Preserves weak edge pixels only if they are physically connected to a strong edge pixel.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q3: What causes Data Leakage in Machine Learning pipelines?</summary>
        <div class="faq-body">
          Data leakage occurs when information from outside the training dataset is inadvertently used to create the model.<br>
          • <strong>Classic Mistake:</strong> Performing scaling (<code>StandardScaler.fit_transform</code>), target encoding, or outlier removal on the <em>entire dataset before splitting into train/test</em>! The mean and variance of the test set leak into the training process.<br>
          • <strong>Prevention:</strong> Always split data first, or wrap preprocessing and modeling inside an end-to-end <code>Pipeline</code>.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q4: How does HOG achieve illumination invariance?</summary>
        <div class="faq-body">
          In HOG, gradients capture edge transitions rather than raw pixel intensities (a shift in overall lighting adds a constant value that cancels out during differentiation: $\frac{{\partial (I + c)}}{{\partial x}} = \frac{{\partial I}}{{\partial x}}$).<br>
          Furthermore, HOG groups cells into overlapping $16 \times 16$ blocks and performs <strong>L2-Hys Normalization</strong> ($v \to \frac{{v}}{{\sqrt{{\|v\|_2^2 + \epsilon^2}}}}$), making the descriptor vector completely invariant to illumination scaling and contrast changes!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q5: What is the difference between Transposed Convolution and Bilinear Upsampling?</summary>
        <div class="faq-body">
          • <strong>Transposed Convolution (Deconvolution):</strong> Learnable upsampling layer with trainable kernel weights. Can learn complex non-linear spatial reconstructions, but prone to "checkerboard artifacts" if kernel size is not divisible by stride.<br>
          • <strong>Bilinear / Nearest-Neighbor Upsampling:</strong> Fixed deterministic mathematical interpolation with zero learnable weights. Cheaper, faster, and avoids checkerboard artifacts; usually followed by a standard $1 \times 1$ conv.
        </div>
      </details>
    </section>
    """
    return toc, content
