#!/usr/bin/python3
# Implement a basic TCP port scanner using Python’s socket module.

# tcp act as a call u must to call and the other person accept the call then complete the call
# 3 - way Handshake 
'''
1. Client : SYN - i want to start a call
2. server: SYN-ACK - Yes, iam ready
3. Client: ACK - okay, start connection

to scan tcp using nmap
nmap -sT ip -p-
	-sT: TCP connect Scan

using socket module
range ports
create a socket and settimeout
'''
import socket


def tcp_scanner(ip):
	open_ports = []
	for port in range(1,100):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(1)

		result = sock.connect_ex((ip, port))
		if result == 0:
			open_ports.append(port)
			print(f'PORT {port}: OPEN')
		sock.close()
	

if __name__ == '__main__':
	ip = input('Enter ip: ')

	tcp_scanner(ip)