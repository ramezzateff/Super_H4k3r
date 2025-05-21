#!/usr/bin/python3
# Write a Python script that validates
# whether a given IP address is IPv4 or IPv6.
# >>> need to get an input from user and valid ip
#  a.b.c.d < {ipv4} &ipv6 > x:x:x:x:x:x:x:x

# Ref: https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/

import ipaddress

def check(ip):
	try:
		ipaddress.ip_address(ip)
		print('valid ip address')
	except ValueError:
		print("Invalid IP address")

if __name__ == '__main__':
	ip_take_from_user = input('Enter the ip to check if it valid: ')
	check(ip_take_from_user)