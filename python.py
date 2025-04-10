#!/usr/bin/python3 
'''
1 - socket:For low-level network connections (like pinging an IP, getting the status of a network, etc.).
Useful for network communication, server-client model, etc.
2 - ipaddress:To work with IP addresses, subnetting, CIDR notation, and network calculations.
You can use it to validate IPs, calculate network and broadcast addresses, etc.
3 - subprocess:To run external commands (like ping) within Python.
Useful for tasks like checking if an IP is reachable or performing network scans.
4 - re: For regular expressions to extract IPs from a file or text.
Helps with searching for IP patterns in any given input (e.g., .txt file).
5 - scapy: A powerful library for network packet manipulation and analysis.
Great for tasks like sending pings, scanning networks, and working with raw packet data.
6 - os: For working with file systems (e.g., opening, reading, and writing files to extract IPs or store results).
7 - pandas: If you need to handle or manipulate data in a tabular format (like logs, extracted data from text files, etc.).
8 - requests: If you plan to make web requests (e.g., checking the availability of a server or IP via HTTP/HTTPS).
'''
'''
import ipaddress
# version 4
ip = ipaddress.IPv4Address('192.168.1.1')

# to check if the ip is correct
try:
    ip = ipaddress.IPv4Address('256.256.256.256')  # عنوان خاطئ
except ValueError as e:
    print(f"Error: {e}")

# can handle with the subnets
network = ipaddress.ip_network('192.168.1.0/24')
print(network)
# the beginning and the last never share to anybody
# 192.168.1.0 and 192.168.1.255
print("beginning: ", network.network_address) # beginning: 192.168.1.0
print("Last ip: ", network.broadcast_address) # Last ip: 192.168.1.255

# total ips of the network > .num_addresses
print("Total IPs in network:", network.num_addresses)

# print (netmask, Hostmask)
print("Netmask:", network.netmask)
print("Hostmask:", network.hostmask)

# can check if ip in the network
network = ipaddress.ip_network('192.168.1.0/24')
ip = ipaddress.IPv4Address('192.168.1.100')
print(ip in network)

# to create all possible ips in the network .hosts()
print([str(ip) for ip in network.hosts()])

# cidr notation using .prefixlen()
print(network.prefixlen) # 24


# version 6 like version 4 in everything
ip = ipaddress.IPv6Address('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
print(ip)

#Network 
network = ipaddress.IPv6Network('2001:db8::/32')
print(network)


# next ip
ip = ipaddress.IPv4Address('192.168.1.1')
next_ip = ip + 1
print(next_ip)

# to know if the ip is private of not
print("Is private?", ip.is_private)

# to get the classes of every number manually
first_octet = int(str(ip).split('.')[0])
if 1 <= first_octet <= 126:
    print("Class A")
elif 128 <= first_octet <= 191:
    print("Class B")
elif 192 <= first_octet <= 223:
    print("Class C")
elif 224 <= first_octet <= 239:
    print("Class D (Multicast)")
else:
    print("Class E (Experimental)")

net1 = ipaddress.ip_network('192.168.1.0/24')
net2 = ipaddress.ip_network('192.168.1.0/25')
print(net1.overlaps(net2))  # True if there an overlap
'''

import subprocess
# to run a command .run(' ') , if in windows would be add the shell=true
# can put the all command into a list ['ls', 'lah'] while into run the command and save into a file
# to stretch the output into a one line capture_output=True, and decode the command and didnot run it while you print it
# stdout=subprocess.PIPE that redirect the output into a pipe 
# if i want to add the output into a file 
# with open("output.txt", 'w') as f:
# can check of the command by check=True
# stderr=subprocess.DEVNULL
#p1 = subprocess.run(['ls' ,'-lah', 'dne'], stderr=subprocess.DEVNULL)

p1 = subprocess.run(['cat', 'output.txt'], capture_output=True, text=True)

# to check the args thats run > p1.args or .returncode=0 then it equals to zero error
# .stdout >>None because that is send a standard command and not none if you use text=True
# .stdout.decode() if you want to decode what capture_output did
# .stderr to get the error line
print(p1.stdout.encode()) #CompletedProcess(args='ls -lah', returncode=0)


