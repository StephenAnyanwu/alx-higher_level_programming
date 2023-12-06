#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set

    Paramters
    ---------
    set_1 : set
        first set
    set_2 : set
        second set
    """

    set_3 = set_1.symmetric_difference(set_2)
    return (set_3)
