#!/usr/bin/python3

""" This is module containing class on Rectangle """


class Rectangle:
    """ Rectangle class – empty for now
    Args:
        number_of_instances (int): number of active instances of this class
        print_symbol (any): symbol for printing area of rect

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        strn = ""
        for i in range(self.height):
            for i in range(self.width):
                strn += str(self.print_symbol)
            strn += "\n"
        return strn[:-1]

    def __repr__(self):
        return "Rectangle("+str(self.width)+", "+str(self.height)+")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter for the width of the rectangle
        Returns:
            the width of rectangle
        """
        return self._Rectangle__width

    @width.setter
    def width(self, width):
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width

    @property
    def height(self):
        """ getter for the height of the rectangle
        Returns:
            the height of the rectangle
        """
        return self._Rectangle__height

    @height.setter
    def height(self, height):
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

    def area(self):
        """ calculates the area of the rectangle instance

        Returns:
            area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """ calculates the perimeter of the rectangle

        Returns:
            the perimeter calculated
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares the area of two Rectangle objects

        Args:
            rect_1 (Rectangle): first rectangle object
            rect_2 (Rectangle): second rectangle object
        Returns:
            the rectangle withe biggest area
        """
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_2.area() == rect_1.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Creates a new square rectangle

        Args:
            size (int): size of the square
            cls (Rectangle): class represents the current class

            Returns: new instance of Rectangle class with size
        """
        return cls(size, size)
