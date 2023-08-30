#!/usr/bin/python3
"""Module containing the square class"""


class Square:
    """The Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of the Square
        Args:
            size: size-length Square
            position: square coordinates
        """
        self.position = position
        self.size = size

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """"
        The len of a side of Square
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is of a non-int data type
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """
        The coordinates of this Square
        Raises:
            TypeError: if value is not a tuple of two ints
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position of this Square
        Args: value as a tuple of two +integers
        Raises:
            TypeError: if value is not a tuple
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calxulates the area of a Square
        Returns: returns the area of the square
        """
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the position of the square"""
        print(self.pos_print(), end='')
