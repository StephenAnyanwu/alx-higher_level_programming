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
    """Unittest for testing the Base class"""
    def test_base_no_arg(self):
        """Test if base class has no arguments"""
        b = Base()
        self.assertEqual(b.id, b.id + 1)

if __name__ == "__main__":
    unittest.main()
