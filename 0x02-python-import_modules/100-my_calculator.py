#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == '+':
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
        elif operator == '-':
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res))
        elif operator == '*':
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
        elif operator == '/':
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
