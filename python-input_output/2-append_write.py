#!/usr/bin/python3
"""This a module that create function"""


def append_write(filename="", text=""):
    """This is a method read a file"""
    with open(filename, mode="a", encoding="utf-8") as Myfile:
        return Myfile.write(text)
