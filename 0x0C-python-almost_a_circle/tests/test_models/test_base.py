#!/usr/bin/python3
""" test file for base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ test unit for the base class – inherits unittest's TestCase class """

    def test_base(self):
        b = Base()
        self.assertIsNotNone(b.id)
        self.assertIs(b.id, 1)
        b2 = Base()
        self.assertIs(b2.id, 2)
        b3 = Base(23)
        self.assertIs(b3.id, 23)
