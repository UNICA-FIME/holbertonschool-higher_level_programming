#!/usr/bin/python3
"""This is module that create type class"""

from models.base import Base


class Rectangle(Base):
    """This is a type class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter to width"""
        return self.__width

    @property
    def height(self):
        """Getter to height"""
        return self.__height

    @property
    def x(self):
        """Getter to x"""
        return self.__x

    @property
    def y(self):
        """Getter to y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Change value pravite"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Change value pravite"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Change value pravite"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Change value pravite"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
