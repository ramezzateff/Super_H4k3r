#!/usr/bin/python3
# Write a script that takes a list of IP addresses
# and pings each one, reporting whether they are reachable.

import subprocess

def ping_ip(ips):
	for ip in ips:
		ping = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
		if ping.returncode != 0:
			print(f"Failed to ping {ip} ")
			print(ping.stderr)
		else:
			print(f"The ping of {ip} is Success!!!")
			print('-----')
			
if __name__ == "__main__": 
	ips = input('Enter a list of ip to ping: ').split(',')
	print(f"{ips} will be ping")
	ping_ip(ips)