#!/usr/bin/python3
for i in range(0, 10):
    for j in range((i * 10) + 1, 90):
        if j % 10 == 0:
            break
        if j % 10 <= i:
            continue
        if j != 89:
            print("{:02d}".format(j), end = ", ")
        else:
            print("{:02d}".format(j))
