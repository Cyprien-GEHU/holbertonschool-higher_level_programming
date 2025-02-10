#!/usr/bin/python3
"""
the function writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    the function save_to_json_file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
