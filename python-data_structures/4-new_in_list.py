#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    len_list = len(my_list) - 1
    if (idx < 0):
        return (copy)
    if (idx > len_list):
        return (copy)
    copy[idx] = element
    return (copy)
