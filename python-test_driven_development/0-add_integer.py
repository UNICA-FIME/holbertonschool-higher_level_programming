#!/usr/bin/python3
""" This is module implement function
for adds 2 integers.
"""


def add_integer(a, b=98):
    """This is function to add 2 integer

    Args:
        a: The first number
        b: The second number

    Returns:
        The addition of  a  and b number
    """
    if (type(a) not in (int, float)):
        raise TypeError("a must be an integer")
    if (type(b) not in (int, float)):
        raise TypeError("b must be an integer")
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
