#!/usr/bin/python3
a = 0
while a < 100:
    if a != 99:
        print("{0}{1}".format(a // 10, a % 10), end=", ")
    a = a + 1
print("99")
