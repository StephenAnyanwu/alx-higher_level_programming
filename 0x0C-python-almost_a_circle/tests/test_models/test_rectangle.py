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

    def test_rectangle_args_not_int(self):
        """
        Test of Rectangle class with arguments not int
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "3")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, "5")

    def test_rectangle_args_not_positive_or_zero(self):
        """
        Test of Rectangle class with arguments not positive or zero
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 3)
            Rectangle(0, 3)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3)
            Rectangle(2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -4)
            Rectangle(2, 3, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -5)
            Rectangle(2, 3, 4, 0)

    def test_rentangle_private_inst_attr(self):
        """
        Test of Rectangle class private instance attributes
        """
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)
            print(Rectangle(1, 2, 3, 4, 5).__height)
            print(Rectangle(1, 2, 3, 4, 5).__x)
            print(Rectangle(1, 2, 3, 4, 5).__y)


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


if __name__ == "__main__":
    unittest.main()
