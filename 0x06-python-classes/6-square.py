#!/usr/bin/python3
"""define a class Square"""


class Square:
    """"
    Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        instantiation with size (no type/value verification)

        Args:
            size (int): size of square (private)
            position (tuple): position of square (private)
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        getter function to retrieve position attribute

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function to validate position attribute

        Args:
            value (tuple): position of square

        Raises:
            (TypeError) exception with the message:
                "position must be a tuple of 2 positive integers"

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Public instance method: def my_print(self):
        that prints in stdout the square with the character ( # ):

        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
