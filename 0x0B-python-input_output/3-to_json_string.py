#!/usr/bin/python3

""" module for working with json data """


import json


def to_json_string(my_obj):
    """ converts an object in to json string
    Args:
        my_obj (object): the object to convert
    Returns:
        the json representation of the object
    """
    return json.dumps(my_obj)
