#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) != int:
            raise TypeError("width must be an intege")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if width == 0 or height == 0:
            return 0
        else:
            return 2 * width + 2 * height

    def __str__(self):
        """returns printable string representation of the rectangle"""
        mgs = ""
        if self.__width == 0 or self.__height == 0:
            mgs = ""
        else:
            for i in range(self.__height):
                mgs = "#" * self.__width
                if i != self.__height:
                    msg = "\n"
            return mgs

    def __repr__(self):
        """returns a string representation of the rectangle for reproduction"""
        print("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints a string when an instance has been deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
