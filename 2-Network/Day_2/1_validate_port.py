#!/usr/bin/python3
# checks if a given port number is valid (0-65535).

def port_check(port_num):
	return f'{port_num} is valid' if 0 <= port_num <= 65535 else f'{port_num} is not valid.'


if __name__ == '__main__':
	port_num = int(input(f'Enter a port to check if it is valid: '))
	print(port_check(port_num))