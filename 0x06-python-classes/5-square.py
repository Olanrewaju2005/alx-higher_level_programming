#!/usr/bin/python3
"""Define a class square"""
class Square:
    """represent the square"""
    def __init__(self, size):
        """initialize a new square
        Args: size(int) - length of the square
        """
        self.size = size
    @property
    def size(self):
        """get/set crrent length of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the squatre with the # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")