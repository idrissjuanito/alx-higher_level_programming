#!/usr/bin/python3
""" Module for serializing a class attributes to JSON"""


def class_to_json(obj):
    """
    Functions serializes an objects attributes to json
    Args:
        obj (object): the object to serialize
    Returns:
        dictionnary attributes
    """
    return obj.__dict__
