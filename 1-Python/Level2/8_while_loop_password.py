#!/usr/bin/python3
# Use a while loop to continuously ask for a password
# 	until the correct one is entered.
password = 'abc123'
while (True):
    asked_password = input('Enter Your Passwrod: ')
    if (asked_password == password):
        print('Enter now')
        break
    else:
        print('You entered the incorrect password, Try Again!')
