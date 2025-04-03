#!/usr/bin/python3
# Create, Write, and Read a File
# Write a script that creates a new text file,
# writes a message to it, and then reads it.
import os

# to create and write
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'task5.txt')

# create and write to the file
with open(file_path, 'w') as file_write:
    file_write.write('Hello!\n')
# file_write_close() == with function

# read from the file
with open(file_path) as file_read:
    for line in file_read:
        print(line, end="")  # Avoids extra newline
