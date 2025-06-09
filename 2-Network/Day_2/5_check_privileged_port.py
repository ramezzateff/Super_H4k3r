#!/usr/bin/python3
# Create a function that tells whether a given port is in the privileged range (0-1023).

def port_check(port_num):
	return f'{port_num} is privileged' if 0 <= port_num <= 1023 else f'{port_num} is not privileged.'


if __name__ == '__main__':
	port_num = int(input(f'Enter a port to check if it is valid: '))
	print(port_check(port_num))