#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
     deletes a key in a dictionary

     Parameters
     ----------
     a_dictionary : dict
        dictionary to delete its key
    key : str
        key of dictionary to delete

    Returns
    -------
    dict
        a new dictionary
    """
    if key not in a_dictionary:
        return (a_dictionary)
    del a_dictionary[key]
    return (a_dictionary)
