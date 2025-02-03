#!/usr/bin/python3
"""
The programme return:
- True if the object is exactly an instance of the specified class
or if the object is an instance of a class inherited from the specified class
- False otherwise
"""


def is_kind_of_class(obj, a_class):
    """
    the function is_king_of_class
    """
    return isinstance(obj, a_class)
