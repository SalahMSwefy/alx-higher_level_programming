#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle:

    """Class Rectangle that defines a rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    """Public class attribute that counts number of instances"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes rectangle with width and height

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        """Method that returns the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.width + self.height)

    def area(self):
        """Method that returns the area of rectangle"""
        return self.width * self.height

    def __str__(self):
        """Method that returns a string of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            for i in range(self.height):
                print("#" * self.width, end="")
                if i != self.height - 1:
                    print()
            return ""

    def __repr__(self):
        """Method that returns a formal string representation"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
