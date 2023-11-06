#!/usr/bin/python3
"""Write a class MyInt that inherits from int
"""


class MyInt(int):
    """Represent a MyInt."""
    def __eq__(self, value):
        """Return the opposite of the equal."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Return the opposite of the not equal."""
        return super().__eq__(value)
