#!/usr/bin/python3
# script that finds all listening ports on your local machine (127.0.0.1)

# using netstat -tunlp, nmap -p- , ss then filter to get only what on (127.0.0.1)

import subprocess as sub
import re



def listen_port(ip):
    """
    Scans all ports on the given IP using nmap,
    extracts open port numbers (TCP or UDP) using regex,
    and returns them as a list.


    Args:
        ip (str): IP address to scan.

    Returns:
        list: A list of open port numbers as strings, or a message if none found.
    """
    # Run the netstat command and get output
    ports = sub.run(['netstat', '-tunlp'], capture_output=True, text=True).stdout

    # Use regex to extract protocol and port from lines with 'LISTEN'
    matches = re.findall(r'127\.0\.0\.1:(\d+)', ports)

    return f'The listening ports is {matches}' if matches else ["No listening ports found."]



if __name__ == '__main__':
	print(listen_port('127.0.0.1'))