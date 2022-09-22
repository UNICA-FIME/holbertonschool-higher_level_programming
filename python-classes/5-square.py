#!/usr/bin/python3
"""This is module create a type of class"""


class Square:
    """This is a type class what return the
    square area"""
    def __init__(self, size):
        """Allow to initialize the
        attributes of a class
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """This is function allows read
        private instance attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is function allows write
        private instance attribute
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This is function what calculate the area of square"""
        self.are = self.__size**2
        return(self.are)

    def my_print(self):
        """This function print the square of #"""
        if (self.__size == 0):
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
