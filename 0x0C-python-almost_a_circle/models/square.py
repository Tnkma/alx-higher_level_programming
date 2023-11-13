#!/usr/bin/python3
""" Imports from rectangle class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ rectangle already got some attributes """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Overrides the str method to return
        [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns attributes to args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of the Square class
        """
        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
