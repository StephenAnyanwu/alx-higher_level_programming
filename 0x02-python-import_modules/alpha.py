#!/usr/bin/python3
def upper_alpha():
    for i in range(65, 91):
        if i == 90:
            print("{}".format(chr(i)))
        else:
            print("{}".format(chr(i)), end="")
