#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle without attributes
    Attirbutes:
        - getter, setter width(int)
        - getter and setter height(int)
        - publics methos area and perimeter
        - str method: string representation"""

    def __init__(self, width=0, height=0):
        """inizialization the variable"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of width, show the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the height: change the value of the height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter of height, show the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the width: change the value of the width"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method: calculate the area of rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Public method that calculate the perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (2 * self.height + 2 * self.width)

    def __str__(self):
        """method that return a string representation to user"""
        msg = ""
        if self.width == 0 or self.height == 0:
            msg = ""
        else:
            for i in range(self.height):
                msg += "#" * self.width
                if i != self.height - 1:
                    msg += "\n"
        return msg
