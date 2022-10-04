#!/usr/bin/python3
"""Thi is a module that create a method"""

import json


def to_json_string(my_obj):
    """This is a function return to JSON string"""
    return (json.dumps(my_obj, skipkeys=True, sort_keys=True))
