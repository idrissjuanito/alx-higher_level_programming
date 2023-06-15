#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary.keys()) < 1:
        return None
    cur_best = None
    for k in a_dictionary.keys():
        num = a_dictionary[k]
        if not cur_best or num > a_dictionary[cur_best]:
            cur_best = k
    return cur_best
