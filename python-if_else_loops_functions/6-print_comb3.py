#!/usr/bin/python3
i = 1
while (i < 100):
    if (i % 10 != 0 and i < 10):
        print("{:02d}".format(i),end=", ")
    elif ((i % 10) > (i / 10) and (i % 11) != 0 and i > 10 and i != 89):
        print("{:02d}".format(i),end=", ")
    elif (i == 89):
        print("{:02d}".format(i))
    i += 1
