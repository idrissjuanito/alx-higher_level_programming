#!/usr/bin/python3
""" test file for base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ test unit for the base class – inherits unittest's TestCase class """

    def test_assign_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_auto_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_assign_id(self):
        b3 = Base(39)
        self.assertEqual(b3.id, 39)
