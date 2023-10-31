#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size: the size of square

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        if size == 0:
            print()
        else:
            for i in range(size):
                print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
