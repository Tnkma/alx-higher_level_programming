#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    # Check if the provided input is a dictionary
    if not isinstance(a_dictionary, dict):
        return a_dictionary

    # Sort the dictionary by its keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print each key-value pair in order of the sorted keys
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
