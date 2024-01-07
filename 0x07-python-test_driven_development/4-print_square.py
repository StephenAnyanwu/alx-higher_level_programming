#!/usr/bin/python3

"""
In this module defines a function print_square that prints
a square with charahter #
"""


def print_square(size):
    """a function that prints a square with the character #.

    Parameters
    ----------
    size : int
        size length of the square.

    Raises
    ------
    TypeError
        if size is not int
    ValueError
        if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
