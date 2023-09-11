#!/usr/bin/python3
""" A module with the definition of the class BaseGeometry"""


class BaseGeometry:
    """ class definition """
    def area(self):
        """ function that raises an exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ function that validates the value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
