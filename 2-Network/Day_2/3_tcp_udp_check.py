#!/usr/bin/python3
# Detects whether a given port uses TCP or UDP.

def detect_tcp_udp(port):
	common_ports = {
	22: ('SSH', 'TCP'),
	53: ('DNS', 'TCP/UDP'),
	80: ('HTTP', 'TCP'),
	443: ('HTTPS', 'TCP'),
	67: ('DHCP', 'UDP'),
	123: ('NTP', 'UDP'),
	161: ('SNMP', 'UDP'),
	25: ('SMTP', 'TCP'),
	}
	if port in common_ports:
		service, protocol = common_ports[port]
		print(f"Port {port} is used by {service} over {protocol}")
	else:
		print("Unknown port.")

if __name__ == '__main__':
	port = int(input("Enter a port number: "))
	detect_tcp_udp(port)

