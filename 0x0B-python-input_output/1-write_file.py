#!/usr/bin/python3
"""Write file"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, "w") as f:
        return f.write(text)
