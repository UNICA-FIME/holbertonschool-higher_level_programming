#!/usr/bin/python3
"""Definition of function is_same_class"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    Arg:
       obj : parameter type object
       a_class: parameter type class

    """
    if (isinstance(obj, a_class) is True):
        return True
    else:
        return False
