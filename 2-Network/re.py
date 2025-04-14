#!/usr/bin/python3 

import re

# re.search() if not : return None
txt = "My name is Ramez"
result = re.search("Ramez", txt)
if result:
    print("Found!")

# re.match()
re.match("My", "My name is Ramez")  # feh 
re.match("name", "My name is Ramez")  # not


# re.findall() : return all u search for in a list
txt = "cat, dog, cat, bird"
animals = re.findall("cat", txt)
print(animals)  # ['cat', 'cat']

# re.sub() change string into another
txt = "I love apples"
new_txt = re.sub("apples", "bananas", txt)
print(new_txt)  # I love bananas

# re.split() split the text
txt = "one-two-three"
parts = re.split("-", txt)
print(parts)  # ['one', 'two', 'three']



# ==== 🔤 REGEX SYMBOLS ====

# .       Any character except newline
# \d      Digit (0-9)
# \D      Not a digit
# \w      Word character (letter, digit, underscore)
# \W      Not a word character
# \s      Whitespace (space, tab, newline)
# \S      Not a whitespace
# ^       Start of string
# $       End of string
# [...]   Match any character inside brackets
# [^...]  Match any character NOT inside brackets
# *       0 or more times
# +       1 or more times
# ?       0 or 1 time (optional)
# {n}     Exactly n times
# {n,}    At least n times
# {n,m}   Between n and m times
# |       OR
# (...)   Group and capture
# (?:...) Group but don’t capture
# \       Escape special characters

# ==== 🧪 PRACTICAL EXAMPLES ====

# ✅ Validate IPv4
ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
ip = '192.168.0.1'
if re.match(ip_pattern, ip):
    print("Valid IPv4")

# ✅ Validate Email
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email = 'example@mail.com'
if re.match(email_pattern, email):
    print("Valid email")

# ✅ Validate Strong Password (min 8 chars, 1 letter, 1 digit)
password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
password = 'pass1234'
if re.match(password_pattern, password):
    print("Strong password")

# ✅ Extract all numbers from a string
text = "Room 12, Floor 3, Code 987"
numbers = re.findall(r'\d+', text)
print("Numbers found:", numbers)  # ['12', '3', '987']