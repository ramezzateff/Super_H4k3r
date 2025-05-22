#!/usr/bin/python3
# Create a script that checks if an IP is reachable by pinging it.
# ref: http://cybrary.it/blog/ping-using-python-script

import subprocess as sub

def Ping_ip(ip):
	'''check output and convert it to str using decode()'''

	output = sub.check_output(['ping', '-c 4', ip]).decode()
	if '0 received' in output:
		print('IP unreachable')
	else:
		print('IP reachable')

if __name__ == '__main__':
	ip = input('Enter ip to ping: ')
	Ping_ip(ip)
