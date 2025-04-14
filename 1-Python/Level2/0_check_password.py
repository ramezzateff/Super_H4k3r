#!/usr/bin/python3
# Write a script that asks for a password and
#     only allows access if it matches "s3cr3t".

passowrd = input("WHat is your password? ")
if passowrd == 's3cr3t':
    print('Your password is correct!')
else:
    print('your password is incorrect!!')