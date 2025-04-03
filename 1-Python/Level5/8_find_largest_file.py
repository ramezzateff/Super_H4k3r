#!/usr/bin/python3
# Find the Largest File in a Directory
# 	Write a script that scans a directory and finds the largest file.
import os


def find_largest_file(current_dir):

    largest_file = ''
    largest_size = 0
    for root, dirs, files in os.walk(current_dir):  # walk on all path
        for file in files:
            # get path of everyfile and get the size of it
            file_path = os.path.join(current_dir, file)
            file_size = os.path.getsize(file_path)
            if file_size > largest_size:
                largest_size = file_size
    largest_file = file_path
    return largest_file


# get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(find_largest_file(current_dir))
