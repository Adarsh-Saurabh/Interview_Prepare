# mod_docker.py - Docker, Containers, Kubernetes & CI/CD Generator
# Conforms to instruction.md Part 6.12 Specification (P1 Track D)

from components import (
    section, subsection, table, callout, code, svg_card, formula_box,
    worked_example, flashcard, followup_chain, decision_matrix, anti_pattern,
    mnemonic, numbers_card, one_liner, see_also, pills
)

def get_content():
    toc = [
        ("sprint-core", "⚡ 15-Min Sprint: Containers vs VMs, CLI & Linux Primitives"),
        ("container-storage-svg", "📊 Container Architecture & OverlayFS Union Mounts"),
        ("kubernetes-core", "☸️ Kubernetes Architecture, Objects & Control Plane"),
        ("probes-resource-qos", "⚡ Probes, Resource Limits & OOMKill vs CPU Throttling"),
        ("production-manifests", "💻 Production Manifests: Compose & K8s Deployment"),
        ("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses")
    ]

    # SVG 1: VM vs Container
    svg_vm_container = """
    <svg viewBox="0 0 860 300" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <!-- Left: VMs -->
      <rect x="30" y="20" width="380" height="260" rx="10" fill="#0f172a" stroke="#334155" stroke-width="2" />
      <text x="220" y="45" fill="#f43f5e" font-size="14" font-weight="800" text-anchor="middle">Virtual Machines (Hypervisor)</text>

      <rect x="50" y="65" width="160" height="35" rx="4" fill="#881337" />
      <text x="130" y="87" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">App A + Libs</text>

      <rect x="230" y="65" width="160" height="35" rx="4" fill="#881337" />
      <text x="310" y="87" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">App B + Libs</text>

      <rect x="50" y="110" width="160" height="35" rx="4" fill="#991b1b" stroke="#f87171" stroke-width="1" />
      <text x="130" y="132" fill="#fecdd3" font-size="11" font-weight="700" text-anchor="middle">Guest OS (Full Kernel)</text>

      <rect x="230" y="110" width="160" height="35" rx="4" fill="#991b1b" stroke="#f87171" stroke-width="1" />
      <text x="310" y="132" fill="#fecdd3" font-size="11" font-weight="700" text-anchor="middle">Guest OS (Full Kernel)</text>

      <rect x="50" y="155" width="340" height="30" rx="4" fill="#1e293b" stroke="#f43f5e" stroke-width="1" />
      <text x="220" y="175" fill="#f43f5e" font-size="11" font-weight="700" text-anchor="middle">Hypervisor (KVM / ESXi / Type 1 &amp; 2)</text>

      <rect x="50" y="195" width="340" height="30" rx="4" fill="#334155" />
      <text x="220" y="215" fill="#f1f5f9" font-size="11" text-anchor="middle">Host OS &amp; Physical Hardware</text>

      <text x="220" y="255" fill="#94a3b8" font-size="10" text-anchor="middle">Heavy: GBs of disk, minutes to boot, duplicate kernels</text>

      <!-- Right: Containers -->
      <rect x="450" y="20" width="380" height="260" rx="10" fill="#0f172a" stroke="#0284c7" stroke-width="2" />
      <text x="640" y="45" fill="#38bdf8" font-size="14" font-weight="800" text-anchor="middle">Docker Containers (Engine)</text>

      <rect x="470" y="65" width="160" height="40" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="1" />
      <text x="550" y="88" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Container A (App A)</text>

      <rect x="650" y="65" width="160" height="40" rx="4" fill="#0369a1" stroke="#38bdf8" stroke-width="1" />
      <text x="730" y="88" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">Container B (App B)</text>

      <rect x="470" y="115" width="340" height="35" rx="4" fill="#0284c7" />
      <text x="640" y="138" fill="#ffffff" font-size="12" font-weight="800" text-anchor="middle">Docker Engine / containerd (runc)</text>

      <rect x="470" y="160" width="340" height="35" rx="4" fill="#065f46" stroke="#34d399" stroke-width="1.5" />
      <text x="640" y="182" fill="#34d399" font-size="11" font-weight="800" text-anchor="middle">Host Linux Kernel (Namespaces &amp; cgroups)</text>

      <rect x="470" y="205" width="340" height="30" rx="4" fill="#1e293b" />
      <text x="640" y="225" fill="#94a3b8" font-size="10" text-anchor="middle">Physical Hardware (Bare Metal)</text>

      <text x="640" y="255" fill="#34d399" font-size="10" font-weight="600" text-anchor="middle">Lightweight: MBs of image, milliseconds to start, 0 hypervisor overhead</text>
    </svg>
    """

    # SVG 2: OverlayFS Union Mount
    svg_overlayfs = """
    <svg viewBox="0 0 860 260" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ov-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
        </marker>
      </defs>
      <!-- Merged View -->
      <rect x="230" y="20" width="400" height="45" rx="6" fill="#065f46" stroke="#34d399" stroke-width="2" />
      <text x="430" y="47" fill="#34d399" font-size="13" font-weight="800" text-anchor="middle">merged/ (Unified Container Filesystem View)</text>

      <line x1="330" y1="95" x2="330" y2="70" stroke="#f43f5e" stroke-width="2" marker-end="url(#ov-arrow)" />
      <line x1="530" y1="95" x2="530" y2="70" stroke="#38bdf8" stroke-width="2" marker-end="url(#ov-arrow)" />

      <!-- UpperDir -->
      <rect x="100" y="100" width="310" height="50" rx="6" fill="#881337" stroke="#f43f5e" stroke-width="2" />
      <text x="255" y="125" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">upperdir/ (Read-Write Container Layer)</text>
      <text x="255" y="140" fill="#fecdd3" font-size="9" text-anchor="middle">Ephemeral writes, modifications, whiteout files</text>

      <!-- LowerDirs -->
      <rect x="450" y="100" width="310" height="50" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="2" />
      <text x="605" y="125" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">lowerdir/ (Read-Only Image Layers)</text>
      <text x="605" y="140" fill="#bae6fd" font-size="9" text-anchor="middle">Layer 3: App binary | Layer 2: Python | Layer 1: Debian base</text>

      <!-- Copy on Write annotation -->
      <rect x="100" y="170" width="660" height="60" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5" />
      <text x="430" y="195" fill="#fbbf24" font-size="11" font-weight="700" text-anchor="middle">⚡ Copy-on-Write (CoW) Mechanism &amp; File Deletion (Whiteout):</text>
      <text x="430" y="215" fill="#cbd5e1" font-size="10" text-anchor="middle">When modifying a file from lowerdir, OverlayFS copies it to upperdir first. Deleting a lowerdir file creates a 0-byte character device (whiteout file) in upperdir!</text>
    </svg>
    """

    # Section 1: Sprint Core
    sprint_html = (
        pills([("P1 Track D", "blue"), ("DevOps & K8s", "teal"), ("Infrastructure", "indigo"), ("15-Min Sprint", "amber")])
        + callout(
            "Docker, Kubernetes & Infrastructure Ground Rules",
            "Modern technical interviews test operational infrastructure: Linux kernel isolation primitives (cgroups v1/v2, 8 namespaces), OverlayFS storage drivers, multi-stage Docker builds, Kubernetes reconciliation loops, and debugging production pod failures (`CrashLoopBackOff`, `OOMKilled`).",
            "important"
        )
        + numbers_card("Container & Cloud Infrastructure Benchmarks", [
            ("Container Startup Time", "~50 - 200 ms", "Forking runc process sharing existing kernel"),
            ("VM Startup Time", "~30 - 120 seconds", "Full BIOS, hypervisor boot, kernel initialization"),
            ("Alpine Base Image", "~5 MB", "Minimal musl-based container image"),
            ("Ubuntu Base Image", "~75 MB", "Standard glibc-based container image"),
            ("Docker OverlayFS CoW Delay", "~1 - 5 ms", "First-write latency when copying file from lowerdir to upperdir"),
            ("Kubernetes Default Sync Loop", "10 seconds", "Kubelet node heartbeat and reconciliation frequency")
        ])
        + subsection(
            "docker-cli-mastery",
            "16 Essential Docker CLI Commands for Production",
            table(
                ["Command", "Syntax Example", "Production Behavior & Flag Nuance"],
                [
                    ["`docker run`", "`docker run -d --rm -p 8080:80 --name web nginx`", "Runs container in background (`-d`), auto-deletes on exit (`--rm`), maps port (`-p`)."],
                    ["`docker ps`", "`docker ps -a --filter status=exited`", "Lists active containers; `-a` includes stopped/crashed containers."],
                    ["`docker exec`", "`docker exec -it <id> sh`", "Executes interactive process inside running container namespace."],
                    ["`docker logs`", "`docker logs -f --tail 100 <id>`", "Follows stdout/stderr stream with tail limit."],
                    ["`docker build`", "`docker build -t app:v1 -f Dockerfile .`", "Builds container image from context directory."],
                    ["`docker inspect`", "`docker inspect --format '{{.NetworkSettings.IPAddress}}' <id>`", "Extracts detailed JSON configuration and runtime state."],
                    ["`docker stats`", "`docker stats --no-stream`", "Real-time streaming CPU, memory, and I/O consumption."],
                    ["`docker cp`", "`docker cp <id>:/app/logs ./host_logs`", "Copies files bidirectionally between container and host."],
                    ["`docker stop / kill`", "`docker stop -t 10 <id>` / `docker kill <id>`", "`stop` sends SIGTERM with timeout before SIGKILL. `kill` sends SIGKILL immediately."],
                    ["`docker rm / rmi`", "`docker rm -f <id>` / `docker rmi <img_id>`", "Removes stopped container / deletes image from local storage."],
                    ["`docker prune`", "`docker system prune -af --volumes`", "Wipes all unused containers, networks, dangling images, and volumes."],
                    ["`docker volume`", "`docker volume create pg_data`", "Manages persistent storage independent of container lifecycle."],
                    ["`docker network`", "`docker network create --driver bridge my_net`", "Creates isolated virtual Ethernet bridge network."]
                ]
            ),
            depth="sprint"
        )
        + subsection(
            "linux-primitives",
            "Linux Kernel Isolation: Namespaces vs cgroups",
            table(
                ["Kernel Primitive", "Namespace / Subsystem", "What It Isolates & Controls"],
                [
                    ["PID Namespace", "`CLONE_NEWPID`", "Process IDs: container sees itself as PID 1; isolated from host process table."],
                    ["NET Namespace", "`CLONE_NEWNET`", "Network stack: dedicated virtual interfaces (`veth`), routing table, port bindings."],
                    ["MNT Namespace", "`CLONE_NEWNS`", "Mount points: container has isolated root filesystem (`/`) via `chroot`/`pivot_root`."],
                    ["IPC Namespace", "`CLONE_NEWIPC`", "System V IPC and POSIX message queues, semaphores, shared memory."],
                    ["UTS Namespace", "`CLONE_NEWUTS`", "Hostname and NIS domain name isolation."],
                    ["USER Namespace", "`CLONE_NEWUSER`", "UID / GID mapping: root inside container maps to non-root UID 10001 on host!"],
                    ["cgroups (v1 / v2)", "`cpu`, `memory`, `pids`, `io`", "Resource accounting and limits: enforces hard CPU quotas and memory boundaries."]
                ]
            ),
            depth="sprint"
        )
    )

    # Section 2: Storage & Union Mounts
    storage_html = (
        subsection(
            "overlayfs-storage",
            "OverlayFS Union Mount Architecture",
            svg_card("OverlayFS Architecture: Merged, UpperDir, and LowerDir Layers", svg_overlayfs)
            + callout(
                "Why Deleting a File Does NOT Shrink a Docker Image",
                "Docker images are immutable stacks of read-only layers.\n"
                "• When a subsequent `RUN rm -rf /tmp/large_file.tar.gz` instruction executes, it cannot modify or delete the file from the preceding layer!\n"
                "• Instead, OverlayFS writes a **Whiteout character device** in the new layer that masks the file in the merged view.\n"
                "• Result: The file is hidden, but the image size STILL includes the full size of the file in the lower layer! Always download, extract, and clean up in a **SINGLE RUN instruction**.",
                "important"
            ),
            depth="deep"
        )
    )

    # Section 3: Kubernetes Architecture
    k8s_html = (
        subsection(
            "k8s-objects",
            "Kubernetes Core Objects & Control Plane",
            table(
                ["Kubernetes Object", "Primary Responsibility", "When to Use"],
                [
                    ["Pod", "Smallest deployable unit; collocated set of 1+ containers sharing localhost & network namespace", "Atomic container deployment unit"],
                    ["ReplicaSet", "Maintains exact specified number of running Pod replicas via reconciliation loop", "Managed automatically by Deployments"],
                    ["Deployment", "Declarative updates for stateless applications; manages rolling updates and rollbacks", "Standard stateless microservices"],
                    ["StatefulSet", "Manages stateful apps with stable network identities (`pod-0, pod-1`) and persistent storage", "Databases, Kafka brokers, Redis clusters"],
                    ["DaemonSet", "Ensures all (or subset of) worker nodes run a single copy of a Pod", "Log forwarders (Fluentd), node monitoring (Prometheus node-exporter)"],
                    ["Service (ClusterIP)", "Stable virtual IP and DNS name load balancing across Pods matching label selector", "Internal service-to-service communication"],
                    ["Service (NodePort)", "Exposes service on each node's static port (30000-32767)", "Direct external debugging without load balancer"],
                    ["Service (LoadBalancer)", "Provisions cloud provider external load balancer (AWS ALB, GCP NLB)", "Public internet-facing services"],
                    ["Ingress", "HTTP/HTTPS Layer 7 reverse proxy routing paths/domains to Services", "Production API gateways and TLS termination"],
                    ["ConfigMap / Secret", "Separates non-confidential configuration (ConfigMap) and base64 credentials (Secret)", "Environment variables and volume mounts"]
                ]
            )
            + callout(
                "The Kubernetes Reconciliation Loop: Desired vs Current State",
                "The core mental model of Kubernetes is an infinite control loop:\n"
                "$$\\text{Reconciliation Loop}: \\text{Observe Current State} \\longrightarrow \\text{Compare with Desired State in etcd} \\longrightarrow \\text{Take Action to Converge}$$\n"
                "The Controller Manager continuously monitors etcd. If a node crashes, the Deployment controller detects `current replicas (2) < desired replicas (3)` and instructs the kube-scheduler to bind a new Pod to a healthy node.",
                "tip"
            ),
            depth="deep"
        )
    )

    # Section 4: Probes & QoS Classes
    probes_html = (
        subsection(
            "probes-qos",
            "Container Health Probes & Resource Limits",
            table(
                ["Probe Type", "Failure Behavior", "Production Role"],
                [
                    ["Startup Probe", "Kubelet kills container and restarts it according to restartPolicy", "Protects slow-starting legacy apps from being killed by liveness probe"],
                    ["Liveness Probe", "Kubelet kills container and restarts it", "Detects deadlocks and unrecoverable app freezes"],
                    ["Readiness Probe", "Removes Pod IP from Service Endpoints (Zero traffic sent; does NOT kill pod!)", "Ensures traffic is only routed when warm and ready to serve"]
                ]
            )
            + callout(
                "Memory Limit vs CPU Limit: OOMKilled vs CPU Throttling",
                "• **Memory Limit Exceeded**: Memory is a non-compressible resource. When a container exceeds its `limits.memory`, the Linux kernel OOM Killer immediately kills the process (`Exit Code 137: OOMKilled`)!\n"
                "• **CPU Limit Exceeded**: CPU is a compressible resource. When a container exceeds its `limits.cpu`, the kernel CFS scheduler throttles the process's CPU time slices. The process slows down, but is NEVER terminated!",
                "important"
            ),
            depth="deep"
        )
    )

    # Section 5: Production Manifests
    manifests_html = (
        subsection(
            "production-manifests",
            "Production Kubernetes Deployment & Service Manifest",
            code(r"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  labels:
    app: order-service
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Max pods created above desired count during update
      maxUnavailable: 0  # Zero downtime: never drop below 3 active pods!
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
    spec:
      containers:
      - name: api
        image: myregistry.io/order-service:v1.2.4@sha256:7b4f... # Pinned digest!
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: "250m"      # 0.25 CPU cores guaranteed
            memory: "256Mi"
          limits:
            cpu: "500m"      # Throttled at 0.5 CPU cores
            memory: "512Mi"  # OOMKilled if exceeds 512Mi
        readinessProbe:
          httpGet:
            path: /health/ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /health/live
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 20
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
spec:
  type: ClusterIP
  selector:
    app: order-service
  ports:
  - port: 80
    targetPort: 8080""", "yaml", "production_k8s_deployment.yaml"),
            depth="deep"
        )
    )

    # Section 6: Top Flashcards
    flashcards_html = subsection(
        "interview-flashcards",
        "🎯 High-Yield DevOps & Container Flashcards",
        flashcard(
            "Your Pod is stuck in 'CrashLoopBackOff'. Walk me through how you debug it.",
            "1. Run `kubectl describe pod <pod-name>` to check Events (inspect for image pull errors, failed readiness probes, or OOMKilled exit code 137).\n2. Check application logs via `kubectl logs <pod-name> --previous` to see why the prior container crashed.\n3. Check resource constraints: verify if the container breached memory limits.\n4. If the container exits with Code 0 immediately, verify that its `CMD`/`ENTRYPOINT` runs a long-running foreground process rather than exiting immediately.",
            "P1 DevOps / SRE"
        )
        + flashcard(
            "What is the difference between CMD and ENTRYPOINT in a Dockerfile?",
            "`ENTRYPOINT` defines the default executable binary that always runs when the container starts. `CMD` provides default arguments passed to the `ENTRYPOINT`. If both are provided, `CMD` arguments are appended to `ENTRYPOINT`. At runtime (`docker run my_image foo bar`), CLI arguments override `CMD` completely, but do NOT override `ENTRYPOINT` (unless `--entrypoint` is explicitly specified).",
            "P1 Docker Semantics"
        )
        + flashcard(
            "Why should you never pass production secrets via '--build-arg'?",
            "Any value passed via `--build-arg` is permanently recorded in the image's metadata and layer history (`docker history <image>`), allowing anyone with read access to the image to extract the plaintext secret! Solution: Use Docker BuildKit Secret Mounts: `RUN --mount=type=secret,id=mysecret cat /run/secrets/mysecret`, which exposes the secret ephemerally in RAM during build without baking it into any image layer.",
            "P1 Security / DevSecOps"
        )
        + flashcard(
            "What is the difference between a Volume and a Bind Mount?",
            "A Volume is managed entirely by the Docker daemon in host storage (`/var/lib/docker/volumes/`). It is isolated from the host filesystem core, safe from non-Docker host processes, and portable across OS platforms. A Bind Mount directly maps an arbitrary directory on the host machine (`/home/user/app`) into the container, exposing the container to host filesystem permissions and dependencies.",
            "P1 Storage Architecture"
        ),
        depth="deep"
    )

    content = (
        section("sprint-core", "⚡ 15-Min Sprint: Containers vs VMs, CLI & Linux Primitives", sprint_html)
        + section("container-storage-svg", "📊 Container Architecture & OverlayFS Union Mounts", storage_html)
        + section("kubernetes-core", "☸️ Kubernetes Architecture, Objects & Control Plane", k8s_html)
        + section("probes-resource-qos", "⚡ Probes, Resource Limits & OOMKill vs CPU Throttling", probes_html)
        + section("production-manifests", "💻 Production Manifests: Compose & K8s Deployment", manifests_html)
        + section("interview-flashcards", "🎯 Top Tech Interview Flashcards & Defenses", flashcards_html)
    )

    return {"toc": toc, "content": content}
