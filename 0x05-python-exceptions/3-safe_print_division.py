#!/usr/bin/python3
def safe_print_division(a, b):
    quot = None
    try:
        quot = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(quot))
    return quot
