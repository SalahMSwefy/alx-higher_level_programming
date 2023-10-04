#!/usr/bin/python3
def uppercase(str):   
     for c in str:
        char = ord(c)
        if 97 <= char <= 122:
            char -= 32
        print("{}".format(char),end="")
print()
