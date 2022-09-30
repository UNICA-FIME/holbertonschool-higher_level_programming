#!/usr/bin/python3
"""Definition of function is sub class"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified
    class ; otherwise False
    Arg:
      obj: This is a parameter type object
      a_class: This is a parameter type class
    """

    if (type(obj) is a_class):
        return False
    if (isinstance(obj, a_class) is True):
        return True
