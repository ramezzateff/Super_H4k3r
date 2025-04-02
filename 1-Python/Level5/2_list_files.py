#!/usr/bin/python3
# List All Files in Current Directory
# Write a program that lists all files in the current directory.
import os
# to get the current path
current_dir = os.path.dirname(os.path.abspath(__file__))

# use os.listdir() to list all file in a list
list_dir = os.listdir(current_dir)

print(list_dir)
'''
['0_read_file.py', '9_scan_files_for_keyword.py',
 '5_create_write_read_file.py', '1_log_user_input.py',
'''
'''
'keystroke.log', '6_delete_all_files.py',
 '7_compress_to_zip.py', 'README.md',
 '3_count_word_occurrences.py', '8_find_largest_file.py',
 '2_list_files.py', '4_rename_txt_to_bak.py']
'''
