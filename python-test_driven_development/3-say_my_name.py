#!/usr/bin/python3
"""task 3"""


def say_my_name(first_name, last_name=""):
    """say_my_name"""

    txt = "My name is {} {}"
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(txt.format(first_name, last_name))
