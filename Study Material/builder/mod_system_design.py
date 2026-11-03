# mod_system_design.py - System Design & Distributed Systems Module Generator

def get_content():
    toc = [
        ("rapid-recall", "⚡ 10-Min Rapid Recall Sheet"),
        ("visual-diagrams", "📊 Visual HLD & Distributed Architectures"),
        ("core-deep-dives", "🧠 Consistent Hashing, Rate Limiting & TinyURL"),
        ("interview-traps", "⚠️ High-Frequency Distributed Systems Traps"),
        ("flashcards", "🎯 10 High-Frequency GFG Interview Q&As")
    ]

    # SVG 1: Consistent Hashing Ring with Virtual Nodes
    svg_hash = """
    <svg viewBox="0 0 860 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ch-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Center Hash Ring -->
      <circle cx="340" cy="180" r="130" fill="none" stroke="#334155" stroke-width="4" stroke-dasharray="6" />
      <text x="340" y="175" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Hash Ring (0 to 2³² - 1)</text>
      <text x="340" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">Clockwise Key Routing &orarr;</text>

      <!-- Server Nodes on Ring -->
      <!-- Node A -->
      <circle cx="340" cy="50" r="18" fill="#0284c7" stroke="#38bdf8" stroke-width="2" />
      <text x="340" y="55" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">A</text>
      <text x="340" y="25" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Server A</text>

      <!-- Node B -->
      <circle cx="470" cy="180" r="18" fill="#059669" stroke="#34d399" stroke-width="2" />
      <text x="470" y="185" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">B</text>
      <text x="515" y="185" fill="#34d399" font-size="10" font-weight="700" text-anchor="start">Server B</text>

      <!-- Node C -->
      <circle cx="210" cy="180" r="18" fill="#d97706" stroke="#fbbf24" stroke-width="2" />
      <text x="210" y="185" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">C</text>
      <text x="165" y="185" fill="#fbbf24" font-size="10" font-weight="700" text-anchor="end">Server C</text>

      <!-- Virtual Nodes (A_v, B_v, C_v) -->
      <circle cx="430" cy="90" r="10" fill="#0369a1" />
      <text x="455" y="93" fill="#94a3b8" font-size="9">A_v1</text>

      <circle cx="430" cy="270" r="10" fill="#047857" />
      <text x="455" y="275" fill="#94a3b8" font-size="9">B_v1</text>

      <circle cx="250" cy="270" r="10" fill="#b45309" />
      <text x="215" y="275" fill="#94a3b8" font-size="9">C_v1</text>

      <!-- Keys mapped on Ring -->
      <!-- Key 1 -->
      <circle cx="390" cy="58" r="6" fill="#f43f5e" />
      <text x="410" y="52" fill="#f43f5e" font-size="9" font-weight="700">Key 1 &rarr; B</text>

      <!-- Key 2 -->
      <circle cx="460" cy="225" r="6" fill="#f43f5e" />
      <text x="480" y="235" fill="#f43f5e" font-size="9" font-weight="700">Key 2 &rarr; C</text>

      <!-- Explanation Box Right -->
      <rect x="560" y="40" width="280" height="280" rx="8" fill="#1e293b" stroke="#334155" />
      <text x="700" y="68" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Consistent Hashing Rules</text>

      <text x="580" y="105" fill="#f1f5f9" font-size="11" font-weight="700">1. Key Placement:</text>
      <text x="580" y="125" fill="#94a3b8" font-size="10">Hash key &rarr; place on ring &rarr; walk</text>
      <text x="580" y="140" fill="#94a3b8" font-size="10">clockwise &rarr; first server owns the key.</text>

      <text x="580" y="170" fill="#f1f5f9" font-size="11" font-weight="700">2. Virtual Nodes (vNodes):</text>
      <text x="580" y="190" fill="#94a3b8" font-size="10">Each physical server has 100-256</text>
      <text x="580" y="205" fill="#94a3b8" font-size="10">virtual positions to eliminate data skew.</text>

      <text x="580" y="235" fill="#f1f5f9" font-size="11" font-weight="700">3. Node Addition / Removal:</text>
      <text x="580" y="255" fill="#34d399" font-size="10">Only K/N keys are moved! (vs 100%</text>
      <text x="580" y="270" fill="#34d399" font-size="10">re-hash in naive key % N).</text>
    </svg>
    """

    # SVG 2: TinyURL Microservices HLD
    svg_tinyurl = """
    <svg viewBox="0 0 860 300" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="tu-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>

      <!-- Client -->
      <rect x="20" y="110" width="90" height="70" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <text x="65" y="140" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Client</text>
      <text x="65" y="158" fill="#94a3b8" font-size="9" text-anchor="middle">Browser/App</text>

      <line x1="110" y1="145" x2="145" y2="145" stroke="#38bdf8" stroke-width="2" marker-end="url(#tu-arrow)" />

      <!-- CDN & L7 LB -->
      <rect x="150" y="100" width="120" height="90" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5" />
      <text x="210" y="130" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">CDN &amp; L7 LB</text>
      <text x="210" y="150" fill="#bae6fd" font-size="9" text-anchor="middle">Cloudflare / NGINX</text>
      <text x="210" y="165" fill="#e0f2fe" font-size="8" text-anchor="middle">SSL / Rate Limit</text>

      <line x1="270" y1="145" x2="315" y2="145" stroke="#38bdf8" stroke-width="2" marker-end="url(#tu-arrow)" />

      <!-- Web / App Cluster -->
      <rect x="320" y="100" width="130" height="90" rx="8" fill="#1e293b" stroke="#34d399" stroke-width="2" />
      <text x="385" y="130" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">API Servers</text>
      <text x="385" y="150" fill="#f1f5f9" font-size="9" text-anchor="middle">Stateless App Nodes</text>
      <text x="385" y="165" fill="#94a3b8" font-size="8" text-anchor="middle">Base62 Encode/Decode</text>

      <!-- Split to Cache (Top) and DB (Bottom) and KGS (Right) -->
      <line x1="450" y1="125" x2="515" y2="70" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#tu-arrow)" />
      <line x1="450" y1="165" x2="515" y2="220" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#tu-arrow)" />

      <!-- Redis Cache Cluster -->
      <rect x="520" y="40" width="140" height="65" rx="6" fill="#881337" stroke="#f43f5e" stroke-width="1.5" />
      <text x="590" y="65" fill="#fecdd3" font-size="11" font-weight="700" text-anchor="middle">Redis Cache</text>
      <text x="590" y="82" fill="#ffffff" font-size="9" text-anchor="middle">ShortURL &rarr; LongURL</text>
      <text x="590" y="95" fill="#fda4af" font-size="8" text-anchor="middle">LRU Eviction (Top 20%)</text>

      <!-- Database Cluster -->
      <rect x="520" y="195" width="140" height="75" rx="6" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="590" y="220" fill="#a7f3d0" font-size="11" font-weight="700" text-anchor="middle">Primary DB (SQL/NoSQL)</text>
      <text x="590" y="238" fill="#ffffff" font-size="9" text-anchor="middle">Stores URL Mappings</text>
      <text x="590" y="252" fill="#6ee7b7" font-size="8" text-anchor="middle">Read Replicas + Sharding</text>

      <!-- KGS (Key Generation Service) -->
      <line x1="450" y1="145" x2="715" y2="145" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#tu-arrow)" />
      <rect x="720" y="105" width="125" height="80" rx="6" fill="#78350f" stroke="#fbbf24" stroke-width="1.5" />
      <text x="782" y="132" fill="#fde68a" font-size="11" font-weight="800" text-anchor="middle">KGS Cluster</text>
      <text x="782" y="150" fill="#ffffff" font-size="9" text-anchor="middle">Pre-generates 7-char</text>
      <text x="782" y="165" fill="#fde68a" font-size="8" text-anchor="middle">Collision-Free Keys</text>

      <text x="430" y="25" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">High-Level Architecture (HLD) of a High-Throughput URL Shortener (TinyURL)</text>
    </svg>
    """

    content = r"""
    <!-- SECTION 1: RAPID RECALL -->
    <section id="rapid-recall" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚡ 10-Minute Rapid Recall Cheat Sheet</h2>
        <span class="pill pill-blue">High-Level Design</span>
      </div>

      <!-- CAP & PACELC -->
      <h3 style="font-size: 1rem; color: var(--accent-blue); margin: 1rem 0 0.5rem;">1. CAP Theorem & PACELC Master Matrix</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Classification</th>
              <th>Guarantees Under Partition (P)</th>
              <th>Behavior During Normal Operation (No Partition)</th>
              <th>Real-World Systems</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>CP (Consistency + Partition)</strong></td>
              <td>Refuses requests or errors out to guarantee strict linearizable consistency across remaining nodes.</td>
              <td>Focuses on ACID consistency over lowest latency.</td>
              <td>Google Spanner, HBase, ZooKeeper, MongoDB (strict write majority).</td>
            </tr>
            <tr>
              <td><strong>AP (Availability + Partition)</strong></td>
              <td>Always accepts reads and writes, returning potentially stale data (Eventual Consistency).</td>
              <td>Focuses on ultra-low read/write latency.</td>
              <td>Amazon DynamoDB, Apache Cassandra, CouchDB.</td>
            </tr>
            <tr>
              <td><strong>PACELC Theorem Extension</strong></td>
              <td colspan="3">
                <strong>If Partition (P):</strong> Choose Availability (A) OR Consistency (C).<br>
                <strong>Else (E):</strong> Choose Latency (L) OR Consistency (C).<br>
                <em>Example:</em> DynamoDB is <strong>PA/EL</strong> (Available under partition, Low latency under normal conditions).
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Rate Limiting Algorithms -->
      <h3 style="font-size: 1rem; color: var(--accent-emerald); margin: 1.5rem 0 0.5rem;">2. Rate Limiting Algorithms Matrix</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Algorithm</th>
              <th>How It Works</th>
              <th>Pros</th>
              <th>Cons / Pitfalls</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Token Bucket</strong></td>
              <td>Tokens added to bucket at constant rate $R$ up to capacity $B$. Request consumes 1 token.</td>
              <td>Allows short controlled bursts up to bucket capacity $B$; memory-efficient ($O(1)$ per user).</td>
              <td>Requires concurrency synchronization (handled via Redis Lua script).</td>
            </tr>
            <tr>
              <td><strong>Leaky Bucket</strong></td>
              <td>Requests enter a FIFO queue and leak out at a strictly constant processing rate.</td>
              <td>Smooths traffic outflow to perfectly constant rate; ideal for message queues.</td>
              <td>Bursts are buffered or dropped even if backend is completely idle.</td>
            </tr>
            <tr>
              <td><strong>Sliding Window Counter</strong></td>
              <td>Blends request count of current window and percentage of previous window: $\text{Count} = C_{curr} + C_{prev} \times (1 - \text{progress})$.</td>
              <td>Smooths out boundary burst spikes of Fixed Window without high memory cost of Sliding Log.</td>
              <td>Approximation based on uniform traffic assumption (near 99.9% accurate).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Caching Invalidation Table -->
      <h3 style="font-size: 1rem; color: var(--accent-amber); margin: 1.5rem 0 0.5rem;">3. Caching Invalidation & Failure Modes Cheat Sheet</h3>
      <div class="table-container">
        <table class="dense-table">
          <thead>
            <tr>
              <th>Cache Failure Mode</th>
              <th>Root Cause</th>
              <th>Impact</th>
              <th>Standard Production Fix</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Cache Stampede (Thundering Herd)</strong></td>
              <td>Hot cached key expires; 10,000 concurrent requests all miss cache and hit the database simultaneously!</td>
              <td>Database CPU spikes to 100%, causing cascading database failure.</td>
              <td><strong>Distributed Mutex Lock</strong> (only 1 request queries DB while others wait) or <strong>Probabilistic Early Expiration (XFetch algorithm)</strong>.</td>
            </tr>
            <tr>
              <td><strong>Cache Penetration</strong></td>
              <td>Malicious or erroneous queries for keys that do NOT exist in DB (e.g. <code>id = -9999</code>).</td>
              <td>Every query bypasses cache and hits disk database every time!</td>
              <td><strong>Bloom Filter</strong> in front of cache (returns "definitely not in DB" in $O(1)$) OR cache the <code>null</code> value with a short TTL.</td>
            </tr>
            <tr>
              <td><strong>Cache Avalanche</strong></td>
              <td>Thousands of cached keys set with the identical expiration time (e.g. 1 hour) expire simultaneously.</td>
              <td>Sudden flood of massive queries overwhelms database at that exact minute.</td>
              <td><strong>Add Random Jitter</strong> to expiration TTL: $\text{TTL} = \text{Base} + \text{rand}(0, 300\text{s})$.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: VISUAL DIAGRAMS -->
    <section id="visual-diagrams" class="section-block">
      <div class="section-head">
        <h2 class="section-title">📊 Visual HLD & Distributed Architectures</h2>
        <span class="pill pill-emerald">System Architectures</span>
      </div>

      <div class="svg-diagram-card">
        __SVG_CONSISTENT_HASH__
        <div class="diagram-caption">Figure 10.1: Consistent Hashing Ring with Virtual Nodes — Eliminating Data Skew and Minimizing Key Migration on Server Scale-Out.</div>
      </div>

      <div class="svg-diagram-card">
        __SVG_TINYURL__
        <div class="diagram-caption">Figure 10.2: Production High-Level Design (HLD) of a Scalable URL Shortener (TinyURL) with Key Generation Service (KGS).</div>
      </div>
    </section>

    <!-- SECTION 3: CORE DEEP DIVES -->
    <section id="core-deep-dives" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🧠 Consistent Hashing, Rate Limiting & TinyURL</h2>
        <span class="pill pill-purple">System Design Mechanics</span>
      </div>

      <!-- TinyURL Math & Encoding -->
      <h3 style="color: var(--accent-blue); font-size: 1.1rem; margin-top: 1rem;">1. Designing TinyURL: Base62 Encoding & Key Generation Service (KGS)</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        <strong>Scale & Capacity Estimations:</strong><br>
        • Write volume: 500 million new URLs / month &rarr; ~200 writes / sec.<br>
        • Read volume: 100:1 read-to-write ratio &rarr; 20,000 reads / sec (20K QPS).<br>
        • Storage for 5 years: $500\text{M} \times 12 \times 5 = 30\text{ billion}$ records. At 500 bytes per record = <strong>15 TB storage</strong>.
      </p>

      <div class="callout callout-pro">
        <div class="callout-title">💡 Why Base62 Encoding instead of MD5/Base64?</div>
        <ul>
          <li><strong>Base64</strong> uses characters <code>[0-9a-zA-Z+/]</code>. The symbols <code>+</code> and <code>/</code> have special reserved meanings in URLs and require encoding (e.g. <code>%2B</code>), breaking URL aesthetics.</li>
          <li><strong>Base62</strong> uses only alphanumeric characters: <code>[0-9a-zA-Z]</code> (10 digits + 26 lowercase + 26 uppercase = 62 characters).</li>
          <li>A 7-character string in Base62 produces: $62^7 = \mathbf{3,521,614,606,208}$ (3.52 Trillion) unique URLs, easily sufficient for centuries!</li>
        </ul>
      </div>

      <!-- KGS vs MD5 -->
      <h3 style="color: var(--accent-amber); font-size: 1.1rem; margin-top: 1.5rem;">2. Resolving Hash Collisions: Key Generation Service (KGS)</h3>
      <p style="color: var(--text-secondary); margin-bottom: 0.5rem;">
        If you hash long URLs using MD5/SHA256 and take the first 7 characters, different URLs can hash to the same 7 characters (Hash Collision). Retrying or appending sequence numbers causes race conditions in distributed clusters.<br><br>
        <strong>The KGS Solution:</strong> A dedicated standalone Key Generation Service pre-generates 7-character random unique strings offline and stores them in a database. When a server needs to shorten a URL, it grabs a batch of 1,000 pre-generated unique keys from KGS into local memory. Zero collisions, zero MD5 hash overhead, and instant $O(1)$ response time!
      </p>
    </section>

    <!-- SECTION 4: INTERVIEW TRAPS -->
    <section id="interview-traps" class="section-block">
      <div class="section-head">
        <h2 class="section-title">⚠️ High-Frequency Distributed Systems Traps</h2>
        <span class="pill pill-rose">System Design Traps</span>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #1: L4 vs L7 Load Balancing — Which should you pick?</div>
        <p><strong>L4 (Transport Layer - TCP/UDP):</strong> Operates strictly on IP address and port numbers without inspecting the payload packet contents. Extremely fast, minimal CPU overhead (handles millions of packets/sec via Linux IPVS / AWS NLB). Cannot route based on HTTP headers, cookies, or URL paths.</p>
        <p><strong>L7 (Application Layer - HTTP/HTTPS):</strong> Terminates the TLS connection, parses the full HTTP request (URL paths, headers, JWT tokens). Enables smart routing (e.g. <code>/api/v1/video</code> &rarr; Video Service; <code>/api/v1/auth</code> &rarr; Auth Service), but consumes significantly more CPU memory for TLS decrypt and request parsing (e.g. AWS ALB, NGINX, HAProxy).</p>
      </div>

      <div class="callout callout-trap">
        <div class="callout-title">Trap #2: Push vs Pull Architecture for Social Feeds (The Celebrity Problem)</div>
        <p>• <strong>Push Model (Fan-out-on-write):</strong> When User A posts a tweet, system pushes it to the home feed cache of all their followers. Reads are instant ($O(1)$). <em>Catastrophic failure:</em> When Elon Musk (200M followers) tweets, the server must write to 200,000,000 user feed mailboxes, creating a massive queue backlog!</p>
        <p>• <strong>Hybrid Solution (Production Twitter/Instagram):</strong> Standard users use Push model. For "Celebrity" users with &gt; 50,000 followers, do NOT fan out their posts! When a follower opens their feed, the system pulls the celebrity's recent tweets and merges them with the follower's feed in-memory at read time (Fan-out-on-read).</p>
      </div>
    </section>

    <!-- SECTION 5: FLASHCARDS (10 GFG QUESTIONS) -->
    <section id="flashcards" class="section-block">
      <div class="section-head">
        <h2 class="section-title">🎯 10 High-Frequency GFG Interview Q&As (Self-Assessment)</h2>
        <span class="pill pill-blue">10 Questions</span>
      </div>

      <details class="faq-accordion">
        <summary>Q1: What is Consistent Hashing and why does adding a node only redistribute K/N keys?</summary>
        <div class="faq-body">
          In standard hashing (<code>hash(key) % N</code>), changing $N$ (adding or removing a server) changes the modulus denominator for almost 100% of keys, invalidating the entire cache fleet and causing a database crash.<br><br>
          In <strong>Consistent Hashing</strong>, both servers and keys are hashed onto the same circular ring ($0$ to $2^{32}-1$). A key belongs to the first server encountered clockwise. When a new server is added, it only claims keys between itself and its predecessor on the ring. Thus, on average, only $K/N$ keys move (where $K = \text{total keys}$, $N = \text{total servers}$)!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q2: How does Apache Kafka achieve its massive throughput?</summary>
        <div class="faq-body">
          Kafka achieves throughput of millions of messages/sec on commodity hardware through 4 architectural design choices:
          <ol style="margin-left: 1.2rem;">
            <li><strong>Sequential Disk I/O:</strong> Kafka appends messages sequentially to an immutable commit log. Sequential disk access is as fast as random memory access on modern NVMe drives.</li>
            <li><strong>OS Page Cache:</strong> Messages are cached in the Linux OS page cache rather than Java JVM heap, eliminating JVM garbage collection pauses.</li>
            <li><strong>Zero-Copy Transfer:</strong> Uses the Linux <code>sendfile()</code> system call to transfer data directly from OS page cache to network socket buffer, bypassing user-space CPU memory copying.</li>
            <li><strong>Batching & Compression:</strong> Producers batch messages into chunks and compress them (Snappy, LZ4) before network transmission.</li>
          </ol>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q3: What are the differences between WebSockets, Long Polling, and Server-Sent Events (SSE)?</summary>
        <div class="faq-body">
          • <strong>Short Polling:</strong> Client repeatedly sends HTTP requests at fixed intervals (high overhead, mostly empty responses).<br>
          • <strong>Long Polling:</strong> Client sends HTTP request; server holds connection open until new data is available or timeout occurs.<br>
          • <strong>WebSockets:</strong> Full-duplex, bi-directional persistent TCP connection initiated via HTTP upgrade handshake. Ideal for real-time multiplayer games, live trading order books (Pace Stock Broking), and chat apps.<br>
          • <strong>Server-Sent Events (SSE):</strong> Monodirectional stream from server to client over HTTP (client cannot send data over the same connection). Ideal for live sports ticker updates, stock price feeds, and LLM text streaming (ChatGPT/Gemini).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q4: How do you implement a distributed Rate Limiter in Redis without race conditions?</summary>
        <div class="faq-body">
          To enforce an atomic sliding window rate limit without race conditions between concurrent requests, use a <strong>Redis Lua Script</strong>:
          <pre><code class="language-lua">-- Redis Lua script for Sliding Window Rate Limiter
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])
local clearBefore = now - window

-- 1. Remove timestamps older than current window
redis.call('ZREMRANGEBYSCORE', key, 0, clearBefore)
-- 2. Count current elements in window
local currentRequests = redis.call('ZCARD', key)

if currentRequests < limit then
    redis.call('ZADD', key, now, now)
    redis.call('EXPIRE', key, window)
    return 1 -- Allowed
else
    return 0 -- Throttled
end</code></pre>
          Because Redis executes Lua scripts atomically in a single thread, no locks are required!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q5: What is the difference between Strong Consistency, Eventual Consistency, and Read-Your-Writes?</summary>
        <div class="faq-body">
          • <strong>Strong (Linearizable) Consistency:</strong> Any read following a write is guaranteed to return the updated value across all replicas. Requires synchronous replication and consensus (Paxos/Raft). High write latency.<br>
          • <strong>Eventual Consistency:</strong> Replicas converge to the same value over time if no new updates are made. Reads immediately after a write may return stale data. High availability and low latency.<br>
          • <strong>Read-Your-Writes (Monotonic Read) Consistency:</strong> Guarantees that a user will always see their own updates immediately (e.g. posting a comment shows up on the author's screen immediately even if other users see it 3 seconds later).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q6: What are Bloom Filters and how do they prevent Cache Penetration?</summary>
        <div class="faq-body">
          A <strong>Bloom Filter</strong> is a space-efficient probabilistic data structure that tests whether an element is a member of a set using a bit array of size $m$ and $k$ independent hash functions.<br>
          • <strong>Guarantees:</strong> Zero False Negatives (If it says an item is NOT in the database, it is 100% definitely NOT in the database!). Small probability of False Positives.<br>
          • <strong>Usage in Caching:</strong> When a request for key $X$ arrives, check the Bloom Filter first. If the Bloom filter returns "false", reject the request immediately with HTTP 404 without querying Redis or touching the SQL database!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q7: How do you design an Idempotent API?</summary>
        <div class="faq-body">
          An operation is <strong>idempotent</strong> if making the request multiple times produces the identical side-effect as making it once (essential for payment processing when network drops mid-request).<br>
          • <strong>Implementation:</strong> Client generates a unique UUID <strong>Idempotency Key</strong> (e.g. in HTTP header <code>Idempotency-Key: 123e4567-e89b...</code>).<br>
          • Server stores the idempotency key in a Redis/SQL distributed lock with state (<code>PROCESSING</code> / <code>COMPLETED</code>).<br>
          • If a duplicate request arrives while processing, reject or wait; if already completed, return the cached successful response without re-charging the credit card!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q8: How does a Content Delivery Network (CDN) route requests using Anycast?</summary>
        <div class="faq-body">
          In <strong>Anycast BGP Routing</strong>, multiple CDN edge servers located across different geographical continents share the <strong>exact same single IP address</strong>.<br>
          When a user queries the IP, internet border routers route the packets to the geographically closest edge server via the shortest BGP autonomous system (AS) hop count. Static assets (images, video chunks, CSS) are served from local edge RAM/SSD in &lt; 10ms without crossing ocean cables!
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q9: Explain the Two-Phase Commit (2PC) Protocol and its biggest flaw.</summary>
        <div class="faq-body">
          2PC coordinates atomic distributed transactions across multiple database nodes:
          <ul>
            <li><strong>Phase 1 (Prepare):</strong> Coordinator sends <code>PREPARE</code> to all cohorts. Cohorts execute transaction, write to undo/redo logs, lock resources, and reply <code>YES</code> or <code>NO</code>.</li>
            <li><strong>Phase 2 (Commit):</strong> If ALL cohorts vote <code>YES</code>, coordinator sends <code>COMMIT</code>. If any cohort votes <code>NO</code>, coordinator sends <code>ROLLBACK</code>.</li>
          </ul>
          <strong>Biggest Flaw (Blocking Coordinator Failure):</strong> If the coordinator crashes mid-commit after cohorts locked their resources, cohorts are permanently blocked in uncertainty, holding table locks and freezing the system! (Modern systems use Saga Pattern or Raft consensus instead).
        </div>
      </details>

      <details class="faq-accordion">
        <summary>Q10: What is Database Sharding and how do you choose a Shard Key?</summary>
        <div class="faq-body">
          <strong>Database Sharding</strong> partitions large database tables horizontally across distinct physical database servers.<br>
          <strong>Shard Key Selection Criteria:</strong>
          <ul>
            <li><strong>High Cardinality:</strong> Keys must have millions of distinct values (e.g. <code>user_id</code> vs low-cardinality <code>country</code>).</li>
            <li><strong>Uniform Data Distribution:</strong> Avoids "hotspot shards" where 90% of traffic hits one physical machine.</li>
            <li><strong>Query Isolation:</strong> Choose a key that groups frequently queried data on the same shard to avoid costly distributed cross-shard joins (Scatter-Gather queries).</li>
          </ul>
        </div>
      </details>
    </section>
    """
    
    rendered_content = content.replace("__SVG_CONSISTENT_HASH__", svg_hash).replace("__SVG_TINYURL__", svg_tinyurl)
    return toc, rendered_content
