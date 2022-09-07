#!/usr/bin/python3
def fizzbuzz():
    i = 1
    e = ""
    while (i <= 100):
        if (i % 15 == 0):
            e = "FizzBuzz"
            print("{}".format(e), end=" ")
        elif(i % 3 == 0 and i % 5 != 0):
            e = "Fizz"
            print("{}".format(e), end=" ")
        elif(i % 3 != 0 and i % 5 == 0):
            e = "Buzz"
            print("{}".format(e), end=" ")
        else:
            print("{:d}".format(i), end=" ")
        i += 1
