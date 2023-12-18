#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    a function that raises a name exception with a message.

    Parameter
    ---------
    message : str
        message of the exception to be printed
        (default is empty string).
    """

    try:
        print(ALX)
    except NameError as e:
        print(message)
