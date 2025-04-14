#!/usr/bin/python3
# Implement a sorting algorithm (like Bubble Sort)
# 	to sort a list of random numbers without using .sort().
# Store port numbers and their corresponding services in a
# 	dictionary and allow the user to query by port number.
port_dict = {
    80: 'HTTP (Hypertext Transfer Protocol)',
    443: 'HTTPS (HTTP Secure)',
    22: 'SSH (Secure Shell)',
    21: 'FTP (File Transfer Protocol)',
    25: 'SMTP (Simple Mail Transfer Protocol)',
    53: 'DNS (Domain Name System)',
    110: 'POP3 (Post Office Protocol version 3)',
    143: 'IMAP (Internet Message Access Protocol)',
    3389: 'RDP (Remote Desktop Protocol)',
    23: 'Telnet',
}
ask_user_Port = int(input('What port Number to get their services: '))
service = port_dict.get(ask_user_Port)

print(f'Port {ask_user_Port}: {service}')
