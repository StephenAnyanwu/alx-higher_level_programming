#!/usr/bin/python3

"""
In this module defines a unittest for rectangle.py
"""


import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    Unittest for testing the Rectangle class
    """
    def test_rectangle_is_base(self):
        """
        Test if Rectangle is subclass of Base
        """
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(10, 2), Base)
        # This is not true:
        # self.assertTrue(isinstance(Rectangle, Base))

    def test_rectangle_no_arg(self):
        """
        Test of Rectangle class with no argument
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        """
        Test of Rectangle class with one argument
        """
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_rectangle_two_args(self):
        """
        Test of Rectangle class with two arguments
        """
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(4, 9)
        self.assertEqual(r2.id, r1.id + 1)

    def test_rectangle_three_args(self):
        """
        Test of Rectangle class with three arguments
        """
        r1 = Rectangle(2, 3, 4)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(4, 9, 7)
        self.assertEqual(r2.id, r1.id + 1)

    def test_rectangle_four_args(self):
        """
        Test of Rectangle class with four arguments
        """
        r1 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r2 = Rectangle(4, 9, 7, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_rectangle_five_args(self):
        """
        Test of Rectangle class with five arguments
        """
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        r2 = Rectangle(4, 9, 7, 2, 3)
        self.assertEqual(r2.id, 3)

    def test_rectangle_more_than_five_args(self):
        """
        Test of Rectangle class with more than five arguments
        """
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7)

    def test_rectangle_id(self):
        """
        Test of Rectangle class with id argument
        """
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 9)
        self.assertEqual(r2.id, r1.id + 1)
        r3 = Rectangle(2, 3, 5)
        self.assertEqual(r3.id, r2.id + 1)
        r4 = Rectangle(2, 3, 5, 6)
        self.assertEqual(r4.id, r3.id + 1)
        r5 = Rectangle(2, 3, 5, 6, 7)
        self.assertEqual(r5.id, 7)

    def test_rectangle_args_not_int(self):
        """
        Test of Rectangle class with arguments not int
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(6.8, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "3")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(6, 8.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "4")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, 9.4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, "5")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 3, 8, 7.2)

    def test_rectangle_args_zero(self):
        """
        Test of Rectangle class with arguments equal to zero
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0)
        r1 = Rectangle(2, 3, 0)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0

    def test_rectangle_args_not_positive(self):
        """
        Test of Rectangle class with arguments not positive
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -5)

    def test_rectangle_private_inst_attr(self):
        """
        Test of Rectangle class private instance attributes
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_width_getter(self):
        """
        Test of Rectangle width getter
        """
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)

    def test_width_setter(self):
        """
        Test of Rectangle width setter nethod
        """
        r = Rectangle(2, 3)
        r.width = 10
        self.assertEqual(r.width, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0

    def test_height_getter(self):
        """
        Test of Rectangle height getter
        """
        r = Rectangle(2, 3)
        self.assertEqual(r.height, 3)

    def test_height_setter(self):
        """
        Test of Rectangle height setter nethod
        """
        r = Rectangle(2, 3)
        r.height = 5
        self.assertEqual(r.height, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -2
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0

    def test_x_getter(self):
        """
        Test of Rectangle x getter
        """
        r = Rectangle(2, 3)
        self.assertEqual(r.x, 0)
        r2 = Rectangle(2, 3, 5)
        self.assertEqual(r2.x, 5)

    def test_x_setter(self):
        """
        Test of Rectangle x setter nethod
        """
        r = Rectangle(2, 3)
        r.x = 4
        self.assertEqual(r.x, 4)
        r.x = 0
        self.assertEqual(r.x, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -2

    def test_y_getter(self):
        """
        Test of Rectangle y getter
        """
        r = Rectangle(2, 3, 5)
        self.assertEqual(r.y, 0)
        r2 = Rectangle(2, 3, 5, 6)
        self.assertEqual(r2.y, 6)

    def test_y_setter(self):
        """
        Test of Rectangle y setter nethod
        """
        r = Rectangle(2, 3)
        r.y = 4
        self.assertEqual(r.y, 4)
        r.y = 0
        self.assertEqual(r.y, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -2

class TestRectangle_area_method(unittest.TestCase):
    """
    Unittest for testing the area method of Rectangle class
    """
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_changed_attributes(self):
        """
        Test of area method with changed attributes
        """
        r = Rectangle(2, 10, 3, 6, 9)
        r.width = 5
        r.height = 6
        self.assertEqual(30, r.area())


class TestRectangle_stdout(unittest.TestCase):
    """
    Unittest for testing the display and __str__  methods
    of Rectangle class
    """
    @ staticmethod
    def retrieve_from_stdout(rect_obj, method_name):
        """
        Retrieve and return the output of a method printed to
        the stdout

        Parameters:
        -----------
        rect_obj : Rectangle
            The rectangle object to print to stdout
        method_name : str
            The method to run on rect_obj

        Returns
        -------
        str
            The output of the method printed to stdout
        """
        #  Redirect stdout to a StringIO object
        output = io.StringIO()
        #  Save the original stdout
        sys.stdout = output
        if method_name == "display":
            rect_obj.display()
        else:
            rect_obj.__str__()
        #  Restore the original stdout
        sys.stdout = sys.__stdout__
        #  Retrieve and return the output from the StringIO object
        return output.getvalue()

    def test_display_method(self):
        """Test of display method"""
        #  Rectangle with width and height
        r1 = Rectangle(3, 4)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r1, "display")
        display_output = "###\n###\n###\n###\n"
        self.assertEqual(retrieved, display_output)
        #  Rectangle with width, height and x
        r2 = Rectangle(2, 3, 1)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r2, "display")
        display_output = " ##\n ##\n ##\n"
        self.assertEqual(retrieved, display_output)
        # Rectangle with width, height, x and y
        r3 = Rectangle(2, 3, 1, 1)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r3, "display")
        display_output = "\n ##\n ##\n ##\n"
        self.assertEqual(retrieved, display_output)

    def test_str_method(self):
        """Test of __str__ method"""
        #  Rectangle with width and height
        r1 = Rectangle(3, 4)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r1, "print")
        display = f"[Rectangle] ({r1.id}) 0/0 - 3/4\n"
        self.assertEqual(retrieved, display)
        #  Rectangle with width, height and x
        r2 = Rectangle(2, 3, 4)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r2, "print")
        display = f"[Rectangle] ({r2.id}) 4/0 - 2/3\n"
        self.assertEqual(retrieved, display)
        # Rectangle with width, height, x and y
        r3 = Rectangle(2, 3, 4, 5)
        retrieved = TestRectangle_stdout.retrieve_from_stdout(r3, "print")
        display = f"[Rectangle] ({r3.id}) 4/5 - 2/3\n"
        self.assertEqual(retrieved, display)


if __name__ == "__main__":
    unittest.main()
