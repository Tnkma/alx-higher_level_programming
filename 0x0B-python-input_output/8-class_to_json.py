#!/usr/bin/python3
"""
Returns the dictionary desc with simple
data structure for serialization
"""


def class_to_json(obj):
    """
    returns obj. the dictionary ref
    """
    dic = obj.__dict__
    return dic
