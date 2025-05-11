#!/usr/bin/python3
# Generate 10 fake but realistic-looking email addresses.
import random

def random_email():
	names = ['admin', 'security', 'ahmed', 'ramez', 'sawsan', 'aly']
	domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'email.com']
	emails = []
	for i in range(0, 10):
		name = random.choice(names)
		num  = random.randint(0,999)
		domain = random.choice(domains)
		email = f'{name}{num}@{domain}'
		emails.append(email)
	value = 0
	for value in emails:
		print(value)
	return 0
if __name__ == '__main__':
	random_email()