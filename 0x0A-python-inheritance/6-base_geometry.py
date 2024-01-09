#!/usr/bin/python3

"""
In this module defines a class 'BaseGeometry'.
"""


class BaseGeometry:
    """
    A class of base geometry.

    Methods
    -------
    area()
        raises an Exception
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
