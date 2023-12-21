#!/usr/bin/python3

"""Classes and Objects
This module demostrates how a private instance attribute is defined,
and how we can use a methods (and getter) to access the private instance
attribute and perform operations with it. It also demostrates how we can
a special method called setter to modify private instance attribute
Note that private instance attribute can not be accessed nor modify by an
instance/object and outside the scope of the class it was defined. We can
only achieve this using a setter. This is refered as Encapsulation in OOP.

Exception is raise when the attribute does not meet some defined
requirements.
This module contain the following class:
    * Square - defines a square (based on 3-square.py). A class used
    for the demostration.
"""


import sys


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
        returns the current square area.
    size()
        retrieves the private instance attribute (a getter)
    size(value)
        modifies or set the private instance attribute (a setter)
    my_print()
        prints in stdout the square with the character #
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
        return self.__size * self.__size

    @property
    def size(self):
        """
        retrieves the private instance attribute size (a getter)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        modifies or set the private instance attribute size (a setter)

        Paramters
        ---------
        value : int
            new value assigned to private instance attribute size.

        Raises
        ------
            if value is not an integer
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """

        if self.size < 0:
            raise ValueError("size must be >= 0")
        if self.size == 0:
            sys.stdout.write(" \n")
        else:
            for i in range(self.size):
                sys.stdout.write("#" * self.__size + "\n")
