#!/usr/bin/python3
""" module containing the is_same_class function"""


def is_same_class(obj, a_class):
    """
    function that checks if obj is an instance of a_class

    Args:
        obj: the instance
        a_class: the object

    Returns:
        returns True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
