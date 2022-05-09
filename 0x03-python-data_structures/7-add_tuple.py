#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 1:
        tuple_a = (tuple_a[0], 0)
    if b == 1:
        tuple_b = (tuple_b[0], 0)
    if a > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if b > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    if a == 0:
        tuple_a = (0, 0)
    if b == 0:
        tuple_b = (0, 0)
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]
    tuple_add = (sum_1, sum_2)
    return (tuple_add)
