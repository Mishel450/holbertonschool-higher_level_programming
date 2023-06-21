#!/usr/bin/python3
"""2-task"""


def append_write(filename="", text=""):
    """append_write"""

    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
