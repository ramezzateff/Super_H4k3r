#!/usr/bin/python3
# Implement a script that finds live hosts on a local network
# nmap with -sn without ping
# then split all lines
# search for each line for the ip.

import subprocess
import re

def live_hosts(subnet):
	nmap_scan = subprocess.run(['nmap', '-sn', subnet], capture_output=True, text=True)
	split_scan_into_lines = nmap_scan.stdout.splitlines()  # put all output in a list

	# search for the live host from the list
	for line in split_scan_into_lines: 
		if 'Nmap scan report for' in line:
			match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
			if match: # if match = None it will reflect an error
				print(f"Live Host: {match.group()}") 

if __name__=="__main__":
	subnet = '192.168.1.0/24'
	live_hosts(subnet)