#!/usr/bin/python3
'''
We write a class square:
size : the private attribue
return:
- the square
- the size of square
'''


class Square:
    """
    The class Square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
