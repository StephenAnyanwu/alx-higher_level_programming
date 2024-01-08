#!/usr/bin/python3

"""
In this module defines a function 'lookup'
"""


def lookup(obj):
    """returns the list of available attributes
    and methods of an object.

    Parameters
    ----------
    obj : any type
        the object
    """
    return dir(obj)
