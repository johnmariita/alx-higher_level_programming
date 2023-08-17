#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_be_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            to_be_del.append(key)
    for key in to_be_del:
        del a_dictionary[key]
    return a_dictionary
