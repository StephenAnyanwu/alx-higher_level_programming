#!/usr/bin/python3

"""
In this module defines a function 'is_kind_of_class'
"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if
    the object is an instance of a class that inherited
    from, the specified class.

    Parameters
    ----------
    obj : any type
        the object
    a_class : class
        the class

    Returns
    -------
    bool
        True if obj is an instance of a_class, or if obj
        is an instance of a class that inherited from a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
