#!/usr/bin/python3

"""
In this module defines a unittest for base.py
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Unittest for testing the Base class"
    """
    def test_base_no_arg(self):
        """
        Test Base class with no arguments
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, b1.id + 1)

    def test_base_with_arg(self):
        """
        Test of Base class with argument (id)
        """
        b1 = Base(12)
        b2 = Base(89)
        b3 = Base(4.5)
        b4 = Base("str")
        b5 = Base(True)
        b6 = Base([3, 4, 5])
        b7 = Base((3, 4, 5))
        b8 = Base({"a": 3, "b": 4, "c": 5})
        b9 = Base(complex(2, 3))
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 89)
        self.assertEqual(b3.id, 4.5)
        self.assertEqual(b4.id, "str")
        self.assertEqual(b5.id, True)
        self.assertEqual(b6.id, [3, 4, 5])
        self.assertEqual(b7.id, (3, 4, 5))
        self.assertEqual(b8.id, {"a": 3, "b": 4, "c": 5})
        self.assertEqual(b9.id, complex(2, 3))

    def test_base_with_multiple_arg(self):
        """
        Test of Base class with multiple argument (id, *args)
        """
        with self.assertRaises(TypeError):
            b1 = Base(12, 13)
            b2 = Base(12, "str")
            b3 = Base(12, 13, 14)


class TestBase_to_json_string_method(unittest.TestCase):
    """
    Unittest for testing the to_json_string method of Base class
    """
    def test_base_private_attr(self):
        """
        Test of the Base class private attribute
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_to_json_string_no_arg(self):
        """
        Test of to_json_string method with no argument
        """
        b = Base()
        with self.assertRaises(TypeError):
            b.to_json_string()

    def test_to_json_string_arg_None(self):
        """
        Test of to_json_string method with argument equals None
        """
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")
        self.assertEqual(Base().to_json_string(None), "[]")

    def test_to_json_string_arg_empty_list(self):
        """
        Test of to_json_string method with argument equals empty list
        """
        b = Base()
        self.assertEqual(b.to_json_string([]), "[]")
        self.assertEqual(Base().to_json_string([]), "[]")

    def test_to_json_string_arg_list_of_dicts(self):
        """
        Test of to_json_string method with argument equals
        list of dictionaries
        """
        b = Base()
        self.assertEqual(b.to_json_string([{"id": 2}]), '[{"id": 2}]')
        self.assertEqual(Base().to_json_string([{"id": 2}]), '[{"id": 2}]')

    def test_to_json_string_type_check(self):
        """
        Test the return type of to_json_string method
        """
        r = Rectangle(2, 3, 4, 5, 6)
        s = Square(2, 3, 4, 5)
        r_dictionary = r.to_dictionary()
        s_dictionary = s.to_dictionary()
        self.assertEqual(str, type(Base().to_json_string([r_dictionary])))
        self.assertEqual(str, type(Base().to_json_string([s_dictionary])))

    def test_to_json_strin_mulitple_arg(self):
        """Test of to_json_string method with multiple argument"""
        with self.assertRaises(TypeError):
            Base().to_json_string([], 5)


class TestBase_from_json_string_method(unittest.TestCase):
    """
    Unittest for testing the from_json_string method of Base class
    """
    def test_from_json_string_no_arg(self):
        """
        Test of from_json_string method with no argument
        """
        with self.assertRaises(TypeError):
            Base().from_json_string()

    def test_from_json_string_arg_None(self):
        """
        Test of from_json_string method with argument
        (json_string)equals None
        """
        self.assertEqual(Base().from_json_string(None), [])

    def test_from_json_string_arg_not_string(self):
        """
        Test of from_json_string method with argument
        (json_string)not a string
        """
        with self.assertRaises(TypeError):
            Base().from_json_string(5)
            Base().from_json_string(True)
            Base().from_json_string(5.5)

    def test_from_json_string_arg_empty_string(self):
        """
        Test of from_json_string method with
        argument (json_string)equals empty string
        """
        self.assertEqual(Base().from_json_string(""), [])

    def test_from_json_string_with_rectangle(self):
        """
        Test of from_json_string method with
        dictionary of Rectangle
        """
        r = Rectangle(2, 3, 4, 5, 6)
        r_dictionary = r.to_dictionary()
        dict_list = Base().to_json_string([r_dictionary])
        r_d = [r_dictionary]
        self.assertEqual(Base().from_json_string(dict_list), r_d)
        list_input = [
                        {'id': 89, 'width': 10, 'height': 4},
                        {'id': 7, 'width': 1, 'height': 7}
                    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_from_json_string_with_square(self):
        """
        Test of from_json_string method with dictionary of Square
        """
        s = Rectangle(2, 3, 4)
        s_dictionary = s.to_dictionary()
        dict_list = Base().to_json_string([s_dictionary])
        s_d = [s_dictionary]
        self.assertEqual(Base().from_json_string(dict_list), s_d)
        list_input = [
                        {'id': 89, 'size': 10},
                        {'id': 7, 'size': 1}
                    ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_from_json_string_type(self):
        """
        Test the return type of from_json_string method
        """
        l1 = '[{"id": 2}]'
        l2 = '[5, "hello", 6.5]'
        self.assertEqual(type(Base().from_json_string(l1)), list)
        self.assertEqual(type(Base().from_json_string(l2)), list)
        d1 = '{"size": 10}'
        self.assertEqual(type(Base().from_json_string(d1)), dict)
        self.assertEqual(type(Base().from_json_string('5')), int)
        self.assertEqual(type(Base().from_json_string('6.5')), float)
        self.assertEqual(type(Base().from_json_string('true')), bool)

    def test_from_json_string_no_args(self):
        """
        Test of from_json_string method with no argument
        """
        with self.assertRaises(TypeError):
            Base().from_json_string()

    def test_from_json_string_mutilple_args(self):
        """
        Test of from_json_string method with multiple argument
        """
        with self.assertRaises(TypeError):
            Base().from_json_string('[]', "hello")


class TestBase_save_to_file_method(unittest.TestCase):
    """
    Unittest for testing the save_to_file method of Base class
    """

    @classmethod
    def tearDown(cls):
        """
        Delete any created files.
        """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_no_arg(self):
        """
        Test of save_to_file method with no argument
        """
        with self.assertRaises(TypeError):
            Base.save_to_file()
            Rectangle.save_to_file()
            Square.save_to_file()

    def test_save_to_file_arg_None(self):
        """
        Test of save_to_file method with argument (list_objs)
        equals None
        """
        Base.save_to_file(None)
        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        file_list = [
                        "Base.json",
                        "Rectangle.json",
                        "Square.json"
                    ]
        for file in file_list:
            with open(file, "r") as jf:
                file_content = jf.read()
                self.assertEqual(file_content, "[]")

    def test_save_to_file_arg_empty_list(self):
        """
        Test of save_to_file method with argument (list_objs)
        equals empty list
        """
        Base.save_to_file([])
        Rectangle.save_to_file([])
        Square.save_to_file([])
        file_list = [
                        "Base.json",
                        "Rectangle.json",
                        "Square.json"
                    ]
        for file in file_list:
            with open(file, "r") as jf:
                file_content = jf.read()
                self.assertEqual(file_content, "[]")

    def test_save_to_file_arg_list_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_arg_list_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_arg_list_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_arg_list_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        """
        Test of save_to_file method for different object
        and different file name
        """
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """
        Test of save_to_file method previously created or
        existing file
        """
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_arg_list_one_rectangle_one_square(self):
        """
        Test of save_to_file method with argument (list_objs)
        equals list of one rectangle and one square
        """
        r = Rectangle(10, 7, 2, 8, 5)
        s = Square(2, 4, 1, 2)
        Rectangle.save_to_file([r, s])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 91)


if __name__ == "__main__":
    unittest.main()
