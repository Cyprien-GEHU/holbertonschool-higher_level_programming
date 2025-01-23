#!/usr/bin/python3
"""
function who add 2 integer
return a+b
"""


def add_integer(a, b=98):
    """
    the function add
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
