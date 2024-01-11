#!/usr/bin/python3

"""
This module contains a script that adds all command line
arguments to a Python list, and then save them to a file
add_item.json in JSON representation. If the file doesn't
exist. it's created.
"""


import sys

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = []
    try:
        json_to_py = load_from_json_file('add_item.json')
        new_py_list = json_to_py + args
        save_to_json_file(new_py_list)
    except Exception:
        save_to_json_file(args, 'add_item.json')
