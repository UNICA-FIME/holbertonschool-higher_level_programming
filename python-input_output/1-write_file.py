#!/usr/bin/python3
"""This is a module that create a method"""


def write_file(filename="", text=""):
    """This a method read a file and count leng the string"""

    with open(filename, mode="w", encoding="utf-8") as Myfile:
        return Myfile.write(text)
