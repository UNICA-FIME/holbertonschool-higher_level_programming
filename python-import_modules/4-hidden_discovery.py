#!/usr/bin/python3
import hidden_4
a = dir(hidden_4)
num_arg = len(a)
i = 0
if __name__ == "__main__":
    while (i < num_arg):
        if(a[i][0] != '_'):
            print("{:s}".format(a[i]))
        i += 1
