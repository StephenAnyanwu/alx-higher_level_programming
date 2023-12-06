#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    finds common elements in two sets

    Paramters
    ---------
    set_1 : set
        first set
    set_2 : set
        second set
    Returns
    -------
    set
        a st of common elements in set_1 and set_2
    """
    return (set_1 & set_2)
