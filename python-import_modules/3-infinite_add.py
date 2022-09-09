#!/usr/bin/python3
from sys import argv, stdout
num_arg = len(argv)
i = 1
sum_arg = 0
if (num_arg > 2):
    while (i < num_arg):
        sum_arg = sum_arg + int(argv[i])
        i += 1
stdout.write("{}\n".format(sum_arg))
