#!/usr/bin/python3

"""
Defines Combination class, pascal_triangle function and
print_triangle function
"""


class Combination:
    """
    Impliment combination of integers

    Attributes
    ----------
    __n : int
        number of elements
    __r : int
        number of combinations
    get : int
        get the combination

    Methods
    -------
    __factorial(x)
        find and return the factorial of an integer recursively
    __combination(m, n)
        find and return the combination of  integers
    """
    def __init__(self, n, r):
        """
        parameters
        ----------
        n : int
            number of elements
        r : int
            number of combinations of elements
        """
        self.__n = n
        self.__r = r
        self.get = self.__combination(n, r)

    def __factorial(self, x):
        """
        find the factorial of an integer recursively

        Parameters
        ----------
        x : int
            number to find its factorial
        Returns
        -------
        int
            factorial of x
        """
        if x == 0 or x == 1:
            return 1
        return (x * self.__factorial(x - 1))

    def __combination(self, m, n):
        """
        find the combination of  integers

        Paramters
        ---------
        m : int
            number of elements
        n : int
            number of combination of elements

        Returns
        -------
        int
            combination of m and n (mCn)
        """
        fact = self.__factorial
        comb_m_n = fact(m) / (fact(m - n) * fact(n))
        return int(comb_m_n)


def pascal_triangle(n):
    """
    return a list of lists of integers representing the
    Pascal’s triangle of n

    Parameters
    ----------
    n : int
        degree of the Pascsl's triangle

    Returns
    -------
    list
        nested list representing a Pascal triangle of
        degree n (ie the length of the list)therwise
        an empty list if n <= 0

    """
    pas_tr = []
    if n <= 0:
        return pas_tr
    for p in range(n):
        pas_tr.append([Combination(p, q).get for q in range(p + 1)])
    return pas_tr


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(100))
