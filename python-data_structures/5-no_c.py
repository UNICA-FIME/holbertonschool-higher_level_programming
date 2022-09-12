#!/usr/bin/python3
def no_c(my_string):
    new_list_1 = []
    new_list = list(my_string)
    for i in new_list:
        if (i != 'c' and i != 'C'):
            new_list_1.append(i)

    return ("".join(new_list_1))
