#!/usr/bin/python3
"""This is a module create a function"""


def read_file(filename=""):
    """This is a function that read a text file"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())
