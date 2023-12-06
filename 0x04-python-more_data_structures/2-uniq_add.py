#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a list
    (only once for each integer)

    Parameter
    ---------
    my_list : list
        list of integers

    Returns
    -------
    int
        sum of unique integers in my_list
    """

    sum = 0
    temp = []
    for i in my_list:
        if i not in temp:
            sum += i
        temp.append(i)
    return (sum)
