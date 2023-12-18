#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    a function that prints x elements of a list

    Parameters
    ----------
    my_list : list(optional)
        list of elements to be printed (default is empty list)
    x : int(optional)
        number of elements to be printed (default is 0).
        x can be bigger that the length of my_list.

    Returns
    -------
    int
        the real number of elements printed.
    """

    num_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_elements += 1
        except Exception:
            pass
    print()
    return (num_elements)
