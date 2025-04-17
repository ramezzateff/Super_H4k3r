#!/usr/bin/python3
# Write a program that takes a domain 
# name and resolves it to an IP address.
import socket

def domain_name(hostname):
	return print(socket.gethostbyname(hostname))

if __name__ == "__main__":
	hostname = input("Put the name to get the ip: ")
	domain_name(hostname)