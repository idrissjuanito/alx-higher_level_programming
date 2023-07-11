#!/usr/bin/python3

""" module for list class """


class MyList(list):
    """ subclass of the list class
        adds methods to the list class
    """
    def print_sorted(self):
        """ sorts and prints a list """
        lst = sorted(self)
        print(lst)
