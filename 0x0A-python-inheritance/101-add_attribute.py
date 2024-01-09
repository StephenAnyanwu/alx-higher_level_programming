#!/usr/bin/python3
"""
In this module defines a function adds_attributes
"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Parameters
    ----------
    obj : any type
        object to add an attribute to.
    att : str
        name of the attribute to add to obj.
    value : any type
        value of the attribute.

    Raises
    ------
    TypeError
        if the object can’t have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
