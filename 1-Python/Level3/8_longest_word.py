#!/usr/bin/python3
#  Given a list of words, determine which word is the longest.
def longest_word(words):
    if not words:
        return None

    longest = words[0]
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest


word_list = ["apple", "banana", "cherry", "blueberry", "kiwi", "pear"]
longest = longest_word(word_list)
print(word_list)
if longest:
    print(f"The longest word is: {longest}")
else:
    print("The list is empty.")
