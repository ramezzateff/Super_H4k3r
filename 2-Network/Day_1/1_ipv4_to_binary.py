#!/usr/bin/python3
# Convert an IPv4 address from dotted-decimal to binary format.
# ---
# the format of ipv4 is x.x.x.x
# Ref: https://youtu.be/icldNo6reNY?si=Hm9shIZiwj4yK2JG
# ---
# format(int(part), '08b') binary
# format(int(part), '02d') decimal
# format(int(part), '03o') oct
# format(int(part), '08b') hex

def Ip_to_bin(ip):
	''' Function to convert ip into a binary number'''
	bin_list = []

	ip_list = ip.split('.')
	for part in ip_list:
		
		bin_list.append(format(int(part), '08b'))
		result = '.'.join(bin_list)

	return print(result)



if __name__ == '__main__':

	ip = input('Enter an ipv4 to convert to binary: ')
	Ip_to_bin(ip)