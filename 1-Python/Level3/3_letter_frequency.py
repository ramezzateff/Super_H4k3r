#!/usr/bin/python3
# Write a program that counts
# 	how many times each letter appears in a given string.
text = str(input('Type to counts letters: '))
dict = {}
for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)
