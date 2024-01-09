#!/usr/bin/python3
"""
In this modeule defines a class MyInt that inherits
built-in class int.
"""


class MyInt(int):
    """
    A class that inverts int operators == and !=
    """

    def __eq__(self, value):
        """Overrides == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavior."""
        return self.real == value


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
