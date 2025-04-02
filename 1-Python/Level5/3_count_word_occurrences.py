#!/usr/bin/python3
# Count Word Occurrences in a File
# Read a file and count how many times a given word appears.
import os
# to get the path of  the words_count.txt
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'words_count.txt')

# read the file_name and add the content of the file
# into a content variable
content = ""
with open(file_path, 'r') as file_name:
    for line in file_name:
        content += line

count = content.count('Python')

print(content)
print(f"the word Python repeated {count} times")

'''
Python is an amazing programming language. Python is versatile,
powerful, and easy to learn.
Many developers love Python because it is great for web development,
data science, automation, and more.
Learning Python can open doors to many opportunities
in software development.

Python's syntax is clear and readable.
Python is a popular choice for beginners and experts alike.
Many industries use Python due to its simplicity and efficiency.
Python, Python, Python everywhere!

the word Python repeated 10 times
'''
