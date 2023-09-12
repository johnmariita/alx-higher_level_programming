#!/usr/bin/python3
""" A module containing a function that serializes """


import json


def to_json_string(my_obj):
    """
    Function that serializes

    Args:
        my_obj: object to be serialized

    Returns:
        returns a json string

    """
    return json.dumps(my_obj)
