#!/usr/bin/python3

""" module for working with json data """


import json


def from_json_string(my_str):
    """ converts a json string to an object
    Args:
        my_str (str): the json string to convert to object
    Returns:
        a python data structure from string
    """
    return json.loads(my_str)
