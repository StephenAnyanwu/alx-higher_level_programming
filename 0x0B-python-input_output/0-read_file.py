#!/usr/bin/python3

"""
In this module defines a function 'read_file'.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Parameters
    ----------
    filename : str (optional)
        the test file to be read.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        my_file = f.read()
        print(my_file, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
