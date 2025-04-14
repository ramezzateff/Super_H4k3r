#!/usr/bin/python3
# 9. Print "H4ck3r" with alternating uppercase and lowercase letters.
text = 'H4ck3r'   
flipped = ''
for char in text:
	if char.islower():
		flipped += char.upper()
	elif char.isupper():
		flipped += char.lower()
	else:
	    flipped +=char  # to get any num or speciacl char the same
print(flipped)