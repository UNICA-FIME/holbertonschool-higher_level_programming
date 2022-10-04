#!/usr/bin/python3
"""This is a module create a function"""


def read_file(filename=""):
    """This is a function that read a text file"""
    with open(filename, encoding="utf-8") as myfile:
        read_data = myfile.read()
        print(read_data, end="")
