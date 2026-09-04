# 07: Caveman & Ponytail Cheat Sheet — Emergency Revision Card

> **Style:** Ultra-dense, zero fluff, maximum technical substance.  
> **Target:** 60-minute quick-review before walking into Lumilens interviews.

---

## 1. Lumilens Core Facts (10 Seconds)

- **What:** Silicon Photonics (SiPh) & Co-Packaged Optics (CPO) interconnects for AI supercomputing.
- **Why:** Copper Direct Attach Copper (DAC) dies past 1.5m at 112G/224G PAM4. AI clusters need light.
- **Funding / Status:** $900M+ funding, $5.5B valuation, CEO Ankur Singla (Contrail $\to$ Juniper, Volterra $\to$ F5), emerged from stealth Aug 2026.
- **Role:** Software Test Automation Engineer (Early Talent). CTC: 29 LPA (M.Tech) / 27 LPA (B.Tech).

---

## 2. Essential Mathematical Formulas & Thresholds

```
+------------------------------------------------------------------------------------------------+
| OPTICAL FORMULAS & NUMERICAL RULES                                                             |
+------------------------------------------------------------------------------------------------+
| Optical Power (dBm):    P(dBm) = 10 * log10(P_mW / 1mW)                                        |
| Optical Power (mW):     P(mW)  = 10^(P_dBm / 10)                                               |
| Quick dBm Table:        -30 dBm = 1 uW | -10 dBm = 100 uW | -3 dBm = 0.5 mW                    |
|                         0 dBm = 1 mW   | +3 dBm = 2 mW   | +10 dBm = 10 mW                     |
| Golden Rules of Thumb:  +3 dB = 2x power | -3 dB = 1/2 power | +10 dB = 10x power              |
| Insertion Loss (IL):    IL(dB) = P_in(dBm) - P_out(dBm)  (always positive dB)                  |
| Extinction Ratio (ER):  ER(dB) = 10 * log10(P_1 / P_0)   (target: 3.5 to 6.0 dB)               |
| Optical Mod Amplitude:  OMA    = P_1 - P_0 (linear mW)                                         |
| Bit Error Rate (BER):   BER    = N_errors / N_total_bits                                       |
| Total Jitter (TJ):      TJ     = DJ + 14.069 * RJ (at BER = 1e-12)                            |
| Process Capability:     Cp     = (USL - LSL) / (6 * sigma)                                     |
|                         Cpk    = min( (USL - mu)/(3*sigma), (mu - LSL)/(3*sigma) )             |
|                         Target: Cpk >= 1.33 (4-sigma), Cpk >= 1.67 (5-sigma)                   |
+------------------------------------------------------------------------------------------------+
```

```
+------------------------------------------------------------------------------------------------+
| HIGH-SPEED NETWORKING CRITICAL THRESHOLDS                                                      |
+------------------------------------------------------------------------------------------------+
| KP4 FEC Threshold:      Pre-FEC BER <= 2.4e-4. (If > 2.4e-4, link fails catastrophically).    |
| Post-FEC BER Target:    Post-FEC BER < 1e-15. (Zero frame drops at Layer 2).                   |
| Standard MTU:           1500 bytes payload (64 bytes min frame, 1518 bytes max frame).         |
| Jumbo Frame MTU:        9000 bytes payload (~9018 to 9022 bytes total frame).                  |
| Min Ethernet Frame:     64 bytes (Preamble/SFD excluded; 14B header + 46B payload + 4B FCS).   |
+------------------------------------------------------------------------------------------------+
```

---

## 3. Layer 1 vs Layer 2 Triage Matrix

```
+-------------------+---------------------------------------+------------------------------------+
| Parameter         | Layer 1 (Physical / Optics)           | Layer 2 (Data Link / Ethernet)     |
+-------------------+---------------------------------------+------------------------------------+
| Data Unit         | Raw Bits / Photons / Symbols          | Ethernet Frames                    |
| Hardware Entity   | Laser, Waveguide, Photodiode, SerDes  | Switch ASIC, MAC, Packet Parser    |
| Addressing        | None (Wavelengths / Lanes)            | 48-bit MAC Addresses (EUI-48)      |
| Core Metrics      | Tx Power, Rx Sensitivity, ER, BER     | Packet Loss %, Throughput, MTU     |
| Error Detection   | Pre-FEC Codewords, Eye Height/Width   | FCS / CRC-32 Checksum              |
| Flow Control      | None (continuous bit stream)          | 802.3x PAUSE, 802.1Qbb PFC         |
+-------------------+---------------------------------------+------------------------------------+
```

---

## 4. SCPI Commands Cheat Sheet (Write These from Memory)

```scpi
*IDN?             # Query Manufacturer, Model, Serial, Firmware
*RST              # Reset instrument to factory default
*CLS              # Clear Status: wipes error queue and event registers
*OPC?             # Returns '1' when previous operation finishes. (CRUCIAL SYNC)
*STB?             # Query 8-bit Status Byte (Bit 4 = MAV / Message Available)
:SYST:ERR?        # Pop oldest error from queue (Expect: '+0,"No error"')
:SENS1:POW:WAV 1310NM   # Set optical power meter wavelength calibration
:MEAS1:POW?             # Read optical power (returns e.g. "-3.42 DBM")
:INP:ATT 10.0DB         # Set Variable Optical Attenuator to 10 dB
:OUTP:STAT 1/0          # Turn laser output / optical shutter ON or OFF
:ROUT:CLOS (@1!4)       # Close optical switch path: route input 1 to output 4
```

---

## 5. Lazy Senior Dev Rules (Ponytail Philosophy)

1. **No `time.sleep()` in Hardware Scripts:**  
   - Bad: `time.sleep(10)`  
   - Good: `while time.time() < deadline: if ready(): break; time.sleep(0.05)`
2. **Guaranteed Hardware Teardown:**  
   - Always put laser shutdown and VOA max attenuation ($30\text{ dB}$) in pytest `yield` teardown or `try...finally`. Avoid burning APD receivers.
3. **Buffer Hygiene:**  
   - Always send `*CLS` on connect and in teardown. Stale unread bytes poison subsequent tests.
4. **Length-Prefixed Binary Sockets:**  
   - Never rely on `\n`-delimited JSON over raw TCP. Use `struct.pack("!I", len(data))` header to eliminate fragmentation truncation.
5. **Pre-FEC vs Post-FEC Triage:**  
   - Zero packet drops at L2 does **not** mean L1 is healthy. Pre-FEC BER can be $2.3 \times 10^{-4}$ (drifting near the edge of link collapse). Always assert Pre-FEC BER.

---

## 6. 10 Rapid-Fire Interview Questions & Punchy Answers

1. **Q: Why does copper fail at 224G beyond 1.5m?**  
   **A:** Skin effect and dielectric loss attenuate high frequencies exponentially. Eye completely closes.

2. **Q: Convert +10 dBm and -3 dBm to milliwatts.**  
   **A:** $+10\text{ dBm} = 10\text{ mW}$. $-3\text{ dBm} \approx 0.5\text{ mW}$.

3. **Q: What is Extinction Ratio and why not make it infinite?**  
   **A:** Ratio $P_1 / P_0$. Infinite ER requires fully switching off laser, causing chirp, turn-on delay, and jitter.

4. **Q: What is the KP4 FEC limit?**  
   **A:** Raw Pre-FEC $\text{BER} \le 2.4 \times 10^{-4}$. Above this, FEC cannot correct errors; frame loss occurs.

5. **Q: What happens if CRC-32 fails on Ethernet frame?**  
   **A:** Hardware MAC drops frame silently, increments `rx_crc_errors` counter. Ethernet sends no NACK.

6. **Q: Why use Jumbo Frames in AI clusters?**  
   **A:** Slashes packet count by factor of 6. Reduces CPU interrupts and cuts header overhead from $2.5\%$ to $<0.4\%$.

7. **Q: What is 802.1Qbb (PFC)?**  
   **A:** Priority Flow Control. Pauses only the congested priority queue (e.g., RoCEv2) while other 7 priorities flow unblocked.

8. **Q: PyVISA script times out on long optical sweep. Fix?**  
   **A:** Increase `inst.timeout = 30000`, send `:INIT; *OPC`, and poll Status Byte (`*STB?` bit 5) instead of synchronous query.

9. **Q: Why use PRBS31 instead of PRBS7?**  
   **A:** PRBS31 ($2 \times 10^9$ bits) has long runs of identical bits, stressing low-frequency baseline wander and thermal drift.

10. **Q: First thing to check when optical power drops 4 dB?**  
    **A:** Clean fiber connector end-faces with fiber scope. Inspect for dust/contamination before debugging software.

---

## 7. The 30-Second Candidate Pitch (Memorize This)

> *"I combine the clean software engineering discipline of a Computer Scientist with the signal integrity and hardware intuition of an M.Tech in Signal Processing from NIT Rourkela.*  
> *Modern AI infrastructure is gated by the physical copper wall. My goal is to build scalable, concurrent, zero-flakiness test automation frameworks in Python that validate Lumilens' silicon photonics from early lab characterization to high-volume manufacturing."*
