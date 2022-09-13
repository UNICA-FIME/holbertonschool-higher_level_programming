#!/usr/bin/python3
def max_integer(my_list=[]):
    tmp = 0
    len_1 = len(my_list) - 1
    if (len_1 == -1):
        return (None)
    for i in range(0, len_1):
        for j in range(0, len_1):
            if (my_list[j] < my_list[j + 1]):
                tmp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = tmp
    return(my_list[0])
