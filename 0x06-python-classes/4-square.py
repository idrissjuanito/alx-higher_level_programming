#!/usr/bin/python3
""" Holds a Square class """


class Square:
    """ Square class to create square objects

    Attributes:
        Square__size (int): size of the square

    Args:
        square__size: total size of the square
    """
    def __init__(self, square__size=0):
        self._Square__size = square__size

    def area(self):
        """Calculates the area of the square instance
        Returns:
            area of the square
        """
        return self._Square__size ** 2

    @property
    def size(self):
        """ getter for accessing the size attribute

        Returns:
            the current value of size attribute
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """Setter for safely setting the value of square size

        Args:
            value: the value to assign to square__size
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
