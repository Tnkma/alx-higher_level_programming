#!/usr/bin/python3
""" Imports the module for json """
import json
"""
A function that writes an object file to text file
using json representation
"""
def save_to_json_file(my_obj, filename):
    """
    using 'with' we will open the file with write mode 
    and then write the file to the path.
    """
    with open(filename, "w") as files:
        json.dump(my_obj, files)

