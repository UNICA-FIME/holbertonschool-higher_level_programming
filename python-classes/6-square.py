#!/usr/bin/python3
"""This module create type class"""


class Square:
    """ This is a class with calculate the area square"""
    def __init__(self, size=0, position=(0, 0)):
        """ This is metode for iniciality the attribute of class"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (type(position) is not tuple and type(position[0]) is not int
                and type(position[1]) is not int or len(position) < 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """This is a function for read the privite instance attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is a function change the privite instance attribute"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """This is a function read the privite instance attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """This is a function write the privite instance attribute"""
        if (type(value) is not tuple and type(value[0]) is not int
                and type(value[1]) is not int and len(position) < 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This is a function the calculate the area square"""
        self.area = self.__size**2
        return (self.area)

    def my_print(self):
        """This is function print square of #"""
        if (self.__size == 0):
            print()
        if (self.__position[1] > 0):
            print()
        for j in range(0, self.__size):
            for x in range(0, self.__size):
                if (x == 0):
                    for i in range(0, self.__position[0]):
                        print(" ", end="")
                print("#", end="")
            print()
