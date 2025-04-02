#!/usr/bin/python3
import re
import random
import string
import hashlib
import ipaddress
import uuid
import socket


def reverse_string(string):
    '''
    Reverses a given string.
    using slicing string
    '''
    return string[::-1]


def is_strong_password(string):
    '''
    Validates if a password meets security criteria.
    check for len, letters, strings
    using regex module
    '''
    if len(string) < 8:
        return False
    elif not re.search(r'\d', string):
        return False
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', string):
        return False
    return True


def generate_random_password():
    '''
    Write a function that generates a random password of 12 characters.
    Include uppercase, lowercase, numbers, and special characters.
    '''
    length = 12  # length for password
    characters = string.ascii_letters + string.digits + string.punctuation
    return (''.join(random.choice(characters) for i in range(length)))


def md5_hash(password):
    '''
    Use the hashlib module to create ant MD5 hash of a user-entered string.
    must be encode the password before hashing
    '''
    message = password.encode()
    md5 = hashlib.md5(message).hexdigest()
    return md5


def validate_ip(number):
    '''
    checks if an IP address is valid (IPv4 format).
    '''
    try:
        ip = ipaddress.ip_address(number)
        return bool(ip)
    except ValueError:
        return False


def generate_mac_address():
    '''
    function that generates a random MAC address.
    '''
    # Generate 11 random hexadecimal digits
    digits = [random.choice('0123456789ABCDEF') for _ in range(11)]

    # Add an even hexadecimal digit for the second character
    second_digit = random.choice('02468ACE')
    digits.insert(1, second_digit)

    # Format the digits into a valid MAC address format
    mac_address = ':'.join(''.join(digits[i:i+2]) for i in range(0, 12, 2))

    return mac_address


def xor_encrypt(text, key):
    '''
    Build a function that performs a simple XOR encryption on text.
    Allow users to specify a key.
    '''
    encrypted_text = []
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_text += encrypted_char

    return encrypted_text


def generate_device_id():
    '''
    generate a random device ID.
    '''
    return uuid.uuid4()


def resolve_hostname(hostname):
    '''
    function that takes a hostname and
    resolves it to an IP address.
    '''
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Hostname could not be resolved"


def extract_vowels(text):
    '''
    function that extracts all vowels from text.
    '''
    vowels = 'aeiuoAEIUO'
    return ''.join([char for char in text if char in vowels])
