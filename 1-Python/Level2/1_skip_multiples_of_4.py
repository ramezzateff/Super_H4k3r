#!/usr/bin/python3
# Print all numbers from 1 to 100 except numbers divisible by 4.
i = 0
for i in range(1, 101):
    if i % 4 != 0:
        print(i)
