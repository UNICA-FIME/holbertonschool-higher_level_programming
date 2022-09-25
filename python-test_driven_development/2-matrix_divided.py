#!/usr/bin/python3
"""This is module implements a function that
splits the elements of an array
"""


def matrix_divided(matrix, div):
    """This is function fot div the element of matrix"""
    if (not matrix or type(matrix[0]) != list):
        raise TypeError('''matrix must be a matrix (list of lists) \
of integers/floats''')
    for i in matrix:
        if (type(i) is not list or len(i) == 0):
            raise TypeError('''matrix must be a matrix (list of lists) \
of integers/floats''')
        if (len(i) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if (type(j) not in (int, float) or j != j):
                raise TypeError('''matrix must be a matrix (list of lists) \
of integers/floats''')
    if (type(div) not in (int, float)):
        raise TypeError("div must be a number")
    elif (div == 0):
        raise ZeroDivisionError("division by zero")
    t = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (t)
