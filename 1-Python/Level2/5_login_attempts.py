#!/usr/bin/python3
# Simulate a login attempt system that locks after 3 failed attempts.
print('Enter correct username and password to get access ')
username = 'ramez@gmail.com'
password = 'test'
count = 0
while (count < 3):
    username = input('Enter username: ')
    password = input('Enter password3')

    if username == 'ramez@gmail.com' and password == 'test':
        print('Access granted')
        break
    else:
        print('Access Denied , Try Again!')
        count += 1
