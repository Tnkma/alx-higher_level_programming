#!/usr/bin/python3
"""
This program sets and retrieve
a private instance height and width
"""


class Rectangle:

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrive and return the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value to the  private instance of width
        if width is not an int, raise TypeError
        if width is less than 0, Raise ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrive and return the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height to the private instance
        if height is not an integer, raise an error message
        if height is less than 0, raise an error message too
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
