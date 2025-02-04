#!/usr/bin/env python3
"""
the programme will create a class VerboseList:
- inherits : built_in list
- override methods append, extend, remove, pop
"""


class VerboseList(list):
    """
    class VerboseList
    """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        item = super().pop(item)
        print("Popped [{}] from the list.".format(item))
