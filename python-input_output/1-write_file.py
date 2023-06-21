#!/usr/bin/python3
"""1-task"""


def write_file(filename="", text=""):
    """write_file"""

    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
