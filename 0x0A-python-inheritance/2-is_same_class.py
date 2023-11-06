#!/usr/bin/python3
"""
A function that returns True if the object is excalty
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns true if the first argument is an instance
    of the second argument.

    Args:
    :obj: the object to check
    :a_class: the class to check
    :return: Either true or false is its same class.
    """
    result = type(obj) is a_class
    return result
