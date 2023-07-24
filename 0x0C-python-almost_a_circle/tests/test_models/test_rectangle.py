#!/usr/bin/python3
"""Tests for rectangle class """
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_two_att(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 5)

    def test_three_att(self):
        r2 = Rectangle(3, 4, 6)
        self.assertEqual(r2.id, 4)

    def test_four_att(self):
        r3 = Rectangle(3, 2, 0, 0)
        self.assertEqual(r3.x, 0)

    def test_five_att(self):
        r4 = Rectangle(2, 4, 0, 1, 90)
        self.assertEqual(r4.y, 1)

    def test_wrong_type_att(self):
        try:
            r4 = Rectangle(3, "2")
        except Exception as e:
            self.assertEqual(e.__class__.__name__, "TypeError")
