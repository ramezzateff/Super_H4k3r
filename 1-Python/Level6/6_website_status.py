#!/usr/bin/python3
# Write a script that checks whether a website is online or down.
import requests
import socket

def check_web(hostname):
    # Strip protocol (http:// or https://) from the hostname if present
    if hostname.startswith(('http://', 'https://')):
        hostname = hostname.split('//')[-1]

    # Dns Resolution
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"!!! DNS resolution failed for {hostname} !!!")
        return  # Exit if DNS resolution fails

    # Try https first
    for protocol in ['https://', 'http://']:
        try:
            url = protocol + hostname
            req = requests.get(url, timeout=5)
            if 200 <= req.status_code < 400:
                print(f"{hostname} is online via {protocol.split('://')[0]} (status: {req.status_code})")
                return
            else:
                print(f"{hostname} responded with status code {req.status_code} via {protocol}")
                return
        except (requests.exceptions.RequestException) as e:
            continue

    print(f"{hostname} is down or unreachable via both https and http")


if __name__ == "__main__":
    hostname = input("Enter the website name to check if it's working: ")
    check_web(hostname)
