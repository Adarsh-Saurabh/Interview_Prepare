# mod_ai_agents.py - AI Agents, RAG, LangChain, LangGraph & Vector DBs Generator

def get_content():
    toc = [
        ("rapid-recall", "⚡ 10-Min Rapid Recall Sheet"),
        ("visual-diagrams", "📊 Visual RAG & LangGraph Architecture"),
        ("core-deep-dives", "🧠 Core RAG, Vector Search & Agent Internals"),
        ("interview-traps", "⚠️ High-Frequency GenAI & Agent Traps"),
        ("flashcards", "🎯 Interview Q&A Flashcards")
    ]

    # SVG 1: Advanced RAG Architecture Flowchart
    svg_rag = """
    <svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="rag-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="rag-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Step 1: User Query -->
      <rect x="20" y="140" width="120" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="80" y="165" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">User Query</text>
      <text x="80" y="183" fill="#94a3b8" font-size="10" text-anchor="middle">Raw Prompt</text>

      <line x1="140" y1="170" x2="185" y2="170" stroke="#38bdf8" stroke-width="2" marker-end="url(#rag-arrow)" />

      <!-- Step 2: Query Transformation (HyDE / Multi-Query) -->
      <rect x="190" y="130" width="130" height="80" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="255" y="155" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">1. Query Transform</text>
      <text x="255" y="175" fill="#e0f2fe" font-size="10" text-anchor="middle">HyDE / Sub-Queries</text>
      <text x="255" y="193" fill="#bae6fd" font-size="9" text-anchor="middle">Hypothetical doc</text>

      <!-- Split to Hybrid Search -->
      <line x1="320" y1="150" x2="365" y2="90" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#rag-arrow)" />
      <line x1="320" y1="190" x2="365" y2="250" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#rag-arrow)" />

      <!-- Branch A: Dense Vector Search -->
      <rect x="370" y="60" width="130" height="65" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
      <text x="435" y="85" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">Dense Retrieval</text>
      <text x="435" y="102" fill="#94a3b8" font-size="9" text-anchor="middle">HNSW / Cosine</text>
      <text x="435" y="115" fill="#a7f3d0" font-size="8" text-anchor="middle">Semantic Similarity</text>

      <!-- Branch B: Sparse Keyword Search (BM25) -->
      <rect x="370" y="220" width="130" height="65" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="435" y="245" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">Sparse Retrieval</text>
      <text x="435" y="262" fill="#94a3b8" font-size="9" text-anchor="middle">BM25 / SPLADE</text>
      <text x="435" y="275" fill="#fde68a" font-size="8" text-anchor="middle">Exact Keyword Match</text>

      <!-- Fusion & Rerank -->
      <line x1="500" y1="90" x2="545" y2="150" stroke="#34d399" stroke-width="1.5" marker-end="url(#rag-arrow)" />
      <line x1="500" y1="250" x2="545" y2="190" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#rag-arrow)" />

      <!-- Step 3: Reciprocal Rank Fusion & Cross-Encoder Reranker -->
      <rect x="550" y="130" width="140" height="80" rx="8" fill="#581c87" stroke="#c084fc" stroke-width="2" />
      <text x="620" y="155" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">2. RRF &amp; Reranker</text>
      <text x="620" y="175" fill="#e9d5ff" font-size="10" text-anchor="middle">Cross-Encoder</text>
      <text x="620" y="193" fill="#d8b4fe" font-size="9" text-anchor="middle">Top 50 &rarr; Top 4 Chunks</text>

      <line x1="690" y1="170" x2="725" y2="170" stroke="#c084fc" stroke-width="2" marker-end="url(#rag-green)" />

      <!-- Step 4: Generation with LLM -->
      <rect x="730" y="130" width="115" height="80" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2" />
      <text x="787" y="155" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">3. Generation</text>
      <text x="787" y="175" fill="#a7f3d0" font-size="10" text-anchor="middle">Grounded LLM</text>
      <text x="787" y="193" fill="#6ee7b7" font-size="9" text-anchor="middle">Zero Hallucination</text>

      <!-- Title Header -->
      <text x="430" y="30" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Production Advanced RAG: Hybrid Search (Dense + BM25) &amp; Cross-Encoder Reranking</text>
    </svg>
    """

    # SVG 2: LangGraph Cyclic State Machine
    svg_langgraph = """
    <svg viewBox="0 0 860 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="lg-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
        </marker>
        <marker id="lg-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="lg-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- START -->
      <circle cx="60" cy="140" r="28" fill="#0284c7" />
      <text x="60" y="145" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">START</text>

      <line x1="88" y1="140" x2="145" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#lg-blue)" />

      <!-- Node 1: Planner / Orchestrator -->
      <rect x="150" y="105" width="140" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
      <text x="220" y="132" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Planner Node</text>
      <text x="220" y="150" fill="#94a3b8" font-size="10" text-anchor="middle">State: plan, tasks</text>
      <text x="220" y="165" fill="#64748b" font-size="9" text-anchor="middle">Decides next step</text>

      <line x1="290" y1="140" x2="345" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#lg-blue)" />

      <!-- Conditional Edge 1: Need Tools? -->
      <polygon points="390,105 435,140 390,175 345,140" fill="#0f172a" stroke="#fbbf24" stroke-width="2" />
      <text x="390" y="143" fill="#fbbf24" font-size="9" font-weight="700" text-anchor="middle">Tool Call?</text>

      <!-- Yes path up to Tool Node -->
      <line x1="390" y1="105" x2="390" y2="55" stroke="#fbbf24" stroke-width="2" marker-end="url(#lg-blue)" />
      <rect x="330" y="10" width="120" height="45" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="390" y="32" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">ToolNode (APIs)</text>
      <text x="390" y="47" fill="#fde68a" font-size="8" text-anchor="middle">Executes &amp; updates State</text>

      <!-- Loop back from ToolNode to Planner -->
      <path d="M 330 32 Q 220 32 220 100" fill="none" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3" marker-end="url(#lg-blue)" />

      <!-- No path to Validator / Critic -->
      <line x1="435" y1="140" x2="495" y2="140" stroke="#38bdf8" stroke-width="2" marker-end="url(#lg-blue)" />

      <!-- Node 2: Evaluator / Critic (Uplan Style) -->
      <rect x="500" y="105" width="140" height="70" rx="8" fill="#1e293b" stroke="#c084fc" stroke-width="2" />
      <text x="570" y="132" fill="#c084fc" font-size="12" font-weight="800" text-anchor="middle">Critic / Validator</text>
      <text x="570" y="150" fill="#94a3b8" font-size="10" text-anchor="middle">Adversarial Check</text>
      <text x="570" y="165" fill="#d8b4fe" font-size="9" text-anchor="middle">Coherence &amp; Guardrails</text>

      <!-- Conditional Edge 2: Passes Criteria? -->
      <polygon points="695,105 735,140 695,175 655,140" fill="#0f172a" stroke="#f43f5e" stroke-width="2" />
      <text x="695" y="143" fill="#f43f5e" font-size="9" font-weight="700" text-anchor="middle">Pass?</text>

      <!-- Fail path loop back to Planner (Cyclic edge) -->
      <path d="M 695 175 Q 695 240 220 240 Q 220 180 220 180" fill="none" stroke="#f43f5e" stroke-width="2" marker-end="url(#lg-arrow)" />
      <rect x="420" y="230" width="140" height="20" rx="4" fill="#881337" />
      <text x="490" y="244" fill="#f43f5e" font-size="9" font-weight="700" text-anchor="middle">RETRY / REBUTTAL CYCLE</text>

      <!-- Pass path to END -->
      <line x1="735" y1="140" x2="790" y2="140" stroke="#34d399" stroke-width="2.5" marker-end="url(#lg-green)" />
      <circle cx="815" cy="140" r="25" fill="#059669" />
      <text x="815" y="145" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">END</text>
    </svg>
    """

    content = f"""
    <!-- SECTION 1: RAPID RECALL -->
    <section id="rapid-recall" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚡ 10-Minute Rapid Recall Cheat Sheet</h2>
        <span class="pill pill-rose">Modern AI & Agents</span>
      </div>

      <!-- Vector Databases Matrix -->
      <h3 style="font-size: 1rem; color: var(--accent-rose); margin: 1rem 0 0.5rem;">1. Vector Databases Master Comparison Matrix</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Vector Database</th>
              <th>Primary Index Algorithms</th>
              <th>Metadata Filtering</th>
              <th>Deployment Model</th>
              <th>Ideal Production Scenario</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pinecone</strong></td>
              <td>Proprietary graph ANN</td>
              <td>Single-stage pre-filtering</td>
              <td>Serverless / Fully Managed SaaS</td>
              <td>Zero-maintenance managed cloud; fast prototyping to scale.</td>
            </tr>
            <tr>
              <td><strong>Qdrant</strong> (Rust-based)</td>
              <td><strong>HNSW</strong> with Payload Indexing</td>
              <td>Native single-stage filtered HNSW</td>
              <td>Open-Source / Self-hosted / Cloud</td>
              <td>Complex hybrid search and rigorous payload metadata filtering.</td>
            </tr>
            <tr>
              <td><strong>Milvus / Zilliz</strong></td>
              <td>HNSW, IVF-PQ, SCaNN, GPU index</td>
              <td>Two-stage filtering</td>
              <td>Distributed (Kubernetes native)</td>
              <td>Billion-scale enterprise vector operations (heavy infra).</td>
            </tr>
            <tr>
              <td><strong>pgvector</strong> (PostgreSQL)</td>
              <td>HNSW, IVFFlat</td>
              <td>Native SQL <code>WHERE</code> clauses</td>
              <td>Self-hosted / AWS RDS / Supabase</td>
              <td>Unified DB (ACID relational data + vectors in single database!).</td>
            </tr>
            <tr>
              <td><strong>Chroma</strong></td>
              <td>HNSW (hnswlib)</td>
              <td>Post-filtering</td>
              <td>Embedded Python / In-memory</td>
              <td>Local development, small hackathons, unit tests.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Agent Frameworks Table -->
      <h3 style="font-size: 1rem; color: var(--accent-purple); margin: 1.5rem 0 0.5rem;">2. Agent Orchestration Frameworks Comparison</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Framework</th>
              <th>Core Abstraction</th>
              <th>Cyclic Loops?</th>
              <th>Human-in-the-Loop?</th>
              <th>Production Recommendation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>LangChain (Classic)</strong></td>
              <td>Chains (DAG pipeline)</td>
              <td>Difficult / Hacky</td>
              <td>Basic callbacks</td>
              <td>Good for simple linear prompt & retrieval pipes; brittle for agents.</td>
            </tr>
            <tr>
              <td><strong>LangGraph</strong></td>
              <td><strong>StateGraph</strong> (Nodes + Edges)</td>
              <td><strong>Native Cyclic Graphs</strong></td>
              <td><strong>First-class</strong> (Time travel, persistent checkpointer)</td>
              <td><strong>Gold Standard for Enterprise Multi-Agent Workflows</strong> (as in Uplan!).</td>
            </tr>
            <tr>
              <td><strong>CrewAI</strong></td>
              <td>Role-Playing Agents + Tasks</td>
              <td>Hierarchical delegation</td>
              <td>Console approval</td>
              <td>Great for persona-driven roleplay (Researcher, Writer).</td>
            </tr>
            <tr>
              <td><strong>AutoGen (Microsoft)</strong></td>
              <td>Conversable Agents</td>
              <td>Multi-agent chat rounds</td>
              <td>Chat interruption</td>
              <td>Conversational consensus and group chat simulations.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: VISUAL DIAGRAMS -->
    <section id="visual-diagrams" class="section-block">
      <div class="section-head">
        <h2 class="section-title">📊 Visual RAG & LangGraph Architecture</h2>
        <span class="pill pill-emerald">Architectural Flowcharts</span>
      </div>

      <div class="svg-diagram-card">
        {svg_rag}
        <div class="diagram-caption">Figure 5.1: Production Modular RAG Pipeline with Query Rewriting, Hybrid Search (Dense HNSW + Sparse BM25), and Cross-Encoder Reranking.</div>
      </div>

      <div class="svg-diagram-card">
        {svg_langgraph}
        <div class="diagram-caption">Figure 5.2: Cyclic State Machine in LangGraph — Demonstrating State Preservation, Tool Call Loops, and Adversarial Validation (Uplan Architecture).</div>
      </div>
    </section>

    <!-- SECTION 3: CORE DEEP DIVES -->
    <section id="core-deep-dives" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🧠 Core RAG, Vector Search & Agent Internals</h2>
        <span class="pill pill-purple">Under The Hood</span>
      </div>

      <!-- Bi-Encoder vs Cross-Encoder -->
      <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-top: 1rem;">1. Bi-Encoder vs Cross-Encoder: The Latency vs Accuracy Trade-off</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Architecture</th>
              <th>How It Operates</th>
              <th>Latency / Complexity</th>
              <th>Role in RAG Pipeline</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Bi-Encoder</strong> (Embedding Models)</td>
              <td>Encodes Query $q$ and Document $d$ independently into vectors $\vec{{u}}$ and $\vec{{v}}$. Similarity computed via dot product: $\cos(\vec{{u}}, \vec{{v}})$.</td>
              <td><strong>$O(1)$ fast dot-product</strong> over pre-computed index. Vectors can be searched across millions of chunks in milliseconds.</td>
              <td><strong>First-Stage Retrieval:</strong> Fetches top 50-100 candidates from database. Cannot model token-level cross-interactions.</td>
            </tr>
            <tr>
              <td><strong>Cross-Encoder</strong> (Reranker Models)</td>
              <td>Passes Query AND Document together into self-attention layers: <code>[CLS] Query [SEP] Document [SEP]</code>. All tokens cross-attend!</td>
              <td><strong>$O(N)$ heavy transformer inference</strong> for every document candidate. Too slow to run across the entire database!</td>
              <td><strong>Second-Stage Reranker:</strong> Reranks top 50 candidates down to top 4 highest-relevance chunks for the LLM context window.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- HNSW Algorithm -->
      <h3 style="color: var(--accent-emerald); font-size: 1.1rem; margin-top: 2rem;">2. How HNSW (Hierarchical Navigable Small World) Works</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        HNSW is the dominant vector indexing algorithm in modern vector databases:
      </p>
      <ul style="margin-left: 1.25rem; color: var(--text-secondary); line-height: 1.7;">
        <li><strong>Multi-Layer Skip-List Graph:</strong> Vectors are organized in hierarchical layers. Top layers have sparse, long-range highway edges; bottom layer (Layer 0) has dense, short-range edges connecting all vectors.</li>
        <li><strong>Logarithmic Search ($O(\log N)$):</strong> Search begins at the top layer with greedy routing (hopping to the neighbor closest to the query vector). When a local minimum is hit, it drops to the next layer down and resumes until it reaches Layer 0.</li>
        <li><strong>Parameters:</strong> <code>M</code> (max bi-directional connections per node, controls memory) and <code>efSearch</code> / <code>efConstruction</code> (size of dynamic candidate list, controls recall vs query latency).</li>
      </ul>
    </section>

    <!-- SECTION 4: INTERVIEW TRAPS -->
    <section id="interview-traps" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚠️ High-Frequency GenAI & Agent Traps</h2>
        <span class="pill pill-rose">Recruiter Traps</span>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #1: Why does Naive RAG fail in real production?</div>
        <p><strong>Recruiter favorite!</strong> Naive RAG (chunking text naively &rarr; embedding &rarr; top-K cosine similarity &rarr; send to LLM) suffers from three catastrophic failure modes:</p>
        <ol style="margin-left: 1.25rem;">
          <li><strong>Semantic Disconnect / Keyword Misses:</strong> Dense embeddings excel at conceptual similarity but fail on exact part numbers, acronyms, or specific IDs (where BM25 keyword search dominates!).</li>
          <li><strong>"Lost in the Middle" Phenomenon:</strong> LLMs attend strongly to the beginning and end of long prompts but ignore facts buried in the middle chunks of a 10-chunk context window.</li>
          <li><strong>Chunk Boundary Truncation:</strong> Fixed 500-token chunks slice sentences or tables in half, destroying relational semantics.</li>
        </ol>
      </div>

      <div class="callout callout-pro">
        <div class="callout-title">💡 The RAG Triad for Hallucination Evaluation (TruLens / Ragas)</div>
        <p>To scientifically evaluate RAG applications without human grading, industry uses the <strong>RAG Triad</strong>:</p>
        <ul style="margin-left: 1.25rem;">
          <li><strong>1. Context Relevance:</strong> Is the retrieved context actually relevant to the user query? (Evaluates Retriever).</li>
          <li><strong>2. Groundedness (Faithfulness):</strong> Is the LLM's answer completely grounded in the retrieved context, or did it invent external claims? (Evaluates Hallucination).</li>
          <li><strong>3. Answer Relevance:</strong> Does the generated response directly answer what the user asked? (Evaluates Generator).</li>
        </ul>
      </div>
    </section>

    <!-- SECTION 5: FLASHCARDS -->
    <section id="flashcards" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🎯 Interview Q&A Flashcards (Self-Assessment)</h2>
        <span class="pill pill-blue">5 Questions</span>
      </div>

      <details class="faq-accordion">
        <summary>Q1: How do you prevent infinite loops in cyclic LangGraph multi-agent systems?</summary>
        <div class="faq-body">
          In LangGraph, infinite cyclic loops are prevented through three defensive mechanisms:
          <ol style="margin-left: 1.2rem;">
            <li><strong>Hard Recursion Limit:</strong> Pass <code>config={{"recursion_limit": 25}}</code> in <code>app.invoke()</code>, which forcibly throws a <code>GraphRecursionError</code> if the graph exceeds the threshold.</li>
            <li><strong>State Step Counter:</strong> Add an integer <code>retry_count: Annotated[int, operator.add]</code> to the graph state. In conditional edge routing, if <code>state["retry_count"] &gt;= MAX_RETRIES</code>, route to a fallback human-escalation or default response node instead of looping back to the planner.</li>
            <li><strong>Deterministic Validator Gates:</strong> Ensure the validator has progressive relaxation criteria or unambiguous pass/fail boundaries.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q2: What is Reciprocal Rank Fusion (RRF) and why is it used in Hybrid Search?</summary>
        <div class="faq-body">
          Cosine similarity scores (e.g. 0.82) from dense embeddings and BM25 scores (e.g. 14.5) operate on completely different numerical scales and cannot be directly summed.<br>
          <strong>RRF (Reciprocal Rank Fusion)</strong> normalizes rankings by combining only their ordinal ranks rather than raw scores:
          $$RRF(d) = \sum_{{m \in M}} \frac{{1}}{{k + rank_m(d)}}$$
          where $k$ is a constant (typically 60). Documents appearing in the top 5 of both BM25 and Dense search shoot to the top of the fused results!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q3: What is the difference between Function Calling and ReAct?</summary>
        <div class="faq-body">
          • <strong>ReAct (Reason + Act):</strong> A prompt engineering pattern where the LLM is prompted to output structured thought chains: <em>Thought &rarr; Action &rarr; Observation &rarr; Thought...</em> Parses text output via regex/string formatting.<br>
          • <strong>Native Function Calling / Tool Calling:</strong> Model fine-tuning level capability (OpenAI, Anthropic, Gemini). The model natively emits valid, structured JSON conforming to a JSON Schema specification, bypassing fragile text parsing.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q4: What is Pre-filtering vs Post-filtering in Vector Databases?</summary>
        <div class="faq-body">
          • <strong>Post-Filtering:</strong> Perform ANN vector search across the entire database to find top 100 vectors, then filter out items that don't match metadata (e.g. <code>user_id == 42</code>). <em>Catastrophic flaw:</em> If only 1% of docs belong to user 42, the top 100 might contain zero matching items!<br>
          • <strong>Single-Stage Filtered HNSW (e.g. Qdrant):</strong> During the graph traversal, the algorithm only considers hops between nodes that satisfy the metadata filter payload, guaranteeing accurate top-K results with zero recall loss.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q5: What is Small-to-Big (Parent Document) Chunking?</summary>
        <div class="faq-body">
          <strong>Problem:</strong> Small chunks (100 tokens) yield accurate vector embedding matches because they contain focused semantics, but lack surrounding context for the LLM to generate answers. Large chunks (1000 tokens) provide rich context but dilute embedding vectors.<br><br>
          <strong>Small-to-Big Solution:</strong> Text is split into small child chunks (e.g. 150 tokens) for vector indexing. Each child chunk stores a reference to its larger parent document (e.g. 1000 tokens). Vector search matches against the child chunk, but the system retrieves and feeds the full <strong>parent chunk</strong> to the LLM context window!
        </div>
      </details>
    </section>
    """
    return toc, content
