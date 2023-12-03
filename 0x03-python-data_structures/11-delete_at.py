#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list

    Parameter
    ---------
    my_list : list, optional
        list with items (default is empty)
    idx : int
        index of the item to be deleted

    Returns
    -------
    list
        same list if idx is negative or out of range,
        else new list
    """

    if len(my_list) == 0 or idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = []
    return (my_list)
