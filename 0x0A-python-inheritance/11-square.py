#!/usr/bin/python3
""" Class containing the definition of the square class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square defiinition """
    def __init__(self, size):
        """ class initialization """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Function that computes the area of a square """
        return self.__size ** 2

    def __str__(self):
        """function that returns a string representation of the square """
        return "[Square] {}/{}".format(self.__size, self.__size)
