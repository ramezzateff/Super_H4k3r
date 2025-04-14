#!/usr/bin/python3
# Check if a given year is a leap year.
# 	leap year is a year can divisable by 4 and 100 and 400
leap_year = int(input("put a year to check if it a leap year or not: "))
if (leap_year % 4 == 0 and leap_year % 100 == 0) or (leap_year % 400 == 0):
    print(f"{leap_year} is a leap year")
else:
    print(f"{leap_year} is not a leap year")
