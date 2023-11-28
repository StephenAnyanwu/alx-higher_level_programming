#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (True)
    return (False)


def uppercase(str):
    upper_str = ""
    for i in range(len(str)):
        if islower(str[i]):
            upper_str += chr(ord(str[i]) - 32)
        else:
            upper_str += str[i]
    print(upper_str)
