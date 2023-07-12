#!/usr/bin/python3
""" rectangle class module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherit geometry base class
    Attributes:
        width (int): width of the rectangle
        height (int): height of the integer
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
