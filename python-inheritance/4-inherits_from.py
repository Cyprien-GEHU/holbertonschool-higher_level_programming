#!/usr/bin/python3
"""
The programme return:
- True if the object is an instance of a class inherited from specified class
- False otherwise
"""


def inherits_from(obj, a_class):
    """
    the function inherits_from
    """
    return not type(obj) is a_class and isinstance(obj, a_class)
