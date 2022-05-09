#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a < 2 and a != 0:
        tuple_a = (tuple_a[0], 0)
    elif b < 2 and b != 0:
        tuple_b = (tuple_b[0], 0)
    elif a > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    elif b > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    elif a == 0:
        tuple_a = (0, 0)
    elif b == 0:
        tuple_b = (0, 0)
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]
    tuple_add = (sum_1, sum_2)
    return (tuple_add)
