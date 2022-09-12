#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    new_list = list(my_string)
    for i in new_list:
        if i in "Cc":
            new_list.remove(i)
    return ("".join(new_list))
