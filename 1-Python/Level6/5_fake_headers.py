#!/usr/bin/python3
# Create a program that mimics different
# browser user-agents by sending fake headers in a request.
## make a list of user-agents, search for user-agent of mac wind linux,etc .., for loop that send a header request
## headers in get request must use a dict not a list
# https://www.zenrows.com/blog/python-requests-user-agent#set-user-agent
## from the list using random library

import random
import requests

user_agent = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15',
'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/33.0',
]
for i in user_agent:
	header = random.choice(user_agent)
	print('sent this Response Header: ')
	print(header)
	response = requests.get('https://httpbin.org/headers', headers={'User-Agent': header})
	print('and this is the jason format: ')
	print(response.json())
	print('-----------------------')

