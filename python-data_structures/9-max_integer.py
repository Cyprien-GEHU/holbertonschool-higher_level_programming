#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = sorted(my_list, key=int, reverse=True)
    if max_value:
        return max_value[0]
    return None
