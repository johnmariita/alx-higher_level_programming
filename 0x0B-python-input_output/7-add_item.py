#!/usr/bin/python3
""" A module containing the load, add and save function """
import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


mylist = []
for i in sys.argv[1:]:
    mylist.append(i)

if not os.path.exists("add_item.json"):
    with open("add_item.json", "w") as f:
        json.dump(mylist, f)

else:
    with open("add_item.json", "r") as f:
        existing = json.load(f)
    with open("add_item.json", "w") as f:
        existing.extend(mylist)
        json.dump(existing, f)
