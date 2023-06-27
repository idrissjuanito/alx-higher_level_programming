#!/usr/bin/python3

def max_integer(my_list=[]):
    mx_num = None
    for num in my_list:
        if (not mx_num):
            mx_num = num
        elif (num > mx_num):
            mx_num = num
    return mx_num
