#!/usr/bin/python3
"""This a module that create type class"""


class Student(object):
    """This is create a class type Student
    Attribute:
           fist_name
           last_name
           age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This is that retrieves a dictionary  representation"""
        return (self.__dict__)
