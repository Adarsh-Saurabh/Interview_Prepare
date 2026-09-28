# 03: Optical Networks, DWDM & Coherent Technologies

## 1. Physics of Optical Transmission

### 1.1 Total Internal Reflection & Fiber Geometry
* Light guides through optical fiber via **Total Internal Reflection (TIR)** at the core-cladding boundary:
  $$	heta_c = rcsin\left(rac{n_{	ext{cladding}}}{n_{	ext{core}}}ight)$$
* **Single-Mode Fiber (SMF-28)**:
  * Core diameter $pprox 9\,\mu	ext{m}$, cladding diameter $= 125\,\mu	ext{m}$.
  * Only one electromagnetic spatial mode propagates. Eliminates modal dispersion. Standard for telecom long-haul.
* **Multi-Mode Fiber (MMF)**:
  * Core diameter $= 50\,\mu	ext{m}$ or $62.5\,\mu	ext{m}$.
  * Multiple light propagation paths. Severe modal dispersion. Restricted to short enterprise distances (<500m).

### 1.2 Optical Transmission Impairments

| Impairment | Physics & Impact | Engineering Solution |
| :--- | :--- | :--- |
| **Attenuation** | Loss of light power over distance due to Rayleigh scattering and OH absorption. (Min loss $pprox 0.2\,	ext{dB/km}$ at $1550\,	ext{nm}$). | Optical Amplifiers (EDFA, Raman) every 80-100 km. |
| **Chromatic Dispersion (CD)** | Different wavelength spectral components travel at different group velocities, causing pulse spreading. | Coherent Digital Signal Processor (DSP) electronic dispersion compensation (EDC). |
| **Polarization Mode Dispersion (PMD)**| Asymmetry in fiber core causes two orthogonal light polarizations to travel at different speeds (Differential Group Delay - DGD). | Adaptive FIR filters in DSP (Nokia PSE engine). |
| **Non-Linearities (Kerr Effect)**| Refractive index varies with light intensity at high power (Self-Phase Modulation - SPM, Cross-Phase Modulation - XPM, Four-Wave Mixing - FWM). | Constellation shaping, digital back-propagation (DBP), power optimization. |

---

## 2. Dense Wavelength Division Multiplexing (DWDM) & ROADM

### 2.1 The Optical Spectrum
* **C-Band (Conventional)**: $1530\,	ext{nm} - 1565\,	ext{nm}$ (Lowest attenuation window in silica fiber; aligns with EDFA amplification spectrum).
* **L-Band (Long Wavelength)**: $1565\,	ext{nm} - 1625\,	ext{nm}$ (Used to double fiber capacity when C-band is saturated).
* **ITU-T Grid**: Standard channel spacing of $50\,	ext{GHz}$ (approx $0.4\,	ext{nm}$), $100\,	ext{GHz}$, or modern **Flex-Grid** (variable $12.5\,	ext{GHz}$ increments allowing channel widths from $37.5\,	ext{GHz}$ to $150\,	ext{GHz}$ tailored to signal baud rates).

### 2.2 ROADM Architecture (Reconfigurable Optical Add-Drop Multiplexer)
* Allows network operators to remotely add, drop, or pass through optical wavelengths at fiber junctions without manual technician intervention.
* **CDC ROADM**:
  * **Colorless**: Any port can accept any wavelength.
  * **Directionless**: Any channel can be routed to any outgoing fiber direction.
  * **Contentionless**: Multiple identical wavelengths can be added/dropped simultaneously on different directions without collision.

---

## 3. Coherent Optical Transmission & Digital Signal Processing (DSP)

### 3.1 The Coherent Revolution
* Early optical transmission used **Direct Detection (On-Off Keying - OOK)**: photodiode simply measured light intensity (presence or absence of photons).
* **Coherent Detection**: Mixes the incoming weak optical signal with a stable local laser called the **Local Oscillator (LO)**:
  * Measures both **Amplitude** and **Phase** of the electromagnetic wave.
  * Employs **Dual-Polarization (DP)**: encodes two independent data streams on horizontal (H) and vertical (V) polarizations of light.
  * Enables high-order modulation schemes: **DP-QPSK** (4 bits/symbol), **DP-16QAM** (8 bits/symbol), and **DP-64QAM** (12 bits/symbol).

### 3.2 The Nokia PSE-6s Engine
* Nokia's **Photonic Service Engine 6s** is fabricated on 5nm process technology.
* Functions executed inside the coherent DSP chip:
  1. **Analog-to-Digital Conversion (ADC)**: Sampling optical waveform at $>130\,	ext{GSamples/s}$.
  2. **Electronic Chromatic Dispersion Compensation**: Inverse filtering compensating thousands of ps/nm of dispersion without optical dispersion compensating fibers.
  3. **Polarization Demultiplexing & Equalization**: Multi-tap adaptive FIR filters un-mixing the crossed polarization states.
  4. **Carrier Phase & Frequency Recovery**: Eliminating phase noise between transmitter laser and local oscillator.
  5. **Soft-Decision Forward Error Correction (SD-FEC)**: Iterative decoding running close to the theoretical Shannon capacity limit.

---

## 4. Optical Transport Network (OTN - ITU-T G.709)

* Known as the "Digital Wrapper" for optical networks.
* Provides deterministic framing, multiplexing, client transparency, and end-to-end performance monitoring:
  * **OPU (Optical Payload Unit)**: Wraps raw client signals (e.g. 100GbE, 400GbE).
  * **ODU (Optical Data Unit)**: Provides path monitoring, tandem connection monitoring (TCM), and switching.
  * **OTU (Optical Transport Unit)**: Adds frame alignment bytes and Reed-Solomon / LDPC Forward Error Correction (FEC).
