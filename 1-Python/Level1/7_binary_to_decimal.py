#!/usr/bin/python3
# 8. Convert the string "100101" to a decimal number.
# method 1
num1 = int(input('Enter your binary number: '))
decimal, i = 0, 0
while num1 > 0:  # 100101 > 0
    reminder = num1 % 10  # 100101 % 10 = 1
    exponential = reminder*(2 ** i)  # 1 * 2**0 > 1
    decimal = decimal + exponential  # 0 + 1
    num1 = num1 // 10  # 10010
    i += 1
print(f"Decimal Number: {decimal}")

# method 2 BUiltin Function
num1 = input('Enter your binary number: ')
decimal = int(num1, 2)
print(f"Decimal Number: {decimal}")
