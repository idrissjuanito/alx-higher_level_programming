#!/usr/bin/python3
"""Tests for rectangle class """
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_two_att(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.id, 9)

    def test_three_att(self):
        r2 = Rectangle(3, 4, 6)
        self.assertEqual(r2.x, 6)

    def test_four_att(self):
        r3 = Rectangle(3, 2, 0, 2)
        self.assertEqual(r3.y, 2)

    def test_string_height(self):
        try:
            rec2 = Rectangle(3, "2")
        except TypeError as e:
            self.assertEqual(e.__str__(), "height must be an integer")

    def test_zero_width(self):
        try:
            rec = Rectangle(0, 9)
        except ValueError as e:
            self.assertEqual(e.__str__(), "width must be > 0")

    def test_zero_height(self):
        try:
            rec6 = Rectangle(3, 0)
        except ValueError as e:
            self.assertEqual(e.__str__(), "height must be > 0")

    def test_negative_width(self):
        try:
            rec4 = Rectangle(-1, 3)
        except ValueError as e:
            self.assertEqual(e.__str__(), "width must be > 0")

    def test_string_width(self):
        try:
            rec3 = Rectangle("2", 3)
        except TypeError as e:
            self.assertEqual(e.__str__(), "width must be an integer")
