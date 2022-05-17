#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    z = 0
    k = 0
    try:
        for i in my_list[:x]:
            print("{0}".format(i), end="")
            z = z + 1
        print()
        return (z)
    except IndexError:
        for a in my_list:
            print("{0}".format(a), end="")
            k = k + 1
        print()
        return (k)
