#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    a = len(my_list)
    if idx >= a - 1 or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
