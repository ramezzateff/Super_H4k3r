#!/usr/bin/python3
# Write a script that checks whether a website is online or down.
import requests
import socket

def check_web(hostname):
    # Strip protocol (http:// or https://) from the hostname if present
    if hostname.startswith(('http://', 'https://')):
        hostname = hostname.split('//')[-1]

    # Check if the domain name resolves to an active IP
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror as e:
        print(f"!!! Temporary failure in name resolution for {hostname} !!!")
        return  # Exit if DNS resolution fails

    # Try connecting to https:// first
    try:
        req = requests.get('https://' + hostname)  # Trying to connect with https
        print(f"{hostname} is working on https!")
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        # If https fails, try connecting with http
        try:
            req = requests.get('http://' + hostname)  # Trying to connect with http
            print(f"{hostname} is working on http!")
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            print(f"{hostname} did not work")
            return  # Exit if both connections fail

    # If the status code is between 200 and 400, the website is working
    if (200 <= req.status_code < 400):
        print(f"{hostname} is working !!!")
    else:
        print(f"{hostname} did not work")

if __name__ == "__main__":
    hostname = input("Enter the website name to check if it's working: ")
    check_web(hostname)
