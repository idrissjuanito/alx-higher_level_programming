#!/usr/bin/python3
""" Holds a Square class """


class Square:
    """ Square class to create square objects
    """
    def __init__(self, square__size=0, position=(0, 0)):
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

    def my_print(self):
        # Prints the area of the square with # symbol
        for i in range(self._Square__size + self.position[1]):
            if i < self.position[1]:
                print()
            else:
                for j in range(self._Square__size + self.position[0]):
                    if (j < self.position[0]):
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
        if not self._Square__size:
            print()

    @property
    def position(self):
        """Tuple that sets the position to start printing square

        Returns: instance position tuple
        """
        return self.position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value
