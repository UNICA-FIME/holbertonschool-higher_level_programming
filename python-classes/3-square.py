#!/usr/bin/python3
""" The module create the type class"""


class Square:
    """ The classes this a type for calculation
    the area of square.
    """
    def __init__(self, size=0):
        """This method is known as the constructor of the
        class and is called every time a new object is instantiated
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This function calutate area of square"""
        self.result = self.__size**2
        return(self.result)
