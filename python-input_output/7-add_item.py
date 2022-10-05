#!/usr/bin/python3
"""This is a  module create script"""

import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
if len(argv) == 1:
    list_new = []
    save_to_json_file(list_new, filename)
if len(argv) > 1:
    try:
        obj_json = load_from_json_file(filename)
    except Exception:
        obj_json = []
    for i in argv[1:]:
        obj_json.append(i)
    save_to_json_file(obj_json, filename)
