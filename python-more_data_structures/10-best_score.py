#!/usr/bin/python3
def best_score(a_dictionary):
    if(a_dictionary is None or len(a_dictionary) == 0):
        return (None)
    key = a_dictionary.keys()
    j = 0
    key_max = ""
    for i in key:
        if a_dictionary[i] > j:
            j = a_dictionary[i]
            key_max = i
    return key_max
