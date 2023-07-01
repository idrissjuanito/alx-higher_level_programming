#!/usr/bin/python3
"""
    module holds function for addition
"""
def add_integer(a, b=98):
    """
        Returns the addition of two numbers
        a (int): first number
        b (int): second number
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
