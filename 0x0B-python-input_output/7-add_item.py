#!/usr/bin/python3
"""
Module doc
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_items():
    """
    function docs
    """
    filename = "add_item.json"
    if path.isfile(filename):
        final_list = load_from_json_file(filename)
    else:
        final_list = []
    for i in range(1, len(argv)):
        final_list.append(argv[i])
    save_to_json_file(final_list, filename)


add_items()
