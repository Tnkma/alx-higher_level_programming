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

    def to_json(self, attrs=None):
        # initialize a empty var
        student_dict = {}

        if attrs is not None:
            for attr_name in attrs:
                if hasattr(self, attr_name):
                    attr_value = getattr(self, attr_name)
                    if isinstance(attr_value, str):
                        student_dict[attr_name] = attr_value
        else:
            student_dict = self.__dict__
        return student_dict
