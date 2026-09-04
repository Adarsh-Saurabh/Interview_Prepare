# 01: Online Test Mastery — Coding, Networking MCQs & Shell Scripting

> **Target:** Lumilens Online Assessment (Round 1 Screening)  
> **Format:** 60–90 Minutes | 2 Coding Problems + 15–20 Networking MCQs + 5–10 Linux Shell/Regex Questions  
> **Platform Typical:** HackerRank / Mettl / CodeSignal / Custom

---

## 1. Assessment Blueprint & What Lumilens Tests

Lumilens does not ask generic LeetCode graph-coloring or dynamic programming riddles. Because they build high-throughput photonic interconnects, their assessment is heavily weighted toward **systems programming, bitwise manipulation, stateful stream processing, and protocol understanding**:

1. **Python Stream & Packet Processing (40%):** Can you parse bytes, unpack binary headers using `struct`, detect missing sequence IDs, and calculate error rates without loading massive datasets into memory?
2. **Layer 1 & Layer 2 Networking MCQs (35%):** Do you understand Ethernet frames, MAC tables, MTU limits, CRC-32, Bit Error Rate (BER), and optical power attenuation (dBm)?
3. **Linux, Shell & Regex (25%):** Can you parse switch log files, extract error counters with `grep`/`awk`, and debug socket connections from the terminal?

---

## 2. Core Coding Problems with Full Solutions

### Problem 1: Ethernet Frame Header Parser & CRC-32 Validator

**Problem Statement:**  
You are given a raw byte stream captured from an optical transceiver interface. Implement a function `parse_ethernet_frame(raw_bytes: bytes) -> dict` that parses the frame into its constituent fields:
- Preamble (7 bytes: `0xAA` repeated) + SFD (1 byte: `0xAB`)
- Destination MAC (6 bytes, formatted as `xx:xx:xx:xx:xx:xx`)
- Source MAC (6 bytes, formatted as `xx:xx:xx:xx:xx:xx`)
- EtherType (2 bytes, big-endian hex, e.g., `0x0800` for IPv4)
- Payload (variable length, minimum 46 bytes, maximum 1500 bytes for standard MTU)
- Frame Check Sequence (FCS / CRC-32, 4 bytes)
Verify if the received FCS matches the computed CRC-32 of the frame (excluding Preamble, SFD, and FCS itself).

```python
import struct
import zlib

def format_mac(mac_bytes: bytes) -> str:
    return ":".join(f"{b:02x}" for b in mac_bytes)

def parse_ethernet_frame(raw_bytes: bytes) -> dict:
    """
    Parses raw Ethernet frame including preamble and FCS.
    Returns parsed dictionary with validation status.
    """
    # Minimum valid Ethernet frame: 7 (Preamble) + 1 (SFD) + 14 (Header) + 46 (Min Payload) + 4 (FCS) = 72 bytes
    if len(raw_bytes) < 72:
        raise ValueError(f"Frame too short: {len(raw_bytes)} bytes (min 72 with preamble)")
    
    # 1. Validate Preamble (7 bytes of 0xAA) and SFD (0xAB)
    preamble = raw_bytes[:7]
    sfd = raw_bytes[7]
    if preamble != b'\xaa' * 7 or sfd != 0xab:
        return {"status": "INVALID_PREAMBLE_OR_SFD", "valid": False}
    
    # Frame body starts at byte 8
    frame_body = raw_bytes[8:]
    
    # 2. Extract Destination MAC, Source MAC, EtherType (14 bytes total)
    header_format = "!6s6sH" # Network byte order (big-endian), 6 bytes, 6 bytes, unsigned short (2 bytes)
    dest_mac_raw, src_mac_raw, ether_type = struct.unpack(header_format, frame_body[:14])
    
    # 3. Payload and FCS
    # The last 4 bytes of the frame body are FCS (CRC-32)
    payload = frame_body[14:-4]
    received_fcs = struct.unpack("!I", frame_body[-4:])[0]
    
    # 4. CRC-32 verification (calculated over Dest MAC + Src MAC + EtherType + Payload)
    calculated_crc = zlib.crc32(frame_body[:-4]) & 0xFFFFFFFF
    is_valid = (calculated_crc == received_fcs)
    
    return {
        "status": "OK" if is_valid else "CRC_ERROR",
        "valid": is_valid,
        "destination_mac": format_mac(dest_mac_raw),
        "source_mac": format_mac(src_mac_raw),
        "ethertype": f"0x{ether_type:04x}",
        "payload_length": len(payload),
        "received_fcs": hex(received_fcs),
        "calculated_crc": hex(calculated_crc)
    }

# Test Verification
if __name__ == "__main__":
    # Construct a synthetic valid packet
    preamble_sfd = b'\xaa' * 7 + b'\xab'
    dst_mac = b'\x00\x1a\x2b\x3c\x4d\x5e'
    src_mac = b'\x00\x11\x22\x33\x44\x55'
    ethertype = struct.pack("!H", 0x0800) # IPv4
    payload = b'LUMILENS_PHOTONIC_INTERCONNECT_TEST_PAYLOAD_PADDING_0123456789' # >= 46 bytes
    
    protected_data = dst_mac + src_mac + ethertype + payload
    fcs = struct.pack("!I", zlib.crc32(protected_data) & 0xFFFFFFFF)
    
    full_frame = preamble_sfd + protected_data + fcs
    result = parse_ethernet_frame(full_frame)
    print("Parsing Result:", result)
    assert result["valid"] is True
    assert result["destination_mac"] == "00:1a:2b:3c:4d:5e"
```

---

### Problem 2: Sliding Window Packet Loss & Burst Drop Detector

**Problem Statement:**  
In high-throughput optical testing, packet sequence numbers are injected by traffic generators (e.g., IXIA) at 100M packets/sec. Due to optical switch buffer contention or laser mode hops, packet drops can happen either randomly or in concentrated bursts.  
Implement a class `PacketDropAnalyzer` that processes incoming integer sequence IDs in an online/streaming fashion:
1. Detects dropped packets (missing sequence IDs).
2. Calculates overall packet drop rate: $\text{Drop Rate} = \frac{\text{Lost Packets}}{\text{Total Expected Packets}}$.
3. Detects "Burst Drops": any single drop event where $\ge K$ consecutive sequence numbers are missing.
4. Memory requirement: $O(1)$ auxiliary memory (cannot store the entire stream).

```python
class PacketDropAnalyzer:
    def __init__(self, burst_threshold: int = 5):
        self.burst_threshold = burst_threshold
        self.expected_seq = None
        self.total_received = 0
        self.total_lost = 0
        self.burst_events = [] # list of (start_seq, count)
        self.out_of_order_count = 0

    def process_packet(self, seq_id: int):
        """Processes a single packet sequence number on the fly."""
        self.total_received += 1
        
        # Initial packet
        if self.expected_seq is None:
            self.expected_seq = seq_id + 1
            return

        # Normal sequential arrival
        if seq_id == self.expected_seq:
            self.expected_seq = seq_id + 1
            return

        # Packet drop detected (gap in sequence)
        if seq_id > self.expected_seq:
            lost_count = seq_id - self.expected_seq
            self.total_lost += lost_count
            
            if lost_count >= self.burst_threshold:
                self.burst_events.append((self.expected_seq, lost_count))
            
            self.expected_seq = seq_id + 1
            return

        # Late / Out-of-order packet (seq_id < self.expected_seq)
        if seq_id < self.expected_seq:
            self.out_of_order_count += 1
            # In real hardware, this indicates multi-path reordering or queue race

    def get_summary(self) -> dict:
        total_expected = self.total_received + self.total_lost
        drop_rate = (self.total_lost / total_expected) if total_expected > 0 else 0.0
        return {
            "total_received": self.total_received,
            "total_lost": self.total_lost,
            "total_expected": total_expected,
            "drop_rate_pct": drop_rate * 100.0,
            "burst_drop_count": len(self.burst_events),
            "burst_details": self.burst_events,
            "out_of_order": self.out_of_order_count
        }

# Verification
if __name__ == "__main__":
    analyzer = PacketDropAnalyzer(burst_threshold=3)
    # Stream: 1, 2, 3, [4,5 missing], 6, 7, [8,9,10,11 missing -> burst], 12
    stream = [1, 2, 3, 6, 7, 12]
    for s in stream:
        analyzer.process_packet(s)
    
    summary = analyzer.get_summary()
    print("Analyzer Summary:", summary)
    assert summary["total_lost"] == 6 # (4,5) = 2, (8,9,10,11) = 4 -> total 6
    assert summary["burst_drop_count"] == 1 # only gap of 4 exceeds threshold 3
```

---

### Problem 3: Layer 2 Switch MAC Learning Table with Aging & Flood Control

**Problem Statement:**  
Implement an L2 Switch MAC Learning Engine. When a packet arrives on a switch port:
1. **Learn:** Associate the Source MAC address with the ingress port and record the arrival timestamp.
2. **Forward:** Look up the Destination MAC address.
   - If found and not expired: Forward unicast to that specific port.
   - If unknown (or expired): **Flood** (forward to all other ports except the ingress port).
   - If broadcast (`FF:FF:FF:FF:FF:FF`): **Flood** to all other ports.
3. **Aging:** Entries older than `aging_time_seconds` must expire and be evicted.
4. **Capacity / CAM Table Overflow:** If table reaches `max_capacity`, evict the Least Recently Used (LRU) entry.

```python
import time
from collections import OrderedDict

class L2SwitchMACTable:
    def __init__(self, ports: list[int], aging_time_sec: float = 300.0, max_capacity: int = 1024):
        self.ports = set(ports)
        self.aging_time = aging_time_sec
        self.max_capacity = max_capacity
        # Store as OrderedDict: mac -> (port, timestamp)
        # Using OrderedDict allows O(1) lookup and O(1) LRU eviction
        self.table = OrderedDict()

    def _purge_expired(self, current_time: float):
        """Purge entries that have exceeded the aging timer."""
        expired_macs = [mac for mac, (_, ts) in self.table.items() if (current_time - ts) > self.aging_time]
        for mac in expired_macs:
            del self.table[mac]

    def process_frame(self, ingress_port: int, src_mac: str, dst_mac: str, current_time: float = None) -> list[int]:
        if ingress_port not in self.ports:
            raise ValueError(f"Invalid ingress port {ingress_port}")
        
        if current_time is None:
            current_time = time.time()
            
        src_mac = src_mac.lower()
        dst_mac = dst_mac.lower()
        
        self._purge_expired(current_time)

        # 1. LEARN: update or insert source MAC
        if src_mac in self.table:
            del self.table[src_mac] # remove to reinsert at end (mark most recently used)
        elif len(self.table) >= self.max_capacity:
            # Evict LRU (first item in OrderedDict)
            self.table.popitem(last=False)
            
        self.table[src_mac] = (ingress_port, current_time)

        # 2. FORWARD: determine egress ports
        # Broadcast or Unknown Unicast -> Flood all ports except ingress
        if dst_mac == "ff:ff:ff:ff:ff:ff" or dst_mac not in self.table:
            return [p for p in sorted(self.ports) if p != ingress_port]

        # Known unicast
        egress_port, _ = self.table[dst_mac]
        if egress_port == ingress_port:
            # Destination is on same port as source -> Drop (hairpinning prevention)
            return []
        
        return [egress_port]

# Verification
if __name__ == "__main__":
    sw = L2SwitchMACTable(ports=[1, 2, 3, 4], aging_time_sec=10.0, max_capacity=2)
    # Frame 1: Port 1, Host A -> Host B (Unknown B -> Flood 2, 3, 4)
    out1 = sw.process_frame(ingress_port=1, src_mac="00:00:00:00:00:0A", dst_mac="00:00:00:00:00:0B", current_time=0.0)
    assert out1 == [2, 3, 4]

    # Frame 2: Port 2, Host B -> Host A (Known A on port 1 -> Unicast to 1)
    out2 = sw.process_frame(ingress_port=2, src_mac="00:00:00:00:00:0B", dst_mac="00:00:00:00:00:0A", current_time=1.0)
    assert out2 == [1]
```

---

### Problem 4: Bit Error Rate (BER) & PRBS-7 Sequence Validator

**Problem Statement:**  
In physical layer optical testing, transceivers transmit standardized **Pseudo-Random Binary Sequences (PRBS)** like PRBS-7, PRBS-15, or PRBS-31 to stress the optical eye diagram.  
PRBS-7 polynomial: $X^7 + X^6 + 1$ (Length = $2^7 - 1 = 127$ bits).  
Write a Python function `calculate_ber(received_bits: list[int], seed: int = 0x7F) -> dict` that:
1. Generates the reference PRBS-7 sequence.
2. Synchronizes with the incoming bit stream (finds phase alignment).
3. Computes bit errors and returns the Bit Error Rate: $\text{BER} = \frac{\text{Bit Errors}}{\text{Total Validated Bits}}$.

```python
def generate_prbs7(length: int, seed: int = 0x7F) -> list[int]:
    """Generates PRBS-7 sequence using polynomial X^7 + X^6 + 1."""
    state = seed & 0x7F
    if state == 0:
        state = 0x7F # All zeros is an invalid state
    
    sequence = []
    for _ in range(length):
        # bit 7 and bit 6 (0-indexed: bit 6 and bit 5)
        b6 = (state >> 6) & 1
        b5 = (state >> 5) & 1
        feedback = b6 ^ b5
        
        output_bit = b6
        sequence.append(output_bit)
        
        state = ((state << 1) & 0x7F) | feedback
    return sequence

def calculate_ber_prbs7(received_bits: list[int]) -> dict:
    """Aligns received stream with PRBS-7 and computes BER."""
    PRBS_PERIOD = 127
    if len(received_bits) < PRBS_PERIOD * 2:
        raise ValueError("Need at least 2 full periods (254 bits) to synchronize")
    
    reference = generate_prbs7(PRBS_PERIOD)
    
    # Find best alignment phase by checking minimum Hamming distance over one period
    best_phase = 0
    min_errors = float('inf')
    
    for phase in range(PRBS_PERIOD):
        errors = 0
        for i in range(PRBS_PERIOD):
            ref_bit = reference[(i + phase) % PRBS_PERIOD]
            if received_bits[i] != ref_bit:
                errors += 1
        if errors < min_errors:
            min_errors = errors
            best_phase = phase
            if errors == 0:
                break # Perfect alignment found
                
    # Now compute total errors across the entire received buffer using the best phase
    total_errors = 0
    total_bits = len(received_bits)
    for i in range(total_bits):
        ref_bit = reference[(i + best_phase) % PRBS_PERIOD]
        if received_bits[i] != ref_bit:
            total_errors += 1
            
    ber = total_errors / total_bits
    return {
        "total_bits": total_bits,
        "bit_errors": total_errors,
        "ber": ber,
        "phase_offset": best_phase,
        "status": "PASS" if ber < 1e-12 else "MARGINAL" if ber < 1e-4 else "FAIL"
    }

# Verification
if __name__ == "__main__":
    clean_seq = generate_prbs7(1000)
    # Inject 2 synthetic bit errors
    corrupted_seq = clean_seq.copy()
    corrupted_seq[150] ^= 1
    corrupted_seq[800] ^= 1
    
    ber_res = calculate_ber_prbs7(corrupted_seq)
    print("BER Test:", ber_res)
    assert ber_res["bit_errors"] == 2
    assert abs(ber_res["ber"] - 0.002) < 1e-6
```

---

## 3. High-Yield Networking MCQs & Technical Rapid-Fire

### Q1: What is the exact difference between OSI Layer 1 and Layer 2 in optical networking?
- **Answer:**  
  - **Layer 1 (Physical):** Governs the physical transmission of raw bits over light. Key parameters: optical wavelengths (1310 nm vs 1550 nm), Tx/Rx optical power (dBm), extinction ratio, chromatic dispersion, jitter, and Bit Error Rate (BER). Layer 1 does **not** understand addresses, frames, or packets.
  - **Layer 2 (Data Link):** Groups raw bits into **Ethernet Frames**. Governs MAC addressing (source & destination), framing delimiters (preamble/SFD), error detection via FCS (CRC-32), flow control (802.3x pause, Priority Flow Control 802.1Qbb), and VLAN tagging (802.1Q).

### Q2: What is the formula for converting Optical Power from milliwatts (mW) to dBm?
- **Formula:**  
  $$\text{Power (dBm)} = 10 \cdot \log_{10}\left(\frac{P_{\text{mW}}}{1\text{ mW}}\right)$$
- **Quick Reference Table:**
  - $1\text{ mW} = 0\text{ dBm}$
  - $2\text{ mW} \approx +3\text{ dBm}$
  - $10\text{ mW} = +10\text{ dBm}$
  - $0.1\text{ mW} = -10\text{ dBm}$
  - $0.001\text{ mW} (1\text{ }\mu\text{W}) = -30\text{ dBm}$
- **Interview Rule of Thumb:** Every $+3\text{ dB}$ doubles power; every $-3\text{ dB}$ halves power. Every $+10\text{ dB}$ multiplies power by 10.

### Q3: What is MTU vs MRU, and what happens if an optical transceiver receives a 9000-byte frame on a standard port?
- **Answer:**
  - **MTU (Maximum Transmission Unit):** Maximum size of the Layer 3 payload that Layer 2 can transmit without fragmentation (default Ethernet = 1500 bytes).
  - **MRU (Maximum Receive Unit):** Maximum frame size the receiver can accept.
  - **Jumbo Frames (9000 bytes):** Used in AI data centers to maximize throughput and minimize CPU overhead.
  - If a switch port configured for 1500-byte MTU receives a 9000-byte frame: It will drop the frame as an **Oversized / Giant Frame** and increment the switch's `rx_oversize_errors` counter. Layer 2 Ethernet does **not** fragment frames; fragmentation is handled only by Layer 3 (IP).

### Q4: What is an Optical Eye Diagram, and what do Eye Height and Eye Width represent?
- **Answer:**
  - An eye diagram is formed by overlaying millions of repetitive binary transitions on a high-speed optical sampling oscilloscope.
  - **Eye Height:** Proportional to vertical noise margin. If the eye height collapses, signal-to-noise ratio (SNR) is degraded, leading to amplitude bit errors.
  - **Eye Width:** Proportional to horizontal jitter tolerance. Narrow eye width indicates timing jitter and clock drift.
  - **Open Eye:** High signal integrity, low BER ($< 10^{-12}$).
  - **Closed Eye:** Receiver cannot distinguish between logical '0' and logical '1'.

### Q5: What is CRC-32 (FCS), and what happens when an Ethernet frame fails CRC check?
- **Answer:**
  - The FCS (Frame Check Sequence) is a 32-bit cyclic redundancy check calculated over the destination MAC, source MAC, EtherType, and payload.
  - When an Ethernet switch receives a frame with an invalid CRC:
    1. The switch **immediately drops** the frame.
    2. Increments the `rx_crc_errors` or `rx_fcs_errors` hardware counter.
    3. **Crucial:** Layer 2 Ethernet does **not** send a NACK or request retransmission. Retransmission is strictly the responsibility of Layer 4 (TCP) or RoCEv2 transport.

---

## 4. Linux Shell & Log Parsing for Automation

### Essential 1-Liners for Optical Test Debugging

```bash
# 1. Filter lines with CRC errors from switch syslog and count occurrences by interface
grep -i "crc error" /var/log/switch.log | awk '{print $4}' | sort | uniq -c | sort -nr

# 2. Extract optical transceiver Rx power values using regex and flag values below -10 dBm
grep -oP 'Port \d+: Rx Power = [-\d.]+ dBm' optical_telemetry.log | awk '$6 < -10.0 {print "CRITICAL LOW POWER: ", $0}'

# 3. Monitor live dropped packets on an interface in real time
watch -n 1 'ethtool -S eth0 | grep -E "drop|error|discard"'

# 4. Check whether port 5025 (SCPI TCP instrument port) is listening and reachable
nc -zv 192.168.1.105 5025

# 5. Capture first 50 Ethernet frames on interface eth1 and save to pcap
tcpdump -i eth1 -c 50 -w test_capture.pcap
```
