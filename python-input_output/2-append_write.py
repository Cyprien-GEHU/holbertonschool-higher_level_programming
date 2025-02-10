#!/usr/bin/python3
"""
the function appends a string at the end of text file
"""


def append_write(filename="", text=""):
    """
    the function append_file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
