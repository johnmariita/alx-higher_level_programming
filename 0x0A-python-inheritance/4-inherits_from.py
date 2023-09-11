#!/usr/bin/python3
"""A module containing the function inherits_from"""


def inherits_from(obj, a_class):
    """
    checks if obj is of a class inherited from a_class

    Args:
        obj: the instance
        a_class: the class name

    Returns:
        returns True if it is inherited, otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
