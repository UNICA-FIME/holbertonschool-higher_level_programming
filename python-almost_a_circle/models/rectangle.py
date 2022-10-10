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

    def area(self):
        """Calculate the are of the rectangle"""
        return self.height * self.width

    def display(self):
        """that prints in stdout the square with the character #:"""
        msg = "\n" * self.y
        for y in range(self.height):
            pos_x = " " * self.x
            msg += pos_x + "#" * self.width + "\n"
        print(msg, end="")
        return msg

    def __str__(self) -> str:
        """string representation method"""
        return "[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        attr = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for key, value in zip(attr, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation"""

        attr = ["id", "width", "height", "x", "y"]
        r_dict = {key: getattr(self, key) for key in attr}

        return r_dict
