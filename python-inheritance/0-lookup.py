#!/usr/bin/python3
"""This module create a function"""


def lookup(obj):
    """This is a function that return the list
    of available attribute and methods of an
    object

    Arg:
        obj: This is a parameter obj

    Return:
        The list of attribute ande methodos of a object
    """
    return (dir(obj))
