#!/usr/bin/python3
# Create a simple Python program with
# a client and a server that communicate over TCP sockets.

# server >> execute at first and wait for any client req
# then sever responce to client request, 
# the conversation will end if user enters 'bye' 
# ref: https://realpython.com/python-sockets/

import socket
import subprocess

def server():
	# Create a TCP/IP socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		# bind is used to connect server add to localhost
		server.bind(('127.0.0.1', 5200))
		# listen for incoming connection 
		server.listen(1)
		print('Server is listening..')

		connection, client_addr = server.accept()
		print(f"Connected to {client_addr}")

		with connection: # to close the server when client log out
			while True:
				data = connection.recv(1024)
				if not data:
					break

				message = data.decode()
				print(f'Client says: {message}')

				connection.send('the message is sent! '.encode())

				if message.lower() == 'bye':
					#connection.sendall(data)
					break


def client():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
		server.connect(('127.0.0.1', 5200))
		while True:
			message = input("message is send to server: ")
			server.send(message.encode())

			# always wait for server reply
			data = server.recv(1024)
			print(f"Server replied: {data.decode()}")

			if message.lower() == 'bye':
				break

if __name__ == '__main__':
    role = input("Enter 's' for server or 'c' for client: ").strip().lower()
    if role == 's':
        server()
    elif role == 'c':
        client()
    else:
        print("Invalid input.")