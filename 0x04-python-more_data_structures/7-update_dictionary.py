#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
     replaces or adds key/value in a dictionary

     Parameters
     ----------
     a_dictionary : dict
        a dictionary to add key/value
    key : str or int
        dictionary key to replace or add
    value : str or int
        value to be added
    """
    a_dictionary.update({key: value})
