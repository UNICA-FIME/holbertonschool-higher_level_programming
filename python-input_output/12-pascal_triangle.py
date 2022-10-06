#!/usr/bin/python3
"""This is a module"""


def pascal_triangle(n):
    """This is a method that returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if (n <= 0):
        return ([])
    a = []
    for i in range(1, n + 1):
        b = []
        for j in range(0, i):
            if (j == 0):
                b.append(1)
            if (j == i - 1) and (j != 0):
                b.append(1)
            if (j == 1 and j < i - 1):
                for k in range(1, len(a[i - 2])):
                    b.append(a[i - 2][k - 1] + a[i - 2][k])
        a.append(b)
    return (a)
