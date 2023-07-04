#!/usr/bin/python3

""" Module holds function for printing names """

def say_my_name(first_name, last_name=""):
    """ function prints a person's name in a string

    Args:
        first_name (string): the persons first name mandatory
        last_name (string): the person's second name optional

    Returns:
        Nothing
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is "+ first_name +" "+ last_name)
