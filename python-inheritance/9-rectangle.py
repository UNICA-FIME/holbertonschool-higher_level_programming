#!/usr/bin/python3
"""This is module create a type class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class what inherits from BaseGeometry class
    Attribute:
         white: firt parameter of rectangule
         height: second parameter of rectangule
    """
    def __init__(self, width, height):
        """This is a function constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This is calculate the area"""
        are_T = self.__width * self.__height
        return (are_T)

    def __str__(self):
        """This is a function what return the area"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
