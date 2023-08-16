#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for i, x in zip(sorted_dict.keys(), sorted_dict.values()):
        print(f"{i}: {x}")
