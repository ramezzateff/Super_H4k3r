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

| Function / Class | Description |
|------------------|-------------|
| `ip_address()`        | Creates an `IPv4Address` or `IPv6Address` object (e.g., `192.168.1.1`).    |
| `ip_network()`        | Create and manipulate an IP network/subnet (e.g., `"10.0.0.0/8"`). Supports `strict=False` for host bits. |
| `ipaddress.ip_interface()` | Represents a host IP address with its network info. |
| `subnets()`           | Divides a network into smaller subnets (prefixlen_diff=N).                  |
| `is_private`          | `True` if IP is in RFC 1918 ranges (e.g., `172.16.0.0/12`).               |
| `.is_global` | Returns `True` if IP is publicly routable. |
| `.hosts()` | Lists all usable host IPs in a network. |
| `is_loopback`         | Checks for `127.0.0.0/8` (IPv4) or `::1` (IPv6).                          |
| `.supernet()` / `.subnets()` | Increase/decrease subnet size. |
| `in` operator | Check if an IP is part of a subnet (`ip in network`). |
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
    # 203.0.113.1
    # 203.0.113.2


# Subnet splitting
large_net = ipaddress.ip_network("192.168.0.0/16")
print("\nFirst 5 /24 subnets:") # Output: 203.0.113.6
for subnet in large_net.subnets(prefixlen_diff=8):
    print(subnet)
    if subnet.prefixlen == 24:  # Stop after 5 examples
        First 5 /24 subnets:
        # 192.168.0.0/24
        # 192.168.1.0/24
        # 192.168.2.0/24
        # 192.168.3.0/24
        # 192.168.4.0/24
        break
```


## 5. Practical Notes
- Validation: Use `strict=True` (default) to reject host bits in networks (e.g., `192.168.1.1/24` raises an error).
- Memory Efficiency: `hosts()` returns a generator—convert to `list()` if reuse is needed.
- IPv6 Support: Works transparently (e.g., `ip_address("2001:db8::1")`).
Compatibility: Converts to/from strings (`str(ipaddress.IPv4Address('192.168.1.1'))`).

## 6. Related Domains
|Field          | How ipaddress Helps|
|---------------|--------------------|
|Cybersecurity:   |Identify IP ranges, automate private/public classification.|
|Networking:      |Manage subnets, route calculations, broadcast/network addressing.|
|Automation:      |Build tools for IP validation, bulk filtering, CIDR calculations.|
|Cloud/DevOps:    |Handle IP blocks and access control in cloud configurations.|

## ✅ Summary
The `ipaddress` module is a powerful and built-in tool to work with IPs and networks in Python. Whether you're writing a scanner, subnetting tool, or validating input — it's a must-know for network-aware scripts. """