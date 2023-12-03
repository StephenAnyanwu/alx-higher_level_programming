#!/usr/bin/python3

def multiple_returns(sentence):
    """
    returns a tuple with the length
    of a string and its first character

    Parameter
    ---------
    sentence : str
        string to return its first character
    Returns
    -------
    tuple
        length of a string and its first character
    """
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
