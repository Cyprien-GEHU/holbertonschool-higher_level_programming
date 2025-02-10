#!/usr/bin/python3
"""
The function write on the file
"""


def write_file(filename="", text=""):
    """
    the function write_file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
