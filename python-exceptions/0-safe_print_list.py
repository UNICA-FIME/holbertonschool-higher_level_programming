#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(1, x+1):
            print("{}".format(my_list[i - 1]), end="")
        print()
    except IndexError:
        i = i - 1
        print()
    return (i)
