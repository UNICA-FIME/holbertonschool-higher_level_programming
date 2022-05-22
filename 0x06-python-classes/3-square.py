#!/usr/bin/python3
"""My first square"""


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0):
        """Instantiation a square
        Attributtes:
          - size (Private): size of the square

        First determinate if the value of the size is right,
        integer and positive
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        area_s = (self.__size) ** 2
        return area_s
