#!/usr/bin/python3
# Create a script that prints every 4-digit PIN code (0000-9999)
array = []

for i in range(10000):
    array.append(f'{i:04}')

print(*array)
