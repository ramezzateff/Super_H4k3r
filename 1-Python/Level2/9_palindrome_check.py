#!/usr/bin/python3
# Check if a string is a palindrome (same forward and backward).
# 	first two letters same as last two letters!
palindrome_word = input('Type palindrome_word: ')
if (palindrome_word == palindrome_word[::-1]):
    print(f'{palindrome_word} is Palindrome word')
else:
    print(f'{palindrome_word} is not a Palindrome word.')
