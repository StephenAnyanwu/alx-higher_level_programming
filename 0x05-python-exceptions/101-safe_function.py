#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    a function that executes a function safely.

    Paramters:
    ---------
    fct : function (always)
        a function to be executed.
    *args : non-keyword arguments.
        to be passed to the function fct as its arguments.

    Returns
    -------
    the result of the function (fct), otherwise None if something
    happens during the function execution and prints in stderr the
    error prcede by Exception:
    """

    try:
        return (fct(*args))
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return (None)
