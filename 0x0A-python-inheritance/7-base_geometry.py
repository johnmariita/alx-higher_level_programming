#!/usr/bin/python3
""" A module with the definition of the class BaseGeometry"""


class BaseGeometry:
    """ class definition """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ function that validates the value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
