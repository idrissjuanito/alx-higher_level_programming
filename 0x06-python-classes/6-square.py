#!/usr/bin/python3
""" Holds a Square class """


class Square:
    """ Square class to create square objects

    Attributes:
        position (tuple): position to start printing sqaure
        size (int): size of the square
    Args:
        position (tuple): position to start printing sqaure
        square__size (int): size of the square
    """
    def __init__(self, square__size=0, position=(0, 0)):
        self.size = square__size
        self.position = position

    def area(self):
        """Calculates the area of the square instance
        Returns:
            area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ getter for accessing the size attribute

        Returns:
            the current value of size attribute
        """
        return self.__size

    @property
    def position(self):
        """Tuple that sets the position to start printing square

        Returns:
            instance position tuple
        """
        return self.__position

    @position.setter
    def position(self, pos):
        if len(pos) != 2 or not type(pos[0] is int or not type(pos[1] is int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        # Prints the area of the square with # symbol
        if not self.__size:
            print()
        for s in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if (j < self.__position[0]):
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
