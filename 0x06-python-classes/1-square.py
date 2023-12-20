#!/usr/bin/python3

"""Classes and Objects
This module demostrates how a private instance attribute is defined.
This module contain the following class:
    * Square - defines a square (based on 0-square.py). A class used
    for the demostration.
"""


class Square:
    """
    A class that defines a square.

    Attribute
    ---------
    size : int
        size of the square. It's a private instance attribute.
    """

    def __init__(self, size):
        self.__size = size
