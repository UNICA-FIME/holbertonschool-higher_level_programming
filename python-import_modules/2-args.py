#!/usr/bin/python3
from sys import argv, stdout
i = 1
num_arg = len(argv) - 1
if __name__ == "__main__":
    if (num_arg == 0):
        stdout.write("{:d} arguments{}\n".format(num_arg, "."))
    elif (num_arg == 1):
        stdout.write("{:d}{:s}argument{:s}\n".format(num_arg, " ", ":"))
        stdout.write("{:d}: {:s}\n".format(num_arg, argv[num_arg]))
    else:
        stdout.write("{:d} arguments:\n".format(num_arg))
        while (i <= num_arg):
            stdout.write("{:d}: {}\n".format(i, argv[i]))
            i += 1
