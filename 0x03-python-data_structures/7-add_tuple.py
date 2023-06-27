#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    lst = []
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    for i in range(2):
        sum = tuple_a[i] if i < len_a else 0
        sum += tuple_b[i] if i < len_b else 0
        lst.append(sum)
    return tuple(lst)
