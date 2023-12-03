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
    if len(my_list) == 1:
        return (my_list[0])
    min_int = 0
    for i in my_list:
        if i < min_int:
            min_int = i
    max_int = min_int
    for j in my_list:
        if j > max_int:
            max_int = j
    return (max_int)
