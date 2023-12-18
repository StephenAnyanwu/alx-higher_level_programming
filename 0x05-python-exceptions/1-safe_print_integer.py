#!/usr/bin/python3

def safe_print_integer(value):
    """
    a function that prints an integer with "{:d}".format().

    Parameter
    ---------
    value : can be any type (integer, string, etc.)
        value to be printed

    Returns
    -------
    bool
        True if value has been correctly printed
        (it means the value is an integer), therwise False.
    """

    try:
        print("{:d}".format(value))
    except Exception:
        return (False)
    return (True)
