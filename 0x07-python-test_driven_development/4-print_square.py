#!/usr/bin/python3

""" square module """

def print_square(size):
    """ Function for printing the square 
    Args:
        size (int): size of a the square
    Returns: nothing
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
