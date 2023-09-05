#!/usr/bin/python3
"""A module containing a defined rectangle class"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Initialization of the recangle class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.__width = width
        self.__height = height
    @property
    def height(self):
        """
        the height of the rectangle
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        sets the height of the rectangle

        Args:
            value: the new height value

        Raises:
            TypeError: when the value type is not an integer
            ValueError: when the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    @property
    def width(self):
        """
        the width of the rectangle
        """
        return self.__width
    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle

        Args:
            value: the new width value

        Raises:
            TypeError: when the value type is not an integer
            ValueError: when the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
