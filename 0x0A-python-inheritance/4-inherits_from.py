#!/usr/bin/python3

"""
In this module defines a function 'inherits_from'.
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class.

    Parameters
    ----------
    obj : any type
        the object
    a_class : class
        the class

    Returns
    -------
    bool
        True if obj is an instance of a class that inherits
        a_class (directly or indirectly), otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
