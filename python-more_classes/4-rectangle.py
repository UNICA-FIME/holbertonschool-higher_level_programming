#!/usr/bin/python3
"""This is a module for create a class type rectangle"""


class Rectangle:
    """ This is a class for create a type rectangle

    Attributes:
         width: This is a privite instance attribute
         height:This is a privite instance attribute

    """
    def __init__(self, width=0, height=0):
        """This is a function that allws you to initialize the
        attributes of a class type Rectangle.

        Args:
           width: Receives the width parameter of the rectangle.
           height: Receive the height parameter of the rectangle.

        """
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """This function allows read the private instance attribute
        or the class.
        named: self.__width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This function allows read the private instance attribute
        or the class.
        named: self.__width
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """This is a function calculate the rectangle area

        Returns:
           The return value ractangule area

        """
        return (self.__width * self.height)

    def perimeter(self):
        """This is a function calculate the rectangle perimeter

        Return:
          The return value rectangule perimeter

        """
        self.peri = 0
        if(self.__width == 0 or self.__height == 0):
            self.perimeter = 0
        else:
            self.peri = 2 * self.__width + 2 * self.__height
        return (self.peri)

    def __str__(self):
        """This is an Instance method that returns an “informal”
        and nicely printable string representation of an instance

        """
        if (self.__width == 0 or self.__height == 0):
            return("")
        else:
            return "\n".join("#" * self.__width for i in range(self.__height))

    def __repr__(self):
        """"This is a Instance method that returns an “official”
        string representation of an instance

        """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))
