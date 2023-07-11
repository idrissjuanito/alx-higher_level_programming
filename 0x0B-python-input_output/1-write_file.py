#!/usr/bin/python3

""" Module with file writing functions """


def write_file(filename="", text=""):
    """ Writes text to a file
    Args:
        filename (str): the file to read
        text: the content to write to file
    Returns:
        the number of characters written
    """
    char = 0
    with open(filename, "w") as fl:
        char = fl.write(text)
    return char
