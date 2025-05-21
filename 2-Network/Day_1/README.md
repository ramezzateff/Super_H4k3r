# 🔥 Day 1: IP Addresses & Subnetting

Welcome to Day 1 of our networking and Python scripting journey! This day focuses on understanding IP addresses, subnetting, and the basics of networking protocols.

---

## 📘 Topics Covered
- IP Basics (IPv4 & IPv6)
- Subnetting & CIDR Notation
- Network Calculations

---

| Day 1                         | Python Tools/Libraries     | Concepts Learned                                 |
| ----------------------------- | -------------------------- | ------------------------------------------------ |
| 01. String format Validate IP | `ipaddress`, `re`          | IP formats                                       |
| 02. IP to Binary              | `split`, `format`, `bin`   | Bitwise understanding<br>String formatting       |
| 03. Extract IPs               | `re`, `file handling`      | Pattern matching<br>Regex + File parsing         |
| 04. Private IP Check          | `ipaddress`                | IP ranges                                        |
| 05. Network/Broadcast         | `ipaddress.ip_network()`   | Subnetting<br>Network calculation                |
| 06. All IPs in Subnet         | `.hosts()`                 | IP iteration<br>Subnetting ranges                |
| 07. Ping IP                   | `subprocess`               | Network reachability<br>System command execution |
| 08. IPv6 Compress/Expand      | `.compressed`, `.exploded` | IPv6 structure                                   |
| 09. IP Class                  | `int`, `if` statements     | IP classification                                |
| 10. Same Subnet               | `ip_network`, comparisons  | Network comparison<br>Binary subnet masking      |

## 🔹 Exercises

Each task is paired with its own dedicated Python file to help keep everything organized.

✅ 1. Validate IP Address Format:
- Description: Write a script that checks whether a given IP address is in IPv4 or IPv6 format.
- File: `0_validate_ip.py`

✅ 2. IPv4 to Binary:
- Description: Convert an IPv4 address from dotted-decimal to binary.
- File: `1_ipv4_to_binary.py`

✅ 3. Extract IPs from File:
- Description: Scan a text file and extract all IP addresses found.
- File: `2_extract_ips.py`

✅ 4. Check Private IP:
- Description: Write a function to check if an IP belongs to a private network (e.g., 192.168.x.x, 10.x.x.x).
- File: `3_check_private_ip.py`

✅ 5. Network & Broadcast Address:
- Description: Given an IP and subnet mask, calculate the network and broadcast addresses.
- File: `4_network_and_broadcast.py`

✅ 6. Generate Subnet IPs:
- Description: Generate all possible IPs within a subnet like 192.168.1.0/24.
- File: `5_generate_ips.py`

✅ 7. Ping an IP Address:
- Description: Script to ping an IP and check its availability.
- File: `6_ping_ip.py`

✅ 8. IPv6 Conversion:
- Description: Convert an IPv6 address into its compressed and expanded forms.
- File: `7_ipv6_conversion.py`

✅ 9. Determine IPv4 Class:
-Description: Function that returns the class (A, B, C, D, E) of a given IPv4 address.
- File: `8_ipv4_class.py`

✅ 10. Check Same Subnet:
Description: Given two IPs, determine whether they belong to the same subnet.
- File: `9_same_subnet.py`

---

## 🛠️ How to Run a Script

> python3 0_validate_ip.py

Replace the filename accordingly for each task.

---

🤖 Happy Networking! 🌐