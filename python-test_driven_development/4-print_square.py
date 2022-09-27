#!/usr/bin/python3
"""This module print square"""


def print_square(size):
    """This function print area square with #"""
    if (type(size) is not int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    new_list = ["#" * size for i in range(0, size)]
    print("\n".join(new_list))
