#!/usr/bin/python3
""" Module containing a function that adds a new attriute to an object """


def add_attribute(obj, attr_name, attr_value):
    """
    Function that adds an attribute to an object if possible

    Args:
        obj: the object
        attr_name: name of the attribute
        attr_value: the value of the attribute

    Raises:
        TypeError: raises a TypeError when the attribute can't be added
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    else:
        raise TypeError("can't add new attribute")
