#!/usr/bin/python3

""" This is module containing class on Rectangle """


class Rectangle:
    """ Rectangle class – empty for now
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle
        Returns:
            the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ getter for the height of the rectangle
        Returns:
            the height of the rectangle
        """
        return self.__width

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
