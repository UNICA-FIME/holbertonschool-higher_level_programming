#!/usr/bin/python3
def element_at(my_list, idx):
    len_list = len(my_list)
    if (idx < 0 or len_list == 0):
        return (None)
    if (idx >len_list):
        return (None)
    return (my_list[idx])

