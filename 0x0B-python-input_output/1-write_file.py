#!/usr/bin/python3

"""
In this module defines a function 'write_file'.
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8),
    overwrites the content of the file if it already
    exists

    Parameters
    ----------
    filename : str, optional
        file to write to (default: empty string)
    text : str, optional
        string to write into filename (default: empty string)

    Returns
    -------
    int
        the number of characters written into filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        num_char = f.write(text)
        return num_char
