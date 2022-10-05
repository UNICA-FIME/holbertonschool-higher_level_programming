#!/usr/bin/python3
"""This is a module create a method"""


def class_to_json(obj):
    """This is a function create base date JSON"""
    data_json = obj.__dict__
    return data_json
