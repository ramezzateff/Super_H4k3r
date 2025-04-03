#!/usr/bin/python3
# Create a script that logs user input to a file (keystroke.log).
import os

# add the dir and create file .log to dir
current_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir, 'keystroke.log')

# open the file
log_file = open(log_file_path, 'w')

print("Type exit to stop logging\n")

# take input and add to the file .log
while 1:
    user_input = input('Enter Input: ')
    if user_input == 'exit':
        break
    log_file.write(user_input + '\n')

print(log_file_path)
