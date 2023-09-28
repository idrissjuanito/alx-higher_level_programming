#!/usr/bin/python3
"""Looks for peaks in a list"""
def find_peak(list_of_integers):
    """ Finds and returns a peak from given list """
    llen = len(list_of_integers)
    peakindex = 0
    if llen < 1: return None
    for i in range(1, llen):
        if list_of_integers[i] < list_of_integers[i-1]:
            continue
        if i + 1 == llen:
            peakindex = i
            break
        if list_of_integers[i] == list_of_integers[i+1]:
            break;
        if list_of_integers[i] > list_of_integers[i+1]:
            peakindex = i
            i += 2
    return list_of_integers[peakindex]
