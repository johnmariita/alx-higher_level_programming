#!/usr/bin/python3
""" A module containing a class rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class definition """
    def __init__(self, width, height):
        """ clas initialization """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
