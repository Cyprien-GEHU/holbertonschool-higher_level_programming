#!/usr/bin/python3
'''
We write a class square:
size : the private attribue
return:
- the square
- the size of square
print :
the square with possition
'''


class Square:
    """
    The class Square
    """
    def __init__(self, size=0, postion=(0, 0)):
        self.size = size
        self.position = postion

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(a, int) and a >= 0 for a in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print()

            for i in range(self.__size):
                if self.__position[0] > 0:
                    for x in range(self.__position[0]):
                        print(end=" ")

                for j in range(self.__size):
                    print("#", end="")
                print()
