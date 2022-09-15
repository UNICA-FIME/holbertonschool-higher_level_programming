#!/usr/bin/python3
def weight_average(my_list=[]):
    list_1 = list(map(lambda x: x[0]*x[1], my_list))
    list_2 = list(map(lambda y: y[1], my_list))
    return (sum(list_1) / sum(list_2))
