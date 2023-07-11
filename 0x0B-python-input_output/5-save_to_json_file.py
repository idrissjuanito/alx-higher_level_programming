#!/usr/bin/python3
""" Module with json data functions """
import json


def save_to_json_file(my_obj, filename):
    """ function for saving python data to file
    Args:
        my_obj (object): python data structure to save to file
        filename (str): file to save data to
    Returns:
        nothing
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
