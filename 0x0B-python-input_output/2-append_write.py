#!/usr/bin/python3

"""
In this module defines a function 'append_write'.
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Parameters
    ----------
    filename : str
        a text file to append text to
    text : str
        a string to append to filename
    Returns
    -------
    int
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num_char = f.write(text)
        return num_char
