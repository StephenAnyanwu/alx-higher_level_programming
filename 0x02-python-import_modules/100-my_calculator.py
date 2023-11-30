#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("{}".format("Usage: "), end="")
        for i in range(len(sys.argv)):
            if i == len(sys.argv) - 1:
                 print("{}".format(sys.argv[i]))
            else:
                print("{} ".format(sys.argv[i]), end="")
        sys.exit(1)
    symbols = ['+', '-', '*', '/']
    if sys.argv[2] not in symbols:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    sym_entered = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sym_entered == symbols[0]:
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    if sym_entered == symbols[1]:
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    if sym_entered == symbols[2]:
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    if sym_entered == symbols[3]:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

