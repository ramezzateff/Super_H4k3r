#!/usr/bin/python3
# List all reserved ports (1-1023) that are commonly used in hacking.

common_hacking_ports = {
    21: "FTP - File Transfer Protocol",
    22: "SSH - Secure Shell",
    23: "Telnet - Remote Login (Not Secure)",
    25: "SMTP - Email Sending",
    53: "DNS - Domain Name System",
    80: "HTTP - Web (Unsecured)",
    88: "Kerberos - Authentication",
    110: "POP3 - Email Receiving",
    123: "NTP - Network Time Protocol",
    143: "IMAP - Email Management",
    161: "SNMP - Network Monitoring",
    389: "LDAP - Directory Service",
    443: "HTTPS - Secure Web",
    445: "SMB - Windows File Sharing",
    2049: "NFS - Network File System",
    3306: "MySQL - Database",
    3389: "RDP - Remote Desktop Protocol",
    5432: "PostgreSQL - Database",
    5900: "VNC - GUI Remote Control",
    9200: "Elasticsearch - API Search Engine",
    6379: "Redis - In-memory DB",
    27017: "MongoDB - NoSQL Database",
}
print(f'Common Port and Services: ')

for key, value in common_hacking_ports.items():
	print(f'{key}: {value}')
