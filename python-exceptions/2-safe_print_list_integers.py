#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    while (i < x):
        try:
            for i in range(i, x):
                print("{:d}".format(my_list[i]), end="")
                j = j + 1
        except (ValueError, TypeError):
            print(end="")
        i = i + 1
    print()
    return (j)
