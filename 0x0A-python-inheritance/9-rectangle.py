#!/usr/bin/python3
""" A module containing the class Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class definition """
    def __init__(self, width, height):
        """ class initialization """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ function that returns the area of a rectangle """
        return self.__height * self.__width

    def __str__(self):
        """ function that returns the string representation of a class """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
