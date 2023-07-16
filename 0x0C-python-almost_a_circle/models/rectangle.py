#!/usr/bin/python3
""" Module rectangle """
from models.base import Base


def validate_int(binding, value):
    """ Validates if value is an integer
    Params:
        binding (str): name of the element to validate
        value (int): value to validate
    Returns: nothing
    """
    if not type(value) is int:
        raise TypeError(binding+" must be an integer")
    if binding == "width" or binding == "height":
        if not value > 0:
            raise ValueError(binding+" must be > 0")
    else:
        if not value >= 0:
            raise ValueError(binding+" must be >= 0")


class Rectangle(Base):
    """ Rectangle class based on base class
    attributes:
        width (int): private width att for rectangle
        height (int): private height rectangle
        x (int): unknown
        y (int): private unknown
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        w = self.width
        h = self.height
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {w}/{h}"

    @property
    def width(self):
        """ Getter for width private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width attribute """
        validate_int("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter for private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private attribute height """
        validate_int("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter for x private attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x attribute """
        validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter for y private attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y private attribute """
        validate_int("y", value)
        self.__y = value

    def area(self):
        """ computes the area of the rectangle instance """
        return self.width * self.height

    def display(self):
        """ Displays to standard output """
        for r in range(self.height):
            for h in range(self.width):
                print("#", end="")
            print()
