#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
     replaces all occurrences of an element by another
     in a new list

     Parameters
     ----------
     my_list : list
        the initial list
    search
        the  element to replace in the list
    replace
        the new element

    Returns
    -------
    list
        a new list
    """

    search_idx = my_list.index(search)
    new_list = my_list.copy()
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
