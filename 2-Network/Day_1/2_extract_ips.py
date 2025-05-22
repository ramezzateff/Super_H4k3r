#!/usr/bin/python3
# Extract all IP addresses from a text file.

import os
import re

# to create and write
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'task2.txt')

# empty list to list the extract ip
ip_list = []

# pattern of regex.
pattern = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
          r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
          r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\." \
          r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

# create and read in the file
with open(file_path, 'r') as file_read:
	for line in file_read:
		
		ip_list = (re.findall(pattern, line))
		print(ip_list)
		