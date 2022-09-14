#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ky_1 = sorted(a_dictionary)
    for i in range(0, len(ky_1)):
        print("{:s}: {}".format(ky_1[i], a_dictionary[ky_1[i]]))
