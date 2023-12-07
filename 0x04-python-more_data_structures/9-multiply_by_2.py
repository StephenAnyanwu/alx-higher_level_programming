#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """"
     returns a new dictionary with all values multiplied by 2

     Paramter
     --------
     a_dictionary : dict
    """

    new_dict = {}
    for key, val in a_dictionary.items():
        new_dict[key] = val * 2
    return (new_dict)
