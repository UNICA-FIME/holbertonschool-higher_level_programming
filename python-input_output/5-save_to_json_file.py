#!/usr/bin/python3
"""This is a create method"""
import json


def save_to_json_file(my_obj, filename):
    """This is a method save object to file"""
    with open(filename, mode="w", encoding="utf-8") as Myfile:
        Myfile.write(json.dumps(my_obj, sort_keys=False))
