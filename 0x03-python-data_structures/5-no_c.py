#!/usr/bin/python3

def no_c(my_string):
    """
    removes all characters c and C from a string

    Parameter
    ---------
    my_string : str
        a string to remove a character from

    Returns
    -------
    str
        a new string
    """
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return (new_string)
