#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len_list = len(my_list) - 1
    my_list.reverse()
    if (len_list == 0):
        return (None)
    for i in my_list:
        print("{:d}".format(i))
