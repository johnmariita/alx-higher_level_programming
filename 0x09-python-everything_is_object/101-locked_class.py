#!/usr/bin/python3
"""
Module containing a class that prevents dynamically created class attributes
"""


class LockedClass:
    """Class LOcked class"""
    __slots__ = ['first_name']
