#!/usr/bin/python3
"""
    module holds function for addition
"""
def add_integer(a, b=98):
    """ Calculates the sum of two numbers
    Args:
        a (int): first number
        b (int): second number
    Returns:
        The result of the addition
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
