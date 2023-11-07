#!/usr/bin/python3
"""
A function that reads a txt file and prints it
"""
def read_file(filename=""):
    """
    Reads in from the filename
    and prints it to stdout.
    """
    with open(filename, "r", encoding="UTF8") as files:
        file_contents = files.read()
        print(file_contents, end="")
