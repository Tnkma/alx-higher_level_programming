#!/usr/bin/python3
""" Imports the json module """
import json
"""
A function that creates an object from
a JSON file
"""


def load_from_json_file(filename):
    """
    creates an object from a json file
    """
    with open(filename, "r") as files:
        file_content = json.load(files)
        return file_content
