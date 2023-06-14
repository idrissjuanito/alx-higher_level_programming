#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = list()
    for vector in matrix:
        new_matrix.append([n**2 for n in vector])
    return new_matrix
