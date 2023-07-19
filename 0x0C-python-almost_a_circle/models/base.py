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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a dictionary to its json equivalent"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return json.dumps(list())
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves the content of the instances in list_objs to json file
        Params:
            list_objs (list): list of intances to save
        """
        lst = list()
        if list_objs and len(list_objs) > 0:
            for ins in list_objs:
                lst.append(ins.to_dictionary())
        json_str = cls.to_json_string(lst)
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as fl:
            fl.write(json_str)
