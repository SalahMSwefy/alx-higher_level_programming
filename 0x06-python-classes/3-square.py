#!/usr/bin/python3
"""define a class Square"""


class Square:
    """"
    Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    """
    def __init__(self, size=0):
        """
        instantiation with size (no type/value verification)

        Args:
            size (int): size of square (private)
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """
        Public instance method: def area(self):
          that returns the current square area
        """
        return self.__size ** 2
