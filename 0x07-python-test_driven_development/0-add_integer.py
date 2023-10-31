#!/bin/usr/python3
"""
This module contains a function that adds two integers.

"""


def add_integer(a, b=98):

    """
    adds two integers

    Args:
        a (int): first integer
        b (int): second integer

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
