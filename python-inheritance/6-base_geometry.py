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
