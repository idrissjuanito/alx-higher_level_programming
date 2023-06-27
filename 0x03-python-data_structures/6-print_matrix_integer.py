#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for elm in mat:
            print("{:d}".format(elm), end=" " if elm != mat[-1] else "")
        print()
