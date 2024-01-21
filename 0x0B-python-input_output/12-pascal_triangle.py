#!/usr/bin/python3

"""
Defines a pascal_triangle function
"""


def pascal_triangle(n):
    """
    Create and return a list of lists of integers representing
    the Pascal’s triangle of n

    Parameters
    ----------
    n : int
        Degree (i.e size) of the the triangle

    Returns
    -------
    list
        nested list representing a Pascal triangle of
        degree n (ie the length of the list)therwise
        an empty list if n <= 0
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) < n:
        temp = triangle[-1]
        tri_next_row = [1]
        for i in range(len(temp) - 1):
            tri_next_row.append(temp[i] + temp[i + 1])
        tri_next_row.append(1)
        triangle.append(tri_next_row)
    return triangle


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
