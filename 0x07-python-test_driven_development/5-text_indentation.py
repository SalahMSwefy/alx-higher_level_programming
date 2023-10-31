#!/usr/bin/python3
"""
Module that prints a text with 
2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    print("\n".join([line.strip() for line in text.split("\n")]), end="")



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")