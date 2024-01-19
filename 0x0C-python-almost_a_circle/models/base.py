#!/usr/bin/python3

"""
In this model defines a class Base
"""

import json


class Base:
    """Base class

    Attributes
    ----------
    __nb_objects : int
        A private class attribute that counts the number
        of Base object created (default: 0).
    id : int
        identity of Base object (default: None).

    Methods
    -------
    to_json_string(list_dictionaries)
        Convert a python list to JSON string representation
        (static method).
    save_to_file(cls, list_objs)
        Write the JSON string representation of
        list_objs to a file (class method).
    from_json_string(json_string):
        Convert a list of JSON string representation
        to python list (static method).
    create(cls, **dictionary):
        Return a dictionary of attributes of an instantiated
        class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        parameters
        ----------
        id : int, optional
            identity of Base object (default: None)
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a python list to JSON string representation.

        Parameters
        ----------
        list_dictionaries : list
            list of dictionaries

        Returns
        -------
        str
            '[]' if list is None or empty.
            The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        py_to_json = json.dumps(list_dictionaries)
        return py_to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.
        The filename must be: <Class name>.json - example: Rectangle.json.

        Parameters
        ----------
        list_objs : list
            a list of instances that inherit of Base
           example: list of Rectangle or list of Square instances
        """
        file_name = cls.__name__ + ".json"
        if list_objs is None or len(list_objs) == 0:
            with open(file_name, 'w') as jf:
                jf.write("[]")
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            with open(file_name, 'w') as jf:
                jf.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Convert a list of JSON string representation
        to python list.

        Parameters
        ----------
        json_string : str
            a string representing a list of dictionaries

        Returns
        -------
        list
            Empty list if json_string is a string representing
            a list of dictionaries.
            The list of the JSON string representation.
        """
        if json_string is None or len(json_string) == 0:
            return []
        json_to_py = json.loads(json_string)
        return json_to_py

    @classmethod
    def create(cls, **dictionary):
        """Return a dictionary of attributes of an instantiated
        class.

        Parameters
        ----------
        **dictionary : dict (keyworded arguments)
            a dictionary representation of an instance attributes.
        """
        if dictionary and dictionary != {}:
            #  has to be Rectangle or Square
            instance_name = cls.__name__
            if instance_name == "Rectangle":
                # create a dummy Rectangle instance assigned with
                # its mandatory attributes i.e 'width' and 'height'
                # (dummy attributes).
                new_instance = cls(3, 8)
            else:
                # create a dummy Square instance assigned with
                # its mandatory attributes i.e 'size'
                # (dummy attributes).
                new_instance = cls(2)
            new_instance.update(**dictionary)
            return new_instance
