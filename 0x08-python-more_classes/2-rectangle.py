#!/usr/bin/python3

"""Classes and Objects
This module demostrates how a private instance attribute is defined,
and how we can use a methods (and getter) to access the private instance
attribute and perform operations with it. It also demostrates how we can
use a special method called setter to modify private instance attribute
Note that private instance attribute can not be accessed nor modify by an
instance/object and outside the scope of the class it was defined. We can
only achieve this using a setter. This is refered as Encapsulation in OOP.

Exception is raise when the attribute does not meet some defined
requirements.
This module contain the following class:
    * Rectangle - defines a rectangle (based on 1-rectangle.py). A class used
    for the demostration.
"""


class Rectangle:
    """
    A class that defines a rectangle

    Attributes
    ----------
    width : int, optional
        width of the rectangle. It's a private instance
        attribute (default is 0)
    height : int, optional
        height of the rectangle. It's a private instance
        attribute (default is 0)

    Methods
    -------
    width()
        retrieves the private instance attribute width (a getter)
    width(value)
        modifies or set the private instance attribute width (a setter)
    height()
        retrieves a private instance attribute height (a getter)
    height(value)
        modifies or set the private instance attribute height (a setter)
    area()
        returns the rectangle area
    perimeter()
        returns the rectangle perimeter
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int, optional
            width of the rectangle. It's a private instance
            attribute (default is 0)
        height : int, optional
            height of the rectangle. It's a private instance
            attribute (default is 0)

        Raises
        ------
        TypeError
            If width is not an integer.
            If height is not an integer.

        ValueError
            If width is less than 0.
            If height is less than 0.
        """

        self.__width = width
        self.__height = height
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """
        retrieves a private instance attribute width (a getter)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        modifies or set the private instance attribute width (a setter)

        Paramters
        ---------
        value : int
            new value assigned to private instance attribute width.

        Raises
        ------
        TypeError
            if value is not an integer
        ValueError
            if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves a private instance attribute height (a getter)
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        modifies or set the private instance attribute height (a setter)

        Paramters
        ---------
        value : int
            new value assigned to private instance attribute height

        Raises
        ------
        TypeError
            if value is not an integer
        ValueError
            if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)
