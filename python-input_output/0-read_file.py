#!/usr/bin/python3
"""0-task"""


def read_file(filename=""):
    """hola"""

    with open(filename, encoding="utf-8") as file:
        file_read = file.read()
        print(file_read, end="")