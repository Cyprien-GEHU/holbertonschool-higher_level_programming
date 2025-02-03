#!/usr/bin/python3
"""
The programme return:
- True if the object is exactly an instance of the specified class
- False otherwise
"""


def is_same_class(obj, a_class):
    """
    the function is_same_class
    """
    return type(obj) is a_class
