#!/usr/bin/python3
"""This is a module that create a type class"""


class Base(object):
    """The goal of it is to manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.
