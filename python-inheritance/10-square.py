#!/usr/bin/python3
"""
write the class Square inherits from Rectangle:
- area : calcul the area of the Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    the class Square
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
