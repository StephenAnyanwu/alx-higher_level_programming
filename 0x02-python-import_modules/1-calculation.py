#!/usr/bin/python3
import calculator_1

if __name__ = "__main__":
    a = 10
    b = 5
    add = calculator_1.add(10, 5)
    print("{:d} + {:d} = {:d}".format(a, b, add))
    sub = calculator_1.sub(10, 5)
    print("{:d} - {:d} = {:d}".format(a, b, sub))
    mul = calculator_1.mul(10, 5)
    print("{:d} * {:d} = {:d}".format(a, b, mul))
    div = calculator_1.div(10, 5)
    print("{:d} / {:d} = {:d}".format(a, b, div))
