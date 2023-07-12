#!/usr/bin/python3
""" Module for class Student """


class Student:
    """ class that defines a student

    Attributes:
        first_name (str): student name
        last_name (str): student's last name
        age (int): student age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
