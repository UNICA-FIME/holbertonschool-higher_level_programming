#!/usr/bin/python3
"""This module  that defines a square"""


class Square:
    """This class create a type square"""
    def __init__(self, size=0):
        """Allows you to initialize attributes of
        a class
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Function allows to read privete attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Function allows to change the privete attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculation Area of square"""
        self.are = self.__size**2
        return (self.are)
