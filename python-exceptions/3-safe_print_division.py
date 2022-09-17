#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div_t = a / b
    except (ValueError, ZeroDivisionError):
        div_t = None
    finally:
        print("Inside result: {}".format(div_t))
    return (div_t)
