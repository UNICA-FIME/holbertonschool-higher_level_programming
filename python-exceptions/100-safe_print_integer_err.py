#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        rsp = True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        rsp = False
    finally:
        return (rsp)
