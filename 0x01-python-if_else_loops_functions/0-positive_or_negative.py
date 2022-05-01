#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    print(f"{number} is positive\n")
elif number == 0:
    print(f"{number} is zero\n")
else:
    print(f"{number} is negative\n")
