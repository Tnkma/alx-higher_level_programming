#!/usr/bin/python3
"""Creating a private instance attributes"""


class Square:
    """Class definition"""

    def __init__(self, size):
        """Setting up the initialization.
        Args:
        size (int): the size of the square.
        """
        self.__size = size
