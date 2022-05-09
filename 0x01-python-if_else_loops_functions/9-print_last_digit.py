#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        a = number % 10
    else:
        a = (-1 * number) % 10
    print("{0}".format(a), end="")
    return a
