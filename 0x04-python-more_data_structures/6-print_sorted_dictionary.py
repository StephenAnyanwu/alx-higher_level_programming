#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
     prints a dictionary by ordered keys

     Parameter
     ---------
     a_dictionary : dict
    """

    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    new_dict = {}
    for k in dict_keys:
        new_dict[k] = a_dictionary[k]
    for key, val in new_dict.items():
        print("{}: {}".format(key, val))
