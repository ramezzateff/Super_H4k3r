# 🔐 Day 2: Ports & Protocols

Welcome to Day 2 of your Python + Networking learning track!  
Today, you'll dive deep into how ports work, the difference between TCP and UDP, and how they are used in scanning and enumeration tasks.

---

## 📘 Topics Covered
- Port Numbers (0–65535)
- Privileged vs. Unprivileged Ports
- Well-Known Port Services
- TCP vs. UDP Protocols
- Basic Port Scanning Techniques (TCP/UDP)

---

## 🔹 Exercises

| #  | Task Description |
|----|------------------|
| 1️| **List Common Ports & Services**  
Print a list of commonly used ports (e.g., 80 → HTTP, 443 → HTTPS).  
**File:** `0_common_ports.py` |
| 2️| **Validate Port Number**  
Write a function to check if a port number is valid (0–65535).  
**File:** `1_validate_port.py` |
| 3️| **Scan First 1000 Ports**  
Create a script to scan ports 1–1000 on a target IP and report open ones.  
**File:** `2_scan_top_ports.py` |
| 4️| **TCP or UDP Detector**  
Given a port number, check if it’s typically used by TCP or UDP.  
**File:** `3_tcp_udp_check.py` |
| 5️| **Random Open Ports Generator**  
Randomly generate and print 5 open port numbers from the unprivileged range (1024–65535).  
**File:** `4_generate_ports.py` |
| 6️| **Privileged Port Checker**  
Determine whether a given port is in the privileged range (0–1023).  
**File:** `5_check_privileged_port.py` |
| 7️| **List Listening Ports (Localhost)**  
List all currently listening ports on `127.0.0.1` (use `socket` or `psutil`).  
**File:** `6_list_local_ports.py` |
| 8️| **Basic TCP Port Scanner**  
Use Python’s `socket` module to implement a basic TCP port scanner.  
**File:** `7_tcp_port_scanner.py` |
| 9️| **Basic UDP Port Scanner**  
Simulate a basic UDP scanner (send UDP packets, check responses or ICMP).  
**File:** `8_udp_port_scanner.py` |
| 10| **Reserved Ports in Hacking**  
List all commonly used reserved ports (1–1023) in hacking tools (e.g., 21 for FTP, 22 for SSH).  
**File:** `9_reserved_ports_list.py` |

---

## 🛠 Tools You Might Use

- `socket` (for TCP/UDP connections)
- `random` (for generating port numbers)
- `psutil` or `subprocess` (for listing open ports)
- Basic Linux tools (`netstat`, `ss`) for testing and comparison

