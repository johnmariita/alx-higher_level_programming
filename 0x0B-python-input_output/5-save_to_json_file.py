#!/usr/bin/python3
""" Module containing the save_to_json_file function """


import json


def save_to_json_file(my_obj, filename):
    """
    function that serializes and saves to a json file

    Args:
        my_obj: the object to be serialized
        filename: the name of the file in which
                    the json should be saved to

    """
    with open(filename, "a") as f:
        json.dump(my_obj, f)
        f.write('\n')
