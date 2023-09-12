#!/usr/bin/python3
""" a function that deserealizes a json string """


import json


def from_json_string(my_str):
    """
    A function that deserealizes a json string

    Args:
        my_str: the json string

    Returns:
        returns a deserealized string
    """
    return json.loads(my_str)
