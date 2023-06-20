#!/usr/bin/python3
"""2-test"""


def is_same_class(obj, a_class):
    """python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    if (type(obj) == a_class):
        return (True)
    else:
        return (False)
