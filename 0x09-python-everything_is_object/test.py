#!/usr/bin/python3

#2
a = 89
b = 100
print(id(a) == id(b)) # False

#3
a = 89
b = 89
print(id(a) == id(b)) # True

#4
a = 89
b = a
print(id(a) == id(b)) # True

#5
a = 89
b = a + 1
print(id(a) == id(b)) # False

#6
s1 = "Best School"
s2 = s1
print(s1 == s2) # True

#7
s1 = "Best"
s2 = s1
print(s1 is s2) # True

#8
s1 = "Best School"
s2 = "Best School"
print(s1 == s2) # True

#9
s1 = "Best School"
s2 = "Best School"
print(s1 is s2) # True  because immutables with same value have same id

#10
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2) # True

#11
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2) # False

#12
l1 = [1, 2, 3]
l1 = l2
print(l1 == l2) # True

#13
l1 = [1, 2, 3]
l2 = l1  
print(l1 is l2) # True  because l2 is alias of l1, both have the same id


#14
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2) # [1, 2, 3, 4]  because mutables (e.g list) can be aliased; modification made with their methods affect both


#15
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2) # [1, 2, 3]  modification made with operators affect only the one it's used on


#16
def increment(n):
    n += 1

a = 1
increment(a)
print(a) # 1  because immutables are passed to function by value; they can't be modify in a function


#17
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l) # [1, 2, 3, 4]  because mutables are passed to function by reference; using their methods for modification will affect them
                        

#18
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1) # [1, 2, 3]  using operators to modify mutables passed to a function will not affect affect them.


#19
def copy_list(l):
    """Return a copy of a list
    Parameters
    ----------
    l : list
        a list to make a copy of
    Returns
    -------
    list
        A copy of list l
    """
    return l[:]

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list) # [1, 2, 3]
print(new_list) # [1, 2, 3]

print(new_list == my_list) # True
print(new_list is my_list) # False


#20
a = ()
# Is a a tuple?  Yes  a is an empty tuple
print(type(a)) # tuple


#21
a = (1, 2)
# Is a a tuple? Yes
print(type(a)) # tuple


#22
a = (1)
# Is a a tuple? No
print(type(a)) # int


#23
a = (1, )
# Is a a tuple? Yes
print(type(a)) # tuple


#24
a = (1)
b = (1)
print(a is b) # True


#25
a = (1, 2)
b = (1, 2)
print(a is b) # True


#26
a = ()
b = ()
print(a is b) # True


#27
a = [1, 2, 3]
print(id(a))
a = a + [5]
print(id(a)) # Not same id because operator was used for modification
print(a)

#28
a = [1, 2, 3]
print(id(a))
a += [5]
print(id(a)) # same id because the binary operator += is used inplace of append method
print(a)
