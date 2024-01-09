#!/usr/bin/python3

"""
In this module defines a class 'BaseGeometry'.
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


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
