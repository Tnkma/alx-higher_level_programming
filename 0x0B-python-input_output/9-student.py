#!/usr/bin/python3
"""
A student Class
"""


class Student:
    """
    defines a student attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        Initailize the instance of the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_dict = self.__dict__
        return student_dict
