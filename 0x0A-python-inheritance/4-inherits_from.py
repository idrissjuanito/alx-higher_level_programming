#!/usr/bin/python3
""" Module on python inheritance """


def inherits_from(obj, a_class):
    """ checks if obj is instance of class
    Args:
        obj (object): object to check
        a_class: class to check against
    Returns:
        True if obj is related to a_class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
