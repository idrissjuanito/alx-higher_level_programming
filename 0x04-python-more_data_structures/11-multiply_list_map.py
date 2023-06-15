#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if not list:
        return None
    if len(my_list) < 1:
        return my_list
    new_list = list(map(lambda it: it * number, my_list))
    return new_list
