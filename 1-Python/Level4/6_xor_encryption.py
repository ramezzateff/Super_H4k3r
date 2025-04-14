#!/usr/bin/python3
# Build a function that performs a simple XOR encryption on text.
# Allow users to specify a key.
from utils import xor_encrypt

print(xor_encrypt("Hello", 123))
# output: Encrypted Text: b'\x1b\x0b\x10\x10\x0b'
