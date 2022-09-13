#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_mt = 0
    for elen in matrix:
        len_mt += len(elen)
    if (len_mt == 0):
        print()
    for matrix_1 in matrix:
        count = len(matrix_1)
        t = 1
        for j in matrix_1:
            if (t < count):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
            t += 1
        t = 0
