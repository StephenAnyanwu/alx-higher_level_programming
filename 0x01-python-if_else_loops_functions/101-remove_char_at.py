#!/usr/bin/python3
"""
creates a copy of the string, removing the character at the position n
"""


def remove_char_at(str, n):
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
        else:
            new_str += ' '
    return new_str
