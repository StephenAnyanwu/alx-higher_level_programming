#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    find the biggest integer of a list

    Parameter
    ---------
    my_list : list
        list containing integers
    Returns
    -------
    int
        if list is not empty
    None
        if list is empty
    """

    if len(my_list) == 0:
        return (None)
    max_int = 0
    for i in my_list:
        if i > max_int:
            max_int = i
    return (max_int)
