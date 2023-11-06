#!/usr/bin/python3
"""
returns false or true if the object
is an instance of the class or subclass
"""


def inherits_from(obj, a_class):
    """
    checks if obj is an isinstance of a_class.

    Args:
    :obj: the object to check.
    :a_class: the class to check.
    :return: either false or true.
    """
    if isinstance(obj, object) and type(obj) != a_class:
        return True
    return False
