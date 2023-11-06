#!/usr/bin/python3
"""
Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """ Function that returns True if the object is exactly
        an instance of the specified class ; otherwise False.
        Args:
            obj: object to look up.
            a_class: class to compare.
        Return:
            True if the object is exactly an instance of the specified class;
            otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
