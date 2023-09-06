#!/usr/bin/python3
"""A module containing a defined rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialization of the recangle class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle

        Raises:
            TypeError: when the value type is not an integer
            ValueError: when the value is less than 0
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        function that computes the area of the rectangle

        Returns:
            returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        function that computes the perimeter of the rectangle

        Returns:
            returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        function that returns the string represantation of the rect

        Returns:
            Str: a string represantation of the rect
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """
        returns an unambigous string representation of an object
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Function that knows once an instance of the class is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        function that compares the areas of two rectangles

        Args:
            rect_1: the first rectangle
            rect_2: the 2nd rectangle

        Returns:
            the bigger rectangle or rect_1 if they're equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        a class method that creates an instance of the Rectangle class
        with equal sides

        Args:
            size: the length of the square(Rectangle)
        Returns:
            returns an instance of the rectangle class with equal width
            and height
        """
        return cls(size, size)
