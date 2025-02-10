#!/usr/bin/python3
"""
the function returns the dictionary description with
simple data strucutre for JSON serialization of an object
"""


def class_to_json(obj):
    """
    the function class_to_json
    """
    return obj.__dict__
