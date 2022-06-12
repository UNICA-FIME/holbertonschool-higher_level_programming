#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    n = len(sys.argv) - 1
    if n == 0:
        print("{:d}".format(n))
    else:
        for i in range(n):
            a = a + int(sys.argv[i + 1])
        print("{:d}".format(a))
