#!/usr/bin/pytuon3
""" Module that contains a function that returns a list with the available
    attributes and methods of an object.
"""


def lookup(obj):
    """ Function that returns a list with the available attributes and methods
        of an object.
        Args:
            obj: object to look up.
        Return:
            List with the available attributes and methods of an object.
    """
    return dir(obj)
