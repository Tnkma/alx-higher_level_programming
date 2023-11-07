#!/usr/bin/python3
""" The json module is called """
import json
"""
A function that returns JSON rep of a str
"""


def from_json_string(my_str):
    """
    returns the json rep of obj
    """
    return json.loads(my_str)
