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
        if not type(square__size) is int:
            raise TypeError("size must be an integer")
        if square__size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = square__size

    def area(self):
        """Calculates the area of the square instance
        Returns:
            area of the square
        """
        return self._Square__size ** 2
