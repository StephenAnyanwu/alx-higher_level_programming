#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces an element in a list at a specific
    position without modifying the original list

    Paramters
    ---------
    my_list : list
        contains the element to be replaced
    idx : int
        index of the element to be replaced
    element
        new element

    Returns
    -------
    list
        new list with replaced element.
    """
    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    new_list = my_list
    new_list[i] = element
    return (new_list)
