#!/usr/bin/python3
""" Module that contains a function that returns True if the object is an
    instance of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ Function that returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class ; otherwise
        False.
        Args:
            obj: object to look up.
            a_class: class to compare.
        Return:
            True if the object is an instance of a class that inherited
            (directly or indirectly) from the specified class; otherwise False.
    """
    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return True
    else:
        return False
