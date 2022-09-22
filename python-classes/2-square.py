#!/usr/bin/python3
"""This module define a square"""


class Square:
    """ This Square type class"""
    def __init__(self, size=0):
        """ This is privite instance attribute
        called size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
