#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()
    if not set_1 or not set_2:
        return set()
    for s in set_1:
        for ss in set_2:
            if s == ss:
                new_set.add(ss)
                break
    return new_set
