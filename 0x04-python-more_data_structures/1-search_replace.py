#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list()
    if not my_list or not replace:
        return None
    for item in my_list:
        if item == search:
            new_list.append(replace)
            continue
        new_list.append(item)
    return new_list
