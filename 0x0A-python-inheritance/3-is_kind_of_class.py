#!/usr/bin/python3
"""
returns false or true if the object
is an instance of the class or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an isinstance of a_class.

    Args:
    :obj: the object to check.
    :a_class: the class to check.
    :return: either false or true.
    """
    return isinstance(obj, a_class)
