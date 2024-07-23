#!/usr/bin/python3
"""
Defines a function  that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    mid = int(size / 2)
    if list_of_integers[mid] > list_of_integers[mid - 1] and\
            list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
