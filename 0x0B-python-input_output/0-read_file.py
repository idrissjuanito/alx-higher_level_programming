#!/usr/bin/python3

""" Module on file reading """

def read_file(filename=""):
    """ reads a file and and prints the content to stdout
    Args:
        filename (str): the file to read
    Returns: nothing
    """
    with open(filename, "r") as fl:
        print(fl.read())
