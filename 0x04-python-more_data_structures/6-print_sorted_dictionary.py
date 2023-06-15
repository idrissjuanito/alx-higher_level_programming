#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        keys = list(a_dictionary)
        keys.sort()
        for key in keys:
            print("{}: {}".format(key, a_dictionary[key]))
