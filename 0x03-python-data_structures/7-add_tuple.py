#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    add integer elements of two tuples consecutively

    Parameter
    ---------
    tuple_a : tuple, optional
        contains integer elements (default is empty)
    tuple_b : tuple, optional
        contains integer elements (default is empty)

    Returns
    -------
    tuple
        consecutive sum of two tuples of length equals 2
    """

    tup_a = tuple_a
    tup_b = tuple_b

    if len(tup_a) == 0:
        tup_a = (0, 0)
    elif len(tup_a) == 1:
        tup_a = (tup_a[0], 0)
    if len(tup_b) == 0:
        tup_b = (0, 0)
    elif len(tup_b) == 1:
        tup_b = (tup_b[0], 0)
    return (sum(tup_a[0], tup_b[0]), sum(tub_a[1], tup_b[1]))
