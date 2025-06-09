#!/usr/bin/python3
# script that scans the first 1000 ports of a given IP to see if they are open.


import subprocess as sub
import re


def scan_port(ip):
	'''
	Scans the target IP using nmap to identify open ports.
	Returns The PORT/STATE/SERVICE table or a message if no ports are found. (using Regex)
	'''

	# Run nmap and get the text output
	op = sub.run(['nmap', ip], capture_output=True, text=True)
	output = op.stdout # get the text output from nmap

	# Use regex to extract the table section that starts with
	# "PORT" and ends before "Nmap done"
	match = re.search(r'PORT[\s\S]*?(?=\nNmap)', output) 

	return match.group() if match else "No open ports found."


if __name__ == '__main__':

    # Ask the user to enter the target IP address
    ip = input('Enter IP to scan: ')
    print(scan_port(ip))