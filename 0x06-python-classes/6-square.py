#!/usr/bin/python3

"""Classes and Objects
This module demostrates how a private instance attribute is defined,
and how we can use a methods (and getter) to access the private instance
attribute and perform operations with it. It also demostrates how we can
use special methods called setters to modify private instance attributes
Note that private instance attribute can not be accessed nor modify by an
instance/object and outside the scope of the class it was defined. We can
only achieve this using a setter. This is refered as Encapsulation in OOP.

Exception is raise when the attribute does not meet some defined
requirements.
This module contain the following class:
    * Square - defines a square (based on 5-square.py). A class used
    for the demostration.
"""


class Square:

    """
    A class that defines a square.

    Attributes
    ---------
    size : int, optional
        size of the square. It's a private instance
        attribute (default is 0)
    position : tuple
        a tuple of two positive integers. It's a private
        instance attribute (default is (0,0)).

    Methods
    ------
    area()
        returns the current square area.
    size()
        retrieves the private instance attribute size (a getter)
    size(value)
        modifies or set the private instance attribute size (a setter)
    my_print()
        prints in stdout the square with the character #
    position()
         retrieves the private instance attribute position (a getter)
    position(value)
         modifies or set the private instance attribute position (a setter)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ---------
        size : int, optional
            size of the square. It's a private instance
            attribute (default is 0)
        position : tuple, optional
            position to start printing by using space.
            Don;t fill line by spaces when posotion[1] > 0.

        Raises
        ------
        TypeError
            If size is not an integer.
            If position is not a tuple of two integer.
        ValueError
            If size is less than zero.

        """

        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    @property
    def size(self):
        """
        retrieves the private instance attribute size (a getter)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        modifies or set the private instance attribute size (a setter)

        Paramters
        ---------
        value : int
            new value assigned to private instance attribute size.

        Raises
        ------
            if value is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        while following the position tuple (ie horizontal
        and vertical spaces)
        """
        if self.__size == 0:
            print("")
            return
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                print("#" * self.__size)

    @property
    def position(self):
        """
        retrieves the private instance attribute position (a getter)
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        modifies or set the private instance attribute position (a setter)

        Paramters
        ---------
        value : tuple
            new value assigned to private instance attribute position.

        Raises
        ------
        TypeError
            if position not a tuple of two positive integers.
        """

        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(num, int) for num in value) or\
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of\
                    2 positive integers")
        self.__position = value

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
