#!/usr/bin/python3
""" test file for base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """ test unit for the base class – inherits unittest's TestCase class """

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(23)
        self.assertEqual(b3.id, 23)
