#!/usr/bin/python3

def best_score(a_dictionary):
    """
    finds a key of a dictionary with the biggest integer value

    a_dictionary : dict

    Returns
    -------
    str
        key with the biggest integer valur, or None is not found
    """
    if (a_dictionary is None) or len(a_dictionary) == 0:
        return (None)
    val = 0
    key = ""
    for k, v in a_dictionary.items():
        if v < val:
            val = v
            key = k
    for k, v in a_dictionary.items():
        if v > val:
            val = v
            key = k
    return (key)
