#!/usr/bin/python3
""" Module with Geometry class """


class BaseGeometry:
    """ Class for a base geometry """
    def area(self):
        """ calculates the area of a shape"""
        raise Exception("area() is not implemented")
