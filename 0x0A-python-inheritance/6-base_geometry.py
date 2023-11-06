#!/usr/bin/python3
"""
An empty class for a base geometry
"""


class BaseGeometry:
    """
    A base class for geometric program
    """
    def area(self):
        """
        A function that raise an exception
        when its not implemented.
        """
        raise Exception("area() is not implemented")
