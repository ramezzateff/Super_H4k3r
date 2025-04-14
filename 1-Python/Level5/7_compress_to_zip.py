#!/usr/bin/python3
# Compress a File into a ZIP Archive
# 	Write a script that compresses a file into a ZIP archive.
import os
import zipfile  # for ziping the file

# to create and write
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'task7.txt')

with open(file_path, 'a') as file_name:
    pass
zip_file_name = 'compress_file.zip'

with zipfile.ZipFile(zip_file_name, 'w') as ZipFile:
    ZipFile.write(zip_file_name, arcname=file_path)
print(f'{file_path} will compress into {zip_file_name}')
