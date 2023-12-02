#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    prints all integers of a list

    Parameter
    ---------
    my_list : list, optional
        contains integers to be printed (default is empty)
    """

    for i in my_list:
        print("{:d}".format(i))
