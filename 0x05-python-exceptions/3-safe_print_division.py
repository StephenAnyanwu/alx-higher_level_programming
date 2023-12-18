#!/usr/bin/python3

def safe_print_division(a, b):
    """
    a function that divides 2 integers and prints the result.

    Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
        the value of the division, otherwise None
    """
    result = 0
    try:
        result = a / b
    except Exception:
        result = None
    print("Inside result: {}".format(result))
    return (result)
