#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list()
    if not my_list:
        return new_list
    if len(my_list) < 1:
        return new_list
    for item in my_list:
        if item == search:
            new_list.append(replace)
            continue
        new_list.append(item)
    return new_list
