#!/usr/bin/python3

"""
In this module defines a class 'MyList' that inherits
from built-in class 'list'
"""


class MyList(list):
    """
    A class that impliments the functionality of the
    inherited built-in class 'list'
    """

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
