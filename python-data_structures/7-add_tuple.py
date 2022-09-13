#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x_1 = 0
    x_2 = 0
    y_1 = 0
    y_2 = 0
    x_t = 0
    y_t = 0
    if (len(tuple_a) < 2 and len(tuple_a) >= 1):
        x_1 = tuple_a[0]
        x_2 = 0
    elif (len(tuple_a) > 2):
        tuple_a1 = taple_a[0:2]
        x_1, x_2 = tuple_a1
    elif (len(tuple_a) == 0):
        x_1 = 0
        x_2 = 0
    else:
        x_1, x_2 = tuple_a
    if (len(tuple_b) < 2 and len(tuple_b) >= 1):
        y_1 = tuple_b[0]
        y_2 = 0
    elif(len(tuple_b) > 2):
        tuple_b1 = tuple_b[0:2]
        y_1, y_2 = tuple_b1
    elif (len(tuple_b) == 0):
        y_1 = 0
        y_2 = 0
    else:
        y_1, y_2 = tuple_b
    x_t = x_1 + y_1
    y_t = x_2 + y_2
    return (x_t, y_t)
