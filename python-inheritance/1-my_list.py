#!/usr/bin/python3
"""This is a module for create a function sort"""


class MyList(list):
    """This is a class what create a type de what sort list

    Attributes:
         list: inherits
    """
    def print_sorted(self):
        """prints the sorted list"""
        list_t = []
        for k in self:
            list_t.append(k)
        for i in range(0, len(list_t)):
            for j in range(0, len(list_t) - 1):
                if list_t[j] > list_t[j + 1]:
                    aux = list_t[j]
                    list_t[j] = list_t[j + 1]
                    list_t[j + 1] = aux
        print(list_t)
