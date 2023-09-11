#!/usr/bin/python3
""" Module with Geometry class """


class BaseGeometry:
    """ Class for a base geometry """
    def area(self):
        """ calculates the area of a shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a value """
        if type(value) != int:
            raise TypeError(name+" must be an integer")
        if value <= 0:
            raise ValueError(name+" must be greater than 0")
