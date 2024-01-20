#!/usr/bin/python3

"""
This module contains a script that adds all command line
arguments to a Python list, and then save them to a file
add_item.json in JSON representation. If the file doesn't
exist, it's created.
"""


import sys

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    cmd_line_args = sys.argv[1:]
    items.extend(cmd_line_args)
    save_to_json_file(items, 'add_item.json')
