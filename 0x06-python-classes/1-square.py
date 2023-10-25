#!/usr/bin/python3
"""define a class Square"""


class Square:
    """"
    Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    """
    def __init__(self, size):
        """
        instantiation with size (no type/value verification)

        Args:
            size (int): size of square (private)
        """
        self.__size = size
