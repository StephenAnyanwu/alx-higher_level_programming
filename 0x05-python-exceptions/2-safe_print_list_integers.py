#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    a function that prints the first x elements of a
    list and only integers using "{:d}".format()

    Parameters
    ----------
    my_list : list (optional)
        a list of elements to be printed (default is empty list)
    x : int (optinal)
        the number of elements to access in my_list (default is 0)
        x can be bigger than the length of my_list - if it’s the case,
        an exception (IndexError) is expected to occur.

    Returns
    -------
    int
        the real number of integers printed.
    """
    num_int = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_int += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return (num_int)
