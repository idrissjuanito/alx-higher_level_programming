#!/usr/bin/python3
""" Module for square class """
from models.rectangle import Rectangle, validate_int


class Square(Rectangle):
    """ class square inherits from rectangle

    Attributes:
        size (int): size of square
        x (int): character offset
        y (int): line offset
        id (int): id of instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """ Getter method for sqaure size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the size of square """
        validate_int("width", value)
        self.__size = value

    def update(self, *args, **kwargs):
        """ updates the values of the square attributes

        params:
            args (list): list of value passed
            kwargs (dict): dictionary with values and their bindings
        Returns: nothing
        """
        if not args or len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
            return
        attr = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, attr[i], args[i])

    def to_dictionary(self):
        """ Returns the dictionary representation of the class """
        return self.__dict__
