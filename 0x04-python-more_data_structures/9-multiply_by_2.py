#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict()
    if not isinstance(a_dictionary, dict):
        return None
    if len(a_dictionary.keys()) < 1:
        return a_dictionary
    for k in a_dictionary.keys():
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
