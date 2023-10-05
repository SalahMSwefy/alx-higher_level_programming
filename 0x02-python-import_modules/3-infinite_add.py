#!/usr/bin/python3
from sys import argv
sum = 0
for arg in argv:
    if arg != argv[0]:
        sum += int(arg)
print(sum)