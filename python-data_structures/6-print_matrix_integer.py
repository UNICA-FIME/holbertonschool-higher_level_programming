#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for matrix_1 in matrix:
        count = len(matrix_1)
        t = 1
        for j in matrix_1:
            if (t < count):
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j))
            t += 1
        t = 0
