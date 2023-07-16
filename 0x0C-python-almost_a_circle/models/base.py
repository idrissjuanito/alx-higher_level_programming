#!/usr/bin/python3
""" Module contains base class """


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
