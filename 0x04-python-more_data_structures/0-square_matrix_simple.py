#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix

    Paramter
    --------
    matrix : list, optional
        2 dimensional array of integers (default is empty)

    Returns
    -------
    list
        2 dimensional array of square value of each integer in matrix
    """

    sqr_matrix = [[i * i for i in matrix[row]] for row in range(len(matrix))]
    return (sqr_matrix)
