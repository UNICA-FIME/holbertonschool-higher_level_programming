#!/usr/bin/python3
def print_last_digit(number):
    a = 0
    if (number > 0):
        a = number % 10
    elif (number < 0):
        a = (((-1)*number) % 10)
    print("{:d}".format(a), end="")
    return (a)
