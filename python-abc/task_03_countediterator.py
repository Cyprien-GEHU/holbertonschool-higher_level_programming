#!/usr/bin/env python3
"""
the program creat a class CountedIterator
"""


class CountedIterator:
    """
    the class CountedIterator
    """
    def __init__(self, item):
        self.__count = 0
        self.iterator = iter(item)

    def __next__(self):
        item = next(self.iterator)
        self.__count += 1
        return item

    def get_count(self):
        return self.__count
