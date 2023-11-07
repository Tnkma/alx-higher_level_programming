#!/usr/bin/python3
""" The json module is called """
import json
"""
A function that returns JSON rep of a str
"""


def to_json_string(my_obj):
    """
    returns the json rep of obj
    """
    return json.dumps(my_obj)
