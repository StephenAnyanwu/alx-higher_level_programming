#!/usr/bin/python3

"""
In this module defines classes:
    BaseGeometry
    Rectangle
In this module, single inheritance is demonstrated.
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
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represent a rectangleusing inherited class
    BaseGeometry

    Methods
    -------
    area()
        calculates the area of the rectangle
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

    def area(self):
        """calculates and returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string repreaentation of Rectangle class"""
        string = f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
        return string


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
