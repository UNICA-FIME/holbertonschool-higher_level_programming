#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        b = None
    elif a != 0:
        b = sentence[0]
    tuple_new = (a, b)
    return (tuple_new)
