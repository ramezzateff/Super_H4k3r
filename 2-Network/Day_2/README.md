# 🔐 Day 2: Ports & Protocols

Welcome to **Day 2** of your Python + Networking learning track!  
Today, you'll explore how ports work, the difference between **TCP** and **UDP**, and how they're used in scanning and enumeration.

---

## 📘 Topics Covered

- Port Numbers (0–65535)
- Privileged vs. Unprivileged Ports
- Well-Known Port Services
- TCP vs. UDP Protocols
- Basic Port Scanning Techniques (TCP/UDP)

---

## 🔹 Exercises

| #   | Task Description                                                                 | File                        |
|-----|----------------------------------------------------------------------------------|-----------------------------|
| 1️⃣ | **List Common Ports & Services**  
      Print commonly used ports (e.g., 80 → HTTP, 443 → HTTPS).                         | `0_common_ports.py`         |
| 2️⃣ | **Validate Port Number**  
      Function to check if port is valid (0–65535).                                      | `1_validate_port.py`        |
| 3️⃣ | **Scan First 1000 Ports**  
      Scan ports 1–1000 on a target IP and report open ones.                             | `2_scan_top_ports.py`       |
| 4️⃣ | **TCP or UDP Detector**  
      Check if a port is typically TCP or UDP.                                           | `3_tcp_udp_check.py`        |
| 5️⃣ | **Random Open Ports Generator**  
      Generate 5 random unprivileged ports (1024–65535).                                 | `4_generate_ports.py`       |
| 6️⃣ | **Privileged Port Checker**  
      Check if a port is in the privileged range (0–1023).                               | `5_check_privileged_port.py`|
| 7️⃣ | **List Listening Ports (Localhost)**  
      List listening ports on `127.0.0.1` using `socket` or `psutil`.                   | `6_list_local_ports.py`     |
| 8️⃣ | **Basic TCP Port Scanner**  
      Use `socket` to build a basic TCP port scanner.                                    | `7_tcp_port_scanner.py`     |
| 9️⃣ | **Basic UDP Port Scanner**  
      Simulate a UDP scan (send packets, check responses or ICMP).                       | `8_udp_port_scanner.py`     |
| 🔟 | **Reserved Ports in Hacking**  
      List reserved ports (1–1023) used in hacking tools (e.g., 21 FTP, 22 SSH).         | `9_reserved_ports_list.py`  |

---

## 🛠 Tools You Might Use

- `socket` (for TCP/UDP communication)
- `random` (generate random ports)
- `psutil` or `subprocess` (list open ports)
- Linux commands: `netstat`, `ss` (to cross-check output)


