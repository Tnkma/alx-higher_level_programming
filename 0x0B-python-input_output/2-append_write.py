#!/usr/bin/python3
"""
A function that appends a string
"""


def append_write(filename="", text=""):
    """
    appends text at the end of the string
    """
    with open(filename, "a", encoding="UTF8") as files:
        file_content = files.write(text)
        return file_content
