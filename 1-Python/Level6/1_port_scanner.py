#!/usr/bin/python3
# Use Python’s socket module to scan for
# open ports (range 20-100) on scanme.nmap.org.
import socket

def scan_ports(host_port, start_port, end_port):
	print(f"Scanning Ports on {host_port}...")

	for port in range(start_port, end_port + 1):
		scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		scan.settimeout(1)  # the amount of time the socket
					# waits for data to become available to read
		result = scan.connect_ex((host_port, port))

		if result == 0:
			print(f"Port {port} is open")
		scan.close()  # to close the connection

if __name__ == "__main__":
    target_hosts = input("Enter the host IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    scan_ports(target_hosts, start_port, end_port)