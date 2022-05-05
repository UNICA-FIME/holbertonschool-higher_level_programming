#!/usr/bin/python3
i = 0
while i < 10:
    j = 0
    while j < 10:
        if i != j and i < j and (i + j) < 17:
            print("{0}{1},".format(i, j), end=" ")
        elif i == 8 and j == 9:
            print("{0}{1}".format(i, j))
        j = j + 1
    i = i + 1
