#!/usr/bin/python3

"""
a program that prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase, ont followed by a newline.
"""

for i in range(122, 96, -1):
    if i % 2 != 0:
        print(chr(i - 32), end="")
    else:
        print(chr(i), end="")
