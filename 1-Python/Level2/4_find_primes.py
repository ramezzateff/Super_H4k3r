#!/usr/bin/python3
# Find prime numbers between 1 and 100.
# A prime number is a number that is only divisible by 1 and
# 	itself and the total number of divisors is 2.
for i in range(2, 101):  # Loop from 2 to 101 (not 0 to 100)
    summing_num = True  # Initialize divisor count
    for j in range(2, i):  # Start checking for divisors from 2 up to i
        if i % j == 0:  # If i is divisible by j
            summing_num = False  # Increment divisor count
            break
    # After the loop, check if summing_num is 0 (indicating that it's prime)
    if summing_num:
        print(f'{i} is a prime number')
