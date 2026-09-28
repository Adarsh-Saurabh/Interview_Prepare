# 00: Nokia Optical Networks Company & Role Intelligence

## 1. Executive Summary & Company Profile
* **Company**: **Nokia Corporation** (Headquartered in Espoo, Finland; global B2B networking and telecommunications innovation leader).
* **Business Unit**: **Network Infrastructure (NI) — Optical Networks**.
* **Global Standing**: Global top-tier market leader in optical transport, high-capacity long-haul, subsea networks, and data center interconnects (DCI).
* **Major Engineering Center**: **Bangalore R&D Hub (Manyata Embassy Business Park)** — core site for optical hardware-software co-design, control plane engineering, high-performance C++ firmware, and AI-driven automation pipelines.
* **The "AI Super Cycle" Driver**: Explosive growth in AI compute clusters (e.g., thousands of GPUs interconnected in AI factories) requires immense data transmission bandwidth. Nokia Optical builds the ultra-high capacity, low-latency coherent optical engines (800G, 1.2T, and 1.6T per wavelength) that feed modern AI data infrastructure.

---

## 2. Core Architecture & Optical Engineering Foundation

Nokia Optical Networks builds solutions that span physical photonics, coherent digital signal processing, embedded control, and cloud-native software:

```
[Cloud Data Centers / AI GPU Clusters]
      │ High-speed Ethernet (400G / 800G Client Interfaces)
      ▼
[Nokia 1830 Photonic Service Switch (PSS) / Optical Transponder]
      │
      ├── Client Optics (QSFP-DD / OSFP Transceivers)
      ├── Embedded Linux Control Plane (C++ / Python / Netconf / YANG)
      │      └── Real-time Telemetry, Protection Switching (<50ms), Fault Recovery
      ├── FPGA / ASIC Hardware Layer (High-speed packet framing, OTN ITU-T G.709)
      ▼
[Nokia PSE-6s / PSE-V Coherent Digital Signal Processor (DSP)]
      │ (Electronic Dispersion Compensation, Carrier Phase Recovery, QAM Modulation)
      ▼
[Optical Line System (OLS) & ROADM Layer]
      │ (Wavelength Selective Switches - WSS, EDFAs, Raman Amplifiers)
      ▼
[Dense Wavelength Division Multiplexing (DWDM) Fiber Network]
(C-Band + L-Band Fibers transmitting 100+ wavelengths simultaneously over thousands of km)
```

### Signature Nokia Optical Technologies to Know:
1. **Nokia 1830 PSS (Photonic Service Switch)**: The flagship optical transport platform deployed by global telcos, cloud hyperscalers, and enterprise data centers.
2. **Nokia PSE-6s (Photonic Service Engine 6s)**: Industry-leading 5nm coherent optical engine capable of driving 1.2 Terabits per second ($1.2\,	ext{Tbps}$) on a single wavelength over multi-span metro/regional networks, slashing power-per-bit by 40%.
3. **ROADM (Reconfigurable Optical Add-Drop Multiplexer)**: Software-controlled optical switching nodes that dynamically route individual optical wavelengths without expensive optical-to-electrical-to-optical (O-E-O) conversion.
4. **WaveSuite Software**: Nokia's carrier-grade SDN (Software-Defined Networking) automation platform providing intent-based network control, predictive optical maintenance, and automated path routing.

---

## 3. Placement Drive Specification (NIT Rourkela 2027 Batch)

| Parameter | Drive Specification |
| :--- | :--- |
| **Company** | **Nokia** |
| **Target Role** | **Associate Engineer (Optical Networking)** |
| **Work Location** | **Bangalore (Manyata Embassy Business Park)** |
| **Compensation (CTC)** | **M.Tech:** **₹18.00 LPA**<br>**B.Tech:** **₹16.50 LPA** |
| **Monthly Stipend** | **M.Tech:** **₹55,000 / month**<br>**B.Tech:** **₹50,000 / month** |
| **Internship Duration** | 6-Month Internship leading directly into Full-Time Employment (PPO conversion) |
| **Eligible Batches & Courses** | Batch of 2027: B.Tech & M.Tech (CS, EC, EE, EI) |
| **Eligibility Criteria** | **CGPA $\ge 6.5$**, No active backlogs |
| **Evaluation Process** | 1. Resume Shortlisting<br>2. Online Assessment (HackerEarth/AMCAT)<br>3. Technical Interview Rounds (1–2 rounds)<br>4. Assignment (if required) / Managerial HR |

---

## 4. The 4 Technical Pillars Evaluated at Nokia

```
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     1. High-Performance C++ & OOP     │   │    2. Concurrency & Linux OS Internals│
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • C++11/14/17 Modern Idioms & RAII    │   │ • Multithreading, Pthreads, `std::thread`│
│ • Virtual Tables (`vtable`/`vptr`)    │   │ • Mutexes, Semaphores, Lock-Free Queues│
│ • Object Slicing & Memory Layout      │   │ • Race Conditions & Deadlock Prevention│
│ • Smart Pointers & Custom Allocators  │   │ • Socket Programming & Linux epoll     │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
┌───────────────────────────────────────┐   ┌───────────────────────────────────────┐
│     3. Optical Networking & Systems   │   │   4. Modern AI Tools & CI/CD Pipelines│
├───────────────────────────────────────┤   ├───────────────────────────────────────┤
│ • DWDM, Wavelength Routing & ROADM    │   │ • Python Automation & Test Frameworks │
│ • OTN Framing (ITU-T G.709) & FEC     │   │ • AI-Assisted Architecture & Code PoCs│
│ • Fiber Impairments (Loss, CD, PMD)   │   │ • Automated Validation & Unit Testing │
│ • Coherent Detection & Modulation     │   │ • Git, CMake, GDB, Linux Debugging    │
└───────────────────────────────────────┘   └───────────────────────────────────────┘
```
