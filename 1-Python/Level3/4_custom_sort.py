#!/usr/bin/python3
# Implement a sorting algorithm (like Bubble Sort)
#   to sort a list of random numbers without using .sort().

nums = input("Enter numbers separated by space: ").split()
numbers = [int(n) for n in nums]

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)