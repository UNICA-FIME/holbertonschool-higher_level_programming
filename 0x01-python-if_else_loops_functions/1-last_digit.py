#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = int(number % 10)
if (number % 10 > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, a))
elif (number % 10 < 6 and number % 10 != 0):
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
elif (number % 10 == 0):
    print("Last digit of {} is {} and is 0".format(number, a))
