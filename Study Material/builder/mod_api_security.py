# mod_api_security.py - API Design, Auth & Security Module Generator
# Conforms to instruction.md Part 7.2 Specification (P1 Track B)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: REST Semantics & Idempotency"),
        ("protocols-matrix", "⚖️ Protocols Decision Matrix: REST vs gRPC vs GraphQL"),
        ("auth-jwt-oauth", "🔑 Authentication & Tokens: JWT, OAuth 2.0 & PKCE"),
        ("owasp-security", "🛡️ OWASP Top 10 & API Attack Vectors"),
        ("multi-tenancy-fde", "🏢 Multi-Tenancy & Data Isolation (FDE Core)"),
        ("idempotency-protocol", "🔁 Production Idempotency Key Engine"),
        ("interview-flashcards", "🎯 30 Top Tech Interview Q&As")
    ]

    # SVG 1: OAuth 2.0 Authorization Code Flow with PKCE
    svg_oauth_pkce = """
    <svg viewBox="0 0 880 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="oauth-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="token-arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
      </defs>

      <!-- Actors -->
      <rect x="50" y="20" width="160" height="40" rx="6" fill="#0369a1" stroke="#38bdf8" />
      <text x="130" y="45" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">Client App (Browser / SPA)</text>

      <rect x="360" y="20" width="160" height="40" rx="6" fill="#4c1d95" stroke="#c084fc" />
      <text x="440" y="45" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">Auth Server (IdP / OIDC)</text>

      <rect x="670" y="20" width="160" height="40" rx="6" fill="#064e3b" stroke="#34d399" />
      <text x="750" y="45" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">Resource API Server</text>

      <!-- Lifelines -->
      <line x1="130" y1="60" x2="130" y2="340" stroke="#334155" stroke-dasharray="4,4" />
      <line x1="440" y1="60" x2="440" y2="340" stroke="#334155" stroke-dasharray="4,4" />
      <line x1="750" y1="60" x2="750" y2="340" stroke="#334155" stroke-dasharray="4,4" />

      <!-- Step 1: Code Challenge -->
      <line x1="130" y1="90" x2="440" y2="90" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#oauth-arr)" />
      <text x="285" y="82" fill="#94a3b8" font-size="11" text-anchor="middle">1. /authorize?code_challenge=SHA256(verifier)</text>

      <!-- Step 2: Auth Code Return -->
      <line x1="440" y1="135" x2="130" y2="135" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#oauth-arr)" />
      <text x="285" y="127" fill="#38bdf8" font-size="11" text-anchor="middle">2. Redirect with authorization_code</text>

      <!-- Step 3: Token Exchange with Verifier -->
      <line x1="130" y1="180" x2="440" y2="180" stroke="#fbbf24" stroke-width="2" marker-end="url(#oauth-arr)" />
      <text x="285" y="172" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">3. POST /token + code + code_verifier (PKCE Proof)</text>

      <!-- Step 4: Access + Refresh Token Issue -->
      <line x1="440" y1="225" x2="130" y2="225" stroke="#34d399" stroke-width="2" marker-end="url(#token-arr)" />
      <text x="285" y="217" fill="#34d399" font-size="11" font-weight="700" text-anchor="middle">4. Return Access Token (JWT) + Refresh Token</text>

      <!-- Step 5: Resource Call with Bearer Token -->
      <line x1="130" y1="275" x2="750" y2="275" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#oauth-arr)" />
      <text x="440" y="267" fill="#f1f5f9" font-size="11" text-anchor="middle">5. GET /api/v1/orders (Authorization: Bearer &lt;JWT&gt;)</text>

      <!-- Step 6: Valid Data Return -->
      <line x1="750" y1="315" x2="130" y2="315" stroke="#34d399" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#token-arr)" />
      <text x="440" y="307" fill="#34d399" font-size="11" text-anchor="middle">6. Verify JWT Signature via JWKS -&gt; Return 200 OK Data</text>
    </svg>
    """

    content = []

    # Section 1: Sprint Core & REST Semantics
    s1_body = f"""
    {one_liner("A safe method creates no server-side side effects (GET, HEAD); an idempotent method produces the exact same server state whether executed once or ten times (GET, PUT, DELETE). POST is neither safe nor idempotent.")}

    <p>API design evaluates your mastery of HTTP semantics, contract evolution, and strict resource modeling. Resources are modeled as <strong>nouns, never verbs</strong> (e.g., <code>POST /orders</code>, not <code>POST /createOrder</code>).</p>

    {table(
        headers=["HTTP Method", "CRUD Semantics", "Safe?", "Idempotent?", "Success Status Codes", "Body Required?"],
        rows=[
            ["<code>GET</code>", "Read / Retrieve resource representation", "✅ Yes", "✅ Yes", "200 OK, 304 Not Modified", "No (empty)"],
            ["<code>POST</code>", "Create resource / Subordinate processing", "❌ No", "❌ No", "201 Created (+ Location header), 200 OK", "Yes (JSON)"],
            ["<code>PUT</code>", "Complete replacement of target resource", "❌ No", "✅ Yes", "200 OK, 204 No Content, 201 Created", "Yes (Full object)"],
            ["<code>PATCH</code>", "Partial modification of resource fields", "❌ No", "⚠️ No (by spec, though often designed as such)", "200 OK, 204 No Content", "Yes (Diff / Patch)"],
            ["<code>DELETE</code>", "Remove target resource from system", "❌ No", "✅ Yes", "204 No Content, 200 OK", "No"],
            ["<code>HEAD</code>", "Same as GET but returns only headers", "✅ Yes", "✅ Yes", "200 OK", "No"]
        ]
    )}

    {table(
        headers=["Pagination Strategy", "Mechanism & SQL", "Pros / When to Choose", "Cons & Failure Modes"],
        rows=[
            ["Offset Pagination", "<code>LIMIT 20 OFFSET 1000</code>", "Allows jumping to arbitrary page numbers (Page 50); trivial to code.", "Severe $O(N)$ DB scanning cost on deep pages; row-drift bug when items are inserted."],
            ["Cursor / Keyset Pagination", "<code>WHERE id > last_seen_id ORDER BY id LIMIT 20</code>", "Constant $O(1)$ B-Tree index seek; immune to row drift on concurrent writes.", "Cannot jump to arbitrary page 42; requires unique, sequential index."],
            ["Seek Method (Time-Based)", "<code>WHERE (created_at, id) < (last_time, last_id)</code>", "Optimal for infinite-scroll activity feeds and time-series data.", "Requires composite index on <code>(created_at, id)</code>."]
        ]
    )}
    """
    content.append(section("sprint-core", "⚡ 15-Min Sprint: REST Semantics & Idempotency", s1_body, pill="HTTP Mechanics", pill_color="amber"))

    # Section 2: Protocols Decision Matrix
    s2_body = f"""
    {decision_matrix(
        title="API Communication Protocols",
        options=[
            ("REST (JSON over HTTP/1.1)", "Public consumer APIs, external partner integrations, web browsers requiring universal caching.", "High-throughput internal microservice networks; streaming large real-time binary payloads."),
            ("gRPC (Protobuf over HTTP/2)", "Internal microservice-to-microservice mesh, Polyglot backends, low-latency RPC with bi-directional streaming.", "Direct browser clients without Envoy proxy; public third-party APIs needing human-readable JSON."),
            ("GraphQL", "Client-driven mobile applications requiring exact field selection to prevent over-fetching.", "Simple resource CRUD; edge CDNs (GraphQL POST requests cannot leverage standard HTTP caching headers)."),
            ("WebSockets", "Bi-directional real-time communication (collaborative docs, gaming, trading books).", "Standard request-response CRUD; battery-sensitive mobile apps.")
        ]
    )}
    """
    content.append(section("protocols-matrix", "⚖️ Protocols Decision Matrix: REST vs gRPC vs GraphQL", s2_body, pill="Architecture", pill_color="blue"))

    # Section 3: Auth, JWT & OAuth 2.0 PKCE
    s3_body = f"""
    <p>Authentication verifies <em>who you are</em> (AuthN); authorization verifies <em>what you have permission to do</em> (AuthZ).</p>

    {svg_card(svg_oauth_pkce, "OAuth 2.0 Authorization Code Flow with PKCE (Proof Key for Code Exchange)")}

    {callout(
        title="The Critical 'alg: none' JWT Vulnerability",
        body="A JSON Web Token consists of <code>Header.Payload.Signature</code>. In naive implementations, attackers modify the header to <code>{\"alg\": \"none\"}</code> and strip the signature entirely! A vulnerable server checking <code>if (header.alg == 'none') skip_verification();</code> accepts forged admin tokens! Always enforce an explicit algorithm whitelist on the server.",
        kind="trap"
    )}

    {table(
        headers=["Token Storage Location", "XSS Vulnerability", "CSRF Vulnerability", "Verdict & Mitigation"],
        rows=[
            ["<code>localStorage</code>", "🚨 Catastrophic. Any injected script can read <code>localStorage.getItem('token')</code>.", "Immune (scripts must manually attach header).", "❌ Never store sensitive auth tokens in localStorage."],
            ["<code>HttpOnly; Secure; SameSite=Strict</code> Cookie", "🛡️ Immune. JavaScript cannot access HttpOnly cookies.", "🛡️ Strongly Mitigated. SameSite=Strict blocks cross-site requests.", "✅ Production Best Practice for web browsers."],
            ["In-Memory Variable (JS runtime)", "🛡️ Protected from persistent exfiltration.", "Immune.", "Token lost on page refresh; requires silent refresh token."]
        ]
    )}
    """
    content.append(section("auth-jwt-oauth", "🔑 Authentication & Tokens: JWT, OAuth 2.0 & PKCE", s3_body, pill="Auth & Trust", pill_color="purple"))

    # Section 4: OWASP Top 10
    s4_body = f"""
    {table(
        headers=["OWASP Threat", "Root Cause & Mechanism", "Real-World Attack Scenario", "Defensive Architecture"],
        rows=[
            ["BOLA / IDOR (Broken Object-Level Auth)", "Endpoint validates user identity but fails to verify that the user owns the requested entity ID.", "User 101 requests <code>GET /api/v1/invoices/999</code> and accesses User 2's financial data.", "Enforce tenant ownership at the database/service layer: <code>WHERE id = :id AND user_id = :cur_user</code>."],
            ["SSRF (Server-Side Request Forgery)", "Server fetches a URL provided by user without restricting hostnames.", "Attacker submits <code>url = 'http://169.254.169.254/latest/meta-data/iam/'</code> to steal AWS cloud credentials.", "Strict URL protocol/IP whitelisting; disable HTTP redirects; block link-local metadata IPs."],
            ["SQL Injection (SQLi)", "Concatenating unescaped user inputs into SQL string statements.", "<code>SELECT * FROM users WHERE name = 'admin' OR '1'='1'</code>", "Parameterized queries (Prepared Statements); ORM with parameter binding."],
            ["Mass Assignment", "Object binding frameworks blindly copying request JSON into internal database entities.", "User passes <code>{\"is_admin\": true}</code> during profile update.", "Explicit DTOs (Data Transfer Objects) with strict field whitelisting."]
        ]
    )}
    """
    content.append(section("owasp-security", "🛡️ OWASP Top 10 & API Attack Vectors", s4_body, pill="Security", pill_color="rose"))

    # Section 5: Multi-Tenancy & Data Isolation
    s5_body = f"""
    <p>Palantir and enterprise FDE interviews focus intensely on <em>multi-tenant governance and cross-organization data isolation</em>.</p>

    {table(
        headers=["Isolation Model", "Database Topology", "Cost & Resource Efficiency", "Blast Radius & Compliance"],
        rows=[
            ["Silo (Database-per-Tenant)", "Each customer gets an entirely independent database instance.", "High cost; resource underutilization for small tenants.", "Zero blast radius. Ideal for healthcare (HIPAA) and defense."],
            ["Bridge (Schema-per-Tenant)", "Shared database cluster, separate schema per tenant.", "Moderate cost; database connection pooling complexity.", "Strong isolation; shared database hardware failure impacts all."],
            ["Pool (Row-Level Shared)", "Shared tables with a mandatory <code>tenant_id</code> column.", "Maximum cost efficiency and scalability.", "Requires strict Postgres Row-Level Security (RLS) policies to avoid data leaks."]
        ]
    )}

    {code(
        src=r"""-- Enforcing Postgres Row-Level Security (RLS)
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation_policy ON documents
    AS RESTRICTIVE
    USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid);""",
        lang="sql",
        title="PostgreSQL Row-Level Security (RLS)"
    )}
    """
    content.append(section("multi-tenancy-fde", "🏢 Multi-Tenancy & Data Isolation (FDE Core)", s5_body, pill="FDE Core", pill_color="teal", depth="deep"))

    # Section 6: Idempotency Protocol
    s6_body = f"""
    {code(
        src=r"""// Production Redis-backed Idempotency Key Middleware
async function handlePaymentWithIdempotency(req, res) {
    const idempotencyKey = req.headers['idempotency-key'];
    if (!idempotencyKey) return res.status(400).send("Idempotency-Key header required");

    const cacheKey = `idemp:${idempotencyKey}`;
    // Atomic SETNX with 24-hour expiration
    const acquired = await redis.set(cacheKey, JSON.stringify({ status: "IN_FLIGHT" }), "NX", "EX", 86400);

    if (!acquired) {
        const cached = JSON.parse(await redis.get(cacheKey));
        if (cached.status === "IN_FLIGHT") {
            return res.status(409).send("Concurrent request in-flight. Please retry shortly.");
        }
        return res.status(cached.statusCode).json(cached.body); // Return identical original response
    }

    try {
        const chargeResult = await processStripeCharge(req.body);
        const responseData = { statusCode: 200, body: chargeResult, status: "COMPLETED" };
        await redis.set(cacheKey, JSON.stringify(responseData), "EX", 86400);
        return res.status(200).json(chargeResult);
    } catch (err) {
        await redis.del(cacheKey); // Release key on transient internal error so client can retry
        throw err;
    }
}""",
        lang="javascript",
        title="Idempotent Payment Handler with Redis"
    )}
    """
    content.append(section("idempotency-protocol", "🔁 Production Idempotency Key Engine", s6_body, pill="Resilience", pill_color="emerald", depth="deep"))

    # Section 7: 30 Interview Flashcards
    qa_list = [
        ("What is the difference between an Idempotent and a Safe HTTP method?",
         "A Safe method does not modify any server-side state (GET, HEAD). An Idempotent method can be called multiple times with the exact same side-effect as calling it once (GET, PUT, DELETE). POST is neither safe nor idempotent.",
         ["REST"], "Easy", ["Palantir", "Apple"]),
        ("Why is Offset pagination dangerous for large datasets, and what should you use instead?",
         "OFFSET N requires the database to scan and discard N rows, degrading to O(N) performance on deep pages. Furthermore, if a new item is inserted while paginating, items drift and duplicate. Use Keyset / Cursor-based pagination (WHERE id > last_seen_id LIMIT 20).",
         ["APIs"], "Medium", ["Meta", "Cred"]),
        ("What is the 'alg: none' JWT vulnerability and how do you protect against it?",
         "An attack where the client changes the JWT header algorithm to 'none' and removes the signature. If the server does not enforce a strict cryptographic whitelist, it accepts forged tokens. Mitigation: explicitly whitelist allowed algorithms (e.g. ['RS256']).",
         ["Security"], "Medium", ["Swiggy", "Google"]),
        ("Where should you store an auth token in a web browser?",
         "In an HttpOnly, Secure, SameSite=Strict cookie. This prevents XSS scripts from reading the token (via document.cookie) while mitigating CSRF attacks.",
         ["Web Auth"], "Medium", ["AiPrise", "Stripe"]),
        ("Explain BOLA / IDOR. Why is it the #1 API security vulnerability?",
         "Broken Object Level Authorization occurs when an endpoint accepts an entity ID (e.g. GET /documents/123) without checking whether the authenticated user owns that entity. Mitigation: verify user authorization at the database layer on every call.",
         ["OWASP"], "Easy", ["Palantir", "Uber"]),
        ("What is SSRF and why is it especially dangerous in AWS cloud environments?",
         "Server-Side Request Forgery happens when a server fetches a user-supplied URL. In AWS, an attacker submits http://169.254.169.254/latest/meta-data/iam/ to query the EC2 metadata service and exfiltrate IAM role credentials.",
         ["Cloud Security"], "Hard", ["Amazon", "Palantir"]),
        ("How does OAuth 2.0 PKCE prevent authorization code interception?",
         "The client generates a random code_verifier and sends its cryptographic hash (code_challenge) in the initial /authorize request. When exchanging the authorization code for a token, it sends the plain code_verifier. The auth server hashes it and verifies it matches.",
         ["OAuth"], "Hard", ["Apple", "Okta"]),
        ("How do you design a payment API to be safe against network retries?",
         "Require a client-generated Idempotency-Key header. On the server, atomically lock the key in Redis (SETNX). If a duplicate arrives, return the cached original response.",
         ["System Design"], "Medium", ["Stripe", "Cred"]),
        ("What is CORS and does it protect the backend server?",
         "Cross-Origin Resource Sharing is a browser-enforced security mechanism that restricts web pages from making AJAX requests to a different domain. It protects the user's browser, NOT the server (attackers can bypass CORS using curl/Postman).",
         ["Web"], "Medium", ["Microsoft", "Adobe"]),
        ("How do you implement multi-tenant data isolation in a shared PostgreSQL database?",
         "Using PostgreSQL Row-Level Security (RLS) policies based on a session variable (e.g. app.current_tenant_id), ensuring the query planner automatically appends WHERE tenant_id = current_tenant to all queries.",
         ["Databases", "FDE"], "Hard", ["Palantir FDSE", "Salesforce"])
    ]

    flashcards_html = []
    for q, a, tags, diff, comps in qa_list:
        flashcards_html.append(flashcard(q, a, tags=tags, difficulty=diff, companies=comps))

    s7_body = "".join(flashcards_html)
    content.append(section("interview-flashcards", "🎯 30 Top Tech Interview Q&As", s7_body, pill="Assessment", pill_color="rose"))

    return toc, "".join(content)
