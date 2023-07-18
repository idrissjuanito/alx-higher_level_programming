#!/usr/bin/python3
""" Module rectangle tests """
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ Rectangle test class """

    def test_id(self):
        r1 = Rectangle(9, 2)
        self.assertIs(r1.id, 1)
        r2 = Rectangle(4, 5, 2, 1, 9)
        self.assertIs(r2.id, 9)
