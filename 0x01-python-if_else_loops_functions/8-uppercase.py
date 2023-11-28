#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upper_str += chr(ord(str[i]) - 32)
        else:
            upper_str += str[i]
    print("{}".format(upper_str))
