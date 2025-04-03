#!/usr/bin/python3
# Read and Print File Contents
# Write a script that reads a file and prints its contents.
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

# add the filename to the directory path
myfile_path = os.path.join(current_dir, '4_rename_txt_to_bak.py')

myfile = open(myfile_path, 'r')

for line in myfile:
    print(line)

myfile.close
