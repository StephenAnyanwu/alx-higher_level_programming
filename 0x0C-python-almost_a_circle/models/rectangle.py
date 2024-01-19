#!/usr/bin/python3

"""
In this module defines a class Rectangle that impliments
a rectangle and that inherits from Base class.
"""
from models.base import Base


class Rectangle(Base):
    """Impliment a rectangle

    Attributes
    ----------
    width : int
        width of the rectangle (private attribute)
    height : int
        height of the rectangle (private attribute)
    x : int
        private attribute
    y : int
        private attribute

    Methods
    -------
    width()
        width getter
    width(value)
        width modifier (setter)
    height()
        height getter
    height(value)
        height modifier (setter)
    x()
        x getter
    x(value)
        x modifier (setter)
    y()
        y getter
    y(value)
        y modifier (setter)
    area()
        calculate and return the area of the rectangle
        instance
    display()
        print in stdout the Rectangle instance with the
        character #
    def update(*args, **kwargs)
        Update th instance attributes. Takes args or
        kwargs as argument.
    to_dictionary(self):
        Return the dictionary representation of a Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Parameters
        ----------
        width : int
            width of the rectangle (private attribute)
        height : int
            height of the rectangle (private attribute)
        x : int
            x coordinate of a new rectangle (default: 0)
        y : int
            y cordinate odf a new rectangle (default: 0)
        id : int
            identity of the rectangle (default: 0)

        Raises
        ------
        TypeError
            if width, height, x or y is not an int
        ValueError
            if width or height is <= 0
            if x or y is < 0
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """Return width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifier width attribute

        Parameters
        ----------
        value : int
            value of width attribute
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifier height attribute

        Parameters
        ----------
        value : int
            value of height attribute
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Modifier x attribute

        Parameters
        ----------
        new_val : int
            value of x attribute
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Modifier y attribute

        Parameters
        ----------
        value : int
            value of y attribute
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """print in the stdout the Rectangle instance with
        character '#'
        """
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update th instance attributes. Takes *args or
        **kwargs as argument.

        Parameters
        ----------
        *args : tuple (no-keyword arguments)
            New values of the attributes.
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        **kwargs : dict (keyworded arguments)
            Each key in this dictionary represents an attribute to the
            instance; it's skipped if *args exists and is not empty.
        """
        if args and len(args) != 0:  # args exist an is not empty
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        if kwargs and len(kwargs) != 0:  # kwargs exist and is not empty
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return and print the string representation of Rectangle
        """
        x_y = f"{self.x}/{self.y}"
        w_h = f"{self.width}/{self.height}"
        return f"[Rectangle] ({self.id}) {x_y} - {w_h}"
