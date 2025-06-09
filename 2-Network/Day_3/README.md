# 🌐 Day 3: TCP & UDP – Connections & Sockets

Welcome to **Day 3** of your Python + Networking learning journey!  
Today, you'll dive deeper into **TCP vs. UDP**, how connections work, simulate real traffic, and build mini tools like packet sniffers and RTT calculators.

---

## 📘 Topics Covered

- Connection-oriented vs. Connectionless protocols  
- TCP 3-way Handshake  
- Python Sockets (TCP & UDP)  
- Round Trip Time (RTT)  
- Basic Scanning and SYN Flood Simulation  
- DNS over UDP  
- Telnet Detection  
- TCP/UDP Packet Sniffing

---

## 🔹 Exercises

| #   | Task Description                                                              | File                        |
|-----|-------------------------------------------------------------------------------|-----------------------------|
| 1️⃣ | Simple TCP Client-Server – Send message from client to server                | `0_tcp_client_server.py`    |
| 2️⃣ | Convert the above to UDP Version                                              | `1_udp_client_server.py`    |
| 3️⃣ | TCP Server on Port 9999 – Responds with "Hello, Client!"                     | `2_tcp_server_hello.py`     |
| 4️⃣ | Measure Round Trip Time (RTT) of a TCP Connection                            | `3_rtt_measure.py`          |
| 5️⃣ | Simulate SYN Flood (for safe environments only)                              | `4_syn_flood_sim.py`        |
| 6️⃣ | Monitor Incoming TCP Connections – Log source IPs                            | `5_tcp_monitor.py`          |
| 7️⃣ | Simulate TCP Handshake (SYN → SYN-ACK → ACK) Logic in Python                | `6_handshake_simulation.py` |
| 8️⃣ | Test if Remote Host Allows Telnet (port 23)                                  | `7_telnet_check.py`         |
| 9️⃣ | Send Manual DNS Request to 8.8.8.8 via UDP                                   | `8_dns_udp_client.py`       |
| 🔟  | Packet Sniffer – Capture & Display TCP and UDP Packets                       | `9_packet_sniffer.py`       |

---

## 🛠 Tools You Might Use

- `socket` module (TCP/UDP connections)
- `time` module (for RTT)
- `threading` (for concurrent server handling)
- `random`, `struct` (in UDP/DNS simulation)
- `scapy` or `raw socket` (for sniffing and SYN floods)
- Terminal commands: `tcpdump`, `wireshark`, `ss`, `netstat`

---

## 📎 Notes

- Avoid using real SYN flood on production or shared networks.
- Always test in VMs or sandboxed labs.
- You can add logging to capture behavior during exercises.
- Telnet might be disabled on most modern servers; simulate locally.
