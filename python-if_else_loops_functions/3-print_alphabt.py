#!/usr/bin/python3
i = 97
while (i < 123):
    if (i != 101 and i != 113):
        print("{:c}".format(i), end="")
    i += 1
