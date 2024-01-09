#!/usr/bin/python3

#2
a = 89
b = 100
print(id(a) == id(b))

#3
a = 89
b = 89
print(id(a) == id(b))

#4
a = 89
b = a
print(id(a) == id(b))

#5
a = 89
b = a + 1
print(id(a) == id(b))

