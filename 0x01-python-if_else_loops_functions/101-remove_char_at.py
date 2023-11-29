#!/usr/bin/python3
"""
creates a copy of the string, removing the character at the position n
(not the Python way, the “C array index”).
"""


def remove_char_at(str, n):
    new_str = ""
    if n >= 0:
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
        return new_str
    return (str)
