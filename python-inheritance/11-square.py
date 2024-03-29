#!/usr/bin/python3
"""This a module create that type class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class type square"""
    def __init__(self, size):
        """This is a function what calculate that area"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size**2)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
