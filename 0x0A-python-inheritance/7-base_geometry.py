#!/usr/bin/python3
"""
An empty class for a base geometry
"""


class BaseGeometry:

    """
    A base class for geometric program
    """

    def integer_validator(self, name, value):

        """
        Validates the value of the method

        Args:
        :name: name of the value
        :value: the value itself
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """
        A function that raise an exception
        when its not implemented.
        """
        raise Exception("area() is not implemented")
