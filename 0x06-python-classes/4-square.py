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

    def area(self):

        """
        Public instance method: def area(self):
          that returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        getter function to retrieve size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function to validate size attribute

        Args:
            value (int): size of square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
