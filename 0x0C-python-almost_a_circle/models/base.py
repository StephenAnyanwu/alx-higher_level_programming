#!/usr/bin/python3

"""
In this model defines a class Base
"""

import json
import csv
import turtle


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
    load_from_file()
        Return a list of classes instantiated from a file of
        JSON strings (class method).
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

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of
        JSON strings.
        The filename must be: <Class name>.json -
        example: Rectangle.json


        Returns
        -------
        list
            An empty list if the file does not exist, otherwise
            a list of instantiated classes.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as jf:
                json_string = jf.read()
                list_dicts = Base.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except IOError as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.
        The filename must be: <Class name>.csv -
        example: Rectangle.csv

        Parameters
        ----------
        list_objs : list
            a list of instances that inherit of Base example:
            list of Rectangle or list of Square instances
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        The filename must be: <Class name>.csv -
        example: Rectangle.csv

        Returns:
            An empty list if file does not exist,
            otherwise a list of instantiated classes.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError as e:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Parameters
        ----------
        list_rectangles : list
            A list of Rectangle objects to draw.
            list_squares : list
                A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()
