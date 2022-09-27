#!/usr/bin/python3
"""This is a module for print a text"""


def text_indentation(text):
    """ This is a function that print a string

    Arg : text is a string

    """
    if (type(text) is not str):
        raise TypeError("text must be a string")
    i = 0
    while(i < len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print()
            print()
            if (text[i + 1] == " "):
                i += 1
        else:
            print(text[i], end="")
        i += 1
