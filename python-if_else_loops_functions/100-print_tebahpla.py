#!/usr/bin/python3
i = 122
while (i > 96):
    if(i % 2 != 0):
        i = i - 32
    print("{:c}".format(i), end="")
    if(i % 2 != 0):
        i = i + 32
    i -= 1
