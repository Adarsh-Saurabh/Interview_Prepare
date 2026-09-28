# 07: Optical Networks & Systems Engineering Quick Reference

## 1. Optical Network Equations & Formulas

| Metric | Formula / Relationship | Practical Meaning |
| :--- | :--- | :--- |
| **Decibel (dB)** | $	ext{Loss/Gain (dB)} = 10 \log_{10}\left(rac{P_{	ext{out}}}{P_{	ext{in}}}ight)$ | $3\,	ext{dB} pprox$ half/double power; $10\,	ext{dB} = 10	imes$; $20\,	ext{dB} = 100	imes$. |
| **Power in dBm** | $P_{	ext{dBm}} = 10 \log_{10}\left(rac{P_{	ext{mW}}}{1\,	ext{mW}}ight)$ | $0\,	ext{dBm} = 1.0\,	ext{mW}$; $-10\,	ext{dBm} = 0.1\,	ext{mW}$; $+20\,	ext{dBm} = 100\,	ext{mW}$. |
| **Fiber Link Budget** | $P_{	ext{Rx}} = P_{	ext{Tx}} - (lpha \cdot L + N_{	ext{splice}} \cdot L_{	ext{splice}} + M)$ | Ensures received optical power is above transceiver sensitivity. |
| **Shannon-Hartley Capacity** | $C = B \log_2(1 + 	ext{SNR})$ | Maximum theoretical error-free data rate over noisy channel. |
| **Chromatic Dispersion Delay** | $\Delta 	au = D \cdot L \cdot \Delta \lambda$ | Pulse spreading ($D pprox 17\,	ext{ps/(nm}\cdot	ext{km)}$ for SMF-28 at $1550\,	ext{nm}$). |

---

## 2. Essential Optical Acronyms

* **DWDM**: Dense Wavelength Division Multiplexing
* **ROADM**: Reconfigurable Optical Add-Drop Multiplexer
* **WSS**: Wavelength Selective Switch
* **OTN**: Optical Transport Network (ITU-T G.709)
* **FEC**: Forward Error Correction (Reed-Solomon, LDPC)
* **BER**: Bit Error Rate (Pre-FEC and Post-FEC)
* **OSNR**: Optical Signal-to-Noise Ratio
* **EDFA**: Erbium-Doped Fiber Amplifier
* **QAM**: Quadrature Amplitude Modulation
* **LO**: Local Oscillator Laser

---

## 3. C++ Modern Systems CheatSheet

```cpp
// RAII Lock Guard
std::lock_guard<std::mutex> lock(mtx);

// Scoped Multi-Lock (Deadlock-Free)
std::scoped_lock lock(mtx1, mtx2);

// Unique Pointer with Custom Deleter
std::unique_ptr<int, void(*)(int*)> ptr(new int(10), [](int* p){ delete p; });

// Hardware Memory Alignment (False Sharing Prevention)
struct alignas(64) PerCoreCounter {
    std::atomic<uint64_t> counter{0};
};

// Check if move constructor is noexcept
static_assert(std::is_nothrow_move_constructible<MyClass>::value, "Must be noexcept");
```

---

## 4. Linux CLI Diagnostics CheatSheet

```bash
# GDB Basics
gdb ./app
(gdb) break main
(gdb) run
(gdb) backtrace full
(gdb) info threads
(gdb) thread apply all bt

# Memory Leaks
valgrind --leak-check=full ./app

# Network Interface & Sockets
netstat -tulpn          # List listening ports
ethtool eth0            # Physical link speed & duplex
ss -s                   # Socket summary statistics
ip route show           # Routing table

# System Profiling
top -H -p <PID>         # Monitor individual thread CPU usage
perf top                # Real-time kernel & userspace hotspots
```
