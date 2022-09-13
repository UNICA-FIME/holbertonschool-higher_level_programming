#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    if (len_str == 0):
        first_elm = None
    else:
        first_elm = sentence[0]
    return ((len_str, first_elm))
