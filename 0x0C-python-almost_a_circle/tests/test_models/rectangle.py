#!/usr/bin/python3
"""Tests for rectangle class """
from models.base from Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    def test_two_att(self):
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.id, 1)

    def test_five_att(self):
        r2 = Rectangle(2, 4, 0, 1, 90)
        self.assertEqual(r2.id, 90)