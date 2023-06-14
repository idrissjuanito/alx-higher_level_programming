#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return None
    if len(my_list) < 1:
        return None
    new_list = sorted(my_list)
    last_num = None
    sum = 0
    for n in new_list:
        if not n == last_num:
            sum += n
            last_num = n
    return sum
