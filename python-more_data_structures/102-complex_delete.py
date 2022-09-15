#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = a_dictionary.keys()
    v = list(map(lambda x: x if(a_dictionary[x] == value) else None, key))
    for i in v:
        if (i is not None):
            del a_dictionary[i]
    return (a_dictionary)
