#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()
    if not set_1 and not set_2:
        return new_set 
    if not set_1 and set_2:
        return set_2
    if not set_2:
        return set_1
    new_set = set_1.difference(set_2)
    new_set.update(set_2.difference(set_1))
    return new_set
