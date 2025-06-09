#!/usr/bin/python3
# Randomly generate 5 open ports between 1024-65535.

import random

port = random.sample((range(1024, 65535)), 5)
print(f'5 Open Ports is {port}')