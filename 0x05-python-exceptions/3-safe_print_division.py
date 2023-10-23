#!/usr/bin/python3

def safe_print_division(a, b):
    de_sum = None
    try:
        de_sum = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(de_sum))
    return de_sum
