#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    f = len(matrix)
    c = len(matrix[0])
    matrix_cp = [x[:] for x in matrix]
    for i in range(f):
        for j in range(c):
            matrix_cp[i][j] = matrix_cp[i][j]**2
    return(matrix_cp)
