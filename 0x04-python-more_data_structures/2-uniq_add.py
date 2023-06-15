#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    if not my_list:
        return sum
    if len(my_list) < 1:
        return sum
    new_list = sorted(my_list)
    last_num = None
    for n in new_list:
        if not n == last_num:
            sum += n
            last_num = n
    return sum
