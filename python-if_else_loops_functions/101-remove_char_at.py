#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if (n < 0):
        return str
    str_1 = str[0:n]
    str_2 = str[n + 1::]
    new_str = str_1 + str_2
    return new_str
