#!/usr/bin/python3
# Scan Files for a Specific Keyword
# Write a script that scans a directory
# for files containing a specific keyword.

import os

def find_keyword(keyword):
    for roots, dirs, files in os.walk(current_dir):
        for file in files:
            filepath = os.path.join(roots, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    if keyword in content:
                        print(f"Keyword found in {filepath}")
            except (IOError, UnicodeDecodeError) as e:
                print(f"Could not open file {filepath}: {e}")

current_dir = os.path.dirname(os.path.abspath(__file__))
keyword = input('Write the word to search in all files: ')
find_keyword(keyword)