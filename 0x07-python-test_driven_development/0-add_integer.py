#!/usr/bin/python3
"""
In this module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """adds two integers

    Parameters
    ----------
    a : int or float
         must be first casted to integers if
         it's float.
    b : int or float, optional
        must be first casted to integers if
        it's float (default is 98).

    Returns
    -------
    int
        the addition of a and b.

    Raises
    ------
    TypeError
        If either of a or b is a non-integer and non-float.
    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
