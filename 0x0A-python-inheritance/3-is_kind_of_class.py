#!/usr/bin/python3
""" module on python inheritance """


def is_kind_of_class(obj, a_class):
    """ check is obj is instance of super or subclass
    Args:
        obj (object): object to check
        a_class: class to check against
    Returns:
        True is obj is is instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    return False
