#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replaces an element of a list at a specific position

    Parameters
    ----------
    my_list : list
        a list that its element will be replaced
    idx : int
        position in the list
    element
        item that will be replaced

    Returns
    -------
    list
        modified list

    """

    if idx < 0:
        return (my_list)
    if idx > len(my_list) - 1:
        return (my_list)
    my_list[idx] = element
    return (my_list)
