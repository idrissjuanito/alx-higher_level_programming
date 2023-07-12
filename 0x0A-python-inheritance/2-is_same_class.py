#!/usr/bin/python3

""" Module on class type """


def is_same_class(obj, a_class):
    """ Function checks if an object is of type a class
    Args:
        obj (object): to check
        a_class: class to compare against
    Returns:
        True if obj is of type a_class or false
    """
    if type(obj) is a_class:
        return True
    return False
