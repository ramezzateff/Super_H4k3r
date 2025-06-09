#!/usr/bin/python3
# List Common Ports & Services – e.g., 80 → HTTP, 443 → HTTPS

# https://blog.netwrix.com/common-ports

common_ports = {
	20  : 'FTP (Data Transfer)',
	21  : '(TCP, UDP) – FTP (File Transfer Protocol)',
	22  : '(TCP, UDP) – SSH (Secure Shell)',
	23  : '(TCP) – Telnet',
	25  : '(TCP) – SMTP (Simple Mail Transfer Protocol)',
	53  : '(TCP, UDP) – DNS (Domain Name System)',
	80  : '(TCP) – HTTP (Hypertext Transfer Protocol)',
	110 : '(TCP) – POP3 (Post Office Protocol version 3)',
	143 : '(TCP, UDP) – IMAP (Internet Message Access Protocol)',
	443 : '(TCP) – HTTPS (HTTP Secure)',
	445 : '(TCP) – SMB (Server Message Block)',
	993 : '(TCP, UDP) – IMAPS (IMAP over SSL)',
	995 : '(TCP, UDP) – POP3S (POP3 over SSL)',
	3306: '(TCP) – MySQL database system',
	3389: '(TCP) – RDP (Remote Desktop Protocol)',
	8080: '(TCP) – Alternative HTTP port, often used for web proxies'
}

print(f'Common Port and Services: ')

for key, value in common_ports.items():
	print(f'{key}: {value}')
