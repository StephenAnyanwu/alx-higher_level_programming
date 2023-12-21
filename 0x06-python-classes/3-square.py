#!/usr/bin/python3

"""Classes and Objects
This module demostrates how a private instance attribute is defined,
and how we can use a getter method to access the private instance
attribute.
Exception is raise when the attribute does not meet some defined
requirements.
This module contain the following class:
    * Square - defines a square (based on 2-square.py). A class used
    for the demostration.
"""


class Square:

    """
    A class that defines a square.

    Attributes
    ---------
    size : int, optional
        size of the square. It's a private instance
        attribute (default is 0)

    Methods
    ------
    area()
        returns the current square area (getter).
    """

    def __init__(self, size=0):
        """
        Parameters
        ---------
        size : int
            size of the square. It's a private instance
            attribute (default is 0)

        Raises
        ------
        TypeError
            If size is not an integer.
        ValueError
            If size is less than zero.
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return self.__size ** 2
