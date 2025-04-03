#!/usr/bin/python3
# Delete All Files in a Directory
# 	Make a Python script that deletes all files in a directory.
import os

# get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a new path for a new folder named 'task6'
new_folder_path = os.path.join(current_dir, 'task6')

# Check if the folder exists; if not, create it, using mkdir(), makedirs()
if not os.path.isdir(new_folder_path):
    os.makedirs(new_folder_path)

# change dir: /Super_H4k3r/1-Python/Level5/task6
change_dir = os.chdir(new_folder_path)

new_file = []
print('Write "Stop" if you want to stop making files')

while True:
    name_file = input('Type your File Name to create: ')
    if name_file.lower() == 'stop':
        break
    with open(name_file, 'a'):
        pass
    new_file.append(name_file)

# List all files in the directory
list_files_in_folder = os.listdir(new_folder_path)

print("\nThe files created are: " + ', '.join(new_file))
print("All files in the directory are: " + str(list_files_in_folder))

# Remove files
for file in list_files_in_folder:
    os.remove(file)

print('\nDirectory after deletion:', os.listdir(new_folder_path))
