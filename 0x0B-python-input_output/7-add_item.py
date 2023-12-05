#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

from sys import argv
save_to_json_file = __import__ ("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__ ("6-load_from_json_file").load_from_json_file

try:
    list_js = load_from_json_file("add_item.json")
except FileNotFoundError:
    list_js = []

for arg in argv[1:]:
    list_js.append(arg)

save_to_json_file(list_js, "add_item.json")
