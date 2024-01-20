#!/usr/bin/python3

"""
Defines LockedClass class
"""


class LockedClass:
    """
    Prevents the user from dynamically creating
    new instance attributes, except if the new
    instance attribute is called first_name.
    """
    __slots__ = ["first_name"]


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
