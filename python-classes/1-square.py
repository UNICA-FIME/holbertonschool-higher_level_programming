#!/usr/bin/python3
"""This module Create a type square class"""


class Square:
    """ This Class define a square with instance
    attribute Privite named size
    """
    def __init__(self, size):
        """The  __init__ method this is constructor of class
        called every time a new object is intantiated

        Arg:
            size: This is a privite instance attribute of class type Square.
        """
        self.__size = size
