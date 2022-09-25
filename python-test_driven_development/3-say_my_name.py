#!/usr/bin/python3
"""This module implements a function that
allows to print an string
"""


def say_my_name(first_name, last_name=""):
    """This a function that print two string

    Arg:
        first_name: This first date string
        last_name: This second date string
    """
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
