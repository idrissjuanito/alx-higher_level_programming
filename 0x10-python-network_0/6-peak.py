#!/usr/bin/python3
"""Looks for peaks in a list"""
def find_peak(list_of_integers):
    """ Finds and returns a peak from given list """
    llen = len(list_of_integers)
    peakindex = None
    if llen < 1: return None
    if llen == 1: return list_of_integers[0]
    for i in range(llen):
        if i == llen - 1:
            if not peakindex:
                peakindex = i
            break
        if list_of_integers[i] > list_of_integers[i+1]:
            if i > 0 and list_of_integers[i] < list_of_integers[i-1]:
                continue
            peakindex = i
        if peakindex != None and list_of_integers[i] == list_of_integers[i+1]:
            break;
    return list_of_integers[peakindex]
