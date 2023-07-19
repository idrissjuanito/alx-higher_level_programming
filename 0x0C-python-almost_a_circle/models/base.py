#!/usr/bin/python3
""" Module contains base class """
import json


class Base():
    """ Base class for futur classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base class construtor
        Args:
            id (int): id of the current object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ Converts a dictionary to its json equivalent"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
