#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square

    Attributes:
         - getter, setter size (int): return and change the value of the size
         - are (int): calculate the area of the square
    """

    def __init__(self, size=0):
        """Initilize a square
        Attributtes:
           - size(Private): size of the square

        first determinate if the value of the size is right,
        integer and positive
        """
        self.__size = size

    @property
    def size(self):
        """int: return the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """change the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Instance method
        Note:
            calcule the area of the square
        Return:
            Area of the square
        """
        area_s = (self.__size)**2
        return area_s
