#!/usr/bin/python3
"""
This program sets and retrieve
"""


class Rectangle:
    """ defines the width and height of rectangle"""

    def __init__(self, width=0, height=0):
        """Initiates the getter and setters."""
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
        Args:
            value: to set to self
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
        Args:
            value: to set to self
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle
        Equals to 0 if area anf height = 0
        """
        perimeter = 0
        if self.width and self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.width + self.height)
        return perimeter
