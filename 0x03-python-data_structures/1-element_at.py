#!/usr/bin/python3

def element_at(my_list, idx):
    """
    retrieves an element from a list like in C

    Parameters
    ----------
        my_list : list
            contains element to be retrieved
        idx : int
            index of element
    Return:
        element retrieved
    """

    if idx < 0:
        return (None)
    if idx > len(my_list) - 1:
        return (None)
    return (my_list[idx])
