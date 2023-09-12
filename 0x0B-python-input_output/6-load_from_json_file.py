#!/usr/bin/python3
""" A module containing the function that deserializes from a json file"""


import json


def load_from_json_file(filename):
    """
    function that deserealizes from a json file.

    Args:
        filename: the filename containing the json string
    """
    with open(filename, "r") as f:
        return json.load(f)
