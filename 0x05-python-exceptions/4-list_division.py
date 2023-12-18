#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    a function that divides element by element 2 lists.

    Parameter
    ---------
    my_list_1 : list
        a list containing any type (integer, string, etc)
    my_list_2 : list
        a list containing any type (integer, string, etc)
    list_length : int
        can be bigger than the length of both lists

    Returns
    -------
    list
        a new list (length = list_length) with all divisions.
    """

    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                new_list.append(0)
                print("wrong type")
                pass
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
                pass
            except IndexError:
                new_list.append(0)
                print("out of range")
                pass
    finally:
        return (new_list)
