# Python `ipaddress` Module Guide

## 1. Simple Definition  
The `ipaddress` module provides tools for creating, manipulating, and operating on **IPv4 and IPv6 addresses and networks**. It simplifies tasks like:
- Validating IP addresses  
- Checking subnet membership  
- Iterating through IP ranges  
- Splitting/merging networks  

---

## 2. Real-world Use Cases  
- **Network Security**: Blocking IP ranges or checking if an IP is in a whitelist.  
- **Cloud Automation**: Managing AWS/GCP firewall rules programmatically.  
- **DevOps**: Validating CIDR blocks in Terraform/Ansible scripts.  
- **Web Apps**: Geo-IP filtering or rate-limiting by subnet.  

---

## 3. Core Functions/Classes  

| Method/Property       | Description                                                                 |
|-----------------------|----------------------------------------------------------------------------|
| `ip_address()`        | Creates an `IPv4Address` or `IPv6Address` object (e.g., `192.168.1.1`).    |
| `ip_network()`        | Defines a network (e.g., `"10.0.0.0/8"`). Supports `strict=False` for host bits. |
| `hosts()`             | Generator for usable IPs in a network (skips network/broadcast addresses).  |
| `subnets()`           | Divides a network into smaller subnets (prefixlen_diff=N).                  |
| `is_private`          | `True` if IP is in RFC 1918 ranges (e.g., `172.16.0.0/12`).               |
| `is_loopback`         | Checks for `127.0.0.0/8` (IPv4) or `::1` (IPv6).                          |
| `with_netmask`        | Returns IP + netmask (e.g., `"192.168.1.1/255.255.255.0"`).               |

---

## 4. Code Example  

```python
import ipaddress

# Check if IP is in a private range
ip = ipaddress.ip_address("10.5.2.99")
print(f"Is {ip} private? {ip.is_private}")  # Output: True

# Iterate through a /29 subnet
network = ipaddress.ip_network("203.0.113.0/29")
print("Usable IPs in network:")
for host in network.hosts():
    print(host)

# Subnet splitting
large_net = ipaddress.ip_network("192.168.0.0/16")
print("\nFirst 5 /24 subnets:")
for subnet in large_net.subnets(prefixlen_diff=8):
    print(subnet)
    if subnet.prefixlen == 24:  # Stop after 5 examples
        break
        ```
Is 10.5.2.99 private? True
Usable IPs in network:
203.0.113.1
203.0.113.2
...
203.0.113.6

First 5 /24 subnets:
192.168.0.0/24
192.168.1.0/24
...
192.168.4.0/24

## 5. Practical Notes
Validation: Use `strict=True` (default) to reject host bits in networks (e.g., `192.168.1.1/24` raises an error).
Memory Efficiency: `hosts()` returns a generator—convert to `list()` if reuse is needed.
IPv6 Support: Works transparently (e.g., `ip_address("2001:db8::1")`).
Compatibility: Converts to/from strings (`str(ipaddress.IPv4Address('192.168.1.1'))`).

## 6. Related Domains
Cybersecurity: Scan for rogue IPs in logs (`if ip in blacklisted_network`).
Data Engineering: Aggregate IPs by subnet in PySpark/pandas.
Automation: Bulk-update firewall rules (AWS Security Groups, iptables).
IoT: Validate device IPs before granting network access.