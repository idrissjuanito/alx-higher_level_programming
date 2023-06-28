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
        """Setter for safely setting the value of square size

        Args:
            value: the value to assign to square__size
        """
        if not type(pos) is tuple or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        # raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

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
        self.__size = value

    def my_print(self):
        # Prints the area of the square with # symbol
        for i in range(self.__size + self.__position[1]):
            if i < self.__position[1]:
                print()
            else:
                for j in range(self.__size + self.__position[0]):
                    if (j < self.__position[0]):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        if not self.__size:
            print()
