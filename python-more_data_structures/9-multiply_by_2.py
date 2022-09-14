#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    keys_1 = a_dictionary.keys()
    for i in keys_1:
        if i in a_dictionary:
            new_dict[i] = a_dictionary[i] * 2
    return (new_dict)
