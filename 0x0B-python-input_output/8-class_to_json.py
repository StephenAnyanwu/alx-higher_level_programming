#!/usr/bin/python3

"""
In this module defines a function class_to_json
"""


def class_to_json(obj):
    """Returns the dictionary description with simple
    data structure for JSON serialization of an object

    Parameters
    ----------
    obj : any type (an instance of a Class)
    """
    return obj.__dict__


if __name__ == "__main__":
    class MyClass:
        """ My class
        """

        def __init__(self, name):
            self.name = name
            self.number = 0

        def __str__(self):
            return "[MyClass] {} - {:d}".format(self.name, self.number)

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
    print("\n***************************\n")

    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number=4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            name = self.__name
            num = self.number
            score = self.score
            return "[MyClass] {} - {:d} => {:d}".format(name, num, score)

    m = MyClass("John")
    m.win()
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
