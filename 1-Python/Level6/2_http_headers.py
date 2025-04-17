#!/usr/bin/python3
# Write a script that sends an
# HTTP GET request to example.com and prints the response headers.

import requests

req = requests.get('https://www.google.co.uk/')
print(req)
response = req.status_code  # to print the status code.

print(req.headers)  # to print the response headers.
