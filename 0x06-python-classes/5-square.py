#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that define a Square
        Attributes:

        - getter, setter size (int): return and change the value of the size
        - area (int): calculate the area of the square
    """

    def __init__(self, size=0):
        """Initilize a square
        Attributtes:
            - size (Private): size of the square
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
               calculate the area of the square
           Returns:
               Area of the square
       """
        area_s = (self.__size)**2
        return area_s

    def my_print(self):
        """prints in stdout the square with the character #"""
        w = self.__size
        h = self.__size
        if (w and h) == 0:
            print()
        i = 0
        while i < h:
            j = 0
            while j < w:
                print("#", end="")
                j = j + 1
            print()
            i = i + 1
