#!/usr/bin/python3
# Rename All .txt Files to .bak
# Create a script that renames all .txt files in a folder to .bak.
import os

# to get the current dir 
current_dir = os.path.dirname(os.path.abspath(__file__))

# empty string to store the .txt file
list_file = ""
for root, dirs, files in os.walk(current_dir):
    for file in files:
        if file.endswith(".txt"):
        	# replace the old path to new .bak
        	old_path = os.path.join(root, file)
        	new_path = os.path.join(root, file[:-4] + ".bak")

            # add all files .txt to list_file
        	list_file += old_path + '\n' + new_path + '\n'
        	
        	# rename the files
        	os.rename(old_path, new_path)

print(f'the old and new name files :\n {list_file}')
'''
the old and new name files :
/root/Super_H4k3r/1-Python/Level5/b.txt
/root/Super_H4k3r/1-Python/Level5/b.bak
/root/Super_H4k3r/1-Python/Level5/words_coun.txt
/root/Super_H4k3r/1-Python/Level5/words_coun.bak
/root/Super_H4k3r/1-Python/Level5/.txt
/root/Super_H4k3r/1-Python/Level5/.bak
/root/Super_H4k3r/1-Python/Level5/a.txt
/root/Super_H4k3r/1-Python/Level5/a.bak
'''