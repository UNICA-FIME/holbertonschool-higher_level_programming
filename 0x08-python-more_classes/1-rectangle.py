#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle with attributes"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Access the attribute self.with"""

        return self.__witdh

    @width.setter
    def width(self, value):
        """change value of attribute self.__with"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Access value of attribute self.__height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Change value of attribute self.__height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
