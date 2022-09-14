#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    sum_t = 0
    for i in new_set:
        sum_t = sum_t + i
    return (sum_t)
