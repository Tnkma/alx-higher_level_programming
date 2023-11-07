#!/usr/bin/python3
"""
A function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="UTF8") as files:
        files_written = files.write(text)
        return files_written
