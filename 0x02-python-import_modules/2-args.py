#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        n = len(sys.argv)
        print("{} arguments:".format(n-1))
        for i in range(n):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
