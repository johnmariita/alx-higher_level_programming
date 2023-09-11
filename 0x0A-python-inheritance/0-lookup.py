#!/usr/bin/python3
"""
Module with the lookup function
"""


def lookup(obj):
    """
    function that returns a list of attributes and methods in an object

    Args:
        obj: the object
    """
    return list(dir(obj))
