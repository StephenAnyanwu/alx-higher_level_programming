"""
In this model defines a class Base
"""


class Base:
    """Base class

    attributes
    ----------
    __nb_objects : int
        A private class attribute that counts the number
        of Base object created (default: 0).
    id : int
        An instance attribute (default: None).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        parameters
        ----------
        id : int, optional
            default is None
        """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id
