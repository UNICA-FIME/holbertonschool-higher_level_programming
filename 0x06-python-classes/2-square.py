#!/usr/bin/python3
""" class Square definition"""


class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0):
        """Initilize a square
        Attributtes:
         - size(Privete): size of the square

         First determinate if the value of the size is right,
          integer and positive
         """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
