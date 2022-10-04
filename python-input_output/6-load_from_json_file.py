#!/usr/bin/python3
"""This is a module create a method"""
import json


def load_from_json_file(filename):
    """This is a method that create object
    from a JSON file
    """
    with open(filename, mode="r", encoding="utf-8") as Myfile:
        data = Myfile.read()
    return json.loads(data)
