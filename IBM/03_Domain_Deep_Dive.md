# IBM Systems Hardware, Firmware & Virtualization Deep Dive

> **Core Focus:** IBM POWER10, z16 Telum Processor, OpenBMC, PowerVM, and Endianness  
> **Target Mastery:** Demonstrating deep, native understanding of IBM's proprietary architecture  

---

## 1. IBM Telum Processor (IBM z16) & Virtual Cache Hierarchy

The **IBM Telum** processor, powering the IBM z16 and LinuxONE systems, represents a radical departure from traditional multi-core CPU cache architectures:

```
+-------------------------------------------------------------------------------+
|                      IBM Telum 8-Core Chip Microarchitecture                  |
+-------------------------------------------------------------------------------+
| [Core 0]  [Core 1]  [Core 2]  [Core 3]  [Core 4]  [Core 5]  [Core 6]  [Core 7] |
| 128K I/D  128K I/D  128K I/D  128K I/D  128K I/D  128K I/D  128K I/D  128K I/D  |
|  32MB L2   32MB L2   32MB L2   32MB L2   32MB L2   32MB L2   32MB L2   32MB L2  |
|                                                                               |
| <== Bi-directional 320 GB/s Dual-Ring Interconnect Fabric ==================> |
|                                                                               |
|     * Virtual L3 Cache: 256 MB (Formed by aggregated L2 caches on-chip)      |
|     * Virtual L4 Cache: 2 GB (Formed across all 4 chips in a compute drawer)  |
|                                                                               |
|       +-------------------------------------------------------------+         |
|       |     Integrated Memory-Coherent On-Chip AI Accelerator       |         |
|       |     (Neural Network Processing Assist - NNPA Instruction)   |         |
|       +-------------------------------------------------------------+         |
+-------------------------------------------------------------------------------+
```

### Key Architectural Breakthroughs:
1. **Virtual L3 Cache (256 MB):**
   - Telum eliminated discrete physical L3 cache silicon to save die area.
   - Each core has a private **32 MB L2 cache**. When a core experiences an L2 miss, it snoops the L2 caches of the other 7 cores via the high-speed ring interconnect.
   - The aggregated 8 $\times$ 32 MB = **256 MB Virtual L3** is dynamically shared with $<12\text{ns}$ latency.
2. **Virtual L4 Cache (2 GB):**
   - Across a 4-chip compute drawer, unused L2 cache lines form a shared **2 GB Virtual L4 cache**.
3. **On-Chip Integrated AI Accelerator (NNPA):**
   - Directly attached to the chip's internal interconnect, sharing the same memory-coherent address space as the cores.
   - Hardware implementation of matrix multiplication, convolution, activation functions (ReLU, GELU), and LSTM/Transformer attention heads.
   - Executes the **NNPA (Neural Network Processing Assist)** assembly instruction directly in the banking transaction pipeline, evaluating fraud risk in $<1\text{ms}$ with zero off-chip PCIe latency.

---

## 2. IBM POWER10 Architecture & Memory Inception

The **IBM POWER10** processor (7nm EUV) is designed specifically for enterprise hybrid cloud and mission-critical SAP HANA / AI workloads:

- **SMT8 Concurrency:** Each core supports up to **8 simultaneous hardware threads** (SMT8), yielding up to 240 threads per socket.
- **Matrix Math Accelerator (MMA):** 4 MMA units per core execute $4\times$ the matrix operations per cycle compared to POWER9, delivering hardware-accelerated tensor arithmetic for enterprise models.
- **Open Memory Interface (OMI):** Low-latency serial memory interface delivering **1 TB/s memory bandwidth** per socket.
- **Memory Inception:** Using optical PCIe Gen 5 cables, POWER10 servers share memory across nodes in a cluster without CPU or OS intervention, creating memory fabrics up to **2 Petabytes** in size.

---

## 3. OpenBMC Firmware Architecture

IBM is a founding member of **OpenBMC** (under the Linux Foundation), replacing legacy proprietary server BMC firmware with a standardized open-source Linux stack:

```
+------------------------------------------------------------------------------------+
|                         OpenBMC Software Architecture                              |
+------------------------------------------------------------------------------------+
|  Northbound Interface: Redfish REST API (HTTPS / JSON), IPMI over LAN, Web UI      |
+------------------------------------------------------------------------------------+
|  System Management Bus (D-Bus): High-speed IPC message bus (/xyz/openbmc_project)  |
|    - Object paths:  /xyz/openbmc_project/sensors/temperature/cpu0                 |
|    - Interfaces:    xyz.openbmc_project.Sensor.Value                               |
|    - Properties:    Value, Unit, Scale                                             |
+------------------------------------------------------------------------------------+
|  Daemons (systemd):                                                                |
|    - phosphor-hwmon (Reads /sys/class/hwmon from Linux kernel)                     |
|    - phosphor-fan-presence & fan-control (Closed-loop PID fan speed algorithm)     |
|    - phosphor-power-control (Chassis power sequencing, power-on reset)             |
+------------------------------------------------------------------------------------+
|  Linux Kernel & Drivers: I2C, SMBus, SPI (Host SPI flash), eSPI, GPIO, UART       |
+------------------------------------------------------------------------------------+
```

### How to Monitor an IBM Server via Redfish REST API:
```bash
# Querying CPU temperature and power status via Redfish API
curl -k -u root:0penBmc https://bmc-host/redfish/v1/Chassis/chassis/Thermal
```

---

## 4. Endianness & Cross-Architecture Serialization

A critical systems interview question at IBM ISDL revolves around **Endianness**:
- **x86_64:** Little-Endian (Least significant byte stored at lowest address).
- **ppc64le (IBM Power):** Little-Endian (modern Linux on Power runs in LE mode).
- **s390x (IBM Z / LinuxONE):** **Big-Endian** (Most significant byte stored at lowest address).

### Why Big-Endian Matters for ISDL Software Engineers:
When serializing network packets or transferring binary records between IBM Z (`s390x`) and cloud servers (`x86_64`), failing to perform byte-order conversion causes silent data corruption:

```cpp
#include <iostream>
#include <cstdint>

// Converting 32-bit integer between Big-Endian and Little-Endian
uint32_t swapEndian32(uint32_t val) {
    return ((val >> 24) & 0x000000FF) |
           ((val >> 8)  & 0x0000FF00) |
           ((val << 8)  & 0x00FF0000) |
           ((val << 24) & 0xFF000000);
}

// In C++23: std::byteswap(val);
// In POSIX: htonl(val) / ntohl(val);
```
