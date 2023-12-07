#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    returns the weighted average of
    all integers tuple (<score>, <weight>)
    """

    if len(my_list) == 0:
        return (0)
    sum_ = 0
    deno = 0
    for i in my_list:
        score, weight = i
        sum_ += score * weight
        deno += weight
    return (sum_ / deno)
