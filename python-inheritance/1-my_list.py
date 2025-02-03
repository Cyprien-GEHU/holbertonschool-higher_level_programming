#!/usr/bin/python3
"""
The programme return:
- True if the object is exactly an instance of the specified class
- False otherwise
"""


class MyList(list):
    """
    the class MyList
    """
    def print_sorted(self):
        lst = self.copy()
        lst.sort()
        print(lst)
