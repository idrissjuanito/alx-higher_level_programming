#!/usr/bin/python3
"""Module contains json data file ops funcs"""
import json


def load_from_json_file(filename):
    """ function loads json data from a file
    Args:
        filename (str): file to read
    Returns:
        nothing
    """
    with open(filename, "r") as fl:
        data = json.load(fl)
    return data
