#!/usr/bin/python3
"""
Here we are writting a program
An addition program.
Including its doctest part on another file
"""
def add_integer(a, b=98):
    """
    Checks if the data type is integer else raise a typeerror 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    return a + b
