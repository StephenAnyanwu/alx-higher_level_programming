#!/usr/bin/python3

"""
In this module defines a function that divides each
element of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """divides each element of a matrix by a number

    Parameters
    ----------
    matrix : list
        a list of lists of integers or floats.
    div : int or float
        divisor of matrix elements.

    Returns
    -------
    a matrix with each element divided by div and
    round to two decimal places.

    Raises
    ------
    TypeError
        > if matrix is not a list of lists of integers or
        floats.
        > if the rows of matrix are not of the same size.
        > if div is not int or float.
    ZeroDivisionError
        if div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
