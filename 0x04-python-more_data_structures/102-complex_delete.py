#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    deletes keys with a specific value in a dictionary.

    Parameters
    ---------
    a_dictionary : dict
    value : any datatype
        value its key should be deleted
    Returns
    -------
    dict
        new dictionary or original dictionary if value
        doesn't exist
    """

    exist = False
    keys = []
    for k, v in a_dictionary.items():
        if value == v:
            keys.append(k)
            exist = True
    if exist is False:
        return (a_dictionary)
    for i in keys:
        del a_dictionary[i]
    return (a_dictionary)
