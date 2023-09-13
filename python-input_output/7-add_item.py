#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

nmb = "add_item.json"

try:
    js = load_from_json_file(nmb)
except Exception:
    js = []
if len(sys.argv) != 1:
    for a in range(1, len(sys.argv)):
        # arranca del 1 para sacar el nombre
        js.append(sys.argv[a])
save_to_json_file(js, nmb)
