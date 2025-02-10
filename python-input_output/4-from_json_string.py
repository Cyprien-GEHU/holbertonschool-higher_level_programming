#!/usr/bin/python3
"""
the function return an object by json string
"""
import json


def from_json_string(my_str):
    """
    the function from_json_string
    """
    return json.loads(my_str)
