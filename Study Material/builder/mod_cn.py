# mod_cn.py - Computer Networks & Network Systems Module Generator
# Conforms to instruction.md Part 6.4 Specification (P1 Track A)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: OSI, TCP vs UDP & Congestion"),
        ("tcp-handshake-svg", "📊 TCP 3-Way Handshake & 4-Way Teardown"),
        ("dns-resolution-svg", "🌐 DNS Resolution Chain & URL Lifecycle"),
        ("sliding-window-routing", "📦 Sliding Window Protocols & Routing Algorithms"),
        ("worked-cn-math", "📐 Worked Numericals: BDP, VLSM & Ethernet Framing"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: TCP Handshake & Teardown
    svg_handshake = """
    <svg viewBox="0 0 850 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
        <marker id="arrow-green" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#34d399" />
        </marker>
        <marker id="arrow-rose" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e" />
        </marker>
      </defs>

      <!-- Client & Server -->
      <rect x="80" y="20" width="140" height="40" rx="8" fill="#0369a1" />
      <text x="150" y="45" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">CLIENT (Host A)</text>
      <line x1="150" y1="60" x2="150" y2="460" stroke="#334155" stroke-width="2" stroke-dasharray="4" />

      <rect x="630" y="20" width="140" height="40" rx="8" fill="#065f46" />
      <text x="700" y="45" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle">SERVER (Host B)</text>
      <line x1="700" y1="60" x2="700" y2="460" stroke="#334155" stroke-width="2" stroke-dasharray="4" />

      <!-- Section 1: 3-Way Handshake -->
      <text x="425" y="85" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">--- 1. ESTABLISHMENT: 3-WAY HANDSHAKE ---</text>

      <line x1="150" y1="110" x2="690" y2="150" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />
      <rect x="330" y="112" width="190" height="24" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1" />
      <text x="425" y="128" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">1. SYN = 1, Seq = x</text>

      <line x1="700" y1="165" x2="160" y2="205" stroke="#34d399" stroke-width="2" marker-end="url(#arrow-green)" />
      <rect x="290" y="167" width="270" height="24" rx="4" fill="#0f172a" stroke="#059669" stroke-width="1" />
      <text x="425" y="183" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">2. SYN = 1, ACK = 1, Seq = y, Ack = x+1</text>

      <line x1="150" y1="220" x2="690" y2="260" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)" />
      <rect x="310" y="222" width="230" height="24" rx="4" fill="#0f172a" stroke="#0284c7" stroke-width="1" />
      <text x="425" y="238" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">3. ACK = 1, Seq = x+1, Ack = y+1</text>

      <!-- Section 2: 4-Way Teardown -->
      <text x="425" y="300" fill="#f43f5e" font-size="13" font-weight="800" text-anchor="middle">--- 2. TERMINATION: 4-WAY TEARDOWN ---</text>

      <line x1="150" y1="320" x2="690" y2="355" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-rose)" />
      <rect x="330" y="322" width="190" height="22" rx="4" fill="#0f172a" stroke="#f43f5e" stroke-width="1" />
      <text x="425" y="337" fill="#f43f5e" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">1. FIN = 1, Seq = u</text>

      <line x1="700" y1="365" x2="160" y2="395" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)" />
      <rect x="310" y="367" width="230" height="22" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1" />
      <text x="425" y="382" fill="#fbbf24" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">2. ACK = 1, Ack = u+1</text>

      <line x1="700" y1="405" x2="160" y2="435" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrow-rose)" />
      <rect x="330" y="407" width="190" height="22" rx="4" fill="#0f172a" stroke="#f43f5e" stroke-width="1" />
      <text x="425" y="422" fill="#f43f5e" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">3. FIN = 1, Seq = v</text>

      <line x1="150" y1="445" x2="690" y2="475" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrow)" />
      <rect x="310" y="447" width="230" height="22" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1" />
      <text x="425" y="462" fill="#fbbf24" font-size="11" font-weight="600" text-anchor="middle" font-family="monospace">4. ACK = 1, Ack = v+1 (Enters TIME_WAIT)</text>
    </svg>
    """

    # SVG 2: DNS Resolution Chain
    svg_dns = """
    <svg viewBox="0 0 880 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="860" height="240" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.5" />
      
      <!-- Client -->
      <rect x="30" y="90" width="110" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
      <text x="85" y="115" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Browser / OS</text>
      <text x="85" y="135" fill="#94a3b8" font-size="10" text-anchor="middle">Cache Miss</text>

      <line x1="140" y1="120" x2="200" y2="120" stroke="#38bdf8" stroke-width="2" />
      <text x="170" y="110" fill="#38bdf8" font-size="9" text-anchor="middle">1. Recursive</text>

      <!-- ISP / Public Recursive Resolver -->
      <rect x="200" y="80" width="150" height="80" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="275" y="110" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">Recursive Resolver</text>
      <text x="275" y="130" fill="#bae6fd" font-size="9" text-anchor="middle">8.8.8.8 / 1.1.1.1</text>
      <text x="275" y="145" fill="#fbbf24" font-size="9" text-anchor="middle">(Does the Legwork)</text>

      <!-- Arrows to 3 Nameservers -->
      <line x1="350" y1="100" x2="480" y2="45" stroke="#fbbf24" stroke-width="1.5" />
      <text x="415" y="65" fill="#fbbf24" font-size="9" text-anchor="middle">2. Iterative</text>

      <line x1="350" y1="120" x2="480" y2="120" stroke="#fbbf24" stroke-width="1.5" />
      <text x="415" y="112" fill="#fbbf24" font-size="9" text-anchor="middle">3. Iterative</text>

      <line x1="350" y1="140" x2="480" y2="195" stroke="#fbbf24" stroke-width="1.5" />
      <text x="415" y="175" fill="#fbbf24" font-size="9" text-anchor="middle">4. Iterative</text>

      <!-- 3 Servers on Right -->
      <rect x="480" y="25" width="360" height="45" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="500" y="52" fill="#fbbf24" font-size="11" font-weight="700">A. Root Nameserver (.):</text>
      <text x="660" y="52" fill="#94a3b8" font-size="10">Points to TLD Nameserver for .com</text>

      <rect x="480" y="100" width="360" height="45" rx="6" fill="#1e293b" stroke="#34d399" stroke-width="1.5" />
      <text x="500" y="127" fill="#34d399" font-size="11" font-weight="700">B. TLD Nameserver (.com):</text>
      <text x="670" y="127" fill="#94a3b8" font-size="10">Points to Authoritative Nameserver</text>

      <rect x="480" y="175" width="360" height="45" rx="6" fill="#064e3b" stroke="#34d399" stroke-width="2" />
      <text x="500" y="202" fill="#34d399" font-size="11" font-weight="800">C. Authoritative Nameserver:</text>
      <text x="690" y="202" fill="#a7f3d0" font-size="10">Returns A / AAAA Record (IP Address!)</text>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P1 Track A", "amber"), ("Networking", "blue"), ("15-Min Sprint", "teal"), ("Systems Core", "indigo")])
        + callout(
            "Computer Networks: Systems & Low-Latency Ground Rules",
            "In engineering loops at Cisco, Apple, Qualcomm, Cloudflare, and HFT firms (Pace Stock Broking, Tower), interviewers probe protocol mechanics, sliding window calculations, subnets, and low-latency TCP socket tuning rather than textbook definitions. Understand why TCP TIME_WAIT lasts 2×MSL, why Nagle's algorithm kills interactive RPCs, and how QUIC solves TCP head-of-line blocking.",
            "important"
        )
        + numbers_card("Networking Latency & Packet Magnitudes", [
            ("L1 Cache / Same Core", "~0.5 - 1 ns", "Fastest CPU memory reference"),
            ("Intra-Datacenter RTT", "~0.5 - 1 ms", "East-West traffic within same availability zone"),
            ("Cross-Country RTT (US Coast-to-Coast)", "~60 - 80 ms", "Speed-of-light in fiber propagation delay"),
            ("Trans-Atlantic RTT (London - NYC)", "~70 - 90 ms", "Subsea fiber optical transmission"),
            ("Ethernet Minimum Frame", "64 Bytes", "Required for CSMA/CD collision detection"),
            ("Standard MTU", "1500 Bytes", "Maximum Transmission Unit for standard Ethernet frame")
        ])
        + subsection(
            "osi-tcp-matrix",
            "OSI 7-Layer vs TCP/IP 4-Layer Architecture",
            table(
                ["Layer Name", "Protocol Data Unit (PDU)", "Core Protocols", "Addressing / Hardware", "Core Responsibility"],
                [
                    ["7. Application", "Data / Message", "HTTP/2/3, DNS, SSH, TLS, gRPC, SMTP", "URLs, Domain Names, Sockets", "User interface and application process communication."],
                    ["6. Presentation", "Data", "TLS/SSL, ASCII, JSON, Protobuf", "Syntax / Encoding", "Data serialization, compression, and cryptographic encryption."],
                    ["5. Session", "Data", "RPC, NetBIOS, SOCKS", "Session IDs, Tokens", "Establishing, managing, and terminating presentation connections."],
                    ["4. Transport", "Segment (TCP) / Datagram (UDP)", "TCP, UDP, QUIC, SCTP", "Port Numbers (16-bit: 0-65535)", "End-to-end host-to-host process communication, flow/congestion control."],
                    ["3. Network", "Packet", "IPv4, IPv6, ICMP, OSPF, BGP, IPsec", "IP Addresses (32-bit / 128-bit), Routers", "Logical addressing and packet routing across networks."],
                    ["2. Data Link", "Frame", "Ethernet (802.3), Wi-Fi (802.11), ARP", "MAC Addresses (48-bit), Switches, NICs", "Node-to-node framing, physical addressing, CRC error checking."],
                    ["1. Physical", "Bit", "1000BASE-T, Fiber Optics, DSL", "Voltages, Photons, Cables, Hubs", "Transmission of raw unstructured bit streams over physical medium."]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "tcp-vs-udp",
            "TCP vs UDP: The Complete Transport Layer Matrix",
            table(
                ["Dimension", "TCP (Transmission Control Protocol)", "UDP (User Datagram Protocol)", "Engineering Tradeoff"],
                [
                    ["Connection State", "Connection-Oriented (3-way handshake required)", "Connectionless (Fire-and-forget datagrams)", "Handshake adds 1 RTT connection latency"],
                    ["Reliability Guarantee", "Guaranteed delivery via ACKs, sequence numbers & retransmissions", "Unreliable: packets can be dropped, duplicated, or arrive out of order", "TCP retransmissions add head-of-line blocking latency"],
                    ["Ordering", "Strict in-order byte stream delivery", "No ordering guarantee", "TCP buffer holds subsequent packets until lost packet arrives"],
                    ["Header Overhead", "20 - 60 Bytes (Includes flags, seq, ack, window, options)", "Strictly 8 Bytes (Source port, dest port, length, checksum)", "UDP headers consume 60% less packet byte overhead"],
                    ["Flow & Congestion Control", "Yes: Sliding window (flow) + AIMD / CUBIC / BBR (congestion)", "None: sends at application line speed", "UDP can overwhelm network queues if unthrottled"],
                    ["Primary Use Cases", "Web (HTTP/1.1, HTTP/2), File transfer, SSH, Financial transactions", "DNS, Video streaming (RTP), Gaming, VoIP, QUIC (HTTP/3)", "Use UDP when low latency is preferred over packet completeness"]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "sliding-window-matrix",
            "Sliding Window Flow Control: Stop-and-Wait vs GBN vs Selective Repeat",
            table(
                ["Protocol", "Sender Window ($W_s$)", "Receiver Window ($W_r$)", "Sequence Numbers Required", "Handling of Lost Frame"],
                [
                    ["Stop-and-Wait", "1", "1", r"$N \ge 2$", "Retransmits single frame upon timer expiry. Extremely low efficiency!"],
                    ["Go-Back-N (GBN)", r"$N \le 2^k - 1$", "1", r"$N \le 2^k - 1$", "Receiver discards all subsequent out-of-order frames. Sender retransmits entire window from lost frame!"],
                    ["Selective Repeat (SR)", r"$N \le 2^{k-1}$", r"$N = W_s \le 2^{k-1}$", r"$W_s + W_r \le 2^k$", "Receiver buffers out-of-order frames. Sender retransmits ONLY the specific lost frame!"]
                ]
            ),
            depth="sprint"
        )
    )

    # Section 2: Visual Handshake & URL Lifecycle
    handshake_html = (
        subsection(
            "handshake-architecture",
            "TCP 3-Way Handshake, 4-Way Teardown & TIME_WAIT (2×MSL)",
            svg_card("TCP Handshake & Teardown Protocol State Machine", svg_handshake)
            + callout(
                "Why Does TCP TIME_WAIT Last for 2×MSL (Maximum Segment Lifetime)?",
                "MSL is the maximum time a packet can wander in an IP network before being dropped by routers (default 60s, so 2×MSL = 2 minutes or 60s in Linux).\n"
                "1. **Acknowledge Final ACK Delivery**: Host A sends the final ACK (Step 4). If that ACK is dropped in the network, Host B will retransmit its FIN. If Host A did not linger in `TIME_WAIT`, it would respond with an RST error, causing Host B to think the connection crashed abnormally instead of clean close!\n"
                "2. **Prevent Stale Packet Contamination**: Ensures old duplicate packets lingering in network routers from this connection expire before a new socket is opened with the same IP and Port tuple.",
                "tip"
            )
            + callout(
                "HFT Low-Latency Callout: Nagle's Algorithm vs Delayed ACKs",
                "• **Nagle's Algorithm** (`RFC 896`): Delays sending small TCP packets until previous packets are ACKed to avoid bandwidth waste on tiny headers.\n"
                "• **Delayed ACK**: Receiver waits up to 200ms before sending an ACK to piggyback on outgoing data.\n"
                "• **The Deadlock**: Nagle waits for an ACK; the receiver waits for data to piggyback the ACK! Result: 200ms latency cliff on every RPC!\n"
                "• **Fix**: Disable Nagle immediately in low-latency systems via `setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &opt, sizeof(opt))`.",
                "important"
            ),
            depth="deep"
        )
        + subsection(
            "url-request-lifecycle",
            "The Complete URL Lifecycle: What Happens When You Type google.com",
            svg_card("DNS Hierarchical Resolution Chain", svg_dns)
            + callout(
                "The 8-Phase End-to-End Interview Narrative",
                "1. **Browser Cache & OS Resolution**: Checks Browser DNS cache → OS hosts file & cache → Local DNS resolver.\n"
                "2. **Recursive DNS Resolution**: Recursive resolver queries Root (.) → TLD (.com) → Authoritative nameserver to obtain IP A/AAAA record.\n"
                "3. **ARP (Address Resolution Protocol)**: If target IP is local or gateway router IP is needed, OS broadcasts ARP request to resolve MAC address.\n"
                "4. **TCP 3-Way Handshake**: Client sends SYN → Server responds SYN-ACK → Client responds ACK. Connection established in 1 RTT.\n"
                "5. **TLS 1.3 Cryptographic Handshake**: ClientHello (with supported ciphers & KeyShare) → ServerHello (KeyShare, Cert, Finished) → 1 RTT secure channel (or 0-RTT on session resumption).\n"
                "6. **HTTP/2 Request**: Client sends binary multiplexed HTTP frame (`GET / HTTP/2`).\n"
                "7. **Server Processing**: Reverse proxy (Nginx) → Gateway → Load Balancer → App service executes business logic and returns HTTP 200 with HTML body.\n"
                "8. **DOM / CSSOM & Rendering**: Browser parses HTML to DOM, CSS to CSSOM, computes Render Tree, executes Layout/Reflow, paints pixels to GPU.",
                "tip"
            ),
            depth="deep"
        )
    )

    # Section 3: Sliding Windows & Routing
    routing_html = (
        subsection(
            "routing-algorithms",
            "Routing Algorithms: Distance-Vector vs Link-State",
            table(
                ["Feature", "Distance-Vector Routing (RIP)", "Link-State Routing (OSPF)", "Path-Vector (BGP)"],
                [
                    ["Algorithm Used", "Bellman-Ford algorithm", "Dijkstra's Shortest Path First (SPF)", "Policy-based path vector"],
                    ["Information Shared", "Shares entire routing table with immediate neighbors only", "Floods link states of immediate interfaces to entire network", "Exchanges AS paths with BGP peers"],
                    ["Convergence Speed", "Slow: prone to routing loops & Count-to-Infinity problem", "Fast: routers build complete network topology graph", "Moderate: driven by inter-AS policy rules"],
                    ["Mitigations", "Split Horizon, Poison Reverse, Hold-down timers", "Hierarchical Areas (Area 0 Backbone), Link State Advertisements (LSAs)", "BGP AS-Path loop detection (rejects route if own AS is in path)"]
                ]
            ),
            depth="deep"
        )
        + subsection(
            "socket-io-c10k",
            "Socket I/O Models: select vs poll vs epoll (C10K Scalability)",
            table(
                ["System Call", "Time Complexity", "Max File Descriptors", "Mechanism & Bottleneck"],
                [
                    ["`select()`", "O(N) linear scan", "Fixed: 1024 (`FD_SETSIZE`)", "User passes bitmasks to kernel; kernel scans all FDs; user must scan all 1024 FDs to find active sockets. Inefficient."],
                    ["`poll()`", "O(N) linear scan", "Unlimited (array of `pollfd`)", "Removes 1024 FD limit, but still requires kernel and user to iterate through the entire array on every event."],
                    ["`epoll()` (Linux)", "O(1) event-driven", "Unlimited (bounded by RAM)", "Uses in-kernel Red-Black Tree to track monitored FDs and a Ready List. Only returns active FDs! Solves the C10K problem."]
                ]
            ),
            depth="deep"
        )
    )

    # Section 4: Worked Numericals
    worked_html = (
        subsection(
            "worked-bdp",
            "Worked Numerical 1: Bandwidth-Delay Product (BDP) & Window Sizing",
            formula_box(
                r"\text{BDP} = \text{Bandwidth (bits/sec)} \times \text{RTT (sec)}",
                "Bandwidth Delay Product represents the volume of unacknowledged data in flight required to fill the network pipe",
                [
                    (r"\text{Bandwidth}", "Bottleneck transmission rate of the link in bits per second."),
                    (r"\text{RTT}", "Round Trip Time in seconds."),
                    (r"\text{Window Size}", "TCP Receive Window buffer must equal or exceed BDP to prevent sender stalling.")
                ],
                "Standard 16-bit TCP header window is capped at 65,535 bytes (64KB). On high-bandwidth links, TCP Window Scaling option (RFC 1323) is mandatory to fill the pipe!"
            )
            + worked_example(
                title="Calculate BDP for a 1 Gbps Trans-Atlantic Fiber Link with 80 ms RTT",
                steps=[
                    ("Convert Units", "Bandwidth = $1\\text{ Gbps} = 10^9\\text{ bits/sec}$. RTT = $80\\text{ ms} = 0.08\\text{ sec}$."),
                    ("Calculate BDP in Bits", r"$$\text{BDP} = 10^9 \times 0.08 = 80,000,000\text{ bits}$$"),
                    ("Convert to Bytes", r"$$\text{BDP} = \frac{80,000,000}{8} = 10,000,000\text{ bytes} \approx 10\text{ MB}$$"),
                    ("Determine Window Scaling", "A standard 64KB TCP window can only achieve throughput of $64\\text{KB} / 80\\text{ms} = 6.4\\text{ Mbps}$ (less than 1% of the 1Gbps pipe!). The TCP Window Scale factor must be at least $\\ge 8$ ($2^8 = 256$) to support a 10MB window.")
                ],
                answer="BDP is 10 MB. Without TCP Window Scaling, a 1 Gbps link operates at less than 1% capacity due to sender stalling."
            ),
            depth="deep"
        )
        + subsection(
            "worked-vlsm",
            "Worked Numerical 2: VLSM Subnetting for 3 Unequal Departments",
            worked_example(
                title="Subnet 192.168.1.0/24 into 3 Subnets for Sales (100 hosts), Dev (50 hosts), HR (25 hosts)",
                steps=[
                    ("Sort Subnets by Size (Largest First)", "Sales needs 100 hosts, Dev needs 50 hosts, HR needs 25 hosts."),
                    ("Subnet 1: Sales (100 Hosts)", "Need $2^h - 2 \\ge 100 \\implies h = 7$ bits ($2^7 - 2 = 126$ usable hosts). Subnet mask: $32 - 7 = /25$ (255.255.255.128). Network: 192.168.1.0/25. Host range: 192.168.1.1 to 192.168.1.126. Broadcast: 192.168.1.127."),
                    ("Subnet 2: Dev (50 Hosts)", "Need $2^h - 2 \\ge 50 \\implies h = 6$ bits ($2^6 - 2 = 62$ usable hosts). Subnet mask: $32 - 6 = /26$ (255.255.255.192). Network: 192.168.1.128/26. Host range: 192.168.1.129 to 192.168.1.190. Broadcast: 192.168.1.191."),
                    ("Subnet 3: HR (25 Hosts)", "Need $2^h - 2 \\ge 25 \\implies h = 5$ bits ($2^5 - 2 = 30$ usable hosts). Subnet mask: $32 - 5 = /27$ (255.255.255.224). Network: 192.168.1.192/27. Host range: 192.168.1.193 to 192.168.1.222. Broadcast: 192.168.1.223.")
                ],
                answer="Successfully partitioned without address overlap: Sales (/25), Dev (/26), and HR (/27), preserving remaining space from 192.168.1.224 for future growth."
            ),
            depth="deep"
        )
    )

    # Section 5: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield Computer Networks Interview Flashcards",
        flashcard(
            "Why is TCP 3-Way Handshake necessary instead of a 2-Way Handshake?",
            "Both client and server must agree on each other's Initial Sequence Numbers (ISNs) to establish bidirectional reliable communication. In a 2-way handshake, if an old delayed SYN packet wanders through the network and arrives at the server after the original connection terminated, the server would send SYN-ACK and immediately allocate resources believing a new connection opened! Host A never sent that SYN, so it ignores the ACK. The server is left holding a half-open ghost connection that wastes memory.",
            "P1 Network Systems"
        )
        + flashcard(
            "How does HTTP/3 with QUIC solve Head-of-Line (HoL) Blocking compared to HTTP/2?",
            "HTTP/2 multiplexes multiple application requests as virtual streams over a SINGLE underlying TCP connection. If a single TCP packet containing Stream 1 data is dropped, the TCP stack buffers all subsequent packets in the OS socket buffer until the dropped packet is retransmitted and acknowledged. Consequently, Streams 2, 3, and 4 are blocked, even though none of their packets were dropped! HTTP/3 runs over QUIC (UDP), implementing stream multiplexing at the transport layer directly: dropping a packet for Stream 1 has ZERO impact on Streams 2, 3, and 4.",
            "P1 Modern Web / Systems"
        )
        + flashcard(
            "Why does Ethernet enforce a 64-Byte Minimum Frame Size?",
            "In classic Ethernet using CSMA/CD, a sender must continue transmitting data long enough to detect a collision from the furthest possible station on the cable before finishing its transmission ($T_{\\text{tx}} \\ge 2 \\times T_{\\text{prop}}$). At 10 Mbps over a maximum cable length of 2500m (with repeaters), round-trip propagation delay is ~51.2 µs. In 51.2 µs, a 10 Mbps transceiver outputs $51.2 \\times 10 = 512\\text{ bits} = 64\\text{ bytes}$. If a frame was smaller than 64 bytes, transmission would finish before the collision signal returned, causing undetected corrupted frames!",
            "P1 Hardware / Systems"
        )
        + flashcard(
            "What is the difference between ARP and RARP?",
            "ARP (Address Resolution Protocol) resolves a known Layer 3 logical IP address to a physical Layer 2 MAC address using broadcast requests and unicast replies. RARP (Reverse ARP) allows a diskless workstation to query a server to find its own IP address given its known hardware MAC address upon boot (superseded by BOOTP and DHCP).",
            "P1 Campus Classic"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Minute Sprint: OSI, TCP vs UDP & Congestion", sprint_html)
        + section("tcp-handshake-svg", "📊 TCP 3-Way Handshake & 4-Way Teardown", handshake_html)
        + section("sliding-window-routing", "📦 Sliding Window Protocols & Routing Algorithms", routing_html)
        + section("worked-cn-math", "📐 Worked Numericals: BDP, VLSM & Ethernet Framing", worked_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
