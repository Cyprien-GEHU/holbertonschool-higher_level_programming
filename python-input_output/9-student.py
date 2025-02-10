#!/usr/bin/python3
"""
Write the class Student with intance:
- first_name
- last_name
- age
"""


class Student:
    """
    the class Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
