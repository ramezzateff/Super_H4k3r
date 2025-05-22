#!/usr/bin/python3
'''Write a function that checks
 	if an IP belongs to a private network.
check if ip start with (192.168.x.x, 10.x.x.x, 17.16.x.x-17.31.x.x)
 	and be x.x.x.x
'''
import ipaddress

def check_valid_ip(ip):
	'''Check if ip is valid or not
	Args: 
		ip(str): The Ip addres to validate

	Return: Ture if valid, False if not
	'''
	try:
		ipaddress.ip_address(ip)
		return True
	except ValueError:
		return False


def is_private_ip(ip):
	'''Check if IP address is private.

	Args:
		ip (str): The ip address to check

	Returns:
		bool or str: True if private, False if not
			or Error message of invalid ip format
	'''
	if not check_valid_ip(ip):
		'''Check the validity of ip'''
		return 'Invalid IP Frmat, must be x.x.x.x'


	if ip.startswith('10.'):
		return True 
	elif ip.startswith('192.168'):
		return True
	elif ip.startswith('172'):
		second_num = int(ip.split('.')[1])
		if 16 <= second_num <= 31:
			return True
		else:
			return 'IP address must be 172.16.x.x to 172.31.x.x'
	else:
		return 'False, This Ip not a private ip'


if __name__ == '__main__':
	ip_input = input('Enter Ipaddress: ')
	print(is_private_ip(ip_input))