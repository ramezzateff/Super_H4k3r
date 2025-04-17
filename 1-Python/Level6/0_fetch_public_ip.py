#!/usr/bin/python3
# Write a script that fetches and prints
# your public IP address using an external API.

import requests

ip = requests.get('https://api.ipify.org/').content.decode('utf8')
print(f"My Public IP address: {ip}")
