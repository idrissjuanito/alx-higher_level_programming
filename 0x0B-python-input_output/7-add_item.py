#!/usr/bin/python3
import json
from sys import argv
import os


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")
    lst = []

for i in range(len(argv)):
    if i > 0:
        lst.append(argv[i])
save_to_json_file(lst, "add_item.json")
