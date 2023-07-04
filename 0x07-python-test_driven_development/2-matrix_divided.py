#!/usr/bin/python3
"""contains functions for matrix manipulation"""

def matrix_divided(matrix, div):
    """Divides elements of a matrix by a given divider
    Args:
        my_list (list): The matrix
        div (int/float): the divider
    Returns:
        A new matrix with the new values after division
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not type(div) is int and not type(div) is float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_len = 0
    for mat in matrix:
        if not type(mat) is list or len(mat) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not row_len:
            row_len = len(mat)
        if len(mat) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        row_list = []
        for elm in mat:
            if not type(elm) is int and not type(elm) is float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row_list.append(round((elm / div), 2))
        new_matrix.append(row_list)
    return new_matrix
