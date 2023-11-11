#!/usr/bin/python3
""" Imports from rectangle class """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ rectangle already got some attributes """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """Overrides the str method to return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
