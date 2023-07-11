#!/usr/bin/python3

""" Module with file appending functions """


def append_write(filename="", text=""):
    """ Appends text to a file
    Args:
        filename (str): the file to read
        text: the content to append to file
    Returns:
        the number of characters written
    """
    char = 0
    with open(filename, "a") as fl:
        char = fl.write(text)
    return char
