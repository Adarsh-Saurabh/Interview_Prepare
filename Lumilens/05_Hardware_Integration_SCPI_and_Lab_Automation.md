# 05: Hardware Integration, SCPI Protocols & Manufacturing Automation

> **Focus:** NI-VISA, SCPI Command Syntax, Lab Instrument Control, High-Volume Manufacturing (HVM), Yield Optimization, and C# .NET/WPF Basics  
> **Direct JD Mapping:** High-Volume Manufacturing test software, change control, SCPI, RS-232, TCP/IP, and instrument automation.

---

## 1. Instrument Communication Architecture

In an optical engineering lab or manufacturing test station, test software communicates with heterogeneous instruments across multiple physical buses through a standardized abstraction layer:

```
+-----------------------------------------------------------------------------------+
|               Test Automation Software (Python / C# .NET WPF)                     |
+-----------------------------------------------------------------------------------+
                                         |
                       [ NI-VISA / PyVISA Driver Layer ]
                                         |
       +--------------------+---------------------+--------------------+
       |                    |                     |                    |
[ VXI-11 / LXI (TCP/IP) ] [ USB (USBTMC) ]    [ Serial (RS-232) ]  [ GPIB (IEEE 488) ]
   Port 5025 / Raw Socket    Vendor IDs           COM Ports            Bus Addresses
       |                    |                     |                    |
[ Optical Power Meter ]  [ Optical Switch ]   [ Switch Console ]   [ Oscilloscope ]
```

---

## 2. SCPI Protocol Mastery (Standard Commands for Programmable Instruments)

SCPI commands are ASCII text strings organized in a hierarchical tree structure defined by IEEE 488.2.

### Essential Mandatory IEEE 488.2 Common Commands

| Command | Name | Function / Behavior |
| :--- | :--- | :--- |
| `*IDN?` | Identification Query | Returns manufacturer, model, serial number, and firmware version (e.g., `Keysight Technologies,N7744A,MY54120102,1.24`). |
| `*RST` | Reset | Restores instrument to known factory default state. Must be called at the start of a test session. |
| `*CLS` | Clear Status | Clears all status registers, the Standard Event Status register, and the instrument error queue. |
| `*OPC?` | Operation Complete Query | Waits until all pending operations (sweeps, motor movements, calibrations) finish, then returns ASCII `'1'`. **Crucial for preventing race conditions!** |
| `*WAI` | Wait-to-Continue | Halts processing of subsequent commands until all current operations complete. |
| `*STB?` | Status Byte Query | Returns 8-bit status byte. Bit 4 = MAV (Message Available), Bit 5 = ESB (Event Status Bit), Bit 6 = MSS (Master Summary Status). |
| `:SYST:ERR?` | System Error Query | Pops the oldest error from the instrument's FIFO error queue. Returns `+0,"No error"` if clean. |

---

### Optical Instrument SCPI Command Reference Table

```scpi
# --- OPTICAL POWER METER (OPM) ---
:SENS1:POW:WAV 1310NM        # Set sensor wavelength calibration to 1310 nm
:SENS1:POW:UNIT DBM          # Set output measurement unit to dBm (or W for Watts)
:SENS1:POW:RANG:AUTO 1       # Enable auto-ranging
:SENS1:POW:ATIM 100MS        # Set averaging time to 100 milliseconds
:MEAS1:POW?                  # Trigger measurement and return current optical power

# --- VARIABLE OPTICAL ATTENUATOR (VOA) ---
:INP:WAV 1310NM              # Set working wavelength
:OUTP:STAT 1                 # Enable optical shutter / output
:INP:ATT 12.5DB              # Set attenuation to 12.5 dB
:INP:ATT?                    # Query current attenuation level

# --- OPTICAL MATRIX SWITCH ---
:ROUT:CLOS (@1!4)            # Connect input channel 1 to output channel 4
:ROUT:CLOS? (@1!4)           # Query whether route (1 to 4) is closed (connected)
:ROUT:OPEN:ALL               # Disconnect all optical routes (safety state)

# --- OPTICAL SAMPLING OSCILLOSCOPE ---
:TRIG:SOUR EXT               # Set trigger source to external clock recovery
:MEAS:EYE:HEIG? CHAN1        # Query measured vertical eye height
:MEAS:EYE:WIDT? CHAN1        # Query measured horizontal eye width
:MEAS:JITT:TOT? CHAN1        # Query Total Jitter (TJ)
```

---

## 3. NI-VISA Resource Strings & RS-232 Serial Mechanics

### Resource String Formats

- **TCP/IP (VXI-11 / LXI):** `TCPIP0::192.168.1.105::inst0::INSTR`
- **TCP/IP (Raw Socket):** `TCPIP0::192.168.1.105::5025::SOCKET`
- **USB (USBTMC):** `USB0::0x0957::0x1807::MY51234567::0::INSTR`
- **Serial (RS-232):** `ASRL1::INSTR` (COM1 on Windows, `/dev/ttyS0` on Linux)
- **GPIB:** `GPIB0::14::INSTR`

### RS-232 Serial Port Configuration Parameters
When automating serial switch consoles or legacy optical attenuators:
- **Baud Rate:** Transmission speed in symbols/sec (e.g., `9600`, `115200`).
- **Data Bits:** Typically 8 bits.
- **Parity:** Error detection bit (`None`, `Even`, `Odd`).
- **Stop Bits:** Framing bit (`1` or `2`).
- **Flow Control:**
  - **Hardware (RTS/CTS):** Request to Send / Clear to Send voltage pins. Prevents buffer overflow.
  - **Software (XON/XOFF):** ASCII control characters `0x11` (resume) and `0x13` (pause).

---

## 4. High-Volume Manufacturing (HVM) Test & Yield Optimization

In high-volume manufacturing of silicon photonics optical transceivers, test automation is directly responsible for **factory throughput, yield, and unit production cost**.

### 1. Cycle Time vs Test Coverage Trade-off
- If a test station takes **10 minutes** to test one optical transceiver, a factory producing 100,000 units/month needs hundreds of expensive test benches ($200k+ per bench).
- **Optimization Strategy:**
  - Use fast multi-channel power meters with parallel optical sweeps.
  - Test coarse sanity checks first (continuity, laser threshold current $I_{\text{th}}$, DDM health) before running expensive multi-billion-bit BER tests.
  - Abort failed units immediately (*Fail Fast*) to free up test stations.

### 2. Statistical Process Control (SPC): $C_p$ and $C_{pk}$
Manufacturing test data is logged into databases to compute process capability indices:

$$C_p = \frac{\text{USL} - \text{LSL}}{6\sigma}$$

$$C_{pk} = \min\left(\frac{\text{USL} - \mu}{3\sigma}, \frac{\mu - \text{LSL}}{3\sigma}\right)$$

- $\text{USL}$ / $\text{LSL}$: Upper / Lower Specification Limits (e.g., Optical Tx Power must be between $+1.0\text{ dBm}$ and $+3.0\text{ dBm}$).
- $\mu$: Process mean.
- $\sigma$: Standard deviation.
- **Benchmark:** A world-class manufacturing line requires **$C_{pk} \ge 1.33$** (4-sigma quality) or **$C_{pk} \ge 1.67$** (5-sigma quality). If $C_{pk} < 1.0$, the process is drifting out of spec and producing defective transceivers.

### 3. Change Control Management
- In high-volume manufacturing, a test engineer cannot simply push unverified code to the production line.
- **Change Control Protocol:**
  1. Test scripts are version-tagged in Git (`v2.4.1-rc1`).
  2. Golden units (calibrated standard transceivers with certified metrics) are run through the station 10 times to prove repeatability.
  3. Change Request (CR) document is approved by Design, Manufacturing, and Quality leads.
  4. Software is signed and deployed to stations with rollback capability.

---

## 5. C# .NET & Windows Presentation Foundation (WPF) Basics

The Lumilens JD notes: *"Exposure to C# for UI validation or tool development is a plus. Technical Skills: C# .NET (Framework or Core), OOP concepts, Windows Form or WPF."*

### Why C# / WPF on the Manufacturing Floor?
Factory floor operators do not run terminal commands or pytest scripts. They use a touchscreen Windows PC connected to barcode scanners.  
The C# WPF UI provides:
1. Operator barcode scanning of DUT serial number.
2. Large visual status indicators (Giant Green "PASS" or Red "FAIL").
3. Real-time live plotting of optical eye diagrams and power levels.
4. User access control (Operator vs Technician vs Calibration Engineer).

### Minimal Production C# VISA Instrument Driver

```csharp
using System;
using Ivi.Visa; // IVI Foundation / National Instruments VISA .NET API

namespace Lumilens.LabAutomation
{
    public interface IOpticalInstrument : IDisposable
    {
        void Connect();
        void Reset();
        string Query(string command);
    }

    public class OpticalPowerMeter : IOpticalInstrument
    {
        private readonly string _resourceAddress;
        private IVisaSession _session;
        private IMessageBasedSession _msgSession;

        public OpticalPowerMeter(string resourceAddress)
        {
            _resourceAddress = resourceAddress;
        }

        public void Connect()
        {
            _session = GlobalResourceManager.Open(_resourceAddress);
            _msgSession = _session as IMessageBasedSession;
            if (_msgSession == null)
            {
                throw new InvalidOperationException("Resource does not support message-based communication.");
            }
            _msgSession.TimeoutMilliseconds = 3000;
            _msgSession.TerminationCharacter = '\n';
            _msgSession.TerminationCharacterEnabled = true;
            
            // Clear status registers on connect
            _msgSession.RawIO.Write("*CLS\n");
        }

        public void Reset()
        {
            _msgSession.RawIO.Write("*RST\n");
            _msgSession.RawIO.Write("*CLS\n");
        }

        public string Query(string command)
        {
            _msgSession.RawIO.Write(command.Trim() + "\n");
            return _msgSession.RawIO.ReadString().Trim();
        }

        public double MeasurePowerDbm(int wavelengthNm)
        {
            _msgSession.RawIO.Write($":SENS:POW:WAV {wavelengthNm}NM\n");
            string response = Query(":MEAS:POW?");
            return double.Parse(response.Replace("DBM", "").Trim());
        }

        public void Dispose()
        {
            if (_msgSession != null)
            {
                _msgSession.Dispose();
                _msgSession = null;
            }
            if (_session != null)
            {
                _session.Dispose();
                _session = null;
            }
        }
    }
}
```

### WPF Model-View-ViewModel (MVVM) Pattern Essentials
- **Model:** The C# hardware driver classes (`OpticalPowerMeter`, `IXIATrafficClient`).
- **ViewModel:** Exposes properties and commands for the UI, implementing `INotifyPropertyChanged` so the UI automatically updates when optical power changes without freezing the UI thread.
- **View:** XAML file declaring buttons, text boxes, and gauge controls.
- **Multithreading Rule:** Long SCPI sweeps and traffic generation must run on a background worker thread (`Task.Run()`); only the final results are marshaled back to the UI thread via `Dispatcher.Invoke()`.
