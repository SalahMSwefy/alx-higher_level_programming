#!/usr/bin/python3
"""Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file,
    after each line containing a specific string (see example):"""
    with open(filename, mode="r") as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

        with open(filename, mode="w") as f:
            f.writelines(new_lines)
