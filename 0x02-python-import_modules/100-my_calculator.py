#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = argv[1]
    b = argv[3]
    operator = argv[2]
    if operator == '+':
        res = add(int(a), int(b))
        print("{} + {} = {}".format(a, b, res))
    elif operator == '-':
        res = sub(int(a), int(b))
        print("{} - {} = {}".format(a, b, res))
    elif operator == '*':
        res = mul(int(a), int(b))
        print("{} * {} = {}".format(a, b, res))
    elif operator == '/':
        res = div(int(a), int(b))
        print("{} / {} = {}".format(a, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
