#!/usr/bin/python3
import random
import sys
number = random.randint(-10, 10)
if number > 0:
    sys.stdout.write("{:d} is positive\n".format(number))
elif number < 0:
    sys.stdout.write("{:d} is negative\n".format(number))
else:
    sys.stdout.write("{:d} is zero\n".format(number))
