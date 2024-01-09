#!/usr/bin/python3

"""
In this module defines a class:
    BaseGeometry
    Rectangle
"""


class BaseGeometry:
    """
    A class the represent Base Geometry

    Methods
    -------
    area()
        Raises an exception.
    integer_validator(name, value)
        validates a value
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value

        Parameters
        ----------
        name : str
        value : int

        Raises
        ------
        TypeError
            if value is not an integer
        ValueError
            if value is less or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represent a rectangleusing inherited class
    BaseGeometry
    """
    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            width of the rectangle
        height : int
            height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
