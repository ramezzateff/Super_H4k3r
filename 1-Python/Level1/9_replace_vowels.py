#!/usr/bin/python3
# 10. Given password = "P@ssw0rd", replace all vowels with "*".

password = "P@ssw0rd"
vowels = "a@ei0ouAEIOU"
new_password = ""

for char in password:
    if char in vowels:
        new_password += "*"
    else:
        new_password += char

print(new_password)