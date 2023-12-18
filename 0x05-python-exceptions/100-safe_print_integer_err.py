#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    a function that prints an integer.

    Parameter
    ---------
    value : can be any type (integer, string, etc.)
        argument to be printed.

    Returns
    -------
    bool
        True if value has been correctly printed
        (it means the value is an integer), otherwise False and
        and prints in stderr the error precede by Exception:
    """

    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (False)
