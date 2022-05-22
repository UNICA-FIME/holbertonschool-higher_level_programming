#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_cp = my_list[:]
    a = len(my_list)
    for i in range(a):
        if my_list_cp[i] == search:
            my_list_cp[i] = replace
        else:
            my_list_cp[i] = my_list_cp[i]
    return my_list_cp
