#!/usr/bin/python3
# Write a Python script that validates
# whether a given IP address is IPv4 or IPv6.
# >>> need to get an input from user and valid ip
#  a.b.c.d < {ipv4} &ipv6 > x:x:x:x:x:x:x:x

import re
ip_take_from_user = input('Enter the ip to check if it valid: ')
print(type(ip_take_from_user))