"""
In this module defines a class Square that impliments
a square and inherits Rectangle class.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Impliments a square

    Methods
    -------
    size()
        Return the size attribute (getter)
    size(value)
        modify the size attribute (setter)
    update()
        Update the square. Takes *args or
        **kwargs as argument.
    to_dictionary()
        Return the dictionary representation of
        Square object.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Parameters
        ----------
        size : int
            size of the square.
        x : int, optional
            x coordinate of the new square (default: 0)
        y : int, optional
            y coordinate of the new square (default: 0)
        id : int, optional
            identity of the new square (default: 0)
        """
        #  The width and the height arguments of the super
        #  class are equal to size argument. Technically,
        #  width = size, height = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        #  We return the getter 'width' defined in the super
        #  class since '__width' can't be accessed.
        return self.width

    @size.setter
    def size(self, value):
        """Modify the size of the square. This is done
        by modify the width and height of the square

        Parameters
        ----------
        value : int
            value of the square size
        """
        #  We can't access private attributes of the inherited
        #  class, but we can through their getters.
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square .Takes *args or
        **kwargs as argument.

        Parameters
        ----------
        *args : tuple (no-keyword arguments)
            New values of the attributes.
                1st argument should be the id attribute
                2nd argument should be the size attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
        **kwargs : dict (keyworded arguments)
            Each key in this dictionary represents an attribute to the
            instance; it's skipped if *args exists and is not empty.
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a
        Square object.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return and print string representation of a
        Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
