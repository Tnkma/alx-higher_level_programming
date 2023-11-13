#!/usr/bin/python3
""" A base module """
import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        # gets the class name
        cl_name = cls.__name__
        # make the filename
        filename = "{}.json".format(cl_name)
        # convert list_objs to a list of dictionaries
        dic_lists = [obj.to_dictionary() for obj in list_objs]

        # get the json representation of dic_lists
        json_rep = cls.to_json_string(dic_lists)

        # Now write the json string into a file
        with open(filename, 'w') as files:
            files.write(json_rep)

    def from_json_string(json_string):
        """
        Returns the list of json string representation json_string
        """
        if json_string is None:
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        # Creating a dummy instance
        dummy = cls(1, 1, 1, 1, 1)

        # update the dummy with update method
        dummy.update(**dictionary)
        return dummy
