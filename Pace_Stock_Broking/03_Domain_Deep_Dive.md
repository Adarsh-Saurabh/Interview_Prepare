# 03: Market Microstructure & Low-Latency Trading

## 1. What is an Electronic Limit Order Book (LOB)?
An exchange order book is an in-memory two-sided auction mechanism:
* **Bids (Buy Orders):** Sorted in descending order (highest willingness to pay at the top).
* **Asks / Offers (Sell Orders):** Sorted in ascending order (lowest willingness to sell at the top).
* **Top of Book (BBO - Best Bid and Offer):**
  $$\text{Best Bid} = \max(P_{\text{buy}}), \quad \text{Best Ask} = \min(P_{\text{sell}})$$
* **The Spread:** $\text{Spread} = \text{Best Ask} - \text{Best Bid}$.
* **Price-Time Priority (FIFO):**
  If Order A and Order B arrive at the exact same price level ₹1,500.00, Order A gets executed first if it arrived 1 nanosecond earlier.

```
       ASKS (Sell Orders)
Level 3: ₹1,501.50  (Qty: 2,500)
Level 2: ₹1,501.00  (Qty: 1,200)
Level 1: ₹1,500.50  (Qty:   400) ◄── BEST ASK
---------------------------------- SPREAD = ₹0.50
Level 1: ₹1,500.00  (Qty:   800) ◄── BEST BID
Level 2: ₹1,499.50  (Qty: 3,000)
Level 3: ₹1,499.00  (Qty: 5,400)
       BIDS (Buy Orders)
```

---

## 2. Exchange Protocol Architecture: Market Data vs Order Entry

### Market Data (Tick Dissemination): Multicast UDP
* **Exchange Side:** Exchanges multicast market events (order inserted, order canceled, trade executed) over raw UDP.
* **Why UDP?** No TCP handshake, no TCP head-of-line blocking, and 1-to-many broadcast efficiency.
* **Protocols:**
  * **NASDAQ ITCH / NSE Multicast:** Binary, fixed-length packets containing `Timestamp`, `Order_ID`, `Side`, `Shares`, `Price`.
  * **Packet Loss Recovery:** When a UDP tick packet drops, feed handlers detect missing sequence numbers and query TCP snapshot/replay recovery channels.

### Order Entry (Execution): Point-to-Point TCP
* **Broker Side:** When a strategy triggers, orders are transmitted over dedicated point-to-point TCP connections to guarantee reliable execution.
* **Protocols:**
  * **NASDAQ OUCH / NSE NEAT:** High-speed binary execution protocols.
  * **FIX (Financial Information eXchange):** Human-readable tag-value protocol (e.g., `35=D|55=RELIANCE|54=1`) used for institutional and retail trading, but avoided in ultra-HFT hot paths due to string parsing overhead.

---

## 3. Kernel Bypass Networking: Solarflare & DPDK

### The Linux Kernel Networking Bottleneck:
```
Normal Linux Socket Path:
NIC RX Wire ──► Hardware Interrupt (IRQ) ──► OS Kernel SoftIRQ 
            ──► Allocate sk_buff in Kernel ──► Copy payload across Kernel-User Boundary 
            ──► Context Switch to User Process ──► recv() returns
            [Total Latency: 1.5 - 3.5 microseconds]

Kernel Bypass (Solarflare OpenOnload / DPDK):
NIC RX Wire ──► Direct Memory Access (DMA) to Pre-Mapped User Memory Ring Buffer 
            ──► User Application polls buffer directly
            [Total Latency: 250 - 450 nanoseconds] (Zero syscalls, zero context switches)
```

### Key Trade-offs:
* **Busy Polling:** Kernel bypass threads run on dedicated isolated CPU cores pinned at 100% CPU utilization (`pthread_setaffinity_np`), spinning continuously on memory addresses rather than sleeping on interrupts.
