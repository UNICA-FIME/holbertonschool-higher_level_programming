#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_list = len(my_list) - 1
    if (idx < 0):
        return (my_list)
    if (idx > len_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
