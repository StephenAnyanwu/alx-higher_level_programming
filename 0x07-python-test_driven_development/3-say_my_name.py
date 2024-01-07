#!/usr/bin/python3

"""
In this module defines a function say_my_name that prints
My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """a function that prints My name is <first name> <last name>

    Parameters
    ----------
    first_name : string
        first name
    last_name : string, optional
        last name (default is empty string).

    Raises
    ------
    TypeError
        if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
