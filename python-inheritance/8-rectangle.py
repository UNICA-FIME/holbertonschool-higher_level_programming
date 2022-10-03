#!/usr/bin/python3
"""This is module create a type class"""


class BaseGeometry(object):
    """This is an empety class"""
    def area(self):
        """This is a methode
        Arg:
          self: This is that direction memory
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a method what validate value
        Arg:
          self: This is that direction memory
          name: this is a parameter type string
          value: This is a parameter type int
        """
        if (type(value) is not int):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a class what inherits from BaseGeometry class
    Attribute:
         white: firt parameter of rectangule
         height: second parameter of rectangule
    """
    def __init__(self, width, height):
        """This is a function constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
