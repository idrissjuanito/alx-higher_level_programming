#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if not isinstance(a_dictionary, dict):
        return None
    if not isinstance(key, str):
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
