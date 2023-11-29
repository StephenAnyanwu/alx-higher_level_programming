#!/usr/bin/python3

"""
a program that prints the ASCII alphabet, in reverse order,
alternating lowercase and uppercase, ont followed by a newline.
"""

for i in range(122, 96, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end='')
